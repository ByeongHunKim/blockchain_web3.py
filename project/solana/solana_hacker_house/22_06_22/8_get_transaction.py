from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.rpc.types import TokenAccountOpts
from solana.keypair import Keypair
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Confirmed
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
import solana.system_program as sys
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.async_client import AsyncToken
from spl.token._layouts import MINT_LAYOUT
import spl.token.instructions as spl_token
import time
from base58 import b58encode, b58decode as b58d
import asyncio



# client = Client("https://api.devnet.solana.com")
# client = Client("https://api.mainnet-beta.solana.com")

txResult = client.get_transaction("")
print(txResult)

blockTime1 = txResult['result']['blockTime']
blockTime = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(blockTime1))
fee1 = txResult['result']['meta']['fee']
fromAddr1 = txResult['result']['transaction']['message']['accountKeys'][1] # 토큰 출금 주소
toAddr1 = txResult['result']['transaction']['message']['accountKeys'][2] # 토큰 입금 주소
beforeBalOfFrom1 = txResult['result']['meta']['postTokenBalances'][0]['uiTokenAmount']['amount'] # 보내는 지갑의 전송 전 잔액 1
beforeOfTo2 = txResult['result']['meta']['postTokenBalances'][1]['uiTokenAmount']['amount'] # 받는 지갑의 전송 후 잔액 2
afterOfFrom3 = txResult['result']['meta']['preTokenBalances'][0]['uiTokenAmount']['amount']
afterOfTo4 = txResult['result']['meta']['preTokenBalances'][1]['uiTokenAmount']['amount'] 
print(blockTime)
print(blockTime1)
print(fee1)
print("토큰 보내는 사람의 주소",fromAddr1)
print("토큰 받는 사람의 주소",toAddr1)
print("from 주소의 전송 전 잔액 ",beforeBalOfFrom1)
print("from 주소의 전송 후 잔액 ",afterOfFrom3)
print("to 주소의 전송 전 잔액 ",beforeOfTo2)
print("to 주소의 전송 후 잔액 ",afterOfTo4)



withdrawLamport = int(afterOfFrom3) - int(beforeBalOfFrom1)
print(withdrawLamport)
depositLamport = int(beforeOfTo2) - int(afterOfTo4)
print(depositLamport)

print("1. 보내는 주소 : ", fromAddr1)
print("2. 받는 주소 : ", toAddr1)
print("3. 출금액 : ", withdrawLamport)
print("4. 입금액 : ", depositLamport)

withdraw_balance = round(withdrawLamport*10**(-9),9)
deposit_balance = round(depositLamport*10**(-9),9)

print(withdraw_balance)
print(deposit_balance)

# import requests
# from requests.structures import CaseInsensitiveDict
# url='https://public-api.solscan.io/account/transactions?account=HHig6VJsWWgNpCkxGDd8UgVquKu5ucrnvKVgNBGM3Jii'
# headers = CaseInsensitiveDict()
# headers["accept"] = "application/json"
# resp = requests.get(url, headers=headers)
# print(resp.json())
