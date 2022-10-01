import json
import os
import random
from contextlib import contextmanager
from time import sleep

from dotenv import load_dotenv
from fake_useragent import FakeUserAgentError, UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

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
    # firefox_options.add_argument("--headless")
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

class FaceBookBot:

    def __init__(self, driver, config) -> None:
        self.driver = driver
        self.config = config

    def listItem(self):
        driver = self.driver
        driver.get('https://www.facebook.com/marketplace/create')
        driver.maximize_window()
        driver.implicitly_wait(3)
        sleep(random.uniform(2,3))

        driver.find_element(By.ID,'email').send_keys(os.getenv('fbUser'))
        driver.find_element(By.ID,'pass').send_keys(os.getenv('fbPassword'))

        driver.find_element(By.ID, 'loginbutton').click()

        sleep(random.uniform(1,2))

        driver.get('https://www.facebook.com/marketplace/create/item/')

        sleep(random.uniform(1,2))

        photoInputElem = driver.find_element(By.XPATH, '//input[contains(@accept, "image/*,image/heif,image/heic")]')

        photoInputElem.send_keys(f'{os.getcwd()}/product_imgs/skateboard/1.jpeg')

        driver.find_element(By.XPATH, '/div[contains(@aria-label, "Next")]').click()

        sleep(random.uniform(2, 3))

        driver.find_element(By.XPATH, '/div[contains(@aria-label, "Next")]').click()

        sleep(random.uniform(2, 3))

        driver.find_element(By.XPATH, '/div[contains(@aria-label, "Publish")]').click()

        driver.save_screenshot('test.png')
        sleep(60)
        if os.path.exists('test.png'):
            os.remove('test.png')



def main():

    # grab data from config file
    with driver() as wd:
        with open(f'{os.getcwd()}/configs/facebook.json') as configList:
            for config in json.load(configList):
                bot = FaceBookBot(wd, config)
                bot.listItem()











if __name__ == '__main__':
	main()













