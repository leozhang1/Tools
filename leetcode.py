import os
import random
from time import strftime, sleep
from selenium import webdriver
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        NoSuchElementException,
                                        TimeoutException)
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from contextlib import contextmanager
from fake_useragent import FakeUserAgentError, UserAgent
import concurrent.futures
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
os.chdir(os.path.dirname(__file__))


ua = None
while True:
    try:
        ua = UserAgent()
        break
    except FakeUserAgentError:
        print('fake user agent error')
        continue
    except Exception:
        continue

fake_agent = ua.random



@contextmanager
def driver(*args, **kwargs):
    firefox_options = Options()
    # firefox_options.add_argument('--no-sandbox')
    # firefox_options.add_argument('--start-maximized')
    # firefox_options.add_argument('--start-fullscreen')
    # firefox_options.add_argument('--single-process')
    # firefox_options.add_argument('--disable-dev-shm-usage')
    # firefox_options.add_argument("--incognito")
    # firefox_options.add_argument('--disable-blink-features=AutomationControlled')
    firefox_options.add_argument("--headless")
    # firefox_options.add_argument(f'user-agent={fake_agent}')
    # firefox_options.add_argument('--ignore-ssl-errors=yes')
    # firefox_options.add_argument('--ignore-certificate-errors')
    # firefox_options.add_argument("--disable-infobars")
    # firefox_options.add_argument("--disable-extensions")
    # firefox_options.add_argument("--disable-popup-blocking")

    d = webdriver.Firefox(service=Service(GeckoDriverManager().install(), log_path='/tmp/geckodriver.log'), options=firefox_options,)

    try:
        yield d
    finally:
        d.quit()

class Bot:

    def __init__(self, driver) -> None:
        self.driver = driver

    def login(self):
        driver = self.driver
        driver.get('https://leetcode.com/accounts/login/')
        driver.implicitly_wait(3)
        sleep(random.uniform(2,3))
        driver.find_element(By.NAME, "login").send_keys(os.getenv("EMAIL"))

        sleep(random.uniform(0.5,1))

        driver.find_element(By.NAME, "password").send_keys(os.getenv("PASSWORD"))

        driver.find_element(By.ID, 'signin_btn').click()

        sleep(5)

        driver.save_screenshot('test.png')
        sleep(1)



def main():
    with driver() as wd:
        bot = Bot(wd)
        bot.login()









if __name__ == '__main__':
	main()













