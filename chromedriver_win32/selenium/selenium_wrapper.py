from selenium.webdriver.support.select import Select
from chromedriver_win32.selenium.wait import wait

class Selenium_Wrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait
    def click_element(self, locator):
        """
        Clicks on the element
        useage: click_element("id", "register")
        """
        self.driver.find_element(*locator).click()       # find_element("link text", "register")

    @wait
    def enter_text(self, locator, *, value):
        """enters something inside the text box"""
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def select_item(self, locator, *, item):
        """Selects some item from the listbox"""
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise TypeError