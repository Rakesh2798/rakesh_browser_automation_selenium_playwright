*** Settings ***
Library           SeleniumLibrary
Library           ${CURDIR}/chrome_options.py
Suite Setup       Open Teams Sign-In Page
Suite Teardown    Close All Browsers

*** Variables ***
${TEAMS_LOGIN_URL}       https://www.microsoft.com/en-in/microsoft-teams/log-in
${SIGN_IN_BUTTON}        xpath://span[normalize-space()='Sign in']
${HEADLESS}              ${FALSE}

*** Test Cases ***
Teams sign-in entry point is visible
    Given the Teams sign-in page is open
    When I look for the sign-in entry point
    Then the sign-in entry point is visible

*** Keywords ***
Open Teams Sign-In Page
    ${chrome_options}=    Create Chrome Options    ${HEADLESS}
    Open Browser    ${TEAMS_LOGIN_URL}    chrome    options=${chrome_options}
    Maximize Browser Window

The Teams sign-in page is open
    Wait Until Element Is Visible    ${SIGN_IN_BUTTON}    timeout=30s

I look for the sign-in entry point
    Element Should Be Visible    ${SIGN_IN_BUTTON}

The sign-in entry point is visible
    Element Should Be Visible    ${SIGN_IN_BUTTON}
