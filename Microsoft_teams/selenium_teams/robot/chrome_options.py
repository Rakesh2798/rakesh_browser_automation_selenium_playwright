from selenium.webdriver import ChromeOptions


def create_chrome_options(headless=False):
    """Create Chrome options, optionally for a non-interactive CI agent."""
    options = ChromeOptions()
    if str(headless).strip().lower() in {"true", "yes", "1"}:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    return options
