#!/usr/bin/env python


import unittest


from top_down import product_1_to_n_oneline
from top_down import product_1_to_n_multiline


class TestTopDown(unittest.TestCase):

    def test_product_1_to_n_oneline(self):
        n = 4

        return_value = product_1_to_n_oneline(n)

        self.assertEqual(return_value, 24)

    def test_product_1_to_n_multiline(self):
        n = 4

        return_value = product_1_to_n_multiline(n)

        self.assertEqual(return_value, 24)


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestTopDown)
    unittest.TextTestRunner(verbosity=2).run(suite)

    unittest.main()
