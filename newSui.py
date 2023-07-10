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


def press_random_arrow_key(driver, index = 0):
    print("----8")
    wait = WebDriverWait(driver, 5)
    clickable = driver.find_element(By.ID, "game")
    ActionChains(driver)\
        .context_click(clickable)
    print("----9")
    # Randomly select an arrow key
    arrow_keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

    if index >= len(arrow_keys):
        return
    
    # Perform the key press action
    print(arrow_keys[index])
    actions = ActionChains(driver)
    actions.send_keys(arrow_keys[index]).perform()
    print("----10")

    num_windows = len(driver.window_handles)
    try:
        if num_windows > 1:
                driver.switch_to.window(driver.window_handles[1])
        else:
            popup_window = wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        return
    except:
        press_random_arrow_key(driver= driver, index= (index + 1))



def click_play(driver, wait):
    buttonPath = "play-button.header-button"
    wait.until(lambda d: d.find_element(By.CLASS_NAME, buttonPath))
    button = driver.find_element(By.CLASS_NAME, buttonPath)
    button.click()


def click_approve(driver, wait):
    print("----7")
    press_random_arrow_key(driver= driver)
    print("----12")
    # click Approve
    buttonPath = "//button[div[contains(@class, 'truncate')] and div[text()='Approve']]"
    wait.until(lambda d: d.find_element(By.XPATH, buttonPath))
    print("----13")
    button = driver.find_element(By.XPATH, buttonPath)
    button.click()
    print("----14")




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

    click_play(driver=driver, wait=wait)

    press_random_arrow_key(driver= driver)

    unlock_wallet(driver, wait)
    time.sleep(7)
    while True:
        # Get the number of open windows
        
        num_windows = len(driver.window_handles)
        #  switch to main
        print("----1")
        # if num_windows > 1:
        #     driver.switch_to.window(driver.window_handles[1])
        #     time.sleep(1)
        #     num_windows = len(driver.window_handles)
        #     if num_windows > 1:
        #         driver.close()
        #     print("----2")
        
        
        driver.switch_to.window(driver.window_handles[0])
        print("----4")
        click_approve(driver, wait)
        print("----20")


if __name__ == "__main__":
    main()