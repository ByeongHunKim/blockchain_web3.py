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

from solana.rpc.async_api import AsyncClient
import solana.system_program as sys
from spl.token.async_client import AsyncToken
from spl.token._layouts import MINT_LAYOUT
import spl.token.instructions as spl_token


b58e = lambda x: b58encode(x).decode('ascii')

client = Client("https://api.devnet.solana.com")

feePayer = ""
feePayerPriv = ""
feePayerKeypair = b58d(feePayerPriv)
feePayer_final = Keypair.from_secret_key(feePayerKeypair)


mint_address = '' # mint Address


queryTokenAcc = client.get_token_accounts_by_owner(feePayer,TokenAccountOpts(mint=mint_address))
getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']

fromAddr = getTokenAcc

#  
toAddrWalletAddr = "" # 유저가 입력할 toAddr을 지갑주소를 입력하면 associated_token_account 주소를 찾아낸다.
queryToAddrTokenAcc = client.get_token_accounts_by_owner(toAddrWalletAddr,TokenAccountOpts(mint=mint_address))
toAddrHaveAcc = queryToAddrTokenAcc['result']['value']


# 일반 지갑주소를 입력하면 -> associated_token_account를 조회해서 없으면 토큰어카운트 생성해서 보내주고, 


# if token account 가 존재하지 않는다면 1. associated_token_account 생성 트랜잭션 -> 2. spl-token-transfer 트랜잭션 # isLoading을 finalized 값을 받으면 로딩 애니메이션 종료

if len(toAddrHaveAcc) != 0 :
  
  toAddrHaveAcc = queryToAddrTokenAcc['result']['value'][0]['pubkey']
  print('toAddrHaveAcc 값 존재 ----> spl-token-transfer 시작', toAddrHaveAcc)
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
          dest=PublicKey(toAddrHaveAcc),
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
  # time.sleep(20)
  isConfirmTxn = client.confirm_transaction(resultOfTxhash)
  print('...............Token Transfer 결과: ', isConfirmTxn)
  print("-----------------------트랜잭션 처리완료 -> 토큰 잔액 계산 진행--------------")
  result = client.get_token_account_balance(getTokenAcc)
  after_tokenVal = result['result']['value']['uiAmount']
  print("9. 토큰 전송 후 유저의 토큰 잔액은? : ", after_tokenVal)

  result_of_value = int(after_tokenVal- before_tokenVal)

  print(f"{result_of_value}TOKEN이 출금되었습니다.")


else :
  print("토큰 어카운트 없음 -> 생성필요 : ", toAddrHaveAcc)
  feePayerKeypair = b58d(feePayerPriv)
  print(f"2.feePayerKeypair = {feePayerKeypair}")
  Signer = Keypair.from_secret_key(feePayerKeypair) # == alice1 = Keypair.from_secret_key(b58d("621yVKGcYBMudqUT9AkHpAohXjunWAWMtXz1NyCjK4wa5NCW886kD5z9AL8wRyjxpqB7LwYPMEaw8444da3roMRu"))
  print(f"3.트랜잭션 서명자 = {Signer}")
  transaction = Transaction()
  create_txn = spl_token.create_associated_token_account(
      payer=PublicKey(feePayer), owner=PublicKey(toAddrWalletAddr), mint=PublicKey(mint_address)
  )
  transaction.add(create_txn)
  result = client.send_transaction(transaction, feePayer_final)
  resultOfTxn = result['result']
  print(f"txHash 결과 == https://solscan.io/tx/{resultOfTxn}?cluster=devnet")
  print('initialize 진행중.........................')
  confirmedTxn = client.get_confirmed_transaction(resultOfTxn)
  print('initialize 결과 : ', confirmedTxn)
  isConfirmTxn = client.confirm_transaction(resultOfTxn)
  print('initialize 결과2 : ', isConfirmTxn)

  queryTokenAcc = client.get_token_accounts_by_owner(PublicKey(toAddrWalletAddr),TokenAccountOpts(mint=mint_address))
  getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']
  print(f'initialize 완료! {toAddrWalletAddr} 에 연동된 token account 주소는: {getTokenAcc} 입니다.')

  amount = float(50) # 유저가 token 출금페이지에서 입력한 금액 -> dest 값
  print("4. amount: ", amount)
  transfer_amount = int(amount*(10**9)) # 4. amount = 유저가 token 출금페이지에서 입력한 금액 -> sol -> lamports 단위로 변경필요 -> amount 값
  print("5. transfer_amount: ", transfer_amount)

  transaction = Transaction()
  transaction.add(transfer_checked(
      TransferCheckedParams(
          amount=transfer_amount,
          decimals=9,
          dest=PublicKey(getTokenAcc),
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
  # time.sleep(20)
  isConfirmTxn = client.confirm_transaction(resultOfTxhash)
  print('...............Token Transfer 결과: ', isConfirmTxn)
  print("-----------------------트랜잭션 처리완료 -> 토큰 잔액 계산 진행--------------")
  result = client.get_token_account_balance(getTokenAcc)
  after_tokenVal = result['result']['value']['uiAmount']
  print("9. 토큰 전송 후 유저의 토큰 잔액은? : ", after_tokenVal)

  result_of_value = int(after_tokenVal- before_tokenVal)

  print(f"{result_of_value}TOKEN이 associate_token_account 주소 생성 후 해당 주소로 출금되었습니다.")



