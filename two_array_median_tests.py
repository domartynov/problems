import unittest
from hypothesis import given, example, assume
import hypothesis.strategies as st
from two_array_median import find_media_sorted_arrays, median


class TwoArrayMedianTests(unittest.TestCase):
    @given(st.lists(st.integers()).map(sorted), st.lists(st.integers()).map(sorted))
    @example([-3, 0], [-1, -1])
    @example([], [0])
    @example([], [0, 1])
    @example([0], [1])
    @example([0, 2], [0, 1])
    @example([-1, -1], [0, 0])
    @example([-2, -2, 0, 0, 0], [-1, -1, 0])
    @example([0], [1, 2])
    @example([1], [0, 1, 2])
    @example([1], [0, 2, 3])  # [ 0, (1, 2), 3]
    @example([-1], [0, 2, 3])  # [-1, (0, 2), 3]
    @example([1], [-1, 0, 2, 3])  # [-1,  0, (1), 2, 3]
    @example([-1], [-2, 0, 2, 3])  # [-2, -1, (0), 2, 3]
    def test_case(self, l1, l2):
        assume(len(l1) + len(l2) > 0)
        m = median(sorted(l1 + l2))
        self.assertEqual(m, find_media_sorted_arrays(l1, l2))
