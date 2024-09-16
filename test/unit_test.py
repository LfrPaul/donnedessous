import unittest
from donnedessouslampe.donne import donne_des_sous


class MyTestCase(unittest.TestCase):
    def test_something(self):
        compte_en_banque = donne_des_sous(8, 11)
        self.assertEqual(19, compte_en_banque)  # add assertion here

    def test_something1(self):
        compte_en_banque = donne_des_sous(12, 10)
        self.assertEqual(24, compte_en_banque)  # add assertion here


if __name__ == '__main__':
    unittest.main()
