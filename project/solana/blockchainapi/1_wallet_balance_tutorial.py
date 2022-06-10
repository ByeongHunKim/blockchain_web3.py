from theblockchainapi import SolanaAPIResource, SolanaMintAddresses, SolanaNetwork, SolanaWallet

MY_API_KEY_ID = "csqwJjSS9TYSUQV"
MY_API_SECRET_KEY = "jgzkcUiwZ4L5BCX"

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)

secret_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
print(secret_phrase)
wallet = SolanaWallet(secret_recovery_phrase=secret_phrase)
public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
print(public_key)
airdrop_tx_signature = BLOCKCHAIN_API_RESOURCE.get_airdrop(public_key)
print(airdrop_tx_signature)
result = BLOCKCHAIN_API_RESOURCE.get_balance(public_key)
print(f"SOL Balance of {public_key}")
print(result)



# (2) Test get USDC balance (or any other SPL token)
# This is the public key of a wallet on Solana: GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ
# We know this public key has some amount of USDC in it already
# public_key = 'AsDHpXLGxHeHNWxpqEZHoMC2LpWjJznfWrm8nTz9FvDn'
# mintAddr = '3oMguQN22MkB8n7BMbsRFqEeJceR8vd2FmuZLiCBcNig'
# result = BLOCKCHAIN_API_RESOURCE.get_balance(
#     public_key=public_key,
#     mint_address=mintAddr  # or replace your own mint address
# )
# print("-" * 20)
# print(f"USDC Balance of {public_key}")
# print(result)


# from theblockchainapi import TheBlockchainAPIResource

# RESOURCE = TheBlockchainAPIResource(
#     api_key_id="csqwJjSS9TYSUQV",
#     api_secret_key="jgzkcUiwZ4L5BCX"
# )

# if __name__ == '__main__':
#     result = RESOURCE.get_balance(
#         public_key = 'G8Wq2zGqJYw7T4RpurJcdfHdyEnrbSvBBgdXPCNP5cQi'
#     )

#     print(result)