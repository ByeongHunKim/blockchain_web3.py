# pip install web3 

from web3 import Web3, IPCProvider

web3 = Web3(IPCProvider("/path/to/geth.ipc"))

@csrf_exempt
def newAccount(request):
    try:
        print("-----------------------------계좌 생성--------------------------------")
        print("web3 - Connection : ", web3.isConnected())
        userID = request.POST.get('userID')
        addr = web3.geth.personal.newAccount('PW')
        print('addr: ', addr)
        userinfo = SignUp.objects.get(id = userID)
        userinfo.ethAddr = addr
        userinfo.save()
        print(userinfo.username + " 님 유저 계좌 생성 완료 : " + addr)
        print("----------------------------------------------------------------------")
        context = {'value':'1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print(error)
        context = {'value':'-99'}
        return HttpResponse(json.dumps(context))