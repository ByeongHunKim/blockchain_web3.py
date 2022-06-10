from solana.publickey import PublicKey
from solana.account import Account
from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.transaction import Transaction
from spl.token.instructions import transfer, TransferParams
from base58 import b58encode, b58decode

serum = PublicKey("FrtYJmnFSPHULjyvCJ2DRyMRUpBrvNYvHh5jxVvcPgdk") # Mainnet address
print("1.", serum)
sender, dest = "FiDa3zBqm1GmfDFjnHsrzbp5TnYnMUZmeVEmFRKXJizu", Account() # These are arbitrary accounts
senderPriv = "2njiVCQv7kjLVKP5g5xSCJfJbRcDgNU5uQJML8jVJP5DLtjb8EF36KQgk378AwUewd4aNWDaccHBwMHgT8G2zDq3"
signKey = b58decode(senderPriv) 
print("2.", sender)
print("2.", dest)
transfer_params = TransferParams(
     amount=10000,
     dest=dest.public_key(),
     owner=sender,
     program_id=serum,
     source=sender)
txn = Transaction()
txn.add(transfer(transfer_params))

solana_client = Client("https://api.devnet.solana.com") # ("https://api.mainnet-beta.solana.com")
solana_client.send_transaction(txn, Keypair.from_secret_key(signKey))

# import subprocess

# # subprocess.run(['ls'], shell=True, check=True)

# mintAddress = "3oMguQN22MkB8n7BMbsRFqEeJceR8vd2FmuZLiCBcNig"
# toAddr = "FiDa3zBqm1GmfDFjnHsrzbp5TnYnMUZmeVEmFRKXJizu"
# amount = 100.00

# subprocess.run(["spl-token", "transfer", "--fund-recipient", mintAddress, amount, toAddr], check=True, text=True)

# def build_spl_transfer_tokens_instructions(
#     context: Context,
#     wallet: Wallet,
#     token: Token,
#     source: PublicKey,
#     destination: PublicKey,
#     quantity: Decimal,
# ) -> CombinableInstructions:
#     amount = int(token.shift_to_native(quantity))
#     instructions = [
#         transfer(
#             TransferParams(
#                 TOKEN_PROGRAM_ID, source, destination, wallet.address, amount, []
#             )
#         )
#     ]
#     return CombinableInstructions(signers=[], instructions=instructions)