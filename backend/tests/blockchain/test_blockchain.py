from numpy import block
from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA


def test_blockchain_instance():
    blockchain = Blockchain()

    assert isinstance(blockchain, Blockchain)
    
    genesis = blockchain.chain[0]
    for key, value in GENESIS_DATA.items():
        assert getattr(genesis, key) ==  value


def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data