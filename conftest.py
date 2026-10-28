"""Shared configuration; each test gets a fresh browser context from pytest-playwright."""

import os
from collections.abc import Iterator

import pytest
from playwright.sync_api import APIRequestContext, Playwright


@pytest.fixture(scope="session", autouse=True)
def test_id_contract(playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(scope="session")
def shop_url() -> str:
    return os.getenv("SHOP_URL", "https://practicesoftwaretesting.com").rstrip("/")


@pytest.fixture(scope="session")
def lab_url() -> str:
    return os.getenv("LAB_URL", "https://the-internet.herokuapp.com").rstrip("/")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    return {
        **browser_context_args,
        "locale": "en-US",
        "viewport": {"width": 1440, "height": 1000},
    }


@pytest.fixture
def api(playwright: Playwright) -> Iterator[APIRequestContext]:
    context = playwright.request.new_context(
        base_url=os.getenv("SHOP_API_URL", "https://api.practicesoftwaretesting.com"),
        extra_http_headers={"Accept": "application/json"},
        timeout=15000,
    )
    yield context
    context.dispose()
