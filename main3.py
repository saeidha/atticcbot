import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user = "Default"


main_user_path = "/Users/saeid/Library/Application Support/Google/Chrome/"
metamask_extension_path = f"{main_user_path}{user}/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn"
metamask_extension_path =  "/Users/saeid/Library/Application Support/Google/Chrome/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.30.4_0/"


# تنظیمات مرورگر کروم
chrome_options = webdriver.ChromeOptions() 
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # غیرفعال کردن ویژگی‌های تشخیص خودکار مرورگر کروم
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation',
'disable-background-networking',
'disable-client-side-phishing-detection',
'disable-default-apps',
'disable-hang-monitor',
'disable-popup-blocking',
'disable-prompt-on-repost',
'disable-sync',
'allow-pre-commit-input',
'enable-logging',
'log-level',
'no-first-run',
'no-service-autorun',
'password-store',
'profile-directory',
'remote-debugging-port',
'test-type',
'use-mock-keychain',
'flag-switches-begin',
'flag-switches-end'])

# profile
chrome_options.add_argument(f"profile-directory={user}")
chrome_options.add_argument(f"user-data-dir={main_user_path}")

# ایجاد شیء درایور مرورگر کروم
driver = webdriver.Chrome(executable_path="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome", options= chrome_options)

driver.get("https://atticc.xyz/")

wait = WebDriverWait(driver, 5)
popup_window = wait.until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[1])

driver.get("https://atticc.xyz/")
time.sleep(5)
button = driver.find_element_by_xpath("//button[text()='Connect Wallet']")
button.click()
# driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/notification.html")
# password_field = driver.find_element("id", "password")
# password_field.send_keys("S12saeed")
# password_field.submit()
time.sleep(5)

# # Perform actions on the MetaMask window
# # For example, enter the password and unlock the wallet

# password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
# password_field = driver.find_element("id", "password")
# password_field.send_keys("246810")
# # Enter the password
# # password_input.send_keys("246810")
# password_field.submit()
# unlock_button = wait.until(EC.element_to_be_clickable((By.ID, "unlock")))
# unlock_button.click()

# # Switch back to the original window
# driver.switch_to.window(driver.window_handles[0])

driver.close()