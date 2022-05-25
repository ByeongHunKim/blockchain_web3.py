from solana.rpc.api import Client


client = Client("https://api.devnet.solana.com")

res = client.is_connected()

print(res)

getBalance = client.get_balance("AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn")
print(getBalance['result']['value'])