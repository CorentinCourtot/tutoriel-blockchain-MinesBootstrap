import hashlib
import time
from transaction import Transaction
from key import verify_signature


class Block:
    def __init__(self, index: int = 0, lasthash: str = "", timestamp=0, minerName: str = ""):
        self.transactions: list[Transaction] = []
        self.index = index
        self.hashval = ""
        self.lasthash = lasthash
        self.timestamp = timestamp
        self.nonce = 0
        self.minerName = ""

    def __repr__(self):
        string = "Block number: " + str(self.index) + "\n" + \
                 "hash val: " + str(self.hashval) + "\n" + \
                 "last hash: " + str(self.lasthash) + "\n" + \
                 "Nonce: " + str(self.nonce) + "\n" + \
                 "Timestamp: " + str(self.timestamp) + "\n" \
                 "Miner name: " + self.minerName + "\n"
        return string

    def add_transaction(self, t: Transaction):
        self.transactions.append(t)

    def hash(self):  #
        string = str(self.index) + str(self.timestamp) + \
            str(self.nonce) + str(self.lasthash)
        for transaction in self.transactions:
            string += str(transaction.sender) + \
                str(transaction.receiver) + str(transaction.amount)

        return hashlib.sha256(string.encode('utf-8')).hexdigest()

    def check_hash(self, difficulty: int = 0, hash: str = "") -> bool:
        return hash.startswith("0" * difficulty)

    def verify(self) -> bool:
        return self.hash() == self.hashval

    def mine(self, difficulty: int = 0):
        self.timestamp = time.time()
        self.minerName = "Corentin C"

        while not(self.hash().startswith("0" * difficulty)):
            self.nonce += 1

        self.hashval = self.hash()
