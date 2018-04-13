def insert_sort(lst):
    """
    插入排序
    """
    length = len(lst)

    if length <= 1:
        return lst

    for x in range(1, length):
        for y in range(x, 0, -1):
            if lst[y] < lst[y - 1]:
                lst[y], lst[y - 1] = lst[y - 1], lst[y]
            else:
                break

    return lst
