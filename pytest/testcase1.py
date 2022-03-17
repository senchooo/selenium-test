import unittest


class Test(unittest.TestCase):
    def setup(self):
        print('setup')

    def test_first(self):
        print('This is my first test case')
        assert True

    def test_second(self):
        print('This is second test case')
        assert False


if __name__ == '__main__':
    unittest.main()
