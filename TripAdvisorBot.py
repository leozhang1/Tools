#!/usr/bin/env python
# coding: utf-8

# Webscraping Zillow

import concurrent.futures
import os
import random
from pathlib import Path
from time import sleep, strftime, perf_counter

import pandas as pd
import undetected_chromedriver as uc
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


os.chdir(os.path.dirname(__file__))
cityName = "Orlando"


def getPageCount():
    cityName = "Orlando"
    URL = f'https://www.tripadvisor.com/Search?q={cityName}&ssrc=A&rf=1'

    userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
    options = webdriver.ChromeOptions()
    options.set_capability("detach", True)
    options.add_argument('--headless')
    options.add_argument('proxy-server=106.122.8.54:3128')
    options.add_argument(f'user-agent={userAgent}')
    driver = uc.Chrome(options=options)
    driver.get(URL)
    driver.implicitly_wait(5)
    div = driver.find_element(By.CLASS_NAME, "pageNumbers")
    ans = div.find_elements(By.TAG_NAME, 'a')[-1].get_attribute('data-offset')
    driver.quit()
    return int(ans)

def getPageData(URL):
    userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
    options = webdriver.ChromeOptions()
    # options.set_capability("detach", True)
    # options.add_argument('--headless')
    options.add_argument('proxy-server=106.122.8.54:3128')
    options.add_argument(f'user-agent={userAgent}')
    driver = uc.Chrome(options=options)
    driver.get(URL)
    driver.implicitly_wait(5)
    lst = driver.find_elements(By.XPATH, '//div[contains(@data-widget-type, "LOCATIONS")]')
    titles = []
    ratings = []
    reviewsCount = []
    reviewsLink = []
    addresses = []
    for e in lst:
        if e:
            try:
                title = e.find_element(By.CLASS_NAME, 'result-title')
                # print(title.text.strip())
                rating = e.find_element(By.XPATH, '//span[contains(@data-clicksource, "BubbleRatingTrackingOnly")]')
                # print(rating.get_attribute("alt").strip())
                reviewRef = e.find_element(By.CLASS_NAME, 'review_count')
                # print(reviewRef.text.strip())
                reviewsURL = reviewRef.get_attribute("href")
                # print(reviewsURL.strip())
                address = e.find_element(By.CLASS_NAME, "address-text")
                mobileAddresses = e.find_element(By.CLASS_NAME, "mobile-address-text")
                # print(address.text.strip())
                # print()
                titles.append(title.text.strip())
                ratings.append(rating.get_attribute("alt").strip())
                reviewsCount.append(reviewRef.text.strip())
                reviewsLink.append(reviewsURL.strip())
                addresses.append(address.text.strip() + '|||' + mobileAddresses.text.strip())

            except Exception as e:
                pass
    driver.quit()

    d = {
		'title': titles,
		'rating': ratings,
		'review_count': reviewsCount,
        'review_url': reviewsLink,
		'address': addresses,
	}

    df = pd.DataFrame(d)
    df.index.name = 'id'
    return df

def getLinks():
    pageCount = getPageCount()
    print(pageCount//30)
    return [ f'https://www.tripadvisor.com/Search?q={cityName}&ssrc=A&o={i}' for i in range(0, pageCount+1, 30) ]


links = getLinks()
start = perf_counter()

ans = None
# multi-threading
with concurrent.futures.ThreadPoolExecutor() as executor:
    res = executor.map(getPageData, links)
    # list of dataframes
    ans = list(res)

final_df = pd.concat(ans)
final_df.index.name = 'id'
output_folder = Path.cwd() / 'data'
output_folder.mkdir(exist_ok=True)
final_df.to_csv(f"{os.getcwd()}/data/trip_advisor_{cityName}_{strftime('%Y-%m-%d-%H-%M-%S')}.csv")
# print(f'total time in seconds: {(perf_counter() - start) // 6}')

