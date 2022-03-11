from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from chromedriver_win32.selenium.config import Config

class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False

def wait(func):
    def wrapper(*args, **kwargs):       # args = (self, ("link text", "Register"))
        # args = (("name", "FirstName"), ) kwargs = {value="hello"}
        instance = args[0]
        locator = args[1]
        wait = WebDriverWait(instance.driver, Config.MAX_TIMEOUT)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        # click_element(("link text", "Register"))
        # enter_text(("name", "fname"), value="hello")
        return func(*args, **kwargs)        # actual generic func gets executed
    return wrapper