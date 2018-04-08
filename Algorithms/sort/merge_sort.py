def merge(s1, s2, s):
    x = y = 0

    while x + y < len(s):
        if y == len(s2) or (x < len(s1) and s1[x] < s2[y]):
            s[x + y] = s1[x]
            x += 1
        else:
            s[x + y] = s2[y]
            y += 1


def merge_sort(s):
    """
    归并排序
    """
    n = len(s)
    if n < 2:
        return

    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]
    merge_sort(s1)
    merge_sort(s2)
    merge(s1, s2, s)
