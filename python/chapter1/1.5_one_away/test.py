import unittest
from one_away import *


class TestOneAway(unittest.TestCase):
    def test_equal_strings(self):
        data = ('hello', 'hello')
        result = one_away(*data)
        self.assertEqual(result, True)

    def test_empty_strings(self):
        data = ('', '')
        result = one_away(*data)
        self.assertEqual(result, True)

    def test_unequal_length(self):
        data = ('hello', 'hello world')
        result = one_away(*data)
        self.assertEqual(result, False)

    def test_character_removed(self):
        data = ('pale', 'ple')
        result = one_away(*data)
        self.assertEqual(result, True)

    def test_character_replaced(self):
        data = ('aaabc', 'xaabc')
        result = one_away(*data)
        self.assertEqual(result, True)

    def test_character_inserted(self):
        data = ('abc', 'abcd')
        result = one_away(*data)
        self.assertEqual(result, True)

    def test_multiple_edits(self):
        data = ('aaaa', 'wxy')
        result = one_away(*data)
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
