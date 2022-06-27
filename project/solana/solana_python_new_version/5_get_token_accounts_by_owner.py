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

client = Client("https://api.devnet.solana.com")

newOwner = '' # wallet_address = owner가 입력한 wallet_address로 이전 된다.
newOwnerPub = PublicKey(newOwner)
mint1 = '' # mint Address
mintAddr = PublicKey(mint1)

queryTokenAcc = client.get_token_accounts_by_owner(newOwnerPub,TokenAccountOpts(mint=mint1))
getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']
print(f"1. FbKFmRjReeuQMcAxz4LFvhrdghLygNH1tondiyzGQLEQ 유저의 {mint1}토큰을 거래할 수 있는 account 주소는 {getTokenAcc} 입니다.")
result = client.get_token_account_balance(getTokenAcc)
ui_tokenVal = result['result']['value']['uiAmount']
print("2. 현재 유저의 토큰 잔액은? : ", ui_tokenVal)

# get_transaction으로 찾는 방법도 있다.

# queryTokenAcc = client.get_transaction("resultOfTxn")
# print(queryTokenAcc)
# getTokenAcc = queryTokenAcc['result']['transaction']['message']['accountKeys'][1]
# print(getTokenAcc)