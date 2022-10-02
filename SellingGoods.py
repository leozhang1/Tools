import json
import os
import random
from contextlib import contextmanager
from time import sleep, perf_counter
from unicodedata import category

from dotenv import load_dotenv
from fake_useragent import FakeUserAgentError, UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        self.title = config['title']
        self.price = config['price']
        self.category = config['category']
        self.condition = config['condition']
        self.description = config['description']
        self.photoFilePath = [os.getcwd() + config['photoFilePath'] + fname for fname in os.listdir(os.getcwd() + config['photoFilePath'])]
        self.videoFilePath = [os.getcwd() + config['videoFilePath'] + fname for fname in os.listdir(os.getcwd() + config['videoFilePath'])]
        print(self.photoFilePath)
        print(self.videoFilePath)


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

        targetKeywords = {
            "Title",
            "Price",
            "Category",
            "Condition",
            "Description"
        }

        lst = driver.find_elements(By.TAG_NAME, 'label')

        lst = [e for e in lst if e and e.get_attribute('aria-label') in targetKeywords]

        print(len(lst))

        title = price = category = condition = description = None

        for e in lst:
            attr = e.get_attribute('aria-label')
            if attr == 'Title':
                title = e.find_element(By.ID, e.get_attribute('for'))
            if attr == 'Price':
                price = e.find_element(By.ID, e.get_attribute('for'))
            if attr == 'Category':
                category = e.find_element(By.ID, e.get_attribute('for'))
            if attr == 'Condition':
                condition = e.find_element(By.ID, e.get_attribute('for'))
            if attr == 'Description':
                description = e.find_element(By.ID, e.get_attribute('for'))
        print(title.tag_name)
        print(price.tag_name)
        print(category.tag_name)
        print(condition.tag_name)
        print(description.tag_name)

        # sleep(60)

        # title
        title.send_keys(self.title)

        # price
        price.send_keys(self.price)

        # category
        category.send_keys(self.category)

        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.DOWN)
        sleep(random.uniform(0.5,1))

        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.ENTER)

        # condition
        condition.click()
        sleep(random.uniform(0.5,1))

        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.DOWN)
        sleep(random.uniform(0.5,1))

        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.ENTER)

        # description
        description.send_keys(self.description)

        photoInputElem = driver.find_element(By.XPATH, '//input[contains(@accept, "image/*,image/heif,image/heic")]')

        for path in self.photoFilePath:
            photoInputElem.send_keys(path)
            sleep(random.uniform(0.5,1))

        sleep(random.uniform(1,2))

        videoInputElem = driver.find_element(By.XPATH, '//input[contains(@accept, "video/*")]')

        videoInputElem.send_keys(self.videoFilePath[0])

        sleep(random.uniform(30,60))

        driver.find_element(By.XPATH, '//div[contains(@aria-label, "Next")]').click()

        sleep(random.uniform(2, 3))

        driver.find_element(By.XPATH, '//div[contains(@aria-label, "Next")]').click()

        sleep(random.uniform(2, 3))

        driver.find_element(By.XPATH, '//div[contains(@aria-label, "Publish")]').click()

        sleep(random.uniform(3,5))

        driver.save_screenshot('test.png')
        # sleep(60)
        # if os.path.exists(f'{os.getcwd()}/test.png'):
        #     os.remove('test.png')



def main():

    start = perf_counter()
    # grab data from config file
    with driver() as wd:
        with open(f'{os.getcwd()}/configs/facebook.json') as configList:
            for config in json.load(configList):
                bot = FaceBookBot(wd, config)
                bot.listItem()
    print('time in ms: {}'.format((perf_counter() - start) * 1000))










if __name__ == '__main__':
	main()













