import solana
from solana.rpc.api import Client
from solana.account import Account
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction
from base58 import b58encode, b58decode


client = Client("https://api.devnet.solana.com")

test = client.is_connected()

print("1. 솔라나와 연결여부:" ,test)



fromAddr = "AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn"
print("2. 보내는 지갑주소 :" ,fromAddr)

fromAddrPriv = "privkey"
print("3. 보내는지갑 비밀키 :" ,fromAddrPriv)

toAddr = "D2oE8PK7zkgNBhPGL6Ro4hctcEStbFZKonZAxStap4zx"
print("4. 받는 지갑주소:" ,toAddr)

signKey = b58decode(fromAddrPriv) 
print("5. 트랜잭션 서명할 signkey:" ,signKey)

sol_amount = 0.1
print("6. 보낼 솔라나 금액:" ,sol_amount)

# transaction
transfer_parameters = TransferParams(
    from_pubkey=PublicKey(fromAddr),
    to_pubkey=PublicKey(toAddr),
    lamports=int(sol_amount*(10**9))
)
print("7. tx 내용 :" ,transfer_parameters)
# 7. tx 내용 : TransferParams(from_pubkey=AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn, to_pubkey=D2oE8PK7zkgNBhPGL6Ro4hctcEStbFZKonZAxStap4zx, lamports=100000000)

sol_transfer = transfer(transfer_parameters)
print("7.1 sol_transfer 내용 :" ,sol_transfer)

transaction = Transaction().add(sol_transfer)
print("7.2 transaction 내용 :" ,transaction)

# transaction sign
transaction_result = client.send_transaction(transaction, Keypair.from_secret_key(signKey))
print("8. tx 결과 :" ,transaction_result)
# 완료된 tx체크 
# 8. tx 결과 : {'jsonrpc': '2.0', 'result': '5kANUdvX1h5181nB8D4c6b3vFyRUSqRvvvGmKMKZRrXiYMvd8wxjUmW2mDBLiAizRUi4RGjVX7CUUAUZwz96jyPC', 'id': 2}
