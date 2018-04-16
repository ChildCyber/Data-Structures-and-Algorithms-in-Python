from core.exceptions import PrioQueueError


class PrioQue:
    """
    顺序表实现优先队列，基于Python内置类型list实现
    """

    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)  # 从大到小

    def enqueue(self, e):
        i = len(self._elems) - 1
        # 从尾端进行比较，结束时i为-1或第一个大于e的元素的下标
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in top")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self._elems.pop()
