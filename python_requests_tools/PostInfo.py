import requests
import json
import os

import platform
import uuid

if platform.system() == "Linux":
    import linux_tools as tools
elif platform.system() == "Windows":
    import windows_tools as tools


data = [
    {
        "id": str(uuid.uuid4()),
        "title": "",
        "username": "",
        "password": ""
    },
]


# r = requests.post("http://localhost:5048/api/Account/many", json=data)

# res = json.loads((r.content).decode('utf-8'))

# print(r.status_code)
# print(res)

# print(r.content)
# print()
# print(r.text)