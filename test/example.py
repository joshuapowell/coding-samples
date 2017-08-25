import unittest

class TestBasicExample(unittest.TestCase):

    def test_example(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestBasicExample)
    unittest.TextTestRunner(verbosity=2).run(suite)

    unittest.main()
