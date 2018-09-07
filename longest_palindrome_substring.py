def longest_palindrome(s):
    ma, mb = 0, 0
    a, b = 0, 0
    while b < len(s):
        if s[a] == s[b]:
            d = 0
            while a - d - 1 >= 0 and b + d + 1 < len(s) and s[a - d - 1] == s[b + d + 1]:
                d += 1

            if b - a + 2 * d > mb - ma:
                ma, mb = a - d, b + d

        a, b = (b, b) if a < b else (a, a + 1)
    return s[ma: mb + 1]


class Solution(object):
    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def longestPalindrome(self, s):
        return longest_palindrome(s)
