from _selenium import webdriver

from time import sleep

from _selenium.webdriver.chrome.service import Service

from _selenium .webdriver.common.action_chains import ActionChains
#mouseover,doubleclick,

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.myntra.com/")

sleep(5)

actions = ActionChains(driver)

profile = driver.find_element_by_xpath("//span[text()='Profile']")

actions.move_to_element(profile).perform()
#web element on which the web element have to mouseoveron use move_to_element
sleep(1)

driver.find_element_by_xpath("//a[text()='login / Signup']").click()

