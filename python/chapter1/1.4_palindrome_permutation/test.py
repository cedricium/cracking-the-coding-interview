import unittest
from palindrome_permutation import *


class TestPalindromPermutation(unittest.TestCase):
    def test_empty_string(self):
        data = ''
        result = palindrome_permutation(data)
        self.assertEqual(result, True)

    def test_case_insensitive_permutation(self):
        data = 'Hello OlLhE'
        result = palindrome_permutation(data)
        self.assertEqual(result, True)

    def test_all_identical_characters_in_string(self):
        data = 'AaaaAa'
        result = palindrome_permutation(data)
        self.assertEqual(result, True)

    def test_unbalanced_characters_in_invalid_string(self):
        data = 'aba bba'
        result = palindrome_permutation(data)
        self.assertEqual(result, False)

    def test_unbalanced_characters_in_valid_string(self):
        data = 'aaa aa'
        result = palindrome_permutation(data)
        self.assertEqual(result, True)

    def test_true_palindrome(self):
        data = 'racecar'
        result = palindrome_permutation(data)
        self.assertEqual(result, True)

    def test_permutated_palindrome(self):
        data = 'race rac'
        result = palindrome_permutation(data)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
