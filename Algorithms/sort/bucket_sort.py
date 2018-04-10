def bucket_sort(lst):
    """
    桶排序
    """
    length = len(lst)
    min_ele = max_ele = lst[0]

    for x in lst:
        if x < min_ele:
            min_ele = x
        if x > max_ele:
            max_ele = x

    d = max_ele - min_ele
    # 初始化桶
    bucket_lst = [[] for _ in range(length)]

    # 遍历原数组，将每个元素放入桶中
    for x in lst:
        index = (x - min_ele) * (length - 1) // d
        bucket_lst[index].append(x)

    # 对每个桶内部进行排序，这里采用快速排序
    for bucket in bucket_lst:
        bucket.sort()
    result = []
    for bucket in bucket_lst:
        result.extend(bucket)

    return result
