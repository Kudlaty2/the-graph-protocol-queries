import json
from datetime import datetime
from Crypto.Hash import SHA256


class Block(object):
    """The block for the blockchain"""

    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash


class Blockchain(object):
    """List of blocks"""

    def __init__(self):
        self._chain = [self.get_genesis_block()]
        self.timestamp = int(datetime.now().timestamp())


    def get_genesis_block(self):
        """First block"""

        return Block(0, '0', 1465154705, "my genesis block!!",
                     "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7"
                     )


    def calculate_hash(self, index, previous_hash, timestamp, data):
        """calculates SHA256 hash value"""

        hash_object = SHA256.new(data=(str(index) + previous_hash +
                                       str(timestamp) + data).encode())
        return hash_object.hexdigest()


    def get_latest_block(self):
        """gets the last block from blockchain"""
        try:
            return self._chain[-1]
        except IndexError as e:
            return None


    def create_block(self, block_data):
        """creates a new block with the given block data"""
        previous_block = self.get_latest_block()
        next_index = previous_block.index + 1
        next_timestamp = self.timestamp
        next_hash = self.calculate_hash(next_index, previous_block.hash, next_timestamp,
                                        block_data)
        return Block(next_index, previous_block.hash, next_timestamp, block_data, next_hash)

    def add_block(self, data):
        """"appends a new block to the blockchain"""
        self._chain.append(self.create_block(data))

    @property
    def chain(self):
        """created a dict containing list of block objects to view"""
        return self.dict(self._chain)

    def dict(self, chain):
        """converts list of blok objects to dictionary"""
        return json.loads(json.dumps(chain, default=lambda o:
                                     o.__dict__))

    def reset(self):
        """resets the blockchain blocks expect genesis block"""
        self._chain = [self._chain[0]]

