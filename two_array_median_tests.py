import unittest
from hypothesis import given, example, assume
import hypothesis.strategies as st
from two_array_median import find_media_sorted_arrays, median_points, merge, median


class TwoArrayMedianTests(unittest.TestCase):
    @given(st.lists(st.integers()).map(sorted), st.lists(st.integers()).map(sorted))
    @example([], [0, 1])
    def test_case(self, l1, l2):
        assume(len(l1) + len(l2) > 0)
        mp = median_points(len(l1) + len(l2))
        m = sum(v for i, v in enumerate(merge(l1, l2)) if i in mp)
        m = m if mp[0] == mp[1] else (m / 2)
        self.assertEqual(m, find_media_sorted_arrays(l1, l2))
