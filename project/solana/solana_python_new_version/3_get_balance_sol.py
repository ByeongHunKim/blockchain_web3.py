from solana.rpc.api import Client


client = Client("https://api.devnet.solana.com")

res = client.is_connected()

print("1. 솔라나와 연결여부 :", res)
# True 가 나오면 연결 및 solana.py 설치가 잘 진행된 것이다.

getBalance = client.get_balance("76z2iLit2eyhwfKXH9hRY3S1HNrxsRTQB41FmUumV5rj")

print("2. get_balance 결과 :",getBalance)
# {'jsonrpc': '2.0', 'result': {'context': {'slot': blockNumber를 의미 }, 'value': lamports 단위의 잔액을 의미}, 'id': 1}

lamports = getBalance['result']['value']
print("3. 지갑 잔액의 lamports 값 접근 :",lamports)
# lamports 단위의 잔액만 조회가 가능하다 토큰은 다르게 , json안에 ui_value가 있음

ui_balance = round(lamports*10**(-9),9) # ,5 의 5라는 숫자는 소수점 몇자리 까지 보여줄지 정하는 것. 
print("4. 지갑 잔액의 lamports 값 sol단위로 변환한 값 :",ui_balance)

total_value = float(1 - ui_balance)
print(total_value)



# 1. airdrop 하기 전 완료 후 10초 정도 뒤
# 2. airdrop 진행 후