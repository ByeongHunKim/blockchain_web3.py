# pip install web3 

from web3 import Web3, IPCProvider

web3 = Web3(IPCProvider("/path/to/geth.ipc"))

# 이더 송금  
@csrf_exempt
def sendEth2User(request):
    try:
        print("web3 - 연결여부 :", web3.isConnected())
        userID = request.POST.get('userID')
        userinfo = SignUp.objects.get(userPK= userID)
        getGasPrice = web3.eth.gasPrice
        Addr = userinfo.userPubKey
        AddrChecksum = web3.toChecksumAddress(Addr)
        # print(AddrChecksum)
        balanceOfAddr = web3.eth.getBalance(Addr)
        # print(balanceOfAddr)
        nonce = web3.eth.getTransactionCount(AddrChecksum)
        # print(nonce)
        value = web3.toWei(0.1, 'ether')
        # print(value)
        sendTx = web3.geth.personal.sendTransaction({
            'nonce':nonce,
            'from' : AddrChecksum,
            'gasPrice' : getGasPrice,
            'to' : '', # ex) 0x91a422C27d162020633B42b91a0FeA13aB6282a1
            'value' : value,
            'data' : ''
        }, 'asd123!')        
        unLock = web3.geth.personal.unlockAccount(AddrChecksum,'asd123!',10)
        lock = web3.geth.personal.lockAccount(AddrChecksum)
        time.sleep(10)
        afterBal = web3.eth.getBalance(AddrChecksum)
        value = web3.fromWei(afterBal,'ether')
        print('잔액은', value, 'ETH')
        context = {'value' : '1', 'afterBal': afterBal}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print('error')
        context = {'value' : '-99'}
        return HttpResponse(json.dumps(context))