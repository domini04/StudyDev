# Fibonacci Numbers

### 개요

![Untitled](Fibonacci%20Numbers%2027d3764082b94d43883a70069759d840/Untitled.png)

- rabbit population등 **기하급수적으로 증가**하는 것을 나타내기 위해 고안된 모델
    - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ….
- **n번째 피보나치 수를 계산하기 위해서 n-1, n-2번째 피보나치 수를 참조함**
    - 이 점으로 인해 **단순 recursive function으로 계산했을 때 연산량이 폭증**
    
    ```python
    #naive 방식
    def Fib(n):
        a = 0
        b = 1
        if n <= 1:
            return n
        else :
            return Fib(n-1)+Fib(n-2)
    
    print(Fib(11))
    >>> 89
    ```
    

### **문제(Naive Algorithm)**

- n번째 피보나치 수열을 계산하기 위해 이전의 수들을 계산하는게 반복됨
- **그 과정에서 같은 수열이 중복되어 계산됨**
    - 이로 인해 연산량 폭증

![n-4번째 수가 총 4번 계산됨](Fibonacci%20Numbers%2027d3764082b94d43883a70069759d840/Untitled%201.png)

n-4번째 수가 총 4번 계산됨

### 해결(Efficient Algorithm)

- array를 만들어서 그 안에 수열을 보관, 필요할 때마다 꺼내쓰는 방식
    - 그러면 매번 피보나치 수열을 계산 할 필요 없음
    
    ![Untitled](Fibonacci%20Numbers%2027d3764082b94d43883a70069759d840/Untitled%202.png)
    
    ```python
    #피보나치 수열 반환
    def Fib(n):
        F = [0, 1]
        for i in range(2,n):
            F.append(F[i-1] + F[i-2])
        return F
    
    #피보나치 수열 마지막 수
    def Fib(n):
        F = [0, 1]
        for i in range(2,n):
            F.append(F[i-1] + F[i-2])
        return F[n-1]
    
    print(Fib(13))
    >>>144
    ```
