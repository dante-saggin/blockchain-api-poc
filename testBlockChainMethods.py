import unittest
import blockchain


class TestBlockChainMethods(unittest.TestCase):
    chain = blockchain.Blockchain()

    def test_newBlock(self):
        block = self.chain.new_block(100, 123)
        self.assertEqual(block["proof"], 100)
        self.assertEqual(block["previous_hash"], 123)

    def test_validate_prof(self):
        self.assertTrue(self.chain.valid_proof(1, 72608))
        self.assertFalse(self.chain.valid_proof(1, 2))

    def test_proof_of_work(self):
        self.assertEqual(self.chain.proof_of_work(1), 72608)
        self.assertEqual(self.chain.proof_of_work(2), 69926)
        self.assertNotEquals(self.chain.proof_of_work(2), 3)


if __name__ == '__main__':
    unittest.main()
