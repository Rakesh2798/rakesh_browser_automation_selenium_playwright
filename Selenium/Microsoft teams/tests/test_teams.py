import sys
import os

# Add the project root to sys.path so we can import 'pages'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.teams_page import TeamsSign

def test_teams_login_and_navigation(email: str, password: str):
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

def get_masked_password(prompt_text: str = "Enter your Teams password: ") -> str:
    """Prompt for password, masking input with asterisks (*) in real terminals,
    or falling back to input() in IDE run consoles (like PyCharm) to prevent hanging.
    """
    import os
    import sys

    # In PyCharm's default Run console or non-tty environments, prompt_toolkit and getpass hang indefinitely
    if os.environ.get("PYCHARM_HOSTED") and not sys.stdin.isatty():
        return input(prompt_text).strip()

    if sys.stdin.isatty():
        try:
            from prompt_toolkit import prompt
            return prompt(prompt_text, is_password=True).strip()
        except Exception:
            pass

        import getpass
        try:
            return getpass.getpass(prompt_text).strip()
        except Exception:
            pass

    return input(prompt_text).strip()


if __name__ == "__main__":
    email = input("Enter your Teams email ID: ").strip()
    password = get_masked_password("Enter your Teams password: ")

    if not email or not password:
        print("Error: Email and password are required to start the test.")
        sys.exit(1)

    print("\nStarting Teams automation test...")
    test_teams_login_and_navigation(email, password)

