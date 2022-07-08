import json
from block_structure import *

simple_chain = Blockchain()
simple_chain.add_block(data="Not to touch the earth")
simple_chain.add_block(data="Not to see the sun")
simple_chain.add_block(data='Nothing left to do, but')
simple_chain.add_block(data='Run, run, run')

print(json.dumps(simple_chain.chain))
simple_chain.reset()