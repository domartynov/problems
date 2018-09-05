class Span(object):
    def __init__(self, l):
        self.l = l
        self.a = 0
        self.b = len(l)

    def trim_left(self, n):
        self.a += n

    def trim_right(self, n):
        self.b -= n

    def __len__(self):
        return self.b - self.a

    def __getitem__(self, i):
        return self.l[self.a + i]

    def __iter__(self):
        return iter(self[i] for i in range(len(self)))

    def __repr__(self):
        return repr(list(self))


def median_points(n):
    return (n - 1) // 2, n // 2


def median(l):
    a, b = median_points(len(l))
    return (l[a] + l[b]) / 2.0 if a < b else l[a]


def merge(i1, i2):
    i1, i2 = iter(i1), iter(i2)
    v1 = next(i1, None)
    v2 = next(i2, None)
    while v1 is not None or v2 is not None:
        if v1 is None:
            yield v2
            v2 = next(i2, None)
        elif v2 is None:
            yield v1
            v1 = next(i1, None)
        elif v1 < v2:
            yield v1
            v1 = next(i1, None)
        else:
            yield v2
            v2 = next(i2, None)


def find_media_sorted_arrays(l1, l2):
    s1, s2 = (Span(l2), Span(l1)) if len(l2) < len(l1) else (Span(l1), Span(l2))

    while len(s1) > 0 and len(s2) > 2:
        h = len(s1) // 2
        m1, m2 = median(s1), median(s2)
        if m1 == m2:
            return m1
        elif m1 < m2:
            s1.trim_left(h)
            s2.trim_right(h)
        else:
            s1.trim_right(h)
            s2.trim_left(h)

    return median(list(merge(iter(s1), iter(s2))))


class Solution(object):
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def findMedianSortedArrays(self, nums1, nums2):
        find_media_sorted_arrays(nums1, nums2)
