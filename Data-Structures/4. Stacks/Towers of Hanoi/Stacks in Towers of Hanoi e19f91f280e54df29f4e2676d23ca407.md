# Stacks in Towers of Hanoi

### 개요

- **위 코드 해설**
    - [**https://www.youtube.com/watch?v=rf6uf3jNjbo&t=8s**](https://www.youtube.com/watch?v=rf6uf3jNjbo&t=8s)
    - [http://www.cs.cmu.edu/~cburch/survey/recurse/hanoiex.html](http://www.cs.cmu.edu/~cburch/survey/recurse/hanoiex.html)
- **What Should happen**
    
    ```python
    #n=3
    H(3, A, B, C)
    H(2, A, C, B)
    H(1, A, B, C)
    **#위 순서대로 call이 이루어지나, Stack자료형이기에 맨 마지막 call(push)부터 해결함**
    	#1. H(1, A, B, C) 
    	#2. H(2, A, C, B)는  H(1..)짜리를 한 번 더 호출해서 2개짜리 stack을 만듬
    	#3. H(3...)은 H(2...)짜리를 한 번 더 호출하고 이는 H(1...)짜리를 호출함
    ```
    
    ![Untitled](Stacks%20in%20Towers%20of%20Hanoi%20e19f91f280e54df29f4e2676d23ca407/Untitled.png)
    

### 정리

- **Recursive Function 두 개가 상호작용 한 결과가 Stack형 자료구조로 나타남**