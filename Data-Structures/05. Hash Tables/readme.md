# Hash Maps

### 개요

- ***map***
    - **relates two pieces of information**
    - 파이썬 **dictionary**와 유사
        - every key that is used can only be the key **to a single value**.
    - elements들의 **순서는 존재하지 않음**
- ***Hash***
    - **Hash function**을 사용해 일정한 알고리즘을 통해 **데이터를 index로 변환**
        - **returns an array of indexs**
    - **map의 각 key들에 index를 부여해 색인이 가능하도록 함**
    
    ![{Friend’s Name : Astrological Sign}으로 이루어진 map을 hashing하여 index를 부여](Hash%20Maps%20928e517468f04f959ec4fb3f1ee78e26/Untitled.png)
    
    {Friend’s Name : Astrological Sign}으로 이루어진 map을 hashing하여 index를 부여
    

### Hash Functions(*compression functions)*

- **개요**
    - takes a **string** (**or some other type of data**) as input and returns an **array index** as output
    - **key값을 임의의 unique한 hash 자료형으로 압축하여 반환**
        - 알맞는 길이의 hash map을 반환하기 위해서는 Hash Function에 **array(map)의 size가 주어져야 한다**
- **장점**
    - **greatly reduce any possible inputs** into a much smaller range of potential outputs
        - (any string you can imagine) → (an integer smaller than the size of our array)
    - the output of a hash function **contains less data** than the input
        - 이로 인해 hashing functions are **irreversible**
        - 데이터의 손실이 일어나고, 이는 복구 불가능하다

### **Hash Collision**

- **Hash Collision**
    - Hash 결과물로 중복된 데이터가 복수 존재하는 경우

![Untitled](Hash%20Maps%20928e517468f04f959ec4fb3f1ee78e26/Untitled%201.png)

- **해결 기법**
    - **Separate Chaining**
    - **Open Addressing**

### **Separate Chaining**

- **개요**
    - Hash array를  만들고, **Linked List**를 **underlying structure**로 사용
        - 반드시 LL을 base로 사용할 필요 없음
    - 같은 해쉬값들을 하나의 Linked List로 묶는 기법
        - If a linked list already exists at the address, **append the value to the linked list** given
    - 중복값이 있을 경우, 해당 Linked List에 append
        - 특정 값을 찾으려면, 해당 LL만 순회하며 검색하면 됨

![중복되는 hash값이 있을 경우, 그 뒤로 붙임](Hash%20Maps%20928e517468f04f959ec4fb3f1ee78e26/Untitled%202.png)

중복되는 hash값이 있을 경우, 그 뒤로 붙임

- **특징**
    - Key, Value를 함께 저장해야 함
        - 중복되는 hash값 존재시 key로 판별하기 위함
    
    ![Untitled](Hash%20Maps%20928e517468f04f959ec4fb3f1ee78e26/Untitled%203.png)
    

### Open Addressing

- **Linear Probing**
    - hash값을 linear array에 넣되, 중복되는 hash값을 **그 다음 빈 칸**에다 넣는 방법
        - <그 다음 빈 칸>은 **Probing Sequence**에 의해 정해짐
            - Probing Sequence만큼 건너뛰면서 빈 칸을 찾는 방식
    - Hash값을 검색할 때도 마찬가지로 Probing Sequence만큼 이동해 가며 검색
    
    ![Probing Seq.이 1인 경우 한 칸씩 넘어가며 빈 칸을 찾음](Hash%20Maps%20928e517468f04f959ec4fb3f1ee78e26/Untitled%204.png)
    
    Probing Seq.이 1인 경우 한 칸씩 넘어가며 빈 칸을 찾음
    
    ![Prob Seq. 3인 경우, 세 칸씩 이동하며 빈 칸을 찾음](Hash%20Maps%20928e517468f04f959ec4fb3f1ee78e26/Untitled%205.png)
    
    Prob Seq. 3인 경우, 세 칸씩 이동하며 빈 칸을 찾음
    
    - **단점**
        - hash값들이 밀집(**Clustering**)되어 있는 구간인 경우, 비어있는 hash값을 찾는데 오래 걸림
            
            ![Untitled](Hash%20Maps%20928e517468f04f959ec4fb3f1ee78e26/Untitled%206.png)
            
- **Quadratic Probing**
    - Open Sequence를 $1^2$, $2^2$, $3^2$… 으로 늘려가며 빈 hash value를 할당
    - hash값이 밀집되어 있는 구간을 빨리 벗어나도록 고안