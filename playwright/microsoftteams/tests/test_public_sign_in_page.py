from playwright.sync_api import expect, sync_playwright

from microsoftteams.pages.locators import TeamsSignLocators


def test_public_teams_sign_in_entry_point_is_visible():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        try:
            page.goto(TeamsSignLocators.LOGIN_URL, wait_until="domcontentloaded")
            expect(page.locator(TeamsSignLocators.SIGN_IN_BTN).first).to_be_visible(
                timeout=30_000
            )
        finally:
            browser.close()
