import time
import pytest

from pages.PasswordForgottenPage import PasswordForgottenPage

my_email = 'maksym.sukhomlyn91+1@gmail.com'

class TestPasswordForgotten:

    def setup_method(self):
        self.pf_page = PasswordForgottenPage(self.driver)
        time.sleep(3)

    @pytest.fixture
    def test_run_site(self):
        self.pf_page.open()
        time.sleep(3)

    @pytest.fixture
    def test_open_login_popup(self, test_run_site):
        self.pf_page.open_login_popup()
        time.sleep(3)

    @pytest.fixture
    def test_get_pf_page(self, test_open_login_popup):
        self.pf_page.open_pf_page()
        time.sleep(3)

    @pytest.fixture
    def test_site_title(self,test_get_pf_page):
        current_title = self.pf_page.get_site_title()
        assert current_title == 'Forgotten password'

    @pytest.fixture
    def test_site_url(self, test_site_title):
        current_url = self.pf_page.get_current_url()
        assert current_url == 'https://demo.solomono.net/password_forgotten.php'

    @pytest.fixture()
    def test_fill_in_email_input(self, test_site_url):
        self.pf_page.type_email(my_email)

    @pytest.fixture()
    def test_submit(self, test_fill_in_email_input):
        self.pf_page.click_continue()

    def test_result(self, test_submit):
        result_text = self.pf_page.get_result()
        print(result_text)
        assert result_text == "×\nClose\n Success: A new password has been sent to your e-mail address."

