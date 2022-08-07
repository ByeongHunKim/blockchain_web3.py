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
from solana.rpc.types import TokenAccountOpts
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer_checked, TransferCheckedParams



client = Client("https://api.devnet.solana.com")

# create_associated_token_account 서명자 - 모계좌 == 관리자 
# 대신 지불해는 이유,, 토큰 생태계에 참여하는데 비용을 본인이 지불한다면 .. 거부감이 생길 것 같기 때문. 만약 본인 부담이라면, 0SOL을 보유하고 있는 경우엔 associated_token_account 생성 불가
feePayerAddr = ""
feePayerWalletAddr = PublicKey("") # feePayer's public_key
feePayerPriv = "" # feePayer's private_key
feePayerKeypair = b58d(feePayerPriv)
feePayer = Keypair.from_secret_key(feePayerKeypair)

# 7J2WXubt3sxFpFWTK2Sh4aMBndxtf1ovcGrbgWNSrfHb E7wNd8L9UusZdzft2rNVqwjsyqQy5BXNatfS2jKTRVMv
newOwner = '' # wallet_address = owner가 입력한 wallet_address로 이전 된다.
newOwnerPub = PublicKey(newOwner)
mint_address = '' # mint Address
mintAddr = PublicKey(mint_address)

# 먼저 associated_token_account가 존재 하는지 여부에 따라 생성 .. 이미 존재한다면 그냥 바로 전송

isUserHaveAcc = client.get_token_accounts_by_owner(newOwnerPub,TokenAccountOpts(mint=mint_address))
# userHaveAcc = isUserHaveAcc['result']['value'][0]['pubkey']
userHaveAcc = isUserHaveAcc['result']['value']


if len(userHaveAcc) != 0 :
  userTokenAcc = isUserHaveAcc['result']['value'][0]['pubkey']
  print("이미 토큰 어카운트 보유 중 : ", userTokenAcc)
  amount = float(50) # 유저가 token 출금페이지에서 입력한 금액 -> dest 값
  transfer_amount = int(amount*(10**9)) # 4. amount = 유저가 token 출금페이지에서 입력한 금액 -> sol -> lamports 단위로 변경필요 -> amount 값
  print("1.......transaction Token Amount2: ", transfer_amount)
  transaction = Transaction()
  transaction.add(transfer_checked(
      TransferCheckedParams(
          amount=transfer_amount,
          decimals=9,
          dest=PublicKey(userTokenAcc),
          mint=PublicKey(mint_address),
          owner=PublicKey(feePayerAddr),
          program_id=TOKEN_PROGRAM_ID,
          source=PublicKey(feePayerAddr)
          )))

  print("3......transaction info : ", transaction)

  transaction_result = client.send_transaction(transaction, feePayer)

  tokenTransferTnx = tranasaction_result['result']
  print('4......Token Transfer 진행중.........................')
  tokenTransferTnx = client.get_confirmed_transaction(tokenTransferTnx)
  print('5......Token Transfer 결과 : ', confirmedTxn)
  isConfirmTxn = client.confirm_transaction(tokenTransferTnx)
  print('6......Token Transfer 결과2 : ', isConfirmTxn)

else :
  print("토큰 어카운트 없음 -> 생성필요 : ", userHaveAcc)
  transaction = Transaction()
  create_txn = spl_token.create_associated_token_account(
      payer=feePayerWalletAddr, owner=newOwnerPub, mint=mintAddr
  )
  transaction.add(create_txn)

  result = client.send_transaction(transaction, feePayer)
  resultOfTxn = result['result']
  print(f"txHash 결과 == https://solscan.io/tx/{resultOfTxn}?cluster=devnet")

  print('initialize 진행중.........................')
  confirmedTxn = client.get_confirmed_transaction(resultOfTxn)
  print('initialize 결과 : ', confirmedTxn)
  isConfirmTxn = client.confirm_transaction(resultOfTxn)
  print('initialize 결과2 : ', isConfirmTxn)

  queryTokenAcc = client.get_token_accounts_by_owner(newOwnerPub,TokenAccountOpts(mint=mint_address))
  getTokenAcc = queryTokenAcc['result']['value'][0]['pubkey']
  print(f'initialize 완료! {newOwner} 에 연동된 token account 주소는: {getTokenAcc} 입니다.')
  
  amount = float(50) # 유저가 token 출금페이지에서 입력한 금액 -> dest 값
  transfer_amount = int(amount*(10**9)) # 4. amount = 유저가 token 출금페이지에서 입력한 금액 -> sol -> lamports 단위로 변경필요 -> amount 값
  print("1.......transaction Token Amount2: ", transfer_amount)
  transaction = Transaction()
  transaction.add(transfer_checked(
      TransferCheckedParams(
          amount=transfer_amount,
          decimals=9,
          dest=PublicKey(getTokenAcc),
          mint=PublicKey(mint_address),
          owner=PublicKey(feePayerAddr),
          program_id=TOKEN_PROGRAM_ID,
          source=PublicKey(feePayerAddr)
          )))

  print("3......transaction info : ", transaction)

  transaction_result = client.send_transaction(transaction, feePayer)

  tokenTransferTnx = tranasaction_result['result']
  print('4......Token Transfer 진행중.........................')
  tokenTransferTnx = client.get_confirmed_transaction(tokenTransferTnx)
  print('5......Token Transfer 결과 : ', confirmedTxn)
  isConfirmTxn = client.confirm_transaction(tokenTransferTnx)
  print('6......Token Transfer 결과2 : ', isConfirmTxn)








