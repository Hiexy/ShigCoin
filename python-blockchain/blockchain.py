from block import Block


class Blockchain:
    """
    Blockchain: a public ledger of public transactions.
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain {self.chain}'


def main():
    blockchian = Blockchain()
    blockchian.add_block('one')
    blockchian.add_block('two')

    print(blockchian)


if __name__ == '__main__':
    main()
