import solana
from solana.rpc.api import Client
from solana.account import Account
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction
from base58 import b58encode, b58decode
from pprint import pprint as p
b58e = lambda x: b58encode(x).decode('ascii')

#  ()

client = Client("https://api.devnet.solana.com")

test = client.is_connected()

# create solana wallet (phantom , sollet wallet)

print("1. 솔라나와 연결여부:" ,test)
# 솔라나와 연결여부: True

keypair = Keypair().generate() # keypair 생성
secret_key = keypair.secret_key # result 안에 있는 비밀키 - bytecode
priv_key = b58e(secret_key) # 이 코드를 endcode 하면 비밀키를 사용할 수 있게 추출할 수 있다.
public_key = keypair.public_key # result 안에 있는 키쌍 중 공개키

print("2. keypair :" ,keypair)
print("3. secret_key :" ,secret_key)
print("4. priv_key :" ,priv_key)
print("5. public_key :" ,public_key)