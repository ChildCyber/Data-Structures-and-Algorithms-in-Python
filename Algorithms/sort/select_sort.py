def select_sort(lst):
    """
    选择排序
    """
    length = len(lst)

    for x in range(0, length):
        min_index = x
        for y in range(x, length):
            if lst[y] < lst[min_index]:
                min_index = y
        lst[min_index], lst[x] = lst[x], lst[min_index]

    return lst
