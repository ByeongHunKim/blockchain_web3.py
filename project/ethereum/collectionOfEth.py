# pip install web3 

from web3 import Web3, IPCProvider

web3 = Web3(IPCProvider("/path/to/geth.ipc"))

# 집금
@csrf_exempt
def collectEthToMain(request):
    try:
        print("web3 - 연결여부 :", web3.isConnected())
        # userID = request.POST.get('userID')
        # userinfo = SignUp.objects.get(userPK= '1')
        userinfo = SignUptest.objects.get(id= '1')
        print("------------------------------모계좌 입금--------------------------------")
        Maddr = ""
        Uaddr = userinfo.ethAddr
        MaddrCheckSumAddr =  web3.toChecksumAddress(Maddr)
        UaddrCheckSumAddr =  web3.toChecksumAddress(Uaddr)
        queryUaddr = web3.eth.getBalance(UaddrCheckSumAddr)
        wei2EthUaddr = queryUaddr / 1000000000000000000
        if wei2EthUaddr >= 0.05:
            print('보내는 계좌: ', UaddrCheckSumAddr)
            print('모 계좌:   ', MaddrCheckSumAddr)
            print('보내는 계좌 잔액: ', wei2EthUaddr, "ETH")
            realValueOfUaddr = queryUaddr - 2000000000000000
            getPrice = web3.eth.gasPrice
            totalGas = int(getPrice * 21000)
            sendTx = web3.geth.personal.sendTransaction({
                "from": UaddrCheckSumAddr,
                "gasPrice": getPrice,
                "gas": "21000",
                "to": MaddrCheckSumAddr,
                "value": realValueOfUaddr,
                "data": ""
            }, 'asd123!')
            print(sendTx)
            time.sleep(20)
            print('보내는 계좌: ', UaddrCheckSumAddr)
            print('모 계좌:   ', MaddrCheckSumAddr)
        else:
            print("유저가 집금되기 부족한 잔액을 가지고 있습니다.")
        context = {'value' : '1'}
        return HttpResponse(json.dump(context))
    except Exception as error:
        print('error')
        context = {'value' : '-99'}
        return HttpResponse(json.dumps(context))
    