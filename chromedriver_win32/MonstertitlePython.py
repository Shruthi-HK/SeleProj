from _selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.monsterindia.com")

driver.find_element_by_xpath("//@id = 'query_autocomplete']").sendkeys('python')

driver.find_element_by_xpath("//a[text() = 'Python Developer']").click()

driver.find_element_by_xpath("//input[@name = 'fts']").click()

driver.find_element_by_xpath("//input[@value = 'Search']").click()




