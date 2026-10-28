"""Read-only API checks complement the browser suite; no seeded IDs are hard-coded."""

from decimal import Decimal

import pytest
from playwright.sync_api import APIRequestContext

pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_catalog_exposes_products_with_usable_prices(api: APIRequestContext) -> None:
    """API-01: A minimal consumer contract for a catalog page."""
    response = api.get("/products")
    assert response.status == 200
    assert "application/json" in response.headers.get("content-type", "")
    payload = response.json()
    assert isinstance(payload["data"], list) and payload["data"]
    for product in payload["data"]:
        assert isinstance(product["id"], str) and product["id"]
        assert isinstance(product["name"], str) and product["name"].strip()
        assert Decimal(str(product["price"])) >= 0


def test_product_details_match_the_catalog_entry(api: APIRequestContext) -> None:
    """API-02: Catalog and detail views must refer to the same product and price."""
    listing = api.get("/products")
    assert listing.status == 200
    products = listing.json()["data"]
    assert products, "Demo catalog is empty"
    expected = products[0]
    response = api.get(f"/products/{expected['id']}")
    assert response.status == 200
    actual = response.json()
    assert actual["id"] == expected["id"]
    assert actual["name"] == expected["name"]
    assert Decimal(str(actual["price"])) == Decimal(str(expected["price"]))
