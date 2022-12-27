# import sys
# sys.path.append(f'/home/{pwd.getpwuid(os.getuid()).pw_name}/Documents/GitHub/automate_texting/')
# from automate_texting import send_message

# send_message('from cron')

import re

import requests
from bs4 import BeautifulSoup

r = requests.get('https://leetcode.com/problemset/all/')
soup = BeautifulSoup(r.content, 'html.parser')
lst = soup.find_all('a', href = re.compile(r'/problems'))

for e in lst:
    print(e['href'])




