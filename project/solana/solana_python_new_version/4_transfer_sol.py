import solana
from solana.rpc.api import Client
from solana.account import Account
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction
from base58 import b58encode, b58decode
b58e = lambda x: b58encode(x).decode('ascii')
import time

client = Client("https://api.devnet.solana.com")
test = client.is_connected()
print("1. 솔라나와 연결여부:" ,test)

fromAddr = ""
print("2. 보내는 지갑주소 :" ,fromAddr)

fromAddrPriv = ""
# fromAddrDecode = b58decode(fromAddrPriv)
# fromAddrEncode = b58e(fromAddrDecode)
print("3. 보내는지갑 비밀키 :" ,fromAddrPriv)
# print("3.1 보내는지갑 비밀키 :" ,fromAddrDecode)
# print("3.2 보내는지갑 비밀키 :" ,fromAddrEncode)

toAddr = "" # toAddr = request.POST.get('toAddr')
print("4. 받는 지갑주소:" ,toAddr)

ready_to_sign = b58decode(fromAddrPriv)
sign_key = Keypair.from_secret_key(ready_to_sign)
print("5. 트랜잭션 서명할 signkey:" ,sign_key)

sol_amount = float(0.1)
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
transaction_result = client.send_transaction(transaction, sign_key)
print("8. tx 결과 :" ,transaction_result)
# 완료된 tx체크 
# 8. tx 결과 : {'jsonrpc': '2.0', 'result': '5kANUdvX1h5181nB8D4c6b3vFyRUSqRvvvGmKMKZRrXiYMvd8wxjUmW2mDBLiAizRUi4RGjVX7CUUAUZwz96jyPC', 'id': 2}

resultOfTxhash = transaction_result['result']

print("8.1 txHash값 :" ,resultOfTxhash)

print(f"9. txHash 결과 == https://solscan.io/tx/{resultOfTxhash}?cluster=devnet")

print("블록에 기록중...........................................................")
getBalance = client.get_balance("")

print("10. get_balance 결과 :",getBalance)
# {'jsonrpc': '2.0', 'result': {'context': {'slot': blockNumber를 의미 }, 'value': lamports 단위의 잔액을 의미}, 'id': 1}

before_lamports = getBalance['result']['value']
print("11. 입금 확인 전 지갑 잔액의 lamports 값 접근 :",before_lamports)
# lamports 단위의 잔액만 조회가 가능하다 토큰은 다르게 , json안에 ui_value가 있음

ui_balance = round(before_lamports*10**(-9),5) # ,5 의 5라는 숫자는 소수점 몇자리 까지 보여줄지 정하는 것. 
print("12. 입금 확인 전 지갑 잔액의 lamports 값 sol단위로 변환한 값 :",ui_balance)
time.sleep(20)
print("블록에 기록완료 --> 입금 금액 확인")
getBalance = client.get_balance("")

print("13. 입금 후 get_balance 결과 :",getBalance)
# {'jsonrpc': '2.0', 'result': {'context': {'slot': blockNumber를 의미 }, 'value': lamports 단위의 잔액을 의미}, 'id': 1}

after_lamports = getBalance['result']['value']
print("14. 입금 후 지갑 잔액의 lamports 값 접근 :",after_lamports)
# lamports 단위의 잔액만 조회가 가능하다 토큰은 다르게 , json안에 ui_value가 있음
ui_balance = round(after_lamports*10**(-9),5) # ,5 의 5라는 숫자는 소수점 몇자리 까지 보여줄지 정하는 것. 

result_of_lamports = int(after_lamports - before_lamports)


result_of_txn = round(result_of_lamports*10**(-9),5) # ,5 의 5라는 숫자는 소수점 몇자리 까지 보여줄지 정하는 것. 
print("15. 입금 후 지갑 잔액의 lamports 값 sol단위로 변환한 값 :",ui_balance)
print(f"16. +{result_of_txn}SOL이 입금되었습니다. phantom wallet 또는 https://solscan.io/tx/{resultOfTxhash}?cluster=devnet 를 확인해보세요")


# 3i6NvQUDi55ehkmgfQR9PK6inQDbuVMHJKT7Gt7ZEyGbhbpsrGvMvtVBFgws7QEQ6qM11nyKMncjE6jLUtfAhdAa
# 위의 txHash를 solscan에 넣으면 조회가 가능하다.

# context = {'value' : '1','ui_balance':ui_balance}
# txFromAddr, txToAddr, txLamport2Sol, resultOfTxhash 등을 넣어서 front에 주던지.. transaction_result['result']
# ExethValue = request.POST.get('ExethValue') # 유저가(from)이 전송하겠다고 UI에 입력한 toAddr값
# toAddr = request.POST.get('toAddr') # 유저가(from)이 전송하겠다고 UI에 입력한 sol 금액 값