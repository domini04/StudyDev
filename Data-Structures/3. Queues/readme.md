# Queues

### 개요

- **Queue**
    - a data structure which **contains an ordered set of data.**
    - **순서**가 존재하는 자료형
- **Methods of Interaction**
    - **Enqueue**
        - adds data to the “back” or end of the queue
    - **Dequeue**
        - provides and removes data from the “front” or beginning of the queue
    - **Peek**
        - reveals data from the “front” of the queue without removing it
    - **오직 front, back에 대한 operation만 허용됨**

[Queue Interaction](Queues%209637165555694cf88a3afa25a338df6f/Queue%20Interaction%2074fb105ed8ab49dc8d5d04d5ffa973b6.md)

- **First In, First Out (FIFO)**
    - process data First In, First Out
    - 순서대로 맨 앞의 data부터 Deque됨 → Enque경우 맨 뒤부터 줄섬

### ****Implementation****

- **linked list**를 underlying data structure로 사용
    - The **front of the queue** is equivalent to the **head node** of a linked list
    - The **back of the queue** is equivalent to the **tail node**

![Untitled](Queues%209637165555694cf88a3afa25a338df6f/Untitled.png)

- **Bounded Queue**
    - queue that has a limit on the amount of data that can be placed into it
    - 넣을 수 있는 데이터의 양이 제한되어 있는 경우
    - ***queue overflow***
        - 이미 꽉 찬 queue에 데이터를 enque하는 경우
    - ***queue underflow***
        - empty queue에서 데이터를 deque하는 경우