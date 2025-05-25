# Open Web browser - Chrome
# Open URL https://opensource-demo.orangehrmlive.com/
# Enter username (Admin)
# Enter password (admin123)
# Click on login
# Capture title of the home page (Actual title)
# Verify title of the HomePage : OrangeHRM (Expected)
# close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time  # Optional, just to see the flow clearly

# Path to your ChromeDriver
service = Service(r"C:\Users\91917\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the OrangeHRM demo site
driver.get("https://opensource-demo.orangehrmlive.com/")

# Optional: Wait for page to load
time.sleep(2)

# Find username and password fields and enter values
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.clear()
password.clear()
username.send_keys("Admin")
password.send_keys("admin123")

# Click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

actual_title = driver.title
exp_title = "OrangeHRM"

if actual_title == exp_title:
    print("Login test Passed!!! -----------------")

else:
    print("Login Test Failed |||||||||||||||||||||")

# Optional: Wait to observe the logged-in page
time.sleep(5)

# Close the browser
driver.quit()
