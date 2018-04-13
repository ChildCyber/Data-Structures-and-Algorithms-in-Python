import math


def radix_sort(lst, radix=10):
    """
    基数排序
    """
    k = int(math.ceil(math.log(max(lst), radix)))
    bucket = [[] for _ in range(radix)]

    for i in range(1, k + 1):
        for j in lst:
            bucket[j % (radix ** i) // radix ** (i - 1)].append(j)
        del lst[:]
        for z in bucket:
            lst.extend(z)

    return lst
