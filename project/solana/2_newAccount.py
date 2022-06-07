import solana
from solana.rpc.api import Client
from solana.account import Account
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction
from base58 import b58encode, b58decode

#  ()

client = Client("https://api.devnet.solana.com")

test = client.is_connected()

# create solana wallet (phantom , sollet wallet)

print("1. 솔라나와 연결여부:" ,test)
# 솔라나와 연결여부: True

account = Account()
print("2. account - 결과 :" ,account)
# <solana.account.Account object at 0x7fe5ab0446a0>

secretKey = account.secret_key()
print("2. secretKey - 결과 :" ,secretKey)
# b"zJD1Js\x00\xb7\x04\xc3V\xbc\xf3\xa9;\xabZ\x05'+\x9f\x81D\xac1\xb8\x1c\xfe.+\x02w"

bytesAccount = bytes(account.public_key())
print("3. bytesAccount - 결과 :" ,bytesAccount)
# b'9\x15\x90\xe2K\xf5[\xda\x87\x1b\xfb%\xb0e\xb4,\xf4\xfaQ\xcd\xde\x1c RC*\xbei\x80@1s'

publicAddr = b58encode(bytesAccount).decode()
print("4. publicAddr - 결과 :" ,publicAddr)
# 4qqK5vyz5GpYXsFVQz2JcC7NfSBWmsBdQsHRhF7pRYrE

makePrivKey = secretKey + bytesAccount
print("5. makePrivKey - 결과 :" ,makePrivKey)
# b"zJD1Js\x00\xb7\x04\xc3V\xbc\xf3\xa9;\xabZ\x05'+\x9f\x81D\xac1\xb8\x1c\xfe.+\x02w9\x15\x90\xe2K\xf5[\xda\x87\x1b\xfb%\xb0e\xb4,\xf4\xfaQ\xcd\xde\x1c RC*\xbei\x80@1s"

privKey = b58encode(makePrivKey).decode()
print("6. privKey - 결과 :" ,privKey)
# 3Sot9qjkZGdZRaLKNZwAcWyAvX3mHoDyPBnxRV51DhA6ZCT813Re6aSGnkd2brXKgzkCs9t6u8hbDAiEeku8xWjL


# 생성된 지갑과 연결한 지갑의 공개키 주소가 같다.4qqK5vyz5GpYXsFVQz2JcC7NfSBWmsBdQsHRhF7pRYrE  
# publicKey = 4qqK5vyz5GpYXsFVQz2JcC7NfSBWmsBdQsHRhF7pRYrE
# privKey = 3Sot9qjkZGdZRaLKNZwAcWyAvX3mHoDyPBnxRV51DhA6ZCT813Re6aSGnkd2brXKgzkCs9t6u8hbDAiEeku8xWjL

# 이더리움은 geth에 연결되어있는 keystore 폴더에 UTC파일로 privKey가 생성되는데, 솔라나는 이렇게 키가 생겨서 보안에 좀 더 신경 써야한다.
