from _selenium import webdriver
from _selenium.webdriver.support.select import Select
from _selenium.webdriver.chrome.service import Service
from time import sleep


driver = webdriver.Chrome("./chromedriver")
#open Chrome Browser

driver.get("https://www.facebook.com/")
# #navigate to facebook page
#
driver.find_element_by_xpath("//*[text()='Create New Account']").click()
sleep(3)
a = driver.find_element_by_xpath("//input[@name='firstname']")
sleep(3)
a.send_keys("Shruti")
# driver.find_element_by_("lastname").send_keys('Bhargav')
# driver.find_element_by_name("reg_email__").send_keys('shruthibhargav@gmail.com')
# #driver.find_element_by_name("")
# driver.find_element_by_id("password_step_input").send_keys('shruthi123')
# day = Select(driver.find_element_by_xpath("//Select[@title='Day'])"))
# day .select_by_visible_text("10")
# month = Select(driver.find_element_by_name('birthday_month'))
# month.select_by_visible_text("Dec")
# year = Select(driver.find_element_by_name('birthday_year'))
# year.select_by_visible_text("1995")
# driver.find_element_by_xpath("//label[text()='//label[text()='Female']']")
# driver.find_element_by_xpath("//button[text()='Sign Up']").click()





#
# password = driver.find_element_by_id("pass")
#
# submit = driver.find_element_by_id("Loginbutton")
#
# username.sendkeys("shruthi123@gmail.com")
#
# password.sendkeys("shru123")
#
# submit.click()









