import unittest
from is_unique import *


class TestIsUnique(unittest.TestCase):
    def test_truly_unique_str(self):
        data = 'abcdefg'
        result = is_unique(data)
        self.assertEqual(result, True)

    def test_non_unique_str(self):
        data = 'aaa'
        result = is_unique(data)
        self.assertEqual(result, False)

    def test_empty_str(self):
        data = ''
        result = is_unique(data)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
