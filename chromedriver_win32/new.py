from selenium.webdriver import Chrome
from time import sleep
import csv
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color


class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        print('Calling visisbility')
        print('   ', result)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False

def wait(func):
    def wrapper(*args, **kwargs):
        locator = args[0]
        print('Calling Wait ')
        print('     args : ', args,'   kwargs : ', kwargs)
        wait = WebDriverWait(driver, 20)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper


@wait
def click_element(locator):
    print(' Calling Click method')
    driver.find_element(*locator).click()


@wait
def enter_text(locator, * , value):
    print('Calling Enter Text method')
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(value)


# @wait
# def select_item(locator, *, item):
#     element = driver.find_element(*locator)
#     s = Select(element)
#     if isinstance(item, str):
#         s.select_by_visible_text(item)
#     elif isinstance(item, int):
#         s.select_by_index(item)
#     else:
#         raise TypeError


driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get('https://www.google.co.in/')
sleep(3)

print()
print()
click_element(("name", "q"))       # click_element = wait(click_element)
print()
print()
enter_text(("name", "q"), value='Shruthi H K')
print()
print()
click_element(('name', 'btnK'))
driver.close()


