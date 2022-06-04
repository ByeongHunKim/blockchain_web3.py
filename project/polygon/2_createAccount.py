from web3 import Web3, IPCProvider, HTTPProvider
from base64 import b64encode, b64decode
from eth_account import Account
import secrets

web3 = Web3(HTTPProvider("https://matic-mumbai.chainstacklabs.com"))

isConnected = web3.isConnected()

print("1. 폴리곤 연결여부:", isConnected)

priv = secrets.token_hex(32)
private_key = "0x" + priv
print ("2. 생성된 비밀키 남에게 보여주지 말 것 :", private_key)
acct = Account.from_key(private_key)
print("3. 생성된 공개키 지갑주소:", acct.address)

# 메타마스크에 2번에 생성된 비밀키로 지갑 가져오기 성공




# privKey = "input_privkey"



#account = web3.eth.account.create()

#publicKey = account.address
#privateKey = account.privateKey

#print('2. account :', account) # <eth_account.signers.local.LocalAccount object at 0x7f18bd173dc0>
#print('-----------------------------------')
#print('3. publickey :', publicKey) # publickey : 0xC63f8bDed84FFd8955f642F2F80EeCd3b2F3Cb9a
#print('4. privkey :', privateKey) # privkey : b'\xea_yT$\x84\n\xd7\x00\xf5`\x16\x9a\x08#\xcdJ"\r\xe9:N\xe3i#|\xa9\xa86\xa9W\x82'

#bytespublicKey = bytes(account.address)

#print('4.1 bytespublicKey :', bytespublicKey)

#realPrivKey = privateKey + bytespublicKey

#realPrivKey = b64encode(privateKey).decode()
#print('5. realPrivKey :', realPrivKey)


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