import time
import pytest

from pages.LoginPage import LoginPage
from parameterized import parameterized

class TestLoginPage:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.open()

    @pytest.mark.parametrize("my_email, my_pass, expected", [('test@email.com',"654321" ,'×\nClose\n Error: No match for E-Mail Address and/or Password.'),
                                                    (' ', ' ', '×\nClose\n Error: No match for E-Mail Address and/or Password.'),
                                                    ('', '', '×\nClose\n Error: No match for E-Mail Address and/or Password.'),
                                                    ('maksym.sukhomlyn91+1@gmail.com', '123456', 'My account')
                                                    ])
    def test_email(self, my_email, my_pass, expected):
        self.login_page.type_email(my_email)
        self.login_page.type_password(my_pass)
        self.login_page.submit()
        if my_email == 'maksym.sukhomlyn91+1@gmail.com':
            text = self.login_page.user_is_logged_in()
            assert text == expected
        else:
            val_text = self.login_page.validation()
            assert val_text == expected