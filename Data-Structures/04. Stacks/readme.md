# Stacks

### 개요

- **Stack**
    - a data structure which contains an **ordered set of data.**
    - mimics a physical stack of objects
    - 각 data의 값은 **weight**라고 부름
    
    ![Untitled](Stacks%20da75a93a2a744c609f1e1c080e10c5e7/Untitled.png)
    
- **Methods  of interaction**
    - **Push**
        - adds data to the “top” of the stack
        
        ![Untitled](Stacks%20da75a93a2a744c609f1e1c080e10c5e7/Untitled%201.png)
        
    - **Pop**
        - **returns and removes** data from the “top” of the stack
        
        ![Untitled](Stacks%20da75a93a2a744c609f1e1c080e10c5e7/Untitled%202.png)
        
    - **Peek**
        - returns data from the “top” of the stack **without removing it**
        
        ![Untitled](Stacks%20da75a93a2a744c609f1e1c080e10c5e7/Untitled%203.png)
        
- **특징**
    - **First In, Last Out(FILO)**
        - Stack의 가장 위의 data (마지막으로 Push한 data)만 접근 가능
        - 맨 위의 data를 제거하기 전에는 그 밑의 데이터는 접근 불가

### Implementation

- Uses linked list as the underlying data structure

![Untitled](Stacks%20da75a93a2a744c609f1e1c080e10c5e7/Untitled%204.png)

- Can have a limited size