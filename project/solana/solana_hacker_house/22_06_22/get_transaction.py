from solana.publickey import PublicKey
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
from solana.rpc.api import Client
from base58 import b58encode, b58decode as b58d
import asyncio;

client = Client("https://api.devnet.solana.com")

test = client.is_connected()
print("1. 솔라나 연결여부:" ,test)
resultOfTxn = "641rUjSxsgmZJ62FmgiFR4GANPt1oWWKv8qsTjAwL5wgBQ7B11JEb78RbcHsrp4rD5UxACzjiZetd8jAKYETBBxR"
print(resultOfTxn)
result = client.get_transaction(resultOfTxn)
print(result)