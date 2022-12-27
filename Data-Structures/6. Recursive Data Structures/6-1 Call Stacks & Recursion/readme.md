# Recursion

### 개요

- **Recursion**
    - 자기 자신을 참조하는 logic이 포함되어 있는 경우
    - strategy for solving problems by defining the problem in terms of itself
- **Recursion functions**
    - function definition includes an invocation of the function **within its own body**
    - function invoking itself **with different arguments**
        - 점점 답안에 근접해가도록 argument가 바뀌도록 설계하는것이 핵심
        
        ```
        define function, speller
          if there are no more letters
            print "all done"
          print the first letter
          invoke speller with the given name minus the first letter
        ```
        
    
    ![Untitled](Recursion%205bac3e64dd1c4dde9a16c5eb2b6c4b61/Untitled.png)
    

### Recursion Function 구성요소

- **base case**
    - Recursion이 반복되어 **문제가 해결된 경우**를 상정
        - dictates whether the function will recurse, or call itself
        - 무한루프를 탈출하게 해주는 역할
    
    ```
    if there are no more letters
         print "all done"
    ```
    
- **piecewise solution to the problem**
    - Recursion하면서 **문제를 조금씩 해결**해 가는 부분
    
    ```
    	print the first letter
    ```
    
- ***recursive* step**
    - 위의 piecewise solution을 반복하여 호출하는 부분
    - calling the function with arguments which bring us closer to the base case
    
    ```
    invoke speller with the given name minus the first letter
    ```
    

### Call Stacks

[Call Stack](https://www.notion.so/Call-Stack-d694e80bf5e34ab0ad9d690ab73b982c) 

- **Call Stacks & Recursive Functions**
    - **함수**들이 recursively 호출되면서 **call stack**에 쌓이는 형태
    - **last function to enter the call stack is the first function to exit the call stack**
    - **가장 먼저 호출되는 함수는 가장 마지막에 처리됨**
- Function Call 예시
    - Recursive Function 예제
    
    ```
    function, sum_list 
       if list has a single element
         return that single element
       otherwise...
         add first element to value of **sum_list** called with every element minus the first
    ```
    
    - **콜스택**
        - [https://www.youtube.com/watch?v=Qm4axEzqw0k](https://www.youtube.com/watch?v=Qm4axEzqw0k)
        - 

### Base Case Design

- **Base Case**
    - 무한루프를 탈출하게 해주는 역할
- **Iteration Function의 경우**
    - 특정 조건 만족시까지 counting variable을 증감시키는게 base case에 해당
- **Recursive Function의 경우**
    - **argument to the recursive call이 이에 해당**
    - break를 조건으로 갖는 while문 design과 유사한듯?
    - **base case가 없거나 부실한 경우 → Stack Overflow**

### Recursion & Time Complexity

- **recursive step이  복수의 function call을 하는 경우, O(n)은 exponential growth**
    - [https://syedtousifahmed.medium.com/fibonacci-iterative-vs-recursive-5182d7783055](https://syedtousifahmed.medium.com/fibonacci-iterative-vs-recursive-5182d7783055)
    - [https://github.com/domini04/Algorithms/tree/main/Coursera/Algorithmic Toolbox/Week2](https://github.com/domini04/Algorithms/tree/main/Coursera/Algorithmic%20Toolbox/Week2)
- 따라서 다른 방법으로 문제 해결하는 것이 적절