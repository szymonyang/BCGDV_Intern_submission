import json
import requests


# class GetAPI:
#     def __init__(self):
#         pass
#

api_url_base = "https://interns.bcgdvsydney.com"
r = requests.get(api_url_base + "/api/v1/key")
content = r.json()
print(r.json())
print(r.status_code)

key = content.get("key")
print(key)
contact = {"name": "Jianwen (Simon) Yang", "email": "jianwen.yeung@gmail.com"}
payload = {"apiKey": key}
r = requests.post(api_url_base + "/api/v1/submit", params=payload, data=json.dumps(contact))

print(r.json())



