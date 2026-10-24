"""Shared browser helpers for the Python BDD examples."""

import sys
import time
import getpass
import os
import sys
import warnings
from pathlib import Path


PLAYWRIGHT_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PLAYWRIGHT_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PLAYWRIGHT_PROJECT_ROOT))

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

from microsoftteams.pages.locators import TeamsSignLocators


def open_teams_login_page():
    """Open the Microsoft account sign-in page in Chromium."""
    print("Opening the Teams sign-in page...", flush=True)
    playwright = sync_playwright().start()
    browser = None
    try:
        headless = os.environ.get("TEAMS_HEADLESS", "false").lower() in {
            "1",
            "true",
            "yes",
        }
        browser = playwright.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        page.goto(
            TeamsSignLocators.LOGIN_URL,
            wait_until="domcontentloaded",
            timeout=30000,
        )
        page.locator(TeamsSignLocators.SIGN_IN_BTN).first.click(timeout=30000)

        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            for candidate in context.pages:
                email_field = candidate.get_by_placeholder(
                    TeamsSignLocators.EMAIL_PLACEHOLDER
                )
                try:
                    email_field.wait_for(state="visible", timeout=500)
                    print("Microsoft sign-in form is ready.", flush=True)
                    return playwright, browser, candidate
                except PlaywrightTimeoutError:
                    continue
            page.wait_for_timeout(200)

        raise PlaywrightTimeoutError(
            "Teams sign-in email field did not become visible after clicking Sign in"
        )
    except Exception:
        close_browser(playwright, browser)
        raise


def get_teams_credentials():
    """Load Teams credentials from environment or securely prompt for them."""
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                name, value = line.split("=", 1)
                os.environ.setdefault(name.strip(), value.strip().strip("'\""))

    email = os.environ.get("TEAMS_EMAIL")
    password = os.environ.get("TEAMS_PASSWORD")
    if not email or not password:
        print(
            "Teams credentials are not configured; enter them when prompted.",
            flush=True,
        )
    if not email:
        try:
            print("Enter Teams email: ", end="", flush=True)
            email = input().strip()
        except (OSError, EOFError) as exc:
            raise RuntimeError(
                "Set TEAMS_EMAIL or run interactively to enter your Teams email."
            ) from exc
    if not password:
        try:
            from prompt_toolkit import prompt

            password = prompt(
                "Enter Teams password (characters hidden): ", is_password=True
            ).strip()
        except ImportError:
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("error", getpass.GetPassWarning)
                    password = getpass.getpass(
                        "Enter Teams password (characters hidden): "
                    ).strip()
            except getpass.GetPassWarning as exc:
                raise RuntimeError(
                    "This terminal cannot hide password input. Install prompt_toolkit "
                    "or set TEAMS_PASSWORD in the ignored project .env file."
                ) from exc
        except (OSError, EOFError) as exc:
            raise RuntimeError(
                "Set TEAMS_PASSWORD or run interactively to enter your Teams password."
            ) from exc

    if not email or not password:
        raise RuntimeError("Both Teams email and password are required.")
    return email, password


def sign_in_to_teams(page, email, password):
    """Submit credentials and wait for the authenticated Teams navigation."""
    print("Submitting Teams email...", flush=True)
    page.get_by_placeholder(TeamsSignLocators.EMAIL_PLACEHOLDER).fill(email)
    page.get_by_role("button", name=TeamsSignLocators.NEXT_BUTTON_NAME).click()

    password_field = page.get_by_role(
        "textbox", name=TeamsSignLocators.PASSWORD_FIELD_NAME
    )
    use_password = page.get_by_role(
        "button", name=TeamsSignLocators.USE_PASSWORD_BUTTON_NAME
    )
    password_field.or_(use_password).first.wait_for(state="visible", timeout=30000)
    if use_password.is_visible():
        use_password.click()

    password_field.wait_for(state="visible", timeout=15000)
    print("Submitting Teams password...", flush=True)
    password_field.fill(password)
    page.get_by_role("button", name=TeamsSignLocators.NEXT_BUTTON_NAME).click()

    stay_signed_in_no = page.get_by_role(
        "button", name=TeamsSignLocators.NO_BUTTON_NAME, exact=True
    )
    try:
        stay_signed_in_no.wait_for(state="visible", timeout=5000)
        stay_signed_in_no.click()
    except PlaywrightTimeoutError:
        pass

    try:
        print(
            "Waiting for the Teams home page (complete MFA in the browser if prompted)...",
            flush=True,
        )
        page.get_by_role(
            "button", name=TeamsSignLocators.CHAT_BUTTON_NAME, exact=True
        ).wait_for(state="visible", timeout=90000)
    except PlaywrightTimeoutError as exc:
        raise PlaywrightTimeoutError(
            "Teams home page did not appear. Check the credentials and complete any "
            "MFA or security verification in the browser."
        ) from exc


def close_browser(playwright, browser):
    try:
        if browser:
            browser.close()
    finally:
        if playwright:
            playwright.stop()
