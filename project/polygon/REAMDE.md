[https://ethereum.stackexchange.com/questions/70240/how-to-send-transaction-with-web3-py](https://ethereum.stackexchange.com/questions/70240/how-to-send-transaction-with-web3-py)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2e05adc5-3077-4230-843c-c1fb92276472/Untitled.png)

## 1. 테스트 matic 받기

```jsx
https://faucet.polygon.technology/
```

이곳에서 생성된 지갑주소를 입력하니까 0.2 matic 을 tx없이 그냥 지갑으로 꽃아준다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3868d028-6bd2-486b-a453-68ac764752cd/Untitled.png)

```jsx
0xab3a34C0039560184493e5eB852aad4213E62e8D : 첫번째 생성한 지감 

0xf1337471403D2D7E7a83166c5E48dd619ecc95c3 : 두번째 생성한 지갑 

```

## 2. getBalance, fromWei

- 문제는 fromWei 쓸 때 ‘ether’ 로 해야 0.2가 나온다.
    - ‘matic’을 해보니까 되지 않는다.
- 그냥 getBalance 할 때는 wei 단위로 나온다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a21dc2e3-ac75-46d0-95f5-9eded97818f5/Untitled.png)

## 첫번째 지갑에서 두번째 지갑으로 0.1 Matic 쏴보기

```jsx
(base) bstudent@DESKTOP-GPR5QBN:~/geth_project/geth_practice$ python3 1_isConnected.py 
1. 폴리곤 연결여부: True
addr:  0x37bbcF3F45fb6357E868175B22a262aE80FB7062
addr:  <eth_account.signers.local.LocalAccount object at 0x7f5bf56c5550>
(base) bstudent@DESKTOP-GPR5QBN:~/geth_project/geth_practice$ python3 1_isConnected.py 
1. 폴리곤 연결여부: True
addr:  0x064Ef1C8E707481dAf28366ee7250Dd7F1c7b5B3
Traceback (most recent call last):
  File "/home/bstudent/geth_project/geth_practice/1_isConnected.py", line 22, in <module>
    print('addr: ', acct.privKey)
AttributeError: 'LocalAccount' object has no attribute 'privKey'
(base) bstudent@DESKTOP-GPR5QBN:~/geth_project/geth_practice$ python3 1_isConnected.py 
1. 폴리곤 연결여부: True
addr:  0xd92386e0A1d45bcF117308d1Ad284bDC110D627F
addr:  b'\xd3\xf5\x07p:h\xcd\xca|\xaeb\xdaT\xdb.\xb6o\xf4_\xac$\xf1\r\x03K\xd0\xd1\xcb\xaa\xff\x1c\xf2'
(base) bstudent@DESKTOP-GPR5QBN:~/geth_project/geth_practice$ python3 2_sendMatic.py 
1. web3 - 연결여부 : True
2. checkSum - 확인여부 : 0xd92386e0A1d45bcF117308d1Ad284bDC110D627F
3. 가스비 - 확인여부 : 1308016699
4. 잔액 - 확인여부 : 200000000000000000
4. 논스 - 확인여부 : 0
5. 보내는금액 - 확인여부 : 100000000000000000
```

```jsx
b'\xd3\xf5\x07p:h\xcd\xca|\xaeb\xdaT\xdb.\xb6o\xf4_\xac$\xf1\r\x03K\xd0\xd1\xcb\xaa\xff\x1c\xf2' 이 걸 변환해야한다.
```

```jsx
(base) bstudent@DESKTOP-GPR5QBN:~/geth_project/geth_practice$ python3 1_isConnected.py 
1. 폴리곤 연결여부: True
publickey:  0x50A2bCA8Fb0634be5BF926659c72A33B417bB979
privkey:  b'cwu\xc3>\xec\xb170\x8e\x80\x0cG\x8co\xe1\x18\xba4\x88\x17\x0f\xc5\xdf\xca\x01Z\x9fh\x19\xd1\xf8'
privkey:  b'cwu\xc3>\xec\xb170\x8e\x80\x0cG\x8co\xe1\x18\xba4\x88\x17\x0f\xc5\xdf\xca\x01Z\x9fh\x19\xd1\xf8'
realPrivKey:  Y3d1wz7ssTcwjoAMR4xv4Ri6NIgXD8XfygFan2gZ0fhjd3XDPuyxNzCOgAxHjG/hGLo0iBcPxd/KAVqfaBnR+A==
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/76900e3b-bfe9-413c-9141-cb3baeba3cf5/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/03be69a6-b9f9-4449-80be-d2ca5a7dd02b/Untitled.png)

```jsx
https://community.infura.io/t/polygon-rpc-only-replay-protected-eip-155-transactions-allowed-over-rpc/2997/3

이곳 참고하여 chainID 추가
```

# 문제는 메타마스크에서 생성된 것은 사용가능한데, 폴리곤은 ?

- geth.personal로 생성된 계좌가 메타마스크연동은 되니까 [web3Views.py](http://web3Views.py) 같은곳에서 HTTPProvider로 폴리곤 연결하고  tx조회할 때는 폴리곤조회하는거임
- 보내줄때는 똑같이 asd123!으로 진행하고

# 시도해볼것

- 지금 로컬에 rinkeby 운영하잖아 그러면 생성된 공개키 지갑주소를 DB에 저장할 수는 없으니까 따로 저장해두고, 다른 [web3Views.py](http://web3Views.py) 파일에서 HTTPProvider로 폴리곤 연결하고
- 폴리곤 전송 시도해볼때, 애초에 geth.personal로 서명해서 보내니까 sign, rawTransaction 할 필요 없어보임
- 만약에 이렇게 가능하면? 굳!

# 내일 마이크 오면 녹화하면서 시도