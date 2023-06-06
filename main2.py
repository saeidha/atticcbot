import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from auto_metamask import *
# setup directories

user = "Default"





metamask_extension_path = "/extension/nkbihfbeogaeaoehlefnkodbefgpgknn"
main_user_path = "/Users/saeid/Library/Application Support/Google/Chrome/"

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

time.sleep(20)


# driver.execute_script("window.open()")



# # بارگذاری اکستنشن Metamask
driver.install_addon(f"{main_user_path}{user}{metamask_extension_path}", temporary=True)
# # انتظار برای بارگذاری Metamask
driver.implicitly_wait(10)  # منتظر شدن حداکثر 10 ثانیه برای بارگذاری Metamask


# Wait for the password input field to be visible
password_field = driver.find_element_by_id("password")

# Enter the password
password_field.send_keys("246810")

# Submit the password form (if necessary)
password_field.submit()



# # ارسال دستورات به Metamask
driver.execute_script("window.ethereum.enable()")

# # تعامل با المان‌های صفحه وب
# element = driver.find_element("id", "myElement")
# element.click()

# # بستن مرورگر کروم
# driver.quit()

driver.close()