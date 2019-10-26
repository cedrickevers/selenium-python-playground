from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="H:\selenium-chrome\chromedriver.exe")

driver.get("https://ryver.com/")

print(driver.title) # Title of the page
print(driver.current_url)
driver.find_element_by_xpath('//*[@id="btnSignupIntegrate"]').click()
time.sleep(5)
driver.close()  # close the brower
