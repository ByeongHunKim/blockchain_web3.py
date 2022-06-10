from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork, Wallet, AvalancheChain
import json


MY_API_KEY_ID = "csqwJjSS9TYSUQV"
MY_API_SECRET_KEY = "jgzkcUiwZ4L5BCX"

BLOCKCHAIN = Blockchain.SOLANA
NETWORK = BlockchainNetwork.SolanaNetwork.DEVNET

BLOCKCHAIN_API_RESOURCE = BlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY,
    blockchain=BLOCKCHAIN,
    network=NETWORK,
    # avalanche_chain=AVALANCHE_CHAIN
)

# def example():
#     try:
#         assert MY_API_KEY_ID is not None
#         assert MY_API_SECRET_KEY is not None
#     except AssertionError:
#         raise Exception("Fill in your key ID pair!")

#     secret_recovery_phrase = BLOCKCHAIN_API_RESOURCE.generate_seed_phrase()
#     print(secret_recovery_phrase)

#     # You can now initialize `SolanaWallet`, which can be used to create an NFT, transfer SOL, etc.
#     # See the other examples.
#     _ = Wallet(secret_recovery_phrase=secret_recovery_phrase)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    private_key = BLOCKCHAIN_API_RESOURCE.generate_private_key()

    if BLOCKCHAIN.value == Blockchain.SOLANA.value:
        b58_private_key = private_key['b58_private_key']
        print("This is a base58-encoded private key. This is what Phantom shows when you click `Show Private Key`")
        print(b58_private_key)

        print("-" * 20)

        private_key = private_key['private_key']
        print("This is a standard private key array. This is what SolFlare shows when you click `Export Private Key`")
        print(private_key)

        # You can now initialize `Wallet`, which can be used to create an NFT, transfer SOL, etc.
        # See the other examples.
        _ = Wallet(b58_private_key=b58_private_key)
        _ = Wallet(private_key=private_key)

    else:
        hex_private_key = private_key['hex_private_key']
        print("This is a standard private key. You can import this into Metamask.")
        print(hex_private_key)

        # You can now initialize `Wallet`, which can be used to create an NFT, transfer SOL, etc.
        # See the other examples.
        _ = Wallet(hex_private_key=hex_private_key)



if __name__ == '__main__':
    example()