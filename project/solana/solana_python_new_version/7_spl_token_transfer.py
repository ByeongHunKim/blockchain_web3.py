from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer_checked, TransferCheckedParams
from solana.publickey import PublicKey
from solana.rpc.commitment import Confirmed
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
from solana.transaction import Transaction
from base58 import b58encode, b58decode as b58d
from base64 import b64decode
from pprint import pprint as p
from solana.rpc.types import TokenAccountOpts
import time


b58e = lambda x: b58encode(x).decode('ascii')

client = Client("https://api.devnet.solana.com")

feePayer = ""
feePayerPriv = ""

mint_address = '' # mint Address


queryTokenAcc = client.get_token_accounts_by_owner(feePayer,TokenAccountOpts(mint=mint_address))
getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']

fromAddr = getTokenAcc
toAddr = "" # 유저가 입력할 associated_token_account 주소


feePayerKeypair = b58d(feePayerPriv)
print(f"2.feePayerKeypair = {feePayerKeypair}")
Signer = Keypair.from_secret_key(feePayerKeypair) # == alice1 = Keypair.from_secret_key(b58d("621yVKGcYBMudqUT9AkHpAohXjunWAWMtXz1NyCjK4wa5NCW886kD5z9AL8wRyjxpqB7LwYPMEaw8444da3roMRu"))
print(f"3.트랜잭션 서명자 = {Signer}")

amount = float(50) # 유저가 token 출금페이지에서 입력한 금액 -> dest 값
print("4. amount: ", amount)
transfer_amount = int(amount*(10**9)) # 4. amount = 유저가 token 출금페이지에서 입력한 금액 -> sol -> lamports 단위로 변경필요 -> amount 값
print("5. transfer_amount: ", transfer_amount)

transaction = Transaction()
transaction.add(transfer_checked(
    TransferCheckedParams(
        amount=transfer_amount,
        decimals=9,
        dest=PublicKey(toAddr),
        mint=PublicKey(mint_address),
        owner=PublicKey(feePayer),
        program_id=TOKEN_PROGRAM_ID,
        source=PublicKey(fromAddr)
        )))

print(f"6.transaction = {transaction}")
transaction_result = client.send_transaction(transaction, Signer)
resultOfTxhash = transaction_result['result']
print(f"7.txHash = https://solscan.io/tx/{resultOfTxhash}?cluster=devnet")

result = client.get_token_account_balance(getTokenAcc)
before_tokenVal = result['result']['value']['uiAmount']
print("8. 토큰 전송 전 유저의 토큰 잔액은? : ", before_tokenVal)
print("------------------------트랜잭션 처리중.........------------------------")
time.sleep(20)
print("-----------------------트랜잭션 처리완료 -> 토큰 잔액 계산 진행--------------")
result = client.get_token_account_balance(getTokenAcc)
after_tokenVal = result['result']['value']['uiAmount']
print("9. 토큰 전송 후 유저의 토큰 잔액은? : ", after_tokenVal)

result_of_value = int(after_tokenVal- before_tokenVal)

print(f"{result_of_value}TOKEN이 출금되었습니다.")