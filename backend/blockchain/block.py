import time
from backend.util.crypto_hash import crypto_hash


class Block:
    """
    Block: a unit of storage.
    Store a transaction in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            f'Block('
            f'timestamp {self.timestamp}, '
            f'last_hash {self.last_hash}, '
            f'hash {self.hash}, '
            f'data {self.data})'
        )

    @staticmethod
    def mine_block(last_block, data):
        """
        Mines a block based on the given last_block and data.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, data)

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        """
        Generate the genesis block.
        """

        return Block(1, 'gensis_last_hash', 'gensis_hash', [])


def main():

    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    block2 = Block.mine_block(block, 'foo2')
    print(genesis_block)
    print(block)
    print(block2)


if __name__ == '__main__':
    main()
