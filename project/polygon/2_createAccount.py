from web3 import Web3, IPCProvider, HTTPProvider
from base58 import b58encode, b58decode

web3 = Web3(HTTPProvider("https://matic-mumbai.chainstacklabs.com"))
print("1. 폴리곤 연결여부:", isConnected)

# privKey = "input_privkey"

# account = web3.eth.accounts.privateKeyToAccount(privKey)

# acct = web3.eth.account.create(privKey)

# publicKey = acct.address
# secretKey = acct.privateKey

# print('publickey: ', publicKey)
# print('privkey: ', secretKey)

#print('privkey: ', acct.privateKey)

#makePrivKey = secretKey + secretKey

#realPrivKey = b64encode(makePrivKey).decode()

#print('realPrivKey: ', realPrivKey)

# print("2. privkey: ", privKey)
# print("3. account: ", account)

# acct = web3.eth.account.create("asd123!")
# print('addr: ', acct.address)


# 두번째로 생성한 지갑주소 0xf1337471403D2D7E7a83166c5E48dd619ecc95c3
# 이 계정이 asd123! 으로 tx 전송이 가능한지.. 그리고 privKey는 어떻게 아는지? 
# 메타마스크 연동을 위함 

# balanceOfAddr = web3.eth.getBalance("0xab3a34C0039560184493e5eB852aad4213E62e8D")

# print(balanceOfAddr)

# eth2Matic = web3.fromWei(balanceOfAddr, "ether")

# print(eth2Matic)