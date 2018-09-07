def convert(s, n):
    if n == 1:
        return s
    r = ''
    for i in range(0, n):
        p = 2 * n - 2
        for j in range(0, len(s), p):
            r += s[j + i: j + i + 1]
            if 0 < i < n - 1:
                r += s[j + p - i: j + p - i + 1]
    return r


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def convert(self, s, numRows):
        return convert(s, numRows)
