# Two-Pointer Linked Lists Techniques

### Problem

- Create a method that **returns the nth last element** of a singly linked list
    
    ```
    For example: 
    given a linked list with the following elements **1 -> 2 -> 3 -> 4 -> 5,** 
    return the **2nd** to last element. 
    The answer would be element **4**.
    ```
    
- **문제점**
    - Single Pointer로는 **current node가 head 혹은 end로부터 얼마나 떨어져있는지 알 수 없음**
        - current node는 오직 연결된 node에 대한 정보만 담고 있기 때문에

### Solution

- **Naive Approach**
    - LL 순서를 담은 리스트를 하나 더 만들기
    
    ```python
    def list_nth_last(linked_list, n):
      linked_list_as_list = []
      current_node = linked_list.head_node
      while current_node:
        linked_list_as_list.append(current_node)
        current_node = current_node.get_next_node()
      return linked_list_as_list[len(linked_list_as_list) - n]
    ```
    
    - **비판**
        - 메모리 많이 먹음. 시간 오래걸림
- **Two-Pointer Approach**
    - **head pointer & tail pointer**을 사용
        1. head pointer가 먼저 움직임
        2. head pointer가 일정 count 만큼 진행했을 때, tail pointer도 같은 속도로 움직이기 시작
        3. head pointer가 None이 되었을 때(LL의 끝에 다다름) 모두 stop
            - **이 때 tail pointer의 위치가 nth last element of Linked Lists에 해당**
        4. count를 튜닝하여 원하는 순서의 element 반환하도록 가능
    
    ![Untitled](Two-Pointer%20Linked%20Lists%20Techniques%20dc3467337050410c90e586b96fb6dade/Untitled.png)
    
    - **뒤에서 2번째 element를 구하는 경우**
    
    ![Untitled](Two-Pointer%20Linked%20Lists%20Techniques%20dc3467337050410c90e586b96fb6dade/Untitled%201.png)
    
    ![count가 2+1 이상일 경우 N도 출발](Two-Pointer%20Linked%20Lists%20Techniques%20dc3467337050410c90e586b96fb6dade/Untitled%202.png)
    
    count가 2+1 이상일 경우 N도 출발
    
    ![T의 값이 None이 되는 경우 멈춘다. 이 때 N의 위치는 뒤에서 2번째](Two-Pointer%20Linked%20Lists%20Techniques%20dc3467337050410c90e586b96fb6dade/Untitled%203.png)
    
    T의 값이 None이 되는 경우 멈춘다. 이 때 N의 위치는 뒤에서 2번째