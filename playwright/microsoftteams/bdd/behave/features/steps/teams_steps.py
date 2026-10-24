import sys
from pathlib import Path

from behave import given, when, then


PLAYWRIGHT_PROJECT_ROOT = Path(__file__).resolve().parents[5]
if str(PLAYWRIGHT_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PLAYWRIGHT_PROJECT_ROOT))

from microsoftteams.bdd.support import (
    get_teams_credentials,
    open_teams_login_page,
    sign_in_to_teams,
)
from microsoftteams.pages.locators import TeamsSignLocators


@given("I provide my Teams email and password")
def provide_teams_credentials(context):
    context.email, context.password = get_teams_credentials()


@when("I sign in to Microsoft Teams")
def sign_in(context):
    context.playwright, context.browser, context.page = open_teams_login_page()
    sign_in_to_teams(context.page, context.email, context.password)


@then("the Teams home page is displayed")
def teams_home_page_is_displayed(context):
    chat_button = context.page.get_by_role(
        "button", name=TeamsSignLocators.CHAT_BUTTON_NAME, exact=True
    )
    chat_button.wait_for(state="visible")
    assert chat_button.is_visible()
