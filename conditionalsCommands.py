from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome(executable_path="H:\selenium-chrome\chromedriver.exe")
driver.get("http://www.newtours.demoaut.com/")
ele=driver.find_element_by_name("userName")
print(ele.is_displayed())
print(ele.is_enabled())

p_ele=driver.find_element_by_name("password")
print(p_ele.is_displayed())
print(p_ele.is_enabled())

ele.send_keys("test")
p_ele.send_keys("test")
driver.find_element_by_name("login").click()

ele=driver.find_element_by_name("userName")
p_ele=driver.find_element_by_name("password")

ele.send_keys("test")
p_ele.send_keys("test")
driver.find_element_by_name("login").click()

roundtrip=driver.find_element_by_css_selector("input[value=roundtrip]")


print(roundtrip.is_selected())


time.sleep(2)

driver.close()