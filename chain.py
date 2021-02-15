import time
import copy
from block import Block
from transaction import Transaction


class Blockchain:
    def __init__(self):
        self.blocks: Block[] = []
