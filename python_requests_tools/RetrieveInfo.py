import requests
import json
import os
import pprint

import platform

if platform.system() == "Linux":
    import linux_tools as tools
elif platform.system() == "Windows":
    import windows_tools as tools


data = [
	{"title": "okcupidbot"},
	{"title": "tdr_bot"},
	{"title": "bmbl_bot"},
	{"title": "GithubAutomation"},
	{"title": "NewsScraper"},
	{"title": "automate_texting"},
]

r = requests.get("http://localhost:5048/api/Account/", json=data)

res = json.loads((r.content).decode('utf-8'))
lstOfDicts = list(eval(res))
# pprint.pprint(lstOfDicts)
# print(type(lstOfDicts))

baseDir = tools.BASE_DIR
currentGitHubFolder = None
for account in lstOfDicts:
    title = account['title']
    password = account['password']
    currentGitHubFolder = baseDir + title
    if os.path.exists(currentGitHubFolder):
        if not os.path.exists(currentGitHubFolder+'/.env'):
            print(f'adding .env with the contents below to file to {currentGitHubFolder}')
            open(currentGitHubFolder+'/.env', 'w').close()
            with open(currentGitHubFolder+'/.env', 'w+') as f:
                f.write(password+'\n')

