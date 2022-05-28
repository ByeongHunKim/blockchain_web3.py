# pip install web3 

from web3 import Web3, IPCProvider

web3 = Web3(IPCProvider("/path/to/geth.ipc"))

# 이더 잔액 조회 
@csrf_exempt
def UserEthbal(request):
    try:
        userID = request.POST.get('userID')
        userinfo = SignUp.objects.get(userPK = userID)
        Addr = userinfo.userPubKey
        AddrChecksum = web3.toChecksumAddress(Addr)
        print(AddrChecksum)
        balanceOfAddr = web3.eth.getBalance(AddrChecksum)
        value = web3.fromWei(balanceOfAddr,'ether')
        print(value)
        context = {'value' : '1', 'value' : value}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print('error')
        context = {'value' : '-99'}
        return HttpResponse(json.dumps(context))