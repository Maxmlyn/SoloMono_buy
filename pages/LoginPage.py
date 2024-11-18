from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    PAGE_URL = '/login.php'

    #List of page locators
    LOC_EMAIL_INPUT = "//input[contains(@name, 'email_address')]"
    LOC_PASSWORD_INPUT = ('xpath',"//input[contains(@name, 'password')]")
    LOC_SUBMIT_BUTTON = ('xpath',"//div[contains(@class,'form-group row')]//button[contains(@TYPE, 'submit')]")
    LOC_VALIDATION_TEXT = ('xpath',"//form[contains(@name,'login')]//div[contains(@role,'alert')]")


    #Page methods
    def type_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.LOC_EMAIL_INPUT)))
        email_input.clear()
        email_input.send_keys(email)

    def type_password(self, password):
        pass_input = self.driver.find_element(*self.LOC_PASSWORD_INPUT)
        pass_input.clear()
        pass_input.send_keys(password)

    def submit(self):
        self.driver.find_element(*self.LOC_SUBMIT_BUTTON).click()

    def validation(self):
        return self.driver.find_element(*self.LOC_VALIDATION_TEXT).text

