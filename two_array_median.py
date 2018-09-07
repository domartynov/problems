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
    return (l[a] + l[b]) / 2 if a < b else l[a]


def find_media_sorted_arrays(l1, l2):
    s1, s2 = (Span(l2), Span(l1)) if len(l2) < len(l1) else (Span(l1), Span(l2))

    while len(s1) > 1:
        a1, b1 = median_points(len(s1))
        a2, b2 = median_points(len(s2))

        if s1[a1] <= s2[a2] and s2[b2] <= s1[b1]:
            return (s2[a2] + s2[b2]) / 2
        if s2[a2] <= s1[a1] and s1[b1] <= s2[b2]:
            return (s1[a1] + s1[b1]) / 2

        if a1 == 0:
            break

        if s1[a1] <= s2[a2]:
            s1.trim_left(a1)
            s2.trim_right(a1)
        elif s1[b1] >= s2[b2]:
            s1.trim_right(a1)
            s2.trim_left(a1)

    tail = (len(s2) - 1) // 2 - len(s1)
    if tail > 0:
        s2.trim_left(tail)
        s2.trim_right(tail)

    return median(sorted(list(s1) + list(s2)))


class Solution(object):
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def findMedianSortedArrays(self, nums1, nums2):
        return find_media_sorted_arrays(nums1, nums2)
