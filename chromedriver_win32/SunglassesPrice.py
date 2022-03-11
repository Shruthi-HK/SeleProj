from _selenium  import webdriver

from time import sleep

import re

driver = webdriver.Chrome("./chromedriver")

driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/sunglasses")

sunglasses = { 'ORIGINAL COLLECTION': 149.00, 'Custom Sunglasses': 179.00, 'Sunglasses Aero': 139.00 }

for glass, expected_price in sunglasses.items():

    _xpath = f"//span[text()='{glass}']/../../..//span[@class='art-price']"

    actual_price = driver.find_element_by_xpath(_xpath).text

    actual_price = re.findall(r"\d+\.\d+",actual_price)

    if float(actual_price[0]) == expected_price:

        print("PASS")

    else:

        print("FAIL")

