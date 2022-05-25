from solana.rpc.api import Client


client = Client("https://api.devnet.solana.com")

res = client.is_connected()

print(res)
# True 가 나오면 연결 및 solana.py 설치가 잘 진행된 것이다.

getBalance = client.get_balance("AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn")

print(getBalance)
# {'jsonrpc': '2.0', 'result': {'context': {'slot': blockNumber를 의미 }, 'value': lamports 단위의 잔액을 의미}, 'id': 1}

print(getBalance['result']['value'])
# lamports 단위의 잔액만 조회가 가능하다 