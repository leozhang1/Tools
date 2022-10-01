# import sys
# sys.path.append('/home/leo_zhang/Documents/GitHub/automate_texting/')
# from automate_texting import send_message

# send_message('from cron')

from urllib import request
from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://leetcode.com/problemset/all/')
soup = BeautifulSoup(r.content, 'html.parser')
lst = soup.find_all('a', href = re.compile(r'/problems'))

for e in lst:
    print(e['href'])




