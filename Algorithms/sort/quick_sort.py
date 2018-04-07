import random


def inplace_quick_sort(lst, start, end):
    """
    原地快速排序
    """
    # 前后哨兵相遇
    if start >= end:
        return

    pivot = lst[end]
    left = start
    right = end - 1

    while left <= right:
        while left <= right and lst[left] < pivot:
            left += 1
        while left <= right and pivot < lst[right]:
            right -= 1
        # 交换前后哨兵元素
        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left, right = left + 1, right - 1
    # 交换枢纽元和前后两个哨兵相交点元素
    # 这里left不能替换成right，最终left会大于right
    lst[left], lst[end] = lst[end], lst[left]

    inplace_quick_sort(lst, start, left - 1)
    inplace_quick_sort(lst, left + 1, end)


def quick_sort(lst):
    """
    快速排序，需要额外空间
    """
    if len(lst) <= 1:
        return lst

    left, right, mid = [], [], []
    pivot = random.choice(lst)

    for x in lst:
        if x == pivot:
            mid.append(x)
        elif x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + mid + quick_sort(right)
