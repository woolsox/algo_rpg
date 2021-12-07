import json
import base64
import hashlib
from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn

def nft_txn(private_key, my_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    hash = hashlib.new("sha512_256")
    hash.update(b"arc0003/amj")
    hash.update("this is metadata".encode("utf-8"))
    json_metadata_hash = hash.digest()

    print("My address: {}".format(my_address))
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))

    params = algod_client.suggested_params()
    txn = AssetConfigTxn(sender="M5Z53RXBTEWQX7VW475J4SPITVDEERX2QLSEGOTQEHNGHETZ7AWQD6XCUY",
                         sp=params,
                         total=1,
                         default_frozen=False,
                         unit_name="woolsox",
                         asset_name="woolsox-char-sheet@arc3",
                         manager=None,
                         reserve=None,
                         freeze=None,
                         clawback=None,
                         strict_empty_address_check=False,
                         url="https://algo_rpg/stats.json",
                         metadata_hash=json_metadata_hash,
                         decimals=0)

    # sign transaction
    signed_txn = txn.sign(private_key)

    # submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Signed transaction with txID: {}".format(txid))

nft_txn("kKt/jyUYl8xmiHnn/PGuk8PNHuCfv32QDROItI70w+xnc93G4ZktC/625/qeSeidRkJG+oLkQzpwIdpjknn4LQ==", "M5Z53RXBTEWQX7VW475J4SPITVDEERX2QLSEGOTQEHNGHETZ7AWQD6XCUY")
