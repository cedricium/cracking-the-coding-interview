import unittest
from check_permutation import *


class TestCheckPermutation(unittest.TestCase):
    def test_known_permutation(self):
        data = ('dog', 'god')
        result = check_permutation(*data)
        self.assertEqual(result, True)

    def test_non_permutation(self):
        data = ('bog', 'dog')
        result = check_permutation(*data)
        self.assertEqual(result, False)

    def test_case_sensitive_permutation(self):
        data = ('dog', 'DOG')
        result = check_permutation(*data)
        self.assertEqual(result, False)

    def test_mismatched_string_lengths(self):
        data = ('dog', 'doggy')
        result = check_permutation(*data)
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
