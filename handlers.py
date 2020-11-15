from blockchain import BlockChain
import time
import json


blockchain = BlockChain()

def new_transaction(author, content):
    print("new tx")
    tx_data = {}
    tx_data["author"] = author
    tx_data["content"] = content
    tx_data["timestamp"] = time.time()
    blockchain.add_new_transaction(tx_data)


def get_chain():
    print("get chain")

    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data}, indent=4)

def mine_unconfirmed_txs():
    print("mine")