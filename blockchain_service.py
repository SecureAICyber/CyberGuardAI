class BlockchainService:
    def __init__(self):
        self.chain = []

    def add_transaction(self, transaction):
        self.chain.append(transaction)

    def get_chain(self):
        return self.chain
