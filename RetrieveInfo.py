import requests
import pprint
import json

data = [
	{"title": "okcupidbot"},
	{"title": "tdr_bot"},
	{"title": "bmbl_bot"},
	{"title": "FlightScraper"},
	{"title": "GeneralDB"},
	{"title": "GitHubAutomation"},
	{"title": "NewsScraper"},
	{"title": "TaxLienScraper"},
	{"title": "Zoom-Automation-Python"},
	{"title": "automate_texting"},
	{"title": "leo_personal_website"},
]

r = requests.get("http://localhost:3001/gh-router/get", json=data)

res = json.loads((r.content).decode('utf-8'))
pprint.pprint(res)
print(type(res))

#baseDir = '/home/leo_zhang/Documents/GitHub/'
#currentGitHubFolder = None
#for obj in res:
#    for k, v in obj:
#        if k == 'title':
#            currentGitHubFolder = v
#        elif k == 'secrets':
#            # create file in the directory baseDir + v
#            if currentGitHubFolder:
#                with open(baseDir+currentGitHubFolder+'/.env', 'a') as f:
#                    for exp in v:
#                        f.write(exp)
#
