from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"C:\Users\91917\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/")

#tag & id (tagname#valueID)
#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")

#tag & class (tagname.valueClass)
#driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@abc")
#time.sleep(2)

#tag & attribute (tagname[attribute=value])
#driver.find_element(By.CSS_SELECTOR, "input[type=text]").send_keys("abc@123")
#time.sleep(2)

#tag, class and attribute (tagname.valueClass[attribute=value])
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal-pass]").send_keys("123")
time.sleep(2)
