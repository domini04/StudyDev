# Towers of Hanoi

[심화 : Towers of Hanoi in Binary](https://www.notion.so/Towers-of-Hanoi-in-Binary-fe7264a1f7f04ea1a4e0e7c3007776e5)

[Stacks in Towers of Hanoi](https://www.notion.so/Stacks-in-Towers-of-Hanoi-e19f91f280e54df29f4e2676d23ca407)

### 개요

- Towers of Hanoi is an ancient mathematical puzzle that starts off with **three stacks** and many disks.
- 목표
    - 제일 왼쪽 스택의 disk들을 가장 오른쪽으로 옮기기
    
    ![Untitled](Towers%20of%20Hanoi%20bf4b9668aeba45c59057b548815f5bc3/Untitled.png)
    
- **규칙**
    1. **Only one disk can be moved at a time.**
    2. Each move consists of **taking the upper disk** from one of the stacks and **placing it on top of another stack or on an empty rod.**
    3. **No disk may be placed on top of a smaller disk.**
        - 항상 더 큰 disk가 밑에 와야 함

### Solution

- 먼저 Peg**(Stack)**을 구분
    - **Source Peg**
    - **Destination Peg**
        - Destination Peg에 Stack을 구현하는게 목표
    - **Aux Peg**
        
        ![순서대로 **source, aux, destination**이라고 가정](Towers%20of%20Hanoi%20bf4b9668aeba45c59057b548815f5bc3/Untitled%201.png)
        
        순서대로 **source, aux, destination**이라고 가정
        
- **단순 구현**
    1. **가장 큰 disk($n^{th}$ disk)를 Destination에 먼저 놓고,** 나머지를 다음 큰 순서대로 쌓기
        - 그 결과 **aux peg**에 **(n-1)크기의 stack이 구현됨**
        - source→Destination으로 **n번째 disk를 옮기기.**
        
        ![n번째 disk가 dest로 옮겨졌고, aux에 n-1짜리 stack이 구현된 상태](Towers%20of%20Hanoi%20bf4b9668aeba45c59057b548815f5bc3/Untitled%202.png)
        
        n번째 disk가 dest로 옮겨졌고, aux에 n-1짜리 stack이 구현된 상태
        
    2. **source, aux를 바꿔서 (n-1)짜리 작업 진행**
        - (**aux → source)**
            - n-1짜리 stack이 구현되어 있는 aux가 source가 된다
            - n-1번째 disk를 **dest**로 옮기는 것이 목표
        - (**source → aux)**
            - 비어있는 source peg를 aux로 사용
        - (**dest → dest)**
            - progress가 있으려면 dest는 고정일 필요
        
        ![Untitled](Towers%20of%20Hanoi%20bf4b9668aeba45c59057b548815f5bc3/Untitled%203.png)
        
    3. 다시 source, aux를 바꿔서 ((n-1)-1)짜리 작업 진행
        - (**aux → source → aux)**
        - (**source → aux → source)**
        - (**dest는 그대로)**
            - 위 예제에서는  n-1-1 == 1이므로 마지막 disk를 dest로 바로 옮김
    4. 반복… until finish
    - 이를 **Recursive Function**을 통해 구현 가능할듯.

### 알고리즘

- **개념**
    1. (n-1) stack을 aux에 구현
    2. n번째 disk를 dest로 옮김
    3. (n-1) stack을 갖고 비어 있는 peg에 1-2를 반복
        - **이 때 비어있는 peg의 alternating  패턴을 파악하는 것이 핵심**
- **정리**
    1. `Move n-1 disks from **source** to **aux`** (n-1짜리 stack 구현)
    2. `Move nth disk from **source** to **dest**`
        - disk 하나만 옮기기
    3. `Move n-1 disks from **aux** to **dest**`
- **Psuedocode**

```python
Hanoi(n, start, end)

move(start, end) if n=1 #helper function

other = sum(range(start, end)) - (start + end) #aux peg의 번호를 찾음
- Hanoi(n-1, start, other) #첫번째 블럭은 aux peg에 n-1짜리 stack 구현 + n번째 disk를 dest로 옮김
	move(start, end)
- Hanoi(n-1, other, end) # 두 번째 블럭은 aux peg에서 stack을 dest로 옮김. 
# 그러기 위해서 첫 번째 블럭을 1씩 감소해가며 recursivly 반복
```

- H(n, source, aux, dest)의 의미
    - ***n개짜리 stack을 source→dest로 옮김***
        - n =1일때 **그 자체로 작동하는 base code로써도 기능함**
- **Python Code**
    
    ```python
    def TowersOfHanoi(n, source, destination, auxiliary):
    		#unit method. 전달받은 source에서 dest로 디스크를 하나 옮김
        if n==1: 
            print("Move disk 1 from peg",source,"to peg",destination) 
            return
    
    		#f1 : dest와 aux을 alternate하며 source에 있는 disk를 옮김
        TowersOfHanoi(n-1, source, auxiliary, destination)
        print("Move disk",n,"from peg",source,"to peg",destination)
    		
    		#f2 : -> source / dest -> aux / source -> dest 사이에서 alternate 하며 disk 옮김
    		#aux/dest/source에서 왼쪽으로 한칸식 shift 
        TowersOfHanoi(n-1, auxiliary, destination, source)
    		
    ```