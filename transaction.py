from key import verify_signature
from key import BitcoinAccount


class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float = 0.0, time=0, tx_number=0):
        self.sender: str = sender
        self.receiver: str = receiver
        self.amount: float = amount
        self.timestamp = time
        self.tx_number = tx_number

    def __repr__(self):
        string = "Transaction number: " + str(self.tx_number) + "\n" + \
                 "Sender: " + str(self.sender) + "\n" + \
                 "Receiver: " + str(self.receiver) + "\n" + \
                 "Amount: " + str(self.amount) + "\n" + \
                 "Timestamp: " + str(self.timestamp) + "\n"
        return string

    def to_dict(self):
        tx_dict = {}
        tx_dict["tx_number"] = self.tx_number
        tx_dict["sender"] = self.sender
        tx_dict["receiver"] = self.receiver
        tx_dict["amount"] = self.amount
        tx_dict["timestamp"] = self.timestamp
        return tx_dict
