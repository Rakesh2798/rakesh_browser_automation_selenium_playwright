import os

import pytest
import requests


GRAPH_ME_URL = "https://graph.microsoft.com/v1.0/me"
REQUEST_TIMEOUT_SECONDS = 15


def test_me_rejects_request_without_access_token():
    response = requests.get(GRAPH_ME_URL, timeout=REQUEST_TIMEOUT_SECONDS)

    assert response.status_code == 401
    error = response.json().get("error", {})
    assert error.get("code")


def test_me_returns_signed_in_user_profile_with_delegated_token():
    access_token = os.getenv("MICROSOFT_GRAPH_ACCESS_TOKEN")
    if not access_token:
        pytest.skip("Set MICROSOFT_GRAPH_ACCESS_TOKEN to run the authenticated Graph API test")

    response = requests.get(
        GRAPH_ME_URL,
        headers={"Authorization": f"Bearer {access_token}"},
        params={"$select": "id,displayName,userPrincipalName"},
        timeout=REQUEST_TIMEOUT_SECONDS,
    )

    assert response.status_code == 200, (
        f"Microsoft Graph returned HTTP {response.status_code}; "
        "check that the token is valid and has delegated User.Read permission"
    )
    profile = response.json()
    assert isinstance(profile.get("id"), str) and profile["id"]
    assert isinstance(profile.get("displayName"), str) and profile["displayName"]
