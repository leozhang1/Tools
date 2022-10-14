import requests
import pprint
import json
import os

data = [
	{"title": "okcupidbot"},
	{"title": "tdr_bot"},
	{"title": "bmbl_bot"},
	{"title": "FlightScraper"},
	{"title": "GeneralDB"},
	{"title": "GithubAutomation"},
	{"title": "NewsScraper"},
	{"title": "TaxLienScraper"},
	{"title": "automate_texting"},
	{"title": "leo_personal_website"},
]

r = requests.get("http://localhost:3001/gh-router/get", json=data)

res = json.loads((r.content).decode('utf-8'))
#pprint.pprint(res)
#print(type(res))

baseDir = '/home/leo_zhang/Documents/GitHub/'
currentGitHubFolder = None
for obj in res:
    for k, v in obj.items():
        if k == 'title':
            currentGitHubFolder = v
        elif k == 'secrets':
            # create file in the directory baseDir + v
            if currentGitHubFolder:
                print(f'adding .env with the contents below to file to {currentGitHubFolder}')
                print(v)
                if not os.path.exists(baseDir+currentGitHubFolder+'/.env'):
                    open(baseDir+currentGitHubFolder+'/.env', 'w').close()
                with open(baseDir+currentGitHubFolder+'/.env', 'w+') as f:
                    for exp in v:
                        f.write(exp+'\n')

