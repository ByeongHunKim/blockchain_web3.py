import requests
from requests.structures import CaseInsensitiveDict


# = 다음에 지갑주소 입력

url='https://public-api.solscan.io/account/transactions?account=' 
headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
resp = requests.get(url, headers=headers)

print(resp.json())
