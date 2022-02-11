import time
from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'gensis_last_hash',
    'hash': 'gensis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'gensis_nonce'
}


class Block:
    """
    Block: a unit of storage.
    Store a transaction in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            f'Block('
            f'timestamp {self.timestamp}, '
            f'last_hash {self.last_hash}, '
            f'hash {self.hash}, '
            f'data {self.data}, '
            f'difficulty {self.difficulty}, '
            f'nonce {self.nonce})'
        )

    @staticmethod
    def mine_block(last_block, data):
        """
        Mines a block based on the given last_block and data, until a block hash
        is found meeting the leading 0's proof of work requirements.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod
    def genesis():
        """
        Generate the genesis block.
        """

        return Block(**GENESIS_DATA)

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        Calculate the adjusted difficulty according to the MINE_RATE.
        Increase the difficulty for quickly mined blocks.
        Decreae the difficulty for slowly mined blocks.
        """

        if new_timestamp - last_block.timestamp < MINE_RATE:
            return last_block.difficulty + 1

        if last_block.difficulty - 1 > 0:
            return last_block.difficulty - 1

        return 1


def main():

    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    block2 = Block.mine_block(block, 'foo2')
    print(genesis_block)
    print(block)
    print(block2)


if __name__ == '__main__':
    main()
