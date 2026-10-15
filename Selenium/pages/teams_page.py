import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import TeamsSignLocators


class TeamsSign:

    def __init__(self, timeout=60):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, timeout)
        self.teams = TeamsSignLocators()

    def _switch_to_login_window(self):
        """Poll every open window until one contains the email field."""
        def found(driver):
            for handle in driver.window_handles:
                driver.switch_to.window(handle)
                if driver.find_elements(*self.teams.EMAIL_INPUT):
                    return True
            return False
        self.wait.until(found)

    def sign_in_teams(self):
        self.driver.get(self.teams.LOGIN_URL)
        self.wait.until(EC.element_to_be_clickable(self.teams.SIGN_IN_BTN)).click()
        self._switch_to_login_window()

    def send_email_id(self, email_address):
        field = self.wait.until(EC.element_to_be_clickable(self.teams.EMAIL_INPUT))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(email_address)

        # Fallback: the page uses Knockout bindings, so set the value via the
        # native setter and fire an 'input' event if typing didn't register.
        if field.get_attribute("value") != email_address:
            self.driver.execute_script(
                """
                const el = arguments[0];
                Object.getOwnPropertyDescriptor(
                    HTMLInputElement.prototype, 'value'
                ).set.call(el, arguments[1]);
                el.dispatchEvent(new Event('input', {bubbles: true}));
                """,
                field,
                email_address,
            )
        assert field.get_attribute("value") == email_address, "Email was not entered"
        self.wait.until(EC.element_to_be_clickable(self.teams.NEXT_BTN_1)).click()

    def enter_email_password(self,password):
        field = self.wait.until(EC.element_to_be_clickable(self.teams.USE_YOUR_PASSWORD))
        field.click()
        field = self.wait.until(EC.element_to_be_clickable(self.teams.PASSWORD_INPUT))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.teams.NEXT_BTN_2)).click()
        self.wait.until(EC.element_to_be_clickable(self.teams.NO_BUTTON)).click()
        time.sleep(60)

    def click_chat_button(self):
        field = self.wait.until(EC.element_to_be_clickable(self.teams.CHAT_BUTTON_XPATH))
        field.click()
        time.sleep(20)

    def click_meet_button(self):
        field = self.wait.until(EC.element_to_be_clickable(self.teams.MEET_BUTTON_XPATH))
        field.click()
        time.sleep(20)

    def click_people_button(self):
        field = self.wait.until(EC.element_to_be_clickable(self.teams.PEOPLE_BUTTON_XPATH))
        field.click()
        time.sleep(20)

    def click_copilot_button(self):
        field = self.wait.until(EC.element_to_be_clickable(self.teams.COPILOT_BUTTON_XPATH))
        field.click()
        time.sleep(20)

    def click_communities_button(self):
        field = self.wait.until(EC.element_to_be_clickable(self.teams.COMMUNITIES_XPATH))
        field.click()
        time.sleep(20)

    def click_activity_button(self):
        field = self.wait.until(EC.element_to_be_clickable(self.teams.ACTIVITY_XPATH))
        field.click()
        time.sleep(20)

    def click_calender_button(self):
        field = self.wait.until(EC.element_to_be_clickable(self.teams.CALENDAR_XPATH))
        field.click()
        time.sleep(20)
        field = self.wait.until(EC.element_to_be_clickable(self.teams.NEW_MEETING_XPATH))
        field.click()
        time.sleep(20)
        field = self.wait.until(EC.element_to_be_clickable(self.teams.SAVE_BUTTON_XPATH1))
        field.click()
        time.sleep(20)
