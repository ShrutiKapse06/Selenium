from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

service = Service(r"C:\Users\91917\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/")

#Absolute path
#username = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
#username.send_keys("trial_1")
#time.sleep(2)

#relative path
username = driver.find_element(By.XPATH, "//*[@id='email']")
username.send_keys("trial_2")
time.sleep(2)
