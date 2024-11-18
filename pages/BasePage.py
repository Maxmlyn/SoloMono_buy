import pytest

from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    MAIN_URL = "https://demo.solomono.net"

#List of page locators
    LOC_LANGUAGE = ('xpath', "//button[contains(@class, 'language-dropdown-button')]")
    LOC_CURRENCIES = ('xpath', "//div[contains(@class, 'selectize-control single')]")
    LOC_HOME_LINK = ""
    LOC_BRANDS_LINK = ""
    LOC_PAYMENT_AND_SHOPPING_LINK = ""
    LOC_WARRANTY_LINK = ""
    LOC_CONTACTS_LINK = ""
    LOC_LOGIN_LINK = ("xpath", "//*[contains(@class, 'enter_link')]")
    LOC_HOME_LOGO = ""
    LOC_QUICK_FIND_INPUT = ('xpath', "//input[@id='searchpr']")
    LOC_QUICK_FIND_SEARCH_ICON = ('xpath', "//button[@id='search-form-button']")
    LOC_CART = ""
    LOC_LAPTOPS_TAB = ""
    LOC_TABLET_TAB = ""
    LOC_SMARTPHONE_TAB = ""
    LOC_GAMES_TAB = ""
    LOC_TV_TAB = ""
    LOC_APPLIANCE_TAB = ""
    LOC_ELECTRIC_TRANSPORT_TAB = ""
    LOC_ACCESSORIES_TAB = ""
    LOC_SCROLL_ICON = ('xpath', "//div[contains(@class, 'scrollup')]")
    LOC_SEARCH_RESULT = "//h1[contains(@class, 'category_heading')]"
    LOC_MY_ACCOUNT_BUTTON = ("xpath", "//div[contains(@class, 'enter_registration')]//a[@href='account_history.php']")

# Page methods
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(f"{self.MAIN_URL}{self.PAGE_URL}")

    def get_site_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_language(self):
        language = self.driver.find_element(*self.LOC_LANGUAGE)
        return language

    def get_currency(self):
        currency = self.driver.find_element(*self.LOC_CURRENCIES)
        return currency

    def get_search_input(self, search_value):
        search_input = self.driver.find_element(*self.LOC_QUICK_FIND_INPUT)
        search_input.send_keys(search_value)
        search_icon = self.driver.find_element(*self.LOC_QUICK_FIND_SEARCH_ICON)
        search_icon.click()
        search_result_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.LOC_SEARCH_RESULT))).text
        return search_result_text

    def open_login_popup(self):
        self.driver.find_element(*self.LOC_LOGIN_LINK).click()

    def get_login_link_text(self):
        return self.driver.find_element(*self.LOC_LOGIN_LINK).text

    def user_is_logged_in(self):
        return self.driver.find_element(*self.LOC_MY_ACCOUNT_BUTTON).text