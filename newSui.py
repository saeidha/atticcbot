import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def unlock_wallet(driver, wait):
    popup_window = wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    
    # Find the password input element
    password_input = driver.find_element(By.NAME, 'password')
    # Enter the password into the input field
    password_input.send_keys("S12saeed@")

    # Find the button element by XPath
    buttonPath = "//button[div[contains(@class, 'truncate')] and div[text()='Unlock Wallet']]"
    wait.until(lambda d: d.find_element(By.XPATH, buttonPath))
    button = driver.find_element(By.XPATH, buttonPath)
    button.click()

    # click Approve
    buttonPath = "//button[div[contains(@class, 'truncate')] and div[text()='Approve']]"
    wait.until(lambda d: d.find_element(By.XPATH, buttonPath))
    button = driver.find_element(By.XPATH, buttonPath)
    button.click()


def press_random_arrow_key(driver):
    # Randomly select an arrow key
    arrow_keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
    random_key = random.choice(arrow_keys)
    # Perform the key press action
    actions = ActionChains(driver)
    actions.send_keys(random_key).perform()


def click_approve(driver, wait):
    press_random_arrow_key(driver= driver)

    popup_window = wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])

    # click Approve
    buttonPath = "//button[div[contains(@class, 'truncate')] and div[text()='Approve']]"
    wait.until(lambda d: d.find_element(By.XPATH, buttonPath))
    button = driver.find_element(By.XPATH, buttonPath)
    button.click()




def main():
    user = "Profile 2"
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
    'emote-debugging-port',
    'test-type',
    'use-mock-keychain',
    'flag-switches-begin',
    'flag-switches-end'])

    # profile
    chrome_options.add_argument(f"profile-directory={user}")
    chrome_options.add_argument(f"user-data-dir={main_user_path}")

    # ایجاد شیء درایور مرورگر کروم
    service = Service(executable_path="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome", options=chrome_options)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://sui8192.ethoswallet.xyz/")
    time.sleep(10)

    wait = WebDriverWait(driver, 20)

    press_random_arrow_key(driver= driver)

    unlock_wallet(driver, wait)

    while True:
        # Get the number of open windows
        num_windows = len(driver.window_handles)
        #  switch to main
        if num_windows > 1:
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        click_approve(driver, wait)
        time.sleep(1)
    driver.quit()


if __name__ == "__main__":
    main()