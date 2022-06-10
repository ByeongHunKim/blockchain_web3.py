# solana.py 
# base58
# solana-cli

# pip install solana
# pip install base58
# sh -c "$(curl -sSfL https://release.solana.com/v1.10.8/install)"

import solana
from solana.rpc.api import Client
from solana.account import Account
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction
from base58 import b58encode, b58decode

#  ()
# client = Client("https://api.mainnet-beta.solana.com")

client = Client("https://api.devnet.solana.com")

test = client.is_connected()

# create solana wallet (phantom , sollet wallet)

print("1. 솔라나와 연결여부:" ,test)
# 솔라나와 연결여부: True