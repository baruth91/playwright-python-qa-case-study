"""Focused learning exercises on The Internet; these are not Toolshop business coverage."""

from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

pytestmark = pytest.mark.lab


def test_dropdown_selection_is_persisted_in_the_control(page: Page, lab_url: str) -> None:
    """LAB-01: Use the native select API, then assert the selected value."""
    page.goto(f"{lab_url}/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option(label="Option 2")
    expect(dropdown).to_have_value("2")
    expect(dropdown.locator("option:checked")).to_have_text("Option 2")


def test_checkboxes_can_be_set_to_an_explicit_state(page: Page, lab_url: str) -> None:
    """LAB-02: check/uncheck express intent independently of initial state."""
    page.goto(f"{lab_url}/checkboxes")
    checkboxes = page.get_by_role("checkbox")
    expect(checkboxes).to_have_count(2)
    checkboxes.nth(0).check()
    checkboxes.nth(1).uncheck()
    expect(checkboxes.nth(0)).to_be_checked()
    expect(checkboxes.nth(1)).not_to_be_checked()


def test_dynamic_loading_waits_for_the_visible_result(page: Page, lab_url: str) -> None:
    """LAB-03: A web-first assertion handles asynchronous rendering without sleep."""
    page.goto(f"{lab_url}/dynamic_loading/2")
    page.get_by_role("button", name="Start", exact=True).click()
    expect(page.locator("#finish")).to_have_text("Hello World!", timeout=15000)
    expect(page.locator("#finish")).to_be_visible()


def test_dynamic_input_becomes_editable(page: Page, lab_url: str) -> None:
    """LAB-04: Enabled state and accepted input are both observable outcomes."""
    page.goto(f"{lab_url}/dynamic_controls")
    form = page.locator("#input-example")
    field = form.get_by_role("textbox")
    expect(field).to_be_disabled()
    form.get_by_role("button", name="Enable", exact=True).click()
    expect(field).to_be_enabled(timeout=15000)
    field.fill("Ready for interaction")
    expect(field).to_have_value("Ready for interaction")


def test_confirm_dialog_cancellation_is_reflected_in_the_page(page: Page, lab_url: str) -> None:
    """LAB-05: Register the dialog handler before the action that creates it."""
    page.goto(f"{lab_url}/javascript_alerts")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm", exact=True).click()
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")


def test_upload_uses_a_disposable_text_file(page: Page, lab_url: str, tmp_path: Path) -> None:
    """LAB-06: Generate synthetic input; never upload a user's local document."""
    sample = tmp_path / "qa-learning-example.txt"
    sample.write_text("Synthetic file for a public automation exercise.\n", encoding="utf-8")
    page.goto(f"{lab_url}/upload")
    page.locator("#file-upload").set_input_files(sample)
    page.get_by_role("button", name="Upload", exact=True).click()
    expect(page.get_by_role("heading", name="File Uploaded!", exact=True)).to_be_visible()
    expect(page.locator("#uploaded-files")).to_have_text(sample.name)


def test_nested_frame_content_can_be_targeted_explicitly(page: Page, lab_url: str) -> None:
    """LAB-07: Frame locators express the document boundary before finding content."""
    page.goto(f"{lab_url}/nested_frames")
    middle = page.frame_locator('frame[name="frame-top"]').frame_locator(
        'frame[name="frame-middle"]'
    )
    expect(middle.locator("#content")).to_have_text("MIDDLE")
