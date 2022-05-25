from solana.rpc.api import Client


client = Client("https://api.devnet.solana.com")

res = client.is_connected()

print(res)
# True 가 나오면 연결 및 solana.py 설치가 잘 진행된 것이다.
