from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Path to your ChromeDriver
service = Service(r"C:\Users\91917\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)

driver.get("https://www.flipkart.com/")
driver.maximize_window()

#Suppress login pop-up
try:
    popup_close_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '×') or contains(@class, 'close')]"))
    )
    popup_close_button.click()
except:
    print("No login popup or close button found, continuing...")

#Click on Login
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Login')]"))
    )
    login_button.click()

except Exception as e:
    print("Login button not found or not clickable:", e)

#Input mobile number and request otp
try:
    # Wait for the mobile input field and enter the mobile number
    mobile_input = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "r4vIwl"))
    )
    time.sleep(1)
    driver.minimize_window()

    mobile_number = input("Enter mobile number to receive OTP : ")
    driver.maximize_window()


    mobile_input.send_keys(str(mobile_number))  # Replace with desired number

    # Wait for the Request OTP button and click it
    otp_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "QqFHMw"))
    )
    otp_button.click()
    time.sleep(2)

except Exception as e:
    print("Error occurred:", e)


#Input OTP and click on verify
try:
    otp_input = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "XDRRi5"))
    )
    driver.minimize_window()

    otp = input("Enter OTP: ").strip()

    otp_boxes = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[@maxlength='1']"))
    )

    for i, digit in enumerate(otp):
        otp_boxes[i].send_keys(digit)

    driver.maximize_window()
      # Replace with the actual OTP

    # Step 4: Click the Verify button with type="submit"
    verify_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    verify_button.click()
    time.sleep(2)

except Exception as e:
    print("Error occurred:", e)
