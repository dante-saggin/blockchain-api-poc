import unittest
import blockchain


class TestBlockChainMethods(unittest.TestCase):
    chain = blockchain.Blockchain()

    def test_newBlock(self):
        block = self.chain.new_block(100, 123)
        self.assertEqual(block["proof"], 100)
        self.assertEqual(block["previous_hash"], 123)


if __name__ == '__main__':
    unittest.main()
