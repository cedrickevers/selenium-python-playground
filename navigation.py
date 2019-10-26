import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="H:\selenium-chrome\chromedriver.exe")

driver.get("https://licorne-kawaii.com")

driver.find_element_by_xpath("/html/body/div[4]/div[1]/section/div/div/a[1]").click()
print(driver.title)
time.sleep(2)
driver.execute_script("window.history.go(-1)")

print(driver.title)
driver.execute_script("window.history.go(+1)")

driver.close()  # close the brower

