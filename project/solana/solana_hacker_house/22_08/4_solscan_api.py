import requests
from requests.structures import CaseInsensitiveDict
url='https://public-api.solscan.io/account/transactions?account=HHig6VJsWWgNpCkxGDd8UgVquKu5ucrnvKVgNBGM3Jii'
headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
resp = requests.get(url, headers=headers)
print(resp.json())

