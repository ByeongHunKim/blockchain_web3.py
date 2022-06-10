# import subprocess
# with open('airdrop.txt', 'r+') as f: #r+ does the work of rw
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         list_files = subprocess.Popen(["spl-token", "transfer", "--fund-recipient", "3oMguQN22MkB8n7BMbsRFqEeJceR8vd2FmuZLiCBcNig", "300000",lines[i].strip()], )
#         list_files.wait()
#     f.seek(0)
#     for line in lines:

#         f.write(line)
#         print(line)

import subprocess
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction
import time

cli = Client("https://api.devnet.solana.com")
print("about to check connection")
print("here is the connection: ", cli.is_connected())

# sender = Keypair()
# print(sender.secret_key)
value = 100
toAddr = "AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn"

# process_airdrop = subprocess.Popen(f"spl-token transfer --fund-recipient 3oMguQN22MkB8n7BMbsRFqEeJceR8vd2FmuZLiCBcNig {value} {toAddr}", shell=True) # solana --url https://api.devnet.solana.com airdrop 1 {sender.public_key}
# process_airdrop.wait()

getBalance = cli.get_balance("AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn")
getBalance1 = cli.get_token_account_balance("G8Wq2zGqJYw7T4RpurJcdfHdyEnrbSvBBgdXPCNP5cQi")
print(getBalance)
print(getBalance1)

# receiver = Keypair()
# process_airdrop = subprocess.Popen(f"solana --url https://api.devnet.solana.com airdrop 1 {receiver.public_key}", shell=True)
# process_airdrop.wait()
        
# time.sleep(10)

# txn = Transaction().add(transfer(TransferParams(from_pubkey=sender.public_key, to_pubkey="FiDa3zBqm1GmfDFjnHsrzbp5TnYnMUZmeVEmFRKXJizu", lamports = int(5e6))))
# result = cli.send_transaction(txn, sender)

# print("result: ", result)

# time.sleep(20)
# print("here is the sender balanace: ", self.get_account_balance(key_value=str(sender.public_key)))
# print("here is the receiver balanace: ", self.get_account_balance(key_value=str(receiver.public_key)))