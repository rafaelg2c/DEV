import requests
import json

url = "https://webexapis.com/v1/rooms"

payload = {}

header = {"Accept": "Application/json",
    "Authorization" : "Bearer NjFjZWQ2ZTMtODE2Ny00MmY1LThhYzQtODBmNmU1NWMxNGNjZWQzNGQ1MGYtZmU3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
            }


response = requests.get(url, headers=header, data=payload).json()

response2 = json.dumps(response, indent=2 , sort_keys=True)
print(response2)