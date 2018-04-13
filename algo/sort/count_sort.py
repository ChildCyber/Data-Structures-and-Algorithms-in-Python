def count_sort(lst):
    """
    计数排序
    """
    result = list()
    min_ele = max_ele = lst[0]

    for x in lst:
        if x < min_ele:
            min_ele = x
        if x > max_ele:
            max_ele = x
    bucket = [0 for _ in range(min_ele, max_ele + 1)]

    for x in lst:
        bucket[x - min_ele] += 1

    for index, y in enumerate(bucket, min_ele):
        if y:
            result.extend([index] * y)

    return result
