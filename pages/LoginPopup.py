from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPopup(BasePage):

    PAGE_URL = ""

# List of page locators
    LOC_LOGIN_LINK = ("xpath", "//*[contains(@class, 'enter_link')]")
    LOC_EMAIL_INPUT = "//form[contains(@name, 'login')]//input[contains(@type, 'email')]"
    LOC_PASSWORD_INPUT = ("xpath", "//form[contains(@name, 'login')]//input[contains(@type, 'password')]")
    LOC_LOGIN_BUTTON = ("xpath", "//form[contains(@name, 'login')]//button[contains(@type, 'submit')]")
    LOC_MY_ACCOUNT_BUTTON = ("xpath", "//div[contains(@class, 'enter_registration')]//a[@href='account_history.php']")
    LOC_LOG_OFF_LINK = "//div[contains(@class, 'enter_registration')]//a[@href='logoff.php']"

# Page methods
    def open_login_popup(self):
        self.driver.find_element(*self.LOC_LOGIN_LINK).click()

    def get_login_link_text(self):
        return self.driver.find_element(*self.LOC_LOGIN_LINK).text

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.LOC_EMAIL_INPUT)))
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.LOC_PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        submit_button = self.driver.find_element(*self.LOC_LOGIN_BUTTON)
        submit_button.click()

    def logged_in(self):
        return self.driver.find_element(*self.LOC_MY_ACCOUNT_BUTTON).text

    def log_off(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.LOC_LOG_OFF_LINK))).click()