# Optional

### 개요

- **java.util.Optional<T>**
    - Integer나 Double 클래스처럼 'T'타입의 객체를 포장해 주는 **Wrapper class**
    - 사용시 예상치 못한 **NullPointerException 예외를 회피**가능
        - 복잡한 조건문 없이도 null 값으로 인해 발생하는 예외를 처리

### 사용

- **of() / ofNullable()**
    - 사용하여 Optional객체 생성
    - 생성된 Optional객체에 참조할 변수를 담음
    - 필요 할 때, 인스턴스 메소드(.**get()** 등)을 사용해 참조값을 반환
    - **ofNullable()**은 null값도 담을 수 있음
    
    ```java
    **Optional<String> opt = Optional.ofNullable("자바 Optional 객체");**
    
    if(opt.isPresent()) {
        System.out.println(opt.get());
    }
    ```
    
- **기타 메소드**
    - orElse()
        - 저장된 값이 존재하면 그 값을 반환하고, 값이 존재하지 않으면 **인수로 전달된 값**을 반환
    - orElseGet()
        - 저장된 값이 존재하면 그 값을 반환하고, 값이 존재하지 않으면 인수로 전달된 **람다 표현식의 결괏값**을 반환
    - orElseThrow()
        - 저장된 값이 존재하면 그 값을 반환하고, 값이 존재하지 않으면 인수로 **전달된 예외를 발생**시킴
    
    ```java
    Optional<String> opt = Optional.empty(); // Optional를 null로 초기화함.
    
    System.out.println(opt.orElse("빈 Optional 객체"));
    System.out.println(opt.orElseGet(String::new));
    ```