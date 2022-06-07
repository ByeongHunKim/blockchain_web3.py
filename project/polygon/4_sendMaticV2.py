from web3 import Web3, IPCProvider, HTTPProvider

# ()
# web3 = Web3(IPCProvider("/home/bstudent/geth_project/rinkeby/geth.ipc"))

## https://matic-mumbai.chainstacklabs.com
print("------------------------------------------------------------------------")
web3 = Web3(HTTPProvider("https://matic-mumbai.chainstacklabs.com"))
print("IPCProvider로 생성된 계정으로는 polygon을 전송하기가 어렵다.")
w3 = Web3(IPCProvider("/home/bstudent/project/rinkeby1/geth.ipc"))
print("------------------------------------------------------------------------")

ethIsConnected = w3.isConnected()
print("1. 이더리움 연결여부:", ethIsConnected)

maticIsConnected = web3.isConnected()
print("1.1 폴리곤 연결여부:", maticIsConnected)


Addr = "0xe47EFa9B187563D533E6F3D01CA0b727cdc1494f"
privKey = "" # privkey
AddrChecksum = web3.toChecksumAddress(Addr)
print("2. checkSum - 확인여부 :", AddrChecksum)
# print("2.1 privKey - 확인여부 :", privKey)

getGasPrice = web3.eth.gasPrice
print("3. 가스비 - 확인여부 :", getGasPrice)

balanceOfAddr = web3.eth.getBalance(Addr)
print("4. 잔액 - 확인여부 :", balanceOfAddr)

nonce = web3.eth.getTransactionCount(AddrChecksum)
print("4. 논스 - 확인여부 :", nonce)

value = web3.toWei(0.19, 'ether')
print("5. 보내는금액 - 확인여부 :", value)

tx = {'nonce': nonce,
      'to': '0xC1F72d2436f6f23384c2d035e509f795450C2434',
      'value': value,
      'gas': 21000,
      'gasPrice': getGasPrice,
      'chainId': 80001
      }

signed_tx = web3.eth.account.signTransaction(tx, privKey)
print("6. 트랜잭션 - 확인여부 :", signed_tx)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print("7. 트랜잭션 전송 - 확인여부 :", web3.toHex(tx_hash))

# unLock = web3.geth.personal.unlockAccount(AddrChecksum,'asd123!',10)
# lock = web3.geth.personal.lockAccount(AddrChecksum)
# time.sleep(10)
# afterBal = web3.eth.getBalance(AddrChecksum)
# value = web3.fromWei(afterBal,'ether')
# print('잔액은', value, 'ETH')


# sendTx = w3.geth.personal.sendTransaction({
#     'nonce':nonce,
#     'from' : AddrChecksum,
#     'gasPrice' : getGasPrice,
#     'to' : '0xC1F72d2436f6f23384c2d035e509f795450C2434',
#     'value' : value,
#     'data' : '',
#     'chainId': 80001
# }, 'asd123!')

# print("7. 트랜잭션 전송 - 확인여부 :", web3.toHex(sendTx))

# 로컬에서 운영하고 있는 geth로 계정을 생성하고 그 계정에 https://faucet.polygon.technology/ 이곳에서 테스트 매틱을 받고 이더리움처럼 sendTx를 보내려고 하였는데, 실패하였다
# web3 를 맨위에서 폴리곤 HTTPProvider를 가져오고, web3.peth.personal.sendTransaction 으로 보내려면 IPCProvider를 해야하기 때문.
