<div align=center><h1>π STACKS</h1></div>

<div align=center>
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
<img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
<br>
<img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> 
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"> 
<img src="https://img.shields.io/badge/ubuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black"> 
</div>

# solana[solana.py] ethereum [web3.py] 
# Development environment setting
`https://bamtory29.tistory.com/entry/GitGithub-%EC%9B%90%EA%B2%A9-%EC%A0%80%EC%9E%A5%EC%86%8C%EC%9D%98-%ED%8C%8C%EC%9D%BC%EC%9D%84-%EC%A7%80%EC%9A%B0%EA%B8%B0`
- git rm --cached -r ν΄λ/νμΌλͺ


## μ νμ§ 1
- λ‘μ»¬νκ²½
    - μ νμ§ 2 μ μλ κ³³μμ λ‘μ»¬νκ²½μ λ§κ² μ€μΉλ₯Ό μ§ννλ©΄ λλ€.
    - awsμλ²λ SSH-FSλ‘ ν΄λλ₯Ό λͺ¨λ λ³Ό μ μλλ°, νμ¬ λ‘μ»¬μμλ awsμ²λΌ μ€μΉλ κ°λ₯νμ§λ§, `code .` λͺλ Ήμ΄κ° μλμ νμ§ μμμ νμΌμ λ³Ό μ μμ΄ λ‘μ»¬μ λΉμ·νκ² μ€μ νμλ€.
    - wsl2λ₯Ό ν€κΈ°λ§νλ©΄ `(base)` κ° λμ€κΈΈλ `pip install solana` λ‘ `solana.py` μ€μΉ ν λ€λ₯Έ ν΄λμμλ μλμ΄ κ°λ₯ν μ€ μμλλ°, μλ¬κ° λ°μνλ€. 
    - νμ€νΈλ `django-admin startproject mysite .` -> `python manage.py startapp <appName>` λ‘ μ€μ ν νκ²½μμλ§ κ°λ₯ν μν©μ΄λ€.
## μ νμ§ 2
- aws μλ²
    - https://velog.io/@hunsm4n/anaconda-%EC%84%9C%EB%B2%84%EC%84%B8%ED%8C%85


## 1,2 λ‘ μ€μΉκ° μλ£ ν 
## μλΌλλ solana.py μ€μΉ

- pip install solana

## μ΄λλ¦¬μμ web3.py μ€μΉ 

- pip install web3


## μλΌλμ μ΄λλ¦¬μ python νκ²½ μ€μ΅ μ°¨μ΄μ 

- μλΌλλ public api ("https://api.devnet.solana.com") or ("https://api.mainnet-beta.solana.com") λ₯Ό μ¬μ©νλ€.
- νμ§λ§ μ apiλ€μ νλ‘λμμ©μ΄ μλκΈ° λλ¬Έμ μ€μ  μλΉμ€ μ΄μμ μ¬μ©λκΈ°μλ μ ν©νμ§ μλ€. κ°μΈ λλ μ¬μ€ rpcλ₯Ό μ¬μ©ν΄μΌνλ€.
- https://docs.solana.com/cluster/rpc-endpoints μ΄κ³³μμ μ κ³΅λλ apiλ€μ Limitsλ₯Ό νμΈν  μ μλ€.

- μ΄λλ¦¬μμ gethλ₯Ό μ§μ  μ΄μ ν  μ μλ€.
- geth μ€μΉν geth.eth.personal.newAccount("password")λ₯Ό νλ©΄ gethμμ μλ keystore νμΌμμ UTCνμΌμ΄ μκΈ°λλ°, μ΄κ²μ΄ privKeyμ΄λ€. 
- https://eun97.tistory.com/entry/%EC%9D%B4%EB%8D%94%EB%A6%AC%EC%9B%80-keystore-PrivateKey-%EB%B3%80%ED%99%98-Node
- μμ λ§ν¬μμ νμΈν  μ μλ―μ΄ UTCνμΌμ convertν  μ μλ€. νμ§λ§ geth.eth.personal.newAccount("password") λ‘ μμ±ν  λ μλ ₯ν 'password' ex) 'asd123!' μΌλ‘ txμλͺμ privKeyλμ ν  μ μλ€.
- κ·Έλμ νμ¬κΉμ§λ UTCνμΌμ κ΅³μ΄ privKeyλ‘ convertν  μ΄μ λ μλ κ² κ°λ€.
- νμ§λ§ μλΌλλ pub,privkeyλ₯Ό λλ€ μμ±ν΄λ΄κΈ° λλ¬Έμ DBμ μ§μ  insertν΄μ€¬λλ°, privKeyλ₯Ό λμ  κ΄λ¦¬ν΄μ£Όλ λλμ΄κΈ° λλ¬Έμ ν΄μνλ₯Ό μμΌμ μ’ μ§μ μ μΌλ‘ κ°μ λλ¬λ΄μ§ μκ² λ³΄μμ μ’ λ κ°νν΄μΌνλ λΈλ ₯μ΄ νμνλ€.