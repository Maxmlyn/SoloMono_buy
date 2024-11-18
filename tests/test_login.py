import time
import pytest

from pages.LoginPopup import LoginPopup

class TestLogin:

    def setup_method(self):
        self.login_popup = LoginPopup(self.driver)

    @pytest.fixture
    def test_login_into_system(self):
        self.login_popup.open()
        self.login_popup.open_login_popup()
        self.login_popup.enter_email('email')
        self.login_popup.enter_password('password')
        self.login_popup.click_login_button()

    @pytest.fixture
    def test_user_is_logged_in(self, test_login_into_system):
        assert self.login_popup.logged_in() == "My account"
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