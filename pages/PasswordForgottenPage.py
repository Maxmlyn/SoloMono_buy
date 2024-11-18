from pages.BasePage import BasePage



class PasswordForgottenPage(BasePage):

    #PAGE_URL = "/password_forgotten.php"
    PAGE_URL = ""

# List of page locators
    LOC_PASSWORD_FORGOTTEN_LINK = ("xpath", "//form[contains(@name,'login')]//a[@href='password_forgotten.php']")
    LOC_PASSWORD_FORGOTTEN_EMAIL_INPUT = ("xpath", "//input[@id='inputEmail_address']")
    LOC_PASSWORD_FORGOTTEN_BACK_BUTTON = ("xpath", "//input[@id='inputEmail_address']//following::a[contains(@href,'login.php')]')]")
    LOC_PASSWORD_FORGOTTEN_CONTINUE_BUTTON = ("xpath", "//input[@id='inputEmail_address']//following::a[contains(@href,'login.php')]//following-sibling::button[contains(@type,'submit')]")
    LOC_PASSWORD_FORGOTTEN_RESULT = ("xpath", "//div[contains(@role,'alert')]")

# Page methods
    def open_pf_page(self):
        self.driver.find_element(*self.LOC_PASSWORD_FORGOTTEN_LINK).click()

    def type_email(self, email):
        email_input = self.driver.find_element(*self.LOC_PASSWORD_FORGOTTEN_EMAIL_INPUT)
        email_input.click()
        email_input.send_keys(email)

    def click_back(self):
        self.driver.find_element(*self.LOC_PASSWORD_FORGOTTEN_BACK_BUTTON).click()

    def click_continue(self):
        self.driver.find_element(*self.LOC_PASSWORD_FORGOTTEN_CONTINUE_BUTTON).click()

    def get_result(self):
        return self.driver.find_element(*self.LOC_PASSWORD_FORGOTTEN_RESULT).text


