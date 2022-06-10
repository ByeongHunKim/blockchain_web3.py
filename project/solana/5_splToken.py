from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer_checked, TransferCheckedParams

from solana.rpc.commitment import Confirmed
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from base58 import b58encode, b58decode
import subprocess
import os
import itertools

client = Client("https://api.devnet.solana.com")

# client = Client("https://api.mainnet-beta.solana.com")

test = client.is_connected()

print("1. 솔라나와 연결여부:" ,test)

# GrqwuHcEknNDB67MofjamrAKWTqmmunnn6G6VwBSWvVW  7fUAJdStEuGbc3sM84cKRL6yYaaSstyLSU4ve5oovLS7 FbKFmRjReeuQMcAxz4LFvhrdghLygNH1tondiyzGQLEQ
test1 = client.get_token_account_balance("B9v4CRFk89fpq3SAwKVd1qphwSc4woRL8oLDxnXTqzgm")

mintAddress = "3oMguQN22MkB8n7BMbsRFqEeJceR8vd2FmuZLiCBcNig"
toAddr = "FiDa3zBqm1GmfDFjnHsrzbp5TnYnMUZmeVEmFRKXJizu"
amount = 100.00
print("2. 솔라나 토큰 조회: ",test1)





# transfer_parameters = TransferParams(
#     from_pubkey=PublicKey(fromAddr),
#     to_pubkey=PublicKey(toAddr),
#     lamports=int(sol_amount*(10**9))
# )




# transaction = Transaction()
# transaction.add(
#     transfer_checked(
#         TransferCheckedParams(
#     program_id="TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
#     source=PublicKey("3fcQrej79fzZAKKPnrg7Jcg1aUKLj573PwGZTn3uu7gR"),
#     mint=PublicKey("Crh6XxeJoKGVbCKaCXzD57pkUv5vYwgW3acnKWP91bWV"),
#     dest=PublicKey("AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn"),
#     owner=PublicKey("FiDa3zBqm1GmfDFjnHsrzbp5TnYnMUZmeVEmFRKXJizu"),
#     amount=5,
#     decimals=6,
#     signers=[]
#         )
#     )
# )
# client = Client(endpoint="https://api.devnet.solana.com", commitment=Confirmed)
# owner = "FiDa3zBqm1GmfDFjnHsrzbp5TnYnMUZmeVEmFRKXJizu" # <-- need the keypair for the token owner here! 5j22en4YDzDNzmGm7WWVxxYGDQ3Y873p7joVbKncZ1Ke b58decode("2njiVCQv7kjLVKP5g5xSCJfJbRcDgNU5uQJML8jVJP5DLtjb8EF36KQgk378AwUewd4aNWDaccHBwMHgT8G2zDq3")
# client.send_transaction(
#     transaction, owner, opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed))