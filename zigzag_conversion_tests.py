import unittest

from zigzag_conversion import convert


class ZigZagConversionTests(unittest.TestCase):
    def test_1_row(self):
        self.assertEqual('abc', convert('abc', 1))

    def test_3_rows(self):
        self.assertEqual('PAHNAPLSIIGYIR', convert('PAYPALISHIRING', 3))

    def test_4_rows(self):
        self.assertEqual("PINALSIGYAHRPI", convert('PAYPALISHIRING', 4))
