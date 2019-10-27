from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(executable_path="H:\selenium-chrome\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("http://www.newtours.demoaut.com")

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()

