# Closure

### 개요

[https://www.youtube.com/watch?v=bwwaSwf7vkE](https://www.youtube.com/watch?v=bwwaSwf7vkE)

- **정의**
    - Combination of a function bundled together (enclosed) with references to its surrounding state (the **lexical environment**)
    - **gives you access to an outer function's scope from an inner function**
    
    ![Untitled](Closure%209638995bc1c9459199241b09428fb7be/Untitled.png)
    
- **주의점**
    - 함수가 정의된 Lexical Context를 기준으로 Scope이 결정된다.

### Closure-Scope

- **함수(A) 밖에서 함수(B)가 정의된 경우**
    - Closure이 다른 함수(A)의 정보를 기억하고 있지 않기에, 내부 실행되어도 참조 불가능
    
    ```jsx
    //1. 내부 실행되는 함수가 함수 밖에서 변경된 경우
        const f0 = () => {
          let f0 = 0;
          console.log(f0, f1);
        }
    
        const f1 = () => {
          let f1 = 1;
          f0();
    
    //에러 발생 : f0()에서 f1을 참조할 수 없다 : f0이 실행(define)되는 순간에 f1이 없었기 때문에, f0이 실행되는 순간에 f1을 참조할 수 없다.
    ```
    
- **함수(A) 안에서 함수(B)가 정의된 경우**
    - Closure이 다른 함수(A)의 정보를 기억하고 있기에, **A의 정보를 참조 가능**
    
    ```jsx
    const f2 = () => {
          let f2 = 2;
          (function f3(){
            let f3 = 3;
            console.log(f2, f3); //0,1 출력된다 : f2는 f3가 실행되는 순간에 존재했기 때문에, f3가 실행되는 순간에 f2를 참조할 수 있다.
          })();
        }
        f2();
    ```