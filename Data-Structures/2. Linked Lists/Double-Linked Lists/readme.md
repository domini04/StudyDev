# Doubly Linked Lists

### 개요

- **Double Linked Lists**
    - Each node contains data and **two links** (or pointers) to the **next and previous nodes** in the list
    - The head node’s previous pointer is set to **`null`** and the tail node’s next pointer is set to **`null`**
    - **포함요소**
        - A value
        - A pointer to the previous node
        - A pointer to the next node
    - 양 방향으로 pointer가 존재하기에 **양 방향으로의 이동이 가능**

![Untitled](Doubly%20Linked%20Lists%2040690bd9db4d4dfd946140773b0e40ba/Untitled.png)

### ****Adding to & Removing from the list****

- **Adding to the List**
    - update 및 신경써야 할 pointer가 많기에 유의
    - **Head 노드 추가**
        1. **check if there is a current head to the list**
            1. **head 없음 → 빈 list임** → 추가하는 노드를 **head 겸 tail**로 삼고 **both pointers = null**
            2. head가 존재하면 일반적인 작업
        2. current head의 previous pointer를 new head로 업데이트
        3. Set the new head’s next pointer to the current head
        4. Set the new head’s previous pointer to **`null`**
    - ****Adding to the tail****
        - 위와 동일
    
    ![Untitled](Doubly%20Linked%20Lists%2040690bd9db4d4dfd946140773b0e40ba/Untitled%201.png)
    
- ****Removing from the list****
    - **Removing from Head or Tail**
        - 마찬가지로 기존 작업에서 null pointer 값을 추는 과정이 추가됨
            
            ![Untitled](Doubly%20Linked%20Lists%2040690bd9db4d4dfd946140773b0e40ba/Untitled%202.png)
            
    - **Removing from the middle**
        - 앞뒤 노드들의 각 포인터들을 모두 변경
    
    ![Untitled](Doubly%20Linked%20Lists%2040690bd9db4d4dfd946140773b0e40ba/Untitled%203.png)