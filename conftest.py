import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()

'''
    @pytest.fixture(autouse=True, params=["Chrome", "Firefox", "Edge"])
    def driver(request):
        if request.param == "Chrome":
            driver = webdriver.Chrome()
        elif request.param == "Firefox":
            driver = webdriver.Firefox()
        elif request.param == "Edge":
            driver = webdriver.Edge()
        request.cls.driver = driver
        driver.maximize_window()
        yield
        driver.quit()'''