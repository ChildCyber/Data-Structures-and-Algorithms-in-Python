def heap_sort(lst):
    """
    堆排序
    """

    def sift_down(start, end):
        # 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
        root = start

        while True:
            child = 2 * root + 1
            # 越界
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            # 父节点与子节点比较
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

        # 创建大根堆：将堆中的所有数据重新排序

    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

        # 堆排序：移除位在第一个数据的根节点，并做最大堆调整的递归运算
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)

    return lst
