def bubble_sort(lst):
    """
    冒泡排序
    """
    length = len(lst)

    for x in range(0, length):
        for y in range(0, length - x - 1):
            if lst[y] > lst[y + 1]:
                lst[y], lst[y + 1] = lst[y + 1], lst[y]

    return lst


def bubble_sort(lst):
    """
    冒泡排序优化
    判断出序列已经有序，跳过有序部分
    """
    length = len(lst)

    for x in range(length):
        is_sorted = True
        for y in range(length - x - 1):
            if lst[y] > lst[y + 1]:
                is_sorted = False
                lst[y], lst[y + 1] = lst[y + 1], lst[y]
        if is_sorted:
            break

    return lst


def bubble_border_sort(lst):
    """
    冒泡排序优化
    添加对序列有序区的界定判定
    """
    length = len(lst)
    # 最后一次交换的位置
    last_ex_index = 0
    # 无序序列的边界，每次比较只需要到这里为止
    sort_border = length - 1

    for x in range(length):
        is_sorted = True
        for y in range(sort_border):
            if lst[y] > lst[y + 1]:
                is_sorted = False
                # 更新为最后一次交换元素的位置
                last_ex_index = y
                lst[y], lst[y + 1] = lst[y + 1], lst[y]
        sort_border = last_ex_index
        if is_sorted:
            break

    return lst
