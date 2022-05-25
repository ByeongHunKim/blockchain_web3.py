# solana[solana.py] 그리고 ethereum [web3.py] 를 사용하기 위한 개발환경 세팅

## 선택지 1
- 로컬환경
    - 선택지 2 에 있는 곳에서 로컬환경에 맞게 설치를 진행하면 된다.
    - aws서버는 SSH-FS로 폴더를 모두 볼 수 있는데, 현재 로컬에서는 aws처럼 설치는 가능했지만, `code .` 명령어가 작동을 하지 않아서 파일을 볼 수 없어 로컬에 비슷하게 설정하였다.
    - wsl2를 키기만하면 `(base)` 가 나오길래 `pip install solana` 로 `solana.py` 설치 후 다른 폴더에서도 작동이 가능한 줄 알았는데, 에러가 발생했다. 
    - 테스트는 `django-admin startproject mysite .` -> `python manage.py startapp <appName>` 로 설정한 환경에서만 가능한 상황이다.
## 선택지 2
- aws 서버
    - https://velog.io/@hunsm4n/anaconda-%EC%84%9C%EB%B2%84%EC%84%B8%ED%8C%85


