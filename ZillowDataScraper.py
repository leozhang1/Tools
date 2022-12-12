#!/usr/bin/env python
# coding: utf-8

# Webscraping Zillow

import os
import random
from time import strftime, sleep

from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import undetected_chromedriver as uc
import pandas as pd

os.chdir(os.path.dirname(__file__))


def getAllPageLinks():
	url = 'https://www.zillow.com/homes/for_rent/Lakeland-FL'

	options = webdriver.ChromeOptions()
	# options.add_argument('--headless')
	options.add_argument('proxy-server=106.122.8.54:3128')
	driver = uc.Chrome(options=options)
	driver.get(url)

	sleep(random.uniform(10,12))

	div = driver.find_element(By.CLASS_NAME, 'search-pagination')

	navChild = div.find_element(By.XPATH, '//nav[contains(@aria-label, "Pagination")]')

	atags = navChild.find_elements(By.TAG_NAME, 'a')

	# for atag in atags:
	# 	if atag:
	# 		print(atag.get_attribute('title'))

	pageLinks = [atag.get_attribute('title') for atag in atags if atag and atag.get_attribute('title').startswith('Page')]

	print(pageLinks)

	driver.quit()

	return pageLinks

def getDataOnPage_ThreadWork():
	url = 'https://www.zillow.com/homes/for_rent/Lakeland-FL'

	options = webdriver.ChromeOptions()
	# options.add_argument('--headless')
	# options.add_argument('proxy-server=106.122.8.54:3128')
	driver = uc.Chrome(options=options)
	driver.get(url)

	sleep(random.uniform(2,3))

	# print(driver.page_source)

	# scroll to bottom of page
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
	sleep(random.uniform(2,3))

	ul = driver.find_element(By.XPATH, "//ul[contains(@class, 'photo-cards with_constellation')]")

	prices = ul.find_elements(By.XPATH, '//span[contains(@data-test, "property-card-price")]')

	links = ul.find_elements(By.XPATH, '//a[contains(@data-test, "property-card-link")]')

	addresses = ul.find_elements(By.XPATH, '//address[contains(@data-test, "property-card-addr")]')

	priceLst = []
	addressLst = []
	linksLst = []

	print(f'number of prices: {len(prices)}')
	print(f'number of links: {len(links)}')
	print(f'number of addresses: {len(addresses)}')

	for price,link,address in zip(prices,links, addresses):
		priceLst.append(price.text)
		linksLst.append(link.get_attribute('href'))
		addressLst.append(address.text)
		print(price.text)
		print(link.get_attribute('href'))
		print(address.text)
		print('========================================')

	d = {
		'price': priceLst,
		'address': addressLst,
		'links': linksLst
	}

	df = pd.DataFrame(d)
	df.index.name = 'id'
	# print(df)
	# sleep(10000)
	driver.quit()
	return df

if __name__ == "__main__":
	getAllPageLinks()
	# output_folder = Path.cwd() / 'data'
	# output_folder.mkdir(exist_ok=True)
	# df.to_csv(f"data/zillow_data_{strftime('%Y-%m-%d-%H-%M-%S')}.csv")






