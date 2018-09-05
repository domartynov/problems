import unittest
from hypothesis import given, example
import hypothesis.strategies as st

from heap import *


class HeapTests(unittest.TestCase):
    @given(st.lists(st.integers()))
    def test_build_heap(self, data):
        m = max(data) if data else None
        build_heap(data)
        for i in range(1, len(data)):
            self.assertGreaterEqual(data[(i-1)//2], data[i])
        self.assertEqual(m, next(iter(data), None))

    @given(st.lists(st.integers()))
    @example([0, 0, 0, -1])
    @example([])
    @example([1])
    @example([3, 2])
    @example([1, 3, 2])
    @example([1, 2, 2, 3])
    @example([1, 1])
    def test_heap_sorted(self, data):
        sorted_data = list(sorted(data))
        heap_sort(data)
        self.assertListEqual(sorted_data, data)

    @given(st.lists(st.integers(), min_size=1))
    def test_head_extract_max(self, data):
        m = max(data)
        build_heap(data)
        self.assertEqual(m, heap_extract_max(data))

    @given(st.integers(), st.lists(st.integers()))
    def test_heap_insert(self, key, data):
        build_heap(data)
        heap_insert(data, key)
        for i in range(1, len(data)):
            self.assertGreaterEqual(data[(i-1)//2], data[i])
        self.assertEqual(max(data), next(iter(data), None))
