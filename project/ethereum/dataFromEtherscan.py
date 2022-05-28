# 우리만의 장부 표면적으로 보여줄 ui처리
@csrf_exempt
def EthScanList(request):
    try:
        blockHash = request.POST.get('blockHash')
        blockNumber = request.POST.get('blockNumber')
        confirmations = request.POST.get('confirmations')
        contractAddress = request.POST.get('contractAddress')
        cumulativeGasUsed = request.POST.get('cumulativeGasUsed')
        fromAddr = request.POST.get('fromAddr')
        gas = request.POST.get('gas')
        gasPrice = request.POST.get('gasPrice')
        gasUsed = request.POST.get('gasUsed')
        hash = request.POST.get('hash')  # txnhash 
        input = request.POST.get('input')
        isError = request.POST.get('isError')
        nonce = request.POST.get('nonce')
        to = request.POST.get('to')
        transactionIndex = request.POST.get('transactionIndex')
        txreceipt_status = request.POST.get('txreceipt_status')
        volume = request.POST.get('volume')
        
        mAddr = ""
    
        blockCount = EthScan.objects.filter(blockNumber = blockNumber).count()
        if blockCount == 0:
            userinfo = SignUptest.objects.get(id = 1)
            userEthAddr = userinfo.ethAddr
            intEth = float(userinfo.ethValue)
            print('intEth: ', intEth)
            print('userEthAddr: ', userEthAddr)
            print('fromAddr: ', fromAddr)
            print('to: ', to)
            if userEthAddr.lower() == to.lower() :
                print('입금')
                intEth += float(volume)
                print('float(volume): ', float(volume))
            userinfo.ethValue = intEth
            userinfo.save()
            test = EthScan(
                userPK = '1',
                # userAddr = userAddr,
                blockHash = blockHash,
                blockNumber = blockNumber,
                confirmations = confirmations,
                contractAddress = contractAddress,
                cumulativeGasUsed = cumulativeGasUsed,
                fromAddr = fromAddr,
                gas = gas,
                gasPrice = gasPrice,
                gasUsed = gasUsed,
                hash = hash,
                input = input,
                isError = isError,
                nonce = nonce,
                # timeStamp = timeStamp,
                to = to,
                transactionIndex = transactionIndex,
                txreceipt_status = txreceipt_status,
                volume = volume
            )
        else :
            print("xxxx")
        test.save()
        context = {'value' : '1'}
        return HttpResponse(json.dump(context))
    except Exception as error:
        print('error')
        context = {'value' : '-99'}
        return HttpResponse(json.dumps(context))


# front 또는 서버에서 수동으로 보내줄 이더스캔 api 코드
# address, apikey, url 은 직접 값을 넣어줘야한다. 
# python manage.py ruserver 0.0.0.0:7272 로 서버를 열어주고 개발자 도구에서 아래의 ajax를 날려주면 위의 코드가 catch하여 DB안에 insert해준다. 

$.ajax({
    url: "https://api-rinkeby.etherscan.io/api",
    type: "GET",
    data: {
      module: "account",
      action: "txlist",
      address: '',
      startblock: 0,
      endblock: 999999999,
      page: 1,
      offset: 10,
      sort: "asc",
      apikey: "",
    },
    dataType: "json",
    async: true,
    success: function (result) {
      var data = result.result;
      var html = "";
      console.log("data: ", data);
      if (data.length == 0) {
      } else {
        for (i = 0; i < data.length; i++) {
          var blockHash = data[i]["blockHash"];
          var block = data[i]["blockNumber"];
          var confirmations = data[i]["confirmations"];
          var contractAddress = data[i]["contractAddress"];
          var cumulativeGasUsed = data[i]["cumulativeGasUsed"];
          var from = data[i]["from"];
          var gas = data[i]["gas"];
          var gasPrice = data[i]["gasPrice"];
          var gasUsed = data[i]["gasUsed"];
          var hash = data[i]["hash"];
          var input = data[i]["input"];
          var isError = data[i]["isError"];
          var nonce = data[i]["nonce"];
          var to = data[i]["to"];
          var transactionIndex = data[i]["transactionIndex"];
          var txreceipt_status = data[i]["txreceipt_status"];
          var volume = data[i]["value"];
              $.ajax({
                url: "" + "",
                type: "POST",
                data: {
                  blockHash: blockHash,
                  blockNumber: block,
                  confirmations: confirmations,
                  contractAddress: contractAddress,
                  cumulativeGasUsed: cumulativeGasUsed,
                  fromAddr: from,
                  gas: gas,
                  gasPrice: gasPrice,
                  gasUsed: gasUsed,
                  hash: hash,
                  input: input,
                  isError: isError,
                  nonce: nonce,
                  to: to,
                  transactionIndex: transactionIndex,
                  txreceipt_status: txreceipt_status,
                  volume: (volume / 1000000000000000000).toFixed(3),
                },
                dataType: "json",
                async: true,
                success: function (result) {},
                error: function (error) {
                  console.log(error);
                },
              });
            }
      }
    },
    error: function (error) {
      $("#loading1").hide();
      console.log(error);
    },
  });