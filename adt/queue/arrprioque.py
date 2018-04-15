from core.exceptions import PrioQueueError


# 表尾端加入元素，以首端作为堆顶，堆实现
class PrioQueue:
    """
    Implementing priority queues using heaps
    """

    def __init__(self, elist):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def enqueue(self, e):
        # add a dummy element
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        # invariant: j == 2 *i+1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                # elems[j]不大于其兄弟节点的数据
                j += 1
            if e < elems[j]:
                # e在三者中最小，已找到了位置
                break
            # elems[j]在三者中最小，上移
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.siftdown(self._elems[i], i, end)
