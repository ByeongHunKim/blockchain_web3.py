
# case 1: 내부 지갑 간 거래
# case 0: 내부지갑 -> 외부지갑 거래
# UI에서보여지는 것은 내부지갑에서 외부지갑 간 전송이지만, 백단에서 실제 이루어지는 작업은 모계좌에서 유저가 입력한 이더리움을 모계좌로 대신 전송해준다
# 하지만 유저가 앱 내부지갑이 생성된 이후 기존에 있던 외부지갑에서 내부지갑으로 이더리움을 전송한 경우, 수수료를 본인이 지불하지만 이후 발생되는 수수료는 전송된 이더리움에서 차감이 된다.
# case0의 경우도 모계좌가 대신 지불해주지 않고 전송하는 이더리움에서 수수료 차감이 된 차액을 to지갑이 받게된다. 

@csrf_exempt
def ethWithdraw(request):
    try:
        userPK = request.POST.get('userPk') # 유저마다 정해지는 고유의 값, 보내는 사람의 pk값이 할당됨
        userAddr = request.POST.get('userAddr') # 보내는 사람 주소
        toAddr = request.POST.get('toAddr') # 유저가 입력한 주소
        volume = request.POST.get('volume') # 수수료를 적용해서 받는사람이 실제 받는 값
        ExethValue = request.POST.get('ExethValue') # 유저가 ui에 보낸다고 입력한 값
        userinfo = SignUptest.objects.filter(ethAddr = toAddr).count()
        if userinfo == 1:  # 내부계좌전송
            userTo = SignUptest.object.get(ethAddr = toAddr) # 만약 유저가 송금할 계좌가 앱에서 만든 계좌면
            ToethVal = float(userTo.ethValue) # 일단 DB에 있는 송금계좌 잔액 가져와
            ToethVal1 = float(volume) + ToethVal # 그리고 db에 유저가 보내겠다고 한 금액을 더해줘
            print('받는사람 계좌 DB에 찍혀야 하는 금액',ToethVal1 )
            userTo.ethValue = str(ToethVal1) # 받는사람 DB 이더 잔액에 들어가야 할 금액 = 기존금액 + 유저가 인터페이스에 보내겠다고 한 금액

            user = SignUptest.objects.get(id = userPK) # 보낸다고 한 사람의 고유 pk값
            SendUserEthbal = float(user.ethValue)  # 보내는 유저의 기존 가지고 있던 잔액
            SendUserEthbal1 = SendUserEthbal - float(ExethValue) # 그러면 보내는 유저 DB에서는 기존에 있던 값에서 보낸다고한 값을 빼줘야 한다
            user.ethValue = str(SendUserEthbal1) 
            user.save()
            userTo.save()
            now = datetime.now()
            now = now.strftime('%Y-%m-%d %H:%M:%S')
            userethwallSave = EthScan(
                userPK = userPK,
                userAddr = userAddr,
                # submitDate = datetime.now(),
                #status = None,
                blockHash = None,
                blockNumber = None,
                confirmations = None,
                contractAddress = None,
                cumulativeGasUsed = None,
                fromAddr = userAddr,
                gas = None,
                gasPrice = None,
                gasUsed = 21000,
                hash = None,
                input = None,
                isError = None,
                nonce = None,
                timeStamp = now,
                to = toAddr,
                transactionIndex = None,
                txreceipt_status = None,
                volume = volume,
            )
            userethwallSave.save()
        elif userinfo == 0:
            print("------------------------------출금--------------------------------")
            Maddr = '모계좌 주소'
            Uaddr = toAddr # 유저가 입력한 외부계좌
            MaddrCheckSumAddr = web3.toChecksumAddress(Maddr)
            UaddrCheckSumAddr = web3.toChecksumAddress(Uaddr)
            moAddr = web3.eth.getBalance(MaddrCheckSumAddr)
            getPrice = web3.eth.gasPrice;
            addrEth = float(ExethValue) * 1000000000000000000 
            addrEth = int(addrEth) 
            addrEth = int(addrEth - 2000000000000000) 
            totalGas = int(getPrice * 21000) 
            sendTx = web3.geth.personal.sendTransaction({
                "from": MaddrCheckSumAddr,
                "gasPrice": getPrice,
                "gas": "21000",
                "to": UaddrCheckSumAddr,
                "value": addrEth,
                "data": ""
            }, 'asd123!')
            print('모 계좌:     ', Maddr)
            print('받는 계좌:   ', Uaddr)
            print('       |------------------(영수증)-------------------|')
            print('             모 계좌 잔액:     ', web3.fromWei(moAddr, 'ether'))
            print('             보내는 금액:      ', web3.fromWei(addrEth, 'ether'))
            print('                    ++++++++++++++++++++++')
            print('             가스비:           ', web3.fromWei(totalGas, 'ether'))
            print('       |---------------------------------------------|')

            user = SignUptest.objects.get(id = userPK) 
            SendUserEthbal = float(user.ethValue) 
            SendUserEthbal1 = SendUserEthbal - float(ExethValue) 
            user.ethValue = SendUserEthbal 
            user.save()
            now = datetime.now()
            now = now.strftime('%Y-%m-%d %H:%M:%S')
            userethwallSave = EthScan(
                userPK = userPK,
                userAddr = userAddr,
                # submitDate = datetime.now(),
                #status = None,
                blockHash = None,
                blockNumber = None,
                confirmations = None,
                contractAddress = None,
                cumulativeGasUsed = None,
                fromAddr = userAddr,
                gas = None,
                gasPrice = None,
                gasUsed = 21000,
                hash = None,
                input = None,
                isError = None,
                nonce = None,
                timeStamp = now,
                to = toAddr,
                transactionIndex = None,
                txreceipt_status = None,
                volume = volume,
            )
            userethwallSave.save()
            print("-----------------------------------------------------------------")
        context = {'value':'1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print(error)
        context = {'value':'-99'}
        return HttpResponse(json.dumps(context))