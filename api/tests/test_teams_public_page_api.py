import requests


TEAMS_WEB_URL = "https://www.microsoft.com/en-in/microsoft-teams/log-in"
REQUEST_TIMEOUT_SECONDS = 20
BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def test_teams_sign_in_page_is_reachable():
    response = requests.get(
        TEAMS_WEB_URL,
        headers=BROWSER_HEADERS,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )

    assert response.status_code == 200
    assert "text/html" in response.headers.get("Content-Type", "").lower()
    assert "teams" in response.text.lower() or "microsoft" in response.text.lower()
