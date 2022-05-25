# solana[solana.py] 
# ethereum [web3.py] 
# Development environment setting

## 선택지 1
- 로컬환경
    - 선택지 2 에 있는 곳에서 로컬환경에 맞게 설치를 진행하면 된다.
    - aws서버는 SSH-FS로 폴더를 모두 볼 수 있는데, 현재 로컬에서는 aws처럼 설치는 가능했지만, `code .` 명령어가 작동을 하지 않아서 파일을 볼 수 없어 로컬에 비슷하게 설정하였다.
    - wsl2를 키기만하면 `(base)` 가 나오길래 `pip install solana` 로 `solana.py` 설치 후 다른 폴더에서도 작동이 가능한 줄 알았는데, 에러가 발생했다. 
    - 테스트는 `django-admin startproject mysite .` -> `python manage.py startapp <appName>` 로 설정한 환경에서만 가능한 상황이다.
## 선택지 2
- aws 서버
    - https://velog.io/@hunsm4n/anaconda-%EC%84%9C%EB%B2%84%EC%84%B8%ED%8C%85


## 1,2 로 설치가 완료 후 
## 솔라나는 solana.py 설치

- pip install solana

## 이더리움은 web3.py 설치 

- pip install web3


## 솔라나와 이더리움 python 환경 실습 차이점

- 솔라나는 public api ("https://api.devnet.solana.com") or ("https://api.mainnet-beta.solana.com") 를 사용한다.
- 하지만 위 api들은 프로덕션용이 아니기 때문에 실제 서비스 운영에 사용되기에는 적합하지 않다. 개인 또는 사설 rpc를 사용해야한다.
- https://docs.solana.com/cluster/rpc-endpoints 이곳에서 제공되는 api들의 Limits를 확인할 수 있다.

- 이더리움은 geth를 직접 운영 할 수 있다.
- geth 설치후 geth.eth.personal.newAccount("password")를 하면 geth안에 있는 keystore 파일안에 UTC파일이 생기는데, 이것이 privKey이다. 
- https://eun97.tistory.com/entry/%EC%9D%B4%EB%8D%94%EB%A6%AC%EC%9B%80-keystore-PrivateKey-%EB%B3%80%ED%99%98-Node
- 위의 링크에서 확인할 수 있듯이 UTC파일을 convert할 수 있다. 하지만 geth.eth.personal.newAccount("password") 로 생성할 때 입력한 'password' ex) 'asd123!' 으로 tx서명을 privKey대신할 수 있다.
- 그래서 현재까지는 UTC파일을 굳이 privKey로 convert할 이유는 없는 것 같다.
- 하지만 솔라나는 pub,privkey를 둘다 생성해내기 때문에 DB에 직접 insert해줬는데, privKey를 대신 관리해주는 느낌이기 때문에 해시화를 시켜서 좀 직접적으로 값을 드러내지 않게 보안을 좀 더 강화해야하는 노력이 필요하다.