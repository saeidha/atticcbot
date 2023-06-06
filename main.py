import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# مسیر فایل اکستنشن Metamask
metamask_extension_path = "/path/to/metamask/extension"

# تنظیمات مرورگر کروم
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # غیرفعال کردن ویژگی‌های تشخیص خودکار مرورگر کروم
# chrome_options.add_argument("--start-maximized")



# profile
chrome_options.add_argument("--profile-directory=/Users/saeid/Library/Application\ Support/Google/Chrome/git")

# ایجاد شیء درایور مرورگر کروم
driver = webdriver.Chrome(executable_path="/Applications/Google\ Chrome.app", options= chrome_options)

driver.get("https://atticc.xyz/")

time.sleep(20)

driver.close()
# driver.execute_script("window.open()")



# # بارگذاری اکستنشن Metamask
# driver.install_addon(metamask_extension_path, temporary=True)
# # انتظار برای بارگذاری Metamask
# driver.implicitly_wait(10)  # منتظر شدن حداکثر 10 ثانیه برای بارگذاری Metamask

# # ارسال دستورات به Metamask
# driver.execute_script("window.ethereum.enable()")

# # تعامل با المان‌های صفحه وب
# element = driver.find_element("id", "myElement")
# element.click()

# # بستن مرورگر کروم
# driver.quit()
