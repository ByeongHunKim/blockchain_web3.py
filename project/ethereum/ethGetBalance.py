# pip install web3 

from web3 import Web3, IPCProvider

web3 = Web3(IPCProvider("/home/bstudent/project/rinkeby1/geth.ipc"))


print("이더리움 연결 결과: ", web3.isConnected())

myAddr = "0xC1F72d2436f6f23384c2d035e509f795450C2434"

myAddrChecksum = web3.toChecksumAddress(myAddr)

print(myAddrChecksum)

balanceOfAddr = web3.eth.getBalance(myAddrChecksum)

print("나의 지갑안에 있는 이더리움 잔액은? :", balanceOfAddr)

realEthValue = web3.fromWei(balanceOfAddr, 'ether')

print("나의 지갑안에 있는 실제 이더리움 잔액은? :", realEthValue)




# 이더 잔액 조회 
# @csrf_exempt
# def UserEthbal(request):
#     try:
#         userID = request.POST.get('userID')
#         userinfo = SignUp.objects.get(userPK = userID)
#         Addr = userinfo.userPubKey
#         AddrChecksum = web3.toChecksumAddress(Addr)
#         print(AddrChecksum)
#         balanceOfAddr = web3.eth.getBalance(AddrChecksum)
#         value = web3.fromWei(balanceOfAddr,'ether')
#         print(value)
#         context = {'value' : '1', 'value' : value}
#         return HttpResponse(json.dumps(context))
#     except Exception as error:
#         print('error')
#         context = {'value' : '-99'}
#         return HttpResponse(json.dumps(context))