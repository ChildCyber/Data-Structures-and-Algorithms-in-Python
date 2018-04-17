## 队列
|     实现方式    | enqueue | dequeue | first | is_empty | len |
| -------------- | ------ | ------ | ------ | ------ | ------ |
|  `ArrayQueue`  | O(1)   | O(1)   | O(1)   | O(1)   | O(1)   |

## 优先级队列
|          实现方式         | len | is_empty | add | min | remove_min |
| ------------------------ | ------ | ------ | ------ | ------ | ------ |
| `UnsortedPriorityQueue`  | O(1)  | O(1)  | O(1)  | O(n)  | O(n)  |
|  `SortedPriorityQueue`   | O(1)  | O(1)  | O(n)  | O(1)  | O(1)  |
|  `HeapPriorityQueue`     | O(1)  | O(1)  | O(log n)  | O(1)  | O(log n)  |
