classDiagram
PriorityQueueBase <|-- UnsortedPriorityQueue
PriorityQueueBase <|-- SortedPriorityQueue
PriorityQueueBase <|-- HeapPriorityQueue
HeapPriorityQueue <|-- AdaptableHeapPriorityQueue

### UnsortedPriorityQueue

|    操作    | 时间复杂度 |
| --------- | ---------- |
|  `len()`  |  O(1)  |
| `is_empty()`  | O(1)  |
| `add()`   | O(1)  |
| `min()`  | O(n)  |
| `remove_min()`  | O(n)  |

### UnsortedPriorityQueue & SortedPriorityQueue对比

|    操作    | Unsorted List | Sorted List |
| --------- | ---------- | ---------- |
|  `len()`  |  O(1)  |  O(1)  |
| `is_empty()`  | O(1)  |  O(1)  |
| `add()`   | O(1)  |  O(n)  |
| `min()`  | O(n)  |  O(1)  |
| `remove_min()`  |  O(n)  |  O(1)  |
