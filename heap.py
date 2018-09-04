def heapify(data, i, size=None):
    size = size if size is not None else len(data)
    l, r = 2*i + 1, 2*i + 2
    m = l if l < size and data[l] > data[i] else i
    m = r if r < size and data[r] > data[m] else m
    if m != i:
        data[m], data[i] = data[i], data[m]
        heapify(data, m, size)


def build_heap(data):
    i = (len(data) - 1) // 2
    while i >= 0:
        heapify(data, i)
        i -= 1
    return data


def heap_insert(data, key):
    data.append(None)
    i = len(data) - 1
    while i > 0 and data[(i-1) // 2] < key:
        data[i] = data[(i-1) // 2]
        i = (i-1) // 2
    data[i] = key


def heap_extract_max(data):
    r = data[0]
    data[0] = data[-1]
    del data[-1]
    heapify(data, 0)
    return r


def heap_sort(data):
    build_heap(data)
    i = len(data) - 1
    while i >= 1:
        data[i], data[0] = data[0], data[i]
        heapify(data, 0, i)
        i -= 1
    return data
