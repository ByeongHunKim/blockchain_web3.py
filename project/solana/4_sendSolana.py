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

fromAddrPriv = ""
print("3. 보내는지갑 비밀키 :" ,fromAddrPriv)

toAddr = "D2oE8PK7zkgNBhPGL6Ro4hctcEStbFZKonZAxStap4zx" # toAddr = request.POST.get('toAddr')
print("4. 받는 지갑주소:" ,toAddr)

signKey = b58decode(fromAddrPriv) 
print("5. 트랜잭션 서명할 signkey:" ,signKey)

sol_amount = 0.1 # ExsolValue = request.POST.get('ExsolValue')
print("6. 보낼 솔라나 금액:" ,sol_amount)

# transaction
transfer_parameters = TransferParams(
    from_pubkey=PublicKey(fromAddr),
    to_pubkey=PublicKey(toAddr),
    lamports=int(sol_amount*(10**9))
)

txFromAddr = transfer_parameters.from_pubkey
txToAddr = transfer_parameters.to_pubkey
txLamport2Sol = round(transfer_parameters.lamports*10**(-9),9)

print("7. tx 내용 :" ,transfer_parameters) # 7. tx 내용 : TransferParams(from_pubkey=AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn, to_pubkey=D2oE8PK7zkgNBhPGL6Ro4hctcEStbFZKonZAxStap4zx, lamports=100000000)
print("7.1 tx 내용 - fromAddr :" ,txFromAddr) # 7.1 tx 내용 - fromAddr : AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn
print("7.1.1 tx 내용 - toAddr :" ,txToAddr) # 7.1.1 tx 내용 - toAddr : D2oE8PK7zkgNBhPGL6Ro4hctcEStbFZKonZAxStap4zx
print("7.1.2 tx 내용 - lamports :" ,txLamport2Sol) # 7.1.2 tx 내용 - lamports : 0.1


sol_transfer = transfer(transfer_parameters)
print("7.2 sol_transfer 내용 :" ,sol_transfer) 
# 7.2 sol_transfer 내용 : TransactionInstruction(keys=[AccountMeta(pubkey=AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn, is_signer=True, is_writable=True), AccountMeta(pubkey=D2oE8PK7zkgNBhPGL6Ro4hctcEStbFZKonZAxStap4zx, is_signer=False, is_writable=True)], program_id=11111111111111111111111111111111, data=b'\x02\x00\x00\x00\x00\xe1\xf5\x05\x00\x00\x00\x00')

transaction = Transaction().add(sol_transfer)
print("7.3 transaction 내용 :" ,transaction) # 7.3 transaction 내용 : <solana.transaction.Transaction object at 0x7f044635d890>
 
# transaction sign
transaction_result = client.send_transaction(transaction, Keypair.from_secret_key(signKey))
print("8. tx 결과 :" ,transaction_result)
# 완료된 tx체크 
# 8. tx 결과 : {'jsonrpc': '2.0', 'result': '5kANUdvX1h5181nB8D4c6b3vFyRUSqRvvvGmKMKZRrXiYMvd8wxjUmW2mDBLiAizRUi4RGjVX7CUUAUZwz96jyPC', 'id': 2}

resultOfTxhash = transaction_result['result']

print("8.1 txHash값 :" ,resultOfTxhash)
# 3i6NvQUDi55ehkmgfQR9PK6inQDbuVMHJKT7Gt7ZEyGbhbpsrGvMvtVBFgws7QEQ6qM11nyKMncjE6jLUtfAhdAa
# 위의 txHash를 solscan에 넣으면 조회가 가능하다.

# context = {'value' : '1','ui_balance':ui_balance}
# txFromAddr, txToAddr, txLamport2Sol, resultOfTxhash 등을 넣어서 front에 주던지.. transaction_result['result']
# ExethValue = request.POST.get('ExethValue') 유저가(from)이 전송하겠다고 UI에 입력한 toAddr값
# toAddr = request.POST.get('toAddr')유저가(from)이 전송하겠다고 UI에 입력한 sol 금액 값
