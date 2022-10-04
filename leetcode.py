# import os
# import random
# from time import strftime, sleep
# from selenium import webdriver
# from selenium.common.exceptions import (ElementClickInterceptedException,
#                                         NoSuchElementException,
#                                         TimeoutException)
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.firefox import GeckoDriverManager
# from contextlib import contextmanager
# from fake_useragent import FakeUserAgentError, UserAgent
# import concurrent.futures
# import pandas as pd
# from dotenv import load_dotenv
# from bs4 import BeautifulSoup
# import requests, re

# r = requests.get('https://leetcode.com/problemset/all/')
# soup = BeautifulSoup(r.content, 'html.parser')
# lst = soup.find_all('a', href = re.compile(r'/problems'))

# load_dotenv()
# os.chdir(os.path.dirname(__file__))


# ua = None
# while True:
#     try:
#         ua = UserAgent()
#         break
#     except FakeUserAgentError:
#         print('fake user agent error')
#         continue
#     except Exception:
#         continue

# fake_agent = ua.random



# @contextmanager
# def driver(*args, **kwargs):
#     firefox_options = Options()
#     firefox_options.add_argument('--no-sandbox')
#     firefox_options.add_argument('--start-maximized')
#     firefox_options.add_argument('--start-fullscreen')
#     firefox_options.add_argument('--single-process')
#     firefox_options.add_argument('--disable-dev-shm-usage')
#     firefox_options.add_argument("--incognito")
#     firefox_options.add_argument('--disable-blink-features=AutomationControlled')
#     # firefox_options.add_argument("--headless")
#     firefox_options.add_argument(f'user-agent={fake_agent}')
#     firefox_options.add_argument('--ignore-ssl-errors=yes')
#     firefox_options.add_argument('--ignore-certificate-errors')
#     firefox_options.add_argument("--disable-infobars")
#     firefox_options.add_argument("--disable-extensions")
#     firefox_options.add_argument("--disable-popup-blocking")

#     d = webdriver.Firefox(service=Service(GeckoDriverManager().install(), log_path='/tmp/geckodriver.log'), options=firefox_options,)

#     try:
#         yield d
#     finally:
#         d.quit()

# class Bot:

#     def __init__(self, driver) -> None:
#         self.driver = driver
#         self.driver.get('https://leetcode.com/accounts/login/?next=%2Fproblemset%2Fall%2F')
#         self.driver.implicitly_wait(3)
#         self.login()

#     def login(self):
#         driver = self.driver

#         try:
#             driver.find_element(By.XPATH, '//span[text()="Sign in"]').find_element(By.XPATH, '../..').click()
#             print('clicked on sign in')
#             sleep(random.uniform(60,90))
#         except Exception as e:
#             pass


#         try:
#             driver.find_element(By.NAME, "login").send_keys(os.getenv("EMAIL"))
#         except Exception as e:
#             pass

#         sleep(random.uniform(0.5,1))

#         try:
#             driver.find_element(By.NAME, "password").send_keys(os.getenv("PASSWORD"))
#         except Exception as e:
#             pass

#         try:
#             driver.find_element(By.ID, 'signin_btn').click()
#         except Exception as e:
#             pass


#     def run(self):
#         driver = self.driver

#         driver.get(f"https://leetcode.com{lst[-1]['href']}submissions/")

#         sleep(random.uniform(2,3))

#         self.login()

#         sleep(random.uniform(2,3))

#         # print(driver.page_source)

#         # TODO: check if already solved this question. If so then retrieve and submit and send a text message to user indicating a success. Otherwise send a text to user indicating that this question has not been solved before.

#         # check if "Accepted" is on the page.
#         print('Accepted' in driver.page_source)
#         if 'Accepted' in driver.page_source:
#             driver.find_element(By.XPATH, '//button[@icon="code"]').click()

#         # sleep(5)

#         driver.save_screenshot('test.png')
#         sleep(60)
#         if os.path.exists('test.png'):
#             os.remove('test.png')



# def main():
#     with driver() as wd:
#         bot = Bot(wd)
#         bot.login()
#         bot.run()









# if __name__ == '__main__':
# 	main()













