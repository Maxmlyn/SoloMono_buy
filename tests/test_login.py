import time
import pytest
from selenium.webdriver.common.bidi.cdp import session_context

from pages.LoginPopup import LoginPopup

class TestLogin:

    def setup_method(self):
        self.login_popup = LoginPopup(self.driver)

    @pytest.fixture
    def test_run_site(self):
        self.login_popup.open()

    @pytest.fixture
    def test_open_login_popup(self, test_run_site):
        self.login_popup.open_login_popup()

    @pytest.fixture
    def test_fill_in_email(self, test_open_login_popup):
        self.login_popup.enter_email('maksym.sukhomlyn91+1@gmail.com')

    @pytest.fixture
    def test_fill_in_password(self, test_fill_in_email):
        self.login_popup.enter_password('123456')

    @pytest.fixture
    def test_submit(self, test_fill_in_password):
        self.login_popup.click_login_button()

    @pytest.fixture
    def test_user_is_logged_in(self, test_submit):
        assert self.login_popup.user_is_logged_in() == "My account"
        print("User is logged in successfully")

        title = self.login_popup.get_site_title()
        assert title == "Solomono Template demo"
        print(title)

        url = self.login_popup.get_current_url()
        assert url == "https://demo.solomono.net/"
        print(url)

    def test_log_off(self, test_user_is_logged_in):
        self.login_popup.log_off()
        time.sleep(2)
        assert "Log into your Account" in self.login_popup.get_login_link_text()