from theblockchainapi import SolanaAPIResource, \
    SolanaNetwork, SolanaCurrencyUnit, SolanaWallet

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = "csqwJjSS9TYSUQV"
MY_API_SECRET_KEY = "jgzkcUiwZ4L5BCX"

# MY_API_KEY_ID = "KaOKJER4wNwkYkK"
# MY_API_SECRET_KEY = "sMhw2pDhLd9s8Ec"

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    network = SolanaNetwork.DEVNET

    # Create a new wallet
    wallet = SolanaWallet(
        # (1) SUPPLY Seed phrase
        # secret_recovery_phrase=BLOCKCHAIN_API_RESOURCE.generate_secret_key(),
        # derivation_path=DerivationPath.CLI_PATH,
        # passphrase=str(),
        # (2) OR You can supply this instead. e.g, [11, 234, ... 99, 24]
        # private_key=None,
        # (3) OR You can supply this instead. e.g, x12x0120jd ... 192j0eds
        # b58_private_key=BLOCKCHAIN_API_RESOURCE.generate_private_key()['b58_private_key']
        # (4) 내 b_58_private_key 입력
        # b58_private_key= "621yVKGcYBMudqUT9AkHpAohXjunWAWMtXz1NyCjK4wa5NCW886kD5z9AL8wRyjxpqB7LwYPMEaw8444da3roMRu"
        # (5) token owner 의 priv key
        b58_private_key= "2K7T6AxYU2aEBVRWdcgUyb5YTSa7fUvr5Nxb1TMVpXArp7YhkxxcoGvqhcZK8ZJLNKaJQAZPqvuzNCenGvoCksMr"
    )

    # public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
    public_key = "AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn"
    print(f"1. 공개키 지갑주소 : {public_key}")

    # for _ in range(3):
    #     # Get an airdrop of 0.045 (0.015 * 3) to be able to pay for the creation of the candy machine
    #     BLOCKCHAIN_API_RESOURCE.get_airdrop(recipient_address=public_key)

    pubInfo = BLOCKCHAIN_API_RESOURCE.get_balance(public_key, SolanaCurrencyUnit.SOL, SolanaNetwork.DEVNET)

    print(f"2. 공개키 지갑의 정보 : {pubInfo}")

    # new_nft = BLOCKCHAIN_API_RESOURCE.create_nft(
    #     wallet=wallet,
    #     network=network,
    #     name="YGBS Coin",
    #     symbol="YGBS"
    # )
    # print(f"3. new_nft, `{new_nft}`.")
    # mint_address = new_nft['mint']

    mint_address = "3oMguQN22MkB8n7BMbsRFqEeJceR8vd2FmuZLiCBcNig"

    print(f"3. token 민트 주소, `{mint_address}`.")

    # nft_owner = BLOCKCHAIN_API_RESOURCE.get_nft_owner(mint_address, network) AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn
    nft_owner = "AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn"
    print(f"4. NFT Owner 주소 : {nft_owner}")

    nft_price = 6900  # lamports

    listing_tx = BLOCKCHAIN_API_RESOURCE.list_token(
        token_address=mint_address,
        wallet=wallet,
        network=network,
        token_price=nft_price
    )
    print(f"5. nft 생성 tx : `{listing_tx}`.")

    # nft_owner = BLOCKCHAIN_API_RESOURCE.get_nft_owner(mint_address, network)
    # print(f"6. nft 소유자: {nft_owner}")

    # Create a second wallet to purchase the NFT BLOCKCHAIN_API_RESOURCE.generate_private_key()['b58_private_key']
    second_wallet = SolanaWallet(
        b58_private_key= "2njiVCQv7kjLVKP5g5xSCJfJbRcDgNU5uQJML8jVJP5DLtjb8EF36KQgk378AwUewd4aNWDaccHBwMHgT8G2zDq3"
    )

    second_public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=second_wallet)
    print(f"7. 생성한 nft 보낼 주소 : {second_public_key}")

    # # BLOCKCHAIN_API_RESOURCE.get_airdrop(recipient_address=second_public_key)

    buying_tx = BLOCKCHAIN_API_RESOURCE.buy_token(
        mint_address=mint_address,
        wallet=second_wallet,
        network=network,
        token_price=nft_price
    )
    print(f"8. nft 전송 tx: `{buying_tx}`.")

    # nft_owner = BLOCKCHAIN_API_RESOURCE.get_nft_owner(mint_address, network)
    # print(f"9. 발행한 nft를 두번째 지갑이 구매를 했기 때문에 이제 소유자는 두번째 지갑: {nft_owner}")


if __name__ == '__main__':
    example()