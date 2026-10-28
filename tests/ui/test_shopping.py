"""Business checks: see docs/coverage-map.md for risk and scenario identifiers."""

import re
from decimal import Decimal

import pytest
from playwright.sync_api import Page, expect

from pages.shop import Catalog, money

pytestmark = pytest.mark.shop
PRODUCT = "Combination Pliers"


@pytest.mark.smoke
def test_search_finds_a_known_product(page: Page, shop_url: str) -> None:
    """SHOP-01: Customers can discover a known catalog item."""
    catalog = Catalog(page, shop_url)
    catalog.open()
    catalog.search(PRODUCT)
    expect(catalog.names).to_have_text([PRODUCT])


def test_unknown_search_has_an_explicit_empty_state(page: Page, shop_url: str) -> None:
    """SHOP-02: Empty results must not silently display stale products."""
    catalog = Catalog(page, shop_url)
    catalog.open()
    catalog.search("qa-no-such-product-9f87a1")
    expect(catalog.names).to_have_count(0)
    expect(page.get_by_text("There are no products found.", exact=True)).to_be_visible()


def test_search_can_recover_after_no_results(page: Page, shop_url: str) -> None:
    """SHOP-03: An unsuccessful search does not trap the customer."""
    catalog = Catalog(page, shop_url)
    catalog.open()
    catalog.search("qa-no-such-product-9f87a1")
    expect(catalog.names).to_have_count(0)
    catalog.search(PRODUCT)
    expect(catalog.names).to_have_text([PRODUCT])


@pytest.mark.parametrize("direction", ["Low - High", "High - Low"])
def test_price_sort_orders_the_visible_page(
    page: Page, shop_url: str, direction: str
) -> None:
    """SHOP-04a/b: Compare numeric prices, not formatted strings."""
    catalog = Catalog(page, shop_url)
    catalog.open()
    catalog.sort_by(f"Price ({direction})")
    # Retry on rendered state; HTTP completion alone does not guarantee a DOM update.
    expect(catalog.prices.first).to_have_text(re.compile(r"\$\d+\.\d{2}"))
    expect(page.locator('[data-test="sort"] option:checked')).to_have_text(
        f"Price ({direction})"
    )
    prices = [money(text) for text in catalog.prices.all_text_contents()]
    assert len(prices) >= 2, "Sorting needs at least two products to be meaningful"
    assert prices == sorted(prices, reverse=direction == "High - Low")


@pytest.mark.parametrize("quantity", [1, 3])
def test_cart_preserves_product_quantity_and_amounts(
    page: Page, shop_url: str, quantity: int
) -> None:
    """SHOP-05a/b: The selected item and its arithmetic survive the page transition."""
    catalog = Catalog(page, shop_url)
    catalog.open()
    catalog.search(PRODUCT)
    product = catalog.open_product(PRODUCT)
    unit_price = money(product.price.inner_text())
    assert unit_price > Decimal("0")
    cart = product.add_to_cart(quantity)
    row = cart.row(PRODUCT)
    expect(row).to_have_count(1)
    expect(row.get_by_test_id("product-quantity")).to_have_value(str(quantity))
    expect(row.get_by_test_id("product-price")).to_have_text(f"${unit_price:.2f}")
    expected_total = unit_price * quantity
    expect(row.get_by_test_id("line-price")).to_have_text(f"${expected_total:.2f}")
    expect(cart.total).to_have_text(f"${expected_total:.2f}")


def test_cart_quantity_change_recalculates_total(page: Page, shop_url: str) -> None:
    """SHOP-06: Changing quantity must update line and cart totals."""
    catalog = Catalog(page, shop_url)
    catalog.open()
    catalog.search(PRODUCT)
    product = catalog.open_product(PRODUCT)
    unit_price = money(product.price.inner_text())
    cart = product.add_to_cart()
    row = cart.row(PRODUCT)
    row.get_by_test_id("product-quantity").fill("2")
    row.get_by_test_id("product-quantity").press("Tab")
    expect(row.get_by_test_id("line-price")).to_have_text(f"${unit_price * 2:.2f}")
    expect(cart.total).to_have_text(f"${unit_price * 2:.2f}")


@pytest.mark.smoke
def test_customer_can_reach_checkout_from_search(page: Page, shop_url: str) -> None:
    """SHOP-07: A thin integration journey stops before identity and payment."""
    catalog = Catalog(page, shop_url)
    catalog.open()
    catalog.search(PRODUCT)
    cart = catalog.open_product(PRODUCT).add_to_cart()
    expect(cart.row(PRODUCT)).to_be_visible()
    cart.proceed()
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()
    page.get_by_role("tab", name="Continue as Guest", exact=True).click()
    expect(page.get_by_test_id("guest-first-name")).to_be_visible()
    expect(page.get_by_test_id("guest-email")).to_be_visible()
