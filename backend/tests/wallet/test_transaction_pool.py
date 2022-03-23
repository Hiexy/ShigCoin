from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.transaction import Transaction
from backend.wallet.wallet import Wallet

def test_set_transaction():
    transactionPool = TransactionPool()
    transaction = Transaction(Wallet(), 'recipient', 1)
    transactionPool.set_transaction(transaction)

    assert transactionPool.transaction_map[transaction.id] == transaction