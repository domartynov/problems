import unittest

from longest_palindrome_substring import longest_palindrome


class LongestPalindromeTests(unittest.TestCase):
    def tests(self):
        self.assertEqual('', longest_palindrome(''))
        self.assertEqual('a', longest_palindrome('a'))
        self.assertEqual('aa', longest_palindrome('aa'))
        self.assertEqual('aa', longest_palindrome('baa'))
        self.assertEqual('aa', longest_palindrome('baae'))
        self.assertEqual('aca', longest_palindrome('bacae'))
        self.assertEqual('acca', longest_palindrome('baccae'))
        self.assertEqual('xyzyx', longest_palindrome('bacaexyzyx'))
        self.assertEqual('xyzzyx', longest_palindrome('bacaexyzzyx'))

    def test_fails(self):
        self.assertEqual('aba', longest_palindrome('abadd'))
