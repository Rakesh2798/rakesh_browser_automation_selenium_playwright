import sys
from pathlib import Path

import pytest
from pytest_bdd import given, scenario, then, when


PLAYWRIGHT_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PLAYWRIGHT_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PLAYWRIGHT_PROJECT_ROOT))

from microsoftteams.bdd.support import (
    close_browser,
    get_teams_credentials,
    open_teams_login_page,
    sign_in_to_teams,
)
from microsoftteams.pages.locators import TeamsSignLocators


@scenario("features/teams_login.feature", "User signs in to Microsoft Teams")
def test_user_signs_in_to_microsoft_teams():
    pass


@given("I provide my Teams email and password", target_fixture="teams_login_state")
def provide_teams_credentials():
    email, password = get_teams_credentials()
    return {"email": email, "password": password}


@when("I sign in to Microsoft Teams", target_fixture="teams_login_state")
def sign_in(teams_login_state, request):
    playwright, browser, page = open_teams_login_page()
    request.addfinalizer(lambda: close_browser(playwright, browser))
    sign_in_to_teams(page, teams_login_state["email"], teams_login_state["password"])
    return {**teams_login_state, "page": page}


@then("the Teams home page is displayed")
def teams_home_page_is_displayed(teams_login_state):
    chat_button = teams_login_state["page"].get_by_role(
        "button", name=TeamsSignLocators.CHAT_BUTTON_NAME, exact=True
    )
    chat_button.wait_for(state="visible")
    assert chat_button.is_visible()
