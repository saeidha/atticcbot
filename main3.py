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


def connect_wallet(driver, wait):
    try: 
        print("Connect Wallet")
        buttonPath = "//button[text()='Connect Wallet']"
        wait.until(lambda d: d.find_element(By.XPATH, buttonPath))
        button = driver.find_element(By.XPATH, buttonPath)
        button.click()

        print("Click MetaMask")
        buttonPath = "//button[text()='MetaMask']"
        wait.until(lambda d: d.find_element(By.XPATH, buttonPath))
        button = driver.find_element(By.XPATH, buttonPath)
        button.click()

    except:
        print("connected")
        
def unlock_wallet(driver, wait):
    try: 
        try:
            print("password")
            # Find the password input element
            passrowInput = "input[id='password'][type='password']"
            wait.until(lambda d: d.find_element(By.CSS_SELECTOR,passrowInput ))
            print("password2")
            password_input = driver.find_element(By.CSS_SELECTOR, passrowInput)
            # Enter the password into the input field
            password_input.send_keys("S12saeed")

            print("Unlock")
            buttonPath = "//button[text()='Unlock']"
            wait.until(lambda d: d.find_element(By.XPATH, buttonPath))
            button = driver.find_element(By.XPATH, buttonPath)
            button.click()
        except:
            print("not")

        print("Sign")
        # Find the button element by XPath
        buttonPath = "//button[text()='Sign']"
        wait.until(lambda d: d.find_element(By.XPATH, buttonPath))
        button = driver.find_element(By.XPATH, buttonPath)
        button.click()
        print("Wallet connected")
        
    except:
        print("Error Wallet connected")

def press_random_arrow_key(driver):

    wait = WebDriverWait(driver, 5)
    clickable = driver.find_element(By.ID, "game")
    ActionChains(driver)\
        .context_click(clickable)

    # Randomly select an arrow key
    arrow_keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
    random_key = random.choice(arrow_keys)

    # Perform the key press action
    actions = ActionChains(driver)
    actions.send_keys(random_key).perform()

    try:
        if len(driver.window_handles) > 1:
                print("have 2 widows")
                driver.switch_to.window(driver.window_handles[-1])
        else:
            print("have 1 widows")
            popup_window = wait.until(EC.number_of_windows_to_be(2))
            driver.switch_to.window(driver.window_handles[-1])
        
        for window_handle in driver.window_handles:
            # Switch to the current window
            driver.switch_to.window(window_handle)
            # Get the title of the current window
            window_title = driver.title
            print("Popup Window Title:", window_title)
        return driver
    except:
        return press_random_arrow_key(driver= driver)


def click_play(driver, wait):
    buttonPath = "play-button.header-button"
    wait.until(lambda d: d.find_element(By.CLASS_NAME, buttonPath))
    button = driver.find_element(By.CLASS_NAME, buttonPath)
    button.click()


def click_leaderboard(driver, wait):
    buttonPath = "leaderboard-button.header-button"
    wait.until(lambda d: d.find_element(By.CLASS_NAME, buttonPath))
    button = driver.find_element(By.CLASS_NAME, buttonPath)
    button.click()
    return driver

def click_NewGame(driver, wait):

    # click mint
    buttonPath = "new-game.signed-in"
    wait.until(lambda d: d.find_element(By.CLASS_NAME, buttonPath))
    button = driver.find_element(By.CLASS_NAME, buttonPath)
    button.click()
    time.sleep(1)

    # click mint
    mintNewGame = "//button[text()='Mint New Game']"
    wait.until(lambda d: d.find_element(By.XPATH, mintNewGame))
    button_element = driver.find_element(By.XPATH, mintNewGame)
    button_element.click()

    return driver



def check_Game_Over_NewGame(driver, wait):
    return driver
    # newWait = WebDriverWait(driver, 1)
    # buttonPath = "button[div[contains(@class, 'subtitle')] and div[text()='Game Over']]"
    # try:
    #     newWait.until(lambda d: d.find_element(By.CLASS_NAME, buttonPath))
    #     driver.find_element(By.CLASS_NAME, buttonPath)
    #     driver = click_leaderboard(driver=driver, wait=wait)
    #     driver = click_NewGame(driver=driver, wait=wait)
    #     # approve
    #     click_approve(driver=driver,wait=wait)
    #     # play
    #     click_play(driver=driver, wait=wait)
    #     return driver
    # except:
    #     return driver


def check_Game_Over_NewGameFirstTime(driver, wait):

    newWait = WebDriverWait(driver, 1)
    try:
        gameOverDive = "//div[not(contains(@class, 'error hidden'))]/div[@class='subtitle' and text()='Game Over']"
        newWait.until(lambda d: d.find_element(By.XPATH, gameOverDive))
        driver.find_element(By.XPATH, gameOverDive)
        print("leaderboard")
        click_leaderboard(driver=driver, wait=wait)
        print("newgame")
        click_NewGame(driver=driver, wait=wait)
        # unlock wallet
        print("unlock wallet")
        unlock_wallet(driver, wait)
        # approve
        print("approve")
        click_approve(driver=driver,wait=wait)
        # play
        print("play")
        click_play(driver=driver, wait=wait)
        return
    except:
        press_random_arrow_key(driver= driver)
        unlock_wallet(driver, wait)
        return



def click_approve(driver, wait):
    print("----12")

    # Get the title of the popup window
    
    # driver.switch_to.window(driver.window_handles[-1])
    # popup_window_title = driver.title
    # print("Popup Window Title:", popup_window_title)
    # if popup_window_title != "Sui Wallet":
    #     driver.switch_to.window(driver.window_handles[-1])
    #     print("Popup Window Title:", driver.title)
    
    try:
        # click Approve
        buttonPath = "//button[div[text()='Approve']]"
        wait.until(lambda d: d.find_element(By.XPATH, buttonPath))
        print("----13")
        button = driver.find_element(By.XPATH, buttonPath)
        button.click()
        return driver
    except :
        return driver




def main():
    user = "Default"
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

    wait = WebDriverWait(driver, 20)
    minWait = WebDriverWait(driver, 5)
    driver.get("https://atticc.xyz/home")
    
    try:
        connect_wallet(driver=driver, wait=minWait)

        minWait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        unlock_wallet(driver=driver, wait=minWait)
    except:
        print("")
    

    # click_play(driver=driver, wait=wait)

    # check_Game_Over_NewGameFirstTime(driver=driver,wait=wait)
    # time.sleep(7)
    # while True:
    #     driver.switch_to.window(driver.window_handles[0])

    #     driver = check_Game_Over_NewGame(driver=driver,wait=wait)
    #     time.sleep(0.25)
    #     driver = press_random_arrow_key(driver=driver)
    #     time.sleep(0.25)
    #     driver = click_approve(driver, wait)
    #     time.sleep(0.25)


if __name__ == "__main__":
    main()