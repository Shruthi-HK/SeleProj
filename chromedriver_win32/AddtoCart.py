from _selenium import webdriver
from _selenium.webdriver import Chrome
from time import sleep

driver = webdriver.Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com/books")

books = ['Health Book', 'Fiction', 'Computing and Internet']

for book in books:
    print(book)

    x_path = f"//a[text()='{book}']/../..//input[@value='Add to cart']"

    print(x_path)

    driver.find_element_by_xpath(x_path).click()

    sleep(2)




