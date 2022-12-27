# Execution Context

### 개요

- **참고자료**
    - [**https://www.youtube.com/watch?v=QtOF0uMBy7k**](https://www.youtube.com/watch?v=QtOF0uMBy7k)
    - [https://www.youtube.com/watch?v=EWfujNzSUmw](https://www.youtube.com/watch?v=EWfujNzSUmw)
- **정의**
    - **container for the code that's currently running, and everything that aids in its execution**
    - 현재  실행되는 코드와, 그것을 실행하기 위한 모든 환경변수들의 세팅을 담은 container객체
- **구성**
    - 각 context scope마다 **Record & Outer Context**로 구성되어 있음
        - 이를 **Lexical Environemnt**라고 지칭

![Untitled](Execution%20Context%2064e0c262d95e4e44ab890529853c1a5e/Untitled.png)

### Lexical Environment

- **Environment Record**
    - **the actual storage space for the variables of the scope**
    - 각 변수들이 k:v pair로 매핑되어 있음
        - 이를 **식별자(Identifier)**를 **바인딩** 되었다고도 함
- **Outer Environment Reference**
    - 외부 환경(Scope)를 참조하도록 연결해주는 객체
        - 현재 실행되는 콜스택에서, **Local Scope에 필요한 데이터가 존재하지 않을 경우**, 외부 환경에서 데이터를 찾아옴
    - **한 단계 상위의 Scope**에서 필요한 **identifier**를 찾을 수 있도록 연결해줌
        - 이렇게 각 scope가 Outer을 통해 연결되어 있는 것을 **Scope Chaining**이라고 함
    
    ![Untitled](Execution%20Context%2064e0c262d95e4e44ab890529853c1a5e/Untitled%201.png)
    

![Untitled](Execution%20Context%2064e0c262d95e4e44ab890529853c1a5e/Untitled%202.png)

- **Lexcial Scope는 함수가 호출된 시점에서의 값을 참조하는 것이 아닌, *생성 당시 환경의 값을 참조한다!!!***
    - 따라서 **Lexical Context는 함수를 어디서 호출했는지가 아니라 어디에 선언했는지가 중요!**

```jsx
// Lexical Scope 예제
let x = 'global';
function call1() {
  let x = 'local';
  call2(); // local이 아닌 global을 출력 : **Lexical Context는 함수를 어디서 호출했는지가 아니라 어디에 선언했는지에 따라 결정된다.**
}
function call2() {
  console.log(x); // global
}
//---------------------------------------------
function call3() {
  let x = 'local';
  call4(); // local 출력
  function call4() {
    console.log(x); // local 출력됨
  }
}
```

### 활용

- **사용목적**
    - global에 너무 많은 변수들이 존재하는 경우, 값들이 서로 꼬일 수 있음
    
    ```jsx
    let num = 0;
    
    const increase = function() {
        // ver2 : 지역변수(호출될때마다 초기화)
        let num = 0;
        return ++num;
    }
    
    console.log(increase()); // 1
    num = 10; //**increase()가 global의 num을 사용하기 때문에 꼬임**
    console.log(increase()); // 11
    console.log(increase()); // 12
    ```
    
    - 이를 Lexical Scope를 활용해서 구분
    
    ```jsx
    const counter = (function(){
        let num = 0;
        **return {
            increase: function() {
                return ++num;
            },
            decrease: function() {
                return num > 0 ? --num : 0;
            }**
        }
    }
    
    console.log(counter.increase()); // 1
    console.log(counter.increase()); // 2
    console.log(counter.decrease()); // 1
    console.log(counter.decrease()); // 0
    ```