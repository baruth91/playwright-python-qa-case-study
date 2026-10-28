"""UI mechanics live here; business expectations remain visible in the tests."""

import re
from decimal import Decimal
from urllib.parse import urlparse

from playwright.sync_api import Locator, Page, expect


def money(text: str) -> Decimal:
    """Convert the demo's English USD display without binary floating-point rounding."""
    return Decimal(text.strip().replace("$", "").replace(",", ""))


class Catalog:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.names = page.get_by_test_id("product-name")
        self.prices = page.get_by_test_id("product-price")

    def open(self) -> None:
        self.page.goto(self.base_url)
        expect(self.names.first).to_be_visible()

    def search(self, query: str) -> None:
        self.page.get_by_test_id("search-query").fill(query)
        # A search heading can update before the async results arrive.
        with self.page.expect_response(
            lambda response: urlparse(response.url).path == "/products/search"
            and response.request.method in {"GET", "QUERY"}
        ) as response:
            self.page.get_by_test_id("search-submit").click()
        assert response.value.ok, f"Search failed with HTTP {response.value.status}"

    def sort_by(self, label: str) -> None:
        with self.page.expect_response(
            lambda response: urlparse(response.url).path == "/products"
            and response.request.method in {"GET", "QUERY"}
        ) as response:
            self.page.get_by_test_id("sort").select_option(label=label)
        assert response.value.ok, f"Sort failed with HTTP {response.value.status}"
        # Synchronize to this response's sequence, then let the test independently
        # verify numeric ordering. The API sequence is not our sorting oracle.
        names = [product["name"] for product in response.value.json()["data"]]
        expect(self.names).to_have_text(names)

    def open_product(self, name: str) -> "Product":
        self.names.filter(has_text=re.compile(rf"^\s*{re.escape(name)}\s*$")).click()
        product = Product(self.page)
        expect(product.name).to_have_text(name)
        expect(product.price).to_be_visible()
        return product


class Product:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.name = page.get_by_test_id("product-name")
        self.price = page.get_by_test_id("unit-price")
        self.quantity = page.get_by_test_id("quantity")

    def add_to_cart(self, quantity: int = 1) -> "Cart":
        self.quantity.fill(str(quantity))
        self.page.get_by_test_id("add-to-cart").click()
        expect(self.page.get_by_test_id("cart-quantity")).to_have_text(str(quantity))
        self.page.get_by_test_id("nav-cart").click()
        cart = Cart(self.page)
        expect(cart.total).to_be_visible()
        return cart


class Cart:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.total = page.get_by_test_id("cart-total")

    def row(self, product_name: str) -> Locator:
        return self.page.get_by_role("row").filter(
            has=self.page.get_by_test_id("product-title").filter(has_text=product_name)
        )

    def proceed(self) -> None:
        self.page.get_by_test_id("proceed-1").click()
        expect(self.page.get_by_test_id("email")).to_be_visible()
