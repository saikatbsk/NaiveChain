from Crypto.PublicKey import RSA

GENESIS_INDEX = 0
GENESIS_PREVIOUS_HASH = '0'
GENESIS_TIMESTAMP = 1495851743
GENESIS_DATA = 'genesis block'

class BlockParams():
    def __init__(self, index, previous_hash, timestamp, data, public_key):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = self.encrypt_data(data, public_key)

    def __str_(self):
        return str(self.index) + self.previous_hash + str(self.timestamp) + self.data

    @classmethod
    def genesis_params(cls):
        return cls(GENESIS_INDEX, GENESIS_PREVIOUS_HASH, GENESIS_TIMESTAMP, GENESIS_DATA)

    def encrypt_data(self, data, public_key):
        key = RSA.importKey(public_key)
        return key.encrypt(data, 32)
