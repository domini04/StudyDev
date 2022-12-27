# Enum Constants

### 개요

- **Enumeration Constants(**`enum`**)**
    - a special "class" that represents a **group of constants**
        - (unchangeable variables, like `final` variables)
        - 여러 종류의 상수 객체들을 집합체 형태로 보관/사용
        - 클래스를 상수(constant variable)처럼 사용가능
    - 하나의 인스턴스만 생성 하여 사용 가능 - 싱글톤 형태
    - **Iterator<E>**와 거의 유사하며, 가능하면 Iterator 사용이 권장
- **장점**
    - 단순한 여러개의 객체를 만들어야 할 경우, Class나 Interface 사용시 너무 복잡해짐
    - 반복문을 통해 데이터를 한 번에 출력가능

### 사용법

- **Enumeration<E>**
    - class 대신 **enum**을 사용
    - 안에 멤버변수 대신 생성하려는 enum객체들을 정의
    
    ```java
    public enum PayType {
    	CARD, //  <- 정의하려는 enum객체들
    	CASH("현금", Arrays.asList("계좌이체", "무통장입금")); // <-Field 값들
    	
    	//정의하려는 필드들을 선언
    	private String typeCategory; 
    	private List<String> typeList;
    	
    	PayType(){}  // 필드가 없는 enum들 생성을 위해 필요
    	PayType(String typeCategory, List<String> typeList) { //enum의 param값을 받아서 생성
    		this.typeCategory = typeCategory;
    		this.typeList = typeList;
    	}	
    }
    ```
    
- **enum parameters**
    - **enum객체들의 필드는 ( )안에 값을 넣음**
        - These values are passed to the constructor when the constant is created
        - Java requires that the constants be defined first
        - 값이 들어간 필드들을 정의하려면 생성자의 this를 통해 정의
- **특이점**
    - this키워드가 가리키는 것은 클래스(PayType) 인스턴스가 아닌**, 각 enum constants**
- **Looping**
    - `values()`
        - returns an array of all enum constants.
        - 껍데기 enum클래스를 iterate해서 안의 enum constants들에 접근 가능
    
    ```java
    for (PayType e : PayType.values()) {
      System.out.println(e);
    }
    ```