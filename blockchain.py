
import hashlib
import json
from datetime import datetime


class Blockchain:
    def __init__(self):
    
        self.chain = []
        self.create_block("Genesis Block", "0")

    def create_block(self, data, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": datetime.now().isoformat(),
            "data": data,
            "previous_hash": previous_hash,
        }

        block["hash"] = self.hash_block(block)
        self.chain.append(block)
        return block

    def hash_block(self, block):
        block_data = json.dumps(
            block, sort_keys=True
        ).encode()

        return hashlib.sha256(block_data).hexdigest()

    def get_chain(self):
        return self.chain


if __name__ == "__main__":
    joy_bangla = Blockchain()

    joy_bangla.create_block(
        "My first Joy Bangla Blockchain block",
        joy_bangla.get_chain()[-1]["hash"],
    )

    print(json.dumps(
        joy_bangla.get_chain(),
        indent=4
    ))
