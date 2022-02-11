import time

from numpy import average
from backend.blockchain.blockchain import Blockchain
from backend.config import MINE_RATE, SECONDS

blockchain = Blockchain()

times = []

for i in range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    mine_time = (end_time - start_time) / SECONDS
    times.append(mine_time)

    average_time = sum(times) / len(times)

    print(f'New block difficutly: {blockchain.chain[-1].difficulty}')
    print(f'Time to mine new block: {mine_time}s')
    print(f'Average time to add blocks: {average_time}s\n')