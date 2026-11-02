import os
import sys
from getpass import getpass
from pathlib import Path

import pytest

# Add the Selenium project root so this test imports Selenium's page object.
SELENIUM_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SELENIUM_ROOT))

from selenium_teams.pages.teams_page import TeamsSign


def get_masked_password(
    prompt_text: str = "Teams password: ",
) -> str:
    """Hide password input in a terminal; use visible input in PyCharm's Run console."""
    if os.environ.get("PYCHARM_HOSTED") and not sys.stdin.isatty():
        return input(prompt_text).strip()

    try:
        return getpass(prompt_text).strip()
    except (EOFError, OSError):
        return input(prompt_text).strip()


def run_teams_login_and_navigation(email: str, password: str) -> None:
    t = TeamsSign()
    try:
        t.sign_in_teams()
        t.send_email_id(email)
        t.enter_email_password(password)
        t.click_chat_button()
        t.click_meet_button()
        t.click_people_button()
        t.click_copilot_button()
        t.click_communities_button()
        t.click_activity_button()
        t.click_calender_button()

        print("\nPASS: Teams sign-in and navigation completed successfully.")
    finally:
        t.driver.quit()


def test_teams_login_and_navigation() -> None:
    email = input("Teams email: ").strip()
    password = get_masked_password()

    if not email or not password:
        pytest.fail("Email and password are required to start the test.")

    # The browser opens only after both credentials have been entered.
    run_teams_login_and_navigation(email, password)


if __name__ == "__main__":
    test_teams_login_and_navigation()
