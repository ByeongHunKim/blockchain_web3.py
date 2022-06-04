from web3 import Web3, IPCProvider, HTTPProvider

# ()
# web3 = Web3(IPCProvider("/home/bstudent/geth_project/rinkeby/geth.ipc"))

## https://matic-mumbai.chainstacklabs.com
web3 = Web3(HTTPProvider("https://matic-mumbai.chainstacklabs.com"))

isConnected = web3.isConnected()
print("1. 폴리곤 연결여부:", isConnected)

Addr = "0x024Aff00fC375270913E0CdF0b91814457075f3d"
privKey = "privkey" # privkey
AddrChecksum = web3.toChecksumAddress(Addr)
print("2. checkSum - 확인여부 :", AddrChecksum)
print("2.1 privKey - 확인여부 :", privKey)

getGasPrice = web3.eth.gasPrice
print("3. 가스비 - 확인여부 :", getGasPrice)

balanceOfAddr = web3.eth.getBalance(Addr)
print("4. 잔액 - 확인여부 :", balanceOfAddr)

nonce = web3.eth.getTransactionCount(AddrChecksum)
print("4. 논스 - 확인여부 :", nonce)

value = web3.toWei(0.05, 'ether')
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