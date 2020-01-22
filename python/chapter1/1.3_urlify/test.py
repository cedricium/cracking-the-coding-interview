import unittest
from urlify import *


class TestURLify(unittest.TestCase):
    def test_no_spaces_in_string(self):
        data = 'helloworld!'
        result = urlify(data)
        self.assertEqual(result, data)

    def test_space_between_words(self):
        data = 'hello, world!'
        expected = 'hello,%20world!'
        result = urlify(data)
        self.assertEqual(result, expected)

    def test_string_with_padded_spaces(self):
        data = '   hello, world!   '
        expected = 'hello,%20world!'
        result = urlify(data)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        data = ''
        result = urlify(data)
        self.assertEqual(result, data)


if __name__ == "__main__":
    unittest.main()
