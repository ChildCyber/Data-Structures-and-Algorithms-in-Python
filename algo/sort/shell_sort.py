def shell_sort(lst):
    """
    希尔排序
    """
    length = len(lst)
    # 初始步长
    gap = length // 2

    while gap > 0:
        for x in range(gap, length):
            # 每个步长进行插入排序
            tmp = lst[x]
            y = x
            # 插入排序
            while y >= gap and lst[y - gap] > tmp:
                lst[y] = lst[y - gap]
                y -= gap
            lst[y] = tmp
        # 得到新的步长
        gap = gap // 2

    return lst
