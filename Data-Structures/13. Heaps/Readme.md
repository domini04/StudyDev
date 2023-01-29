# Heaps

### 개요

- **Heaps**
    - used to **maintain a maximum or minimum value in a dataset**
    - 일종의 **priority queue**
- **종류**
    - **max-heaps**
        - Heaps that track the maximum value in a dataset
    - **min-heaps**
        - heaps that track the minimum value
- **특징(max-heap)**
    - The root is the *maximum value* of the dataset.
    - Every parent’s value is *greater than its children*.

### Representation

- **Conceptual**
    - Binary Tree where each node has ***at most* two children**
        - Elements  are added from left to right until level is filled
- **Practical**
    - Sequential Datastructure is used

![추상적 개념 이해를 위해선 왼쪽 BTree를, 실제 사용을 위해선 Array/List 등을 사용](Heaps%200771fca52ea94a948233342715755c63/Untitled.png)

추상적 개념 이해를 위해선 왼쪽 BTree를, 실제 사용을 위해선 Array/List 등을 사용

- **index 패턴**
    - **left child = `(index * 2) + 1`**
        - 1, 3, 5, 7, 9, …
    - **right child =  `(index * 2) + 2`**
        - 2, 4, 6, 8, 10, …
    - **parent =  `index // 2` — *not used on the root!***
- **List 표현**
    
    ![Untitled](Heaps%200771fca52ea94a948233342715755c63/Untitled%201.png)
    
    ```python
    print(heap.heap_list)
    # Outputs: [None, 88, 76, 65, 41, 53, 51, 46, 32, 38, 39, 21, 34]
    # Indices: [0, 1, 2, 3, 4, 5, 6, 7, ... 12]
    ```
    

[Heapifying](https://www.notion.so/Heapifying-99221123414f4c32bb885c3172ce9d07)