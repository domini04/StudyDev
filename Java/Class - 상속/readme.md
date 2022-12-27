# Class 상속

### 개요

- **상속(Inheritance)**
    - 부모가 자식에게 물려주는 행위
    - **Parent Class**
        - 상속을 해 주는 클래스
        - **상위** class, **super**, **base**라고도 부름
    - **Child Class**
        - 상속 받는 클래스
        - **하위** class, **sub**, **derived**라고도 부름
    - 클래스 구성요소 中 **변수**와 **메소드**만 상속
    - **java.lang.Object** : 모든 클래스의 최상위 class
- **장점**
    - **재사용성**
        - 기존의 구현 코드 상속 받아 사용
    - **확장성**
        - 필요 속성 혹은 기능 확장 개발

### 상속

- **사용법**
    
    ```java
    class Child extends Parent {
    }
    ```
    
    - 생성자는 생략하더라도 자동으로 추가
    - **property, method** 를 **override**하여 사용 가능
- s**uper 키워드**
    - 하위 클래스에서 가지는 **상위클래스에 대한 참조 값**
        - super 키워드를 사용하여 **superClass의 메소드, 멤버변수 접근** 가능
    - **super()** : 상위 클래스 기본 생성자 호출
    
    ```java
    class Parent {
    	public void printInfo() {
    			System.out.println(name);
    			System.out.println(age);
    			System.out.println("부모 메소드입니다.");
    		}
    }
    //위의 Parent 클래스를 상속
    public class Child extends Parent  {
    	
    	public Child() {
    //		super(); //Parent를 상속. 생략되어도 자동으로 발동
    	}
    	public void printInfo() { //메소드 오버라이딩 : return type, 메소드명, parameter 모두 동일해야 함. 안그러면 부모의 메소드가 호출됨
    			**super.printInfo(); //부모 클래스의 printInfo()메소드를 먼저 호출함**
    			System.out.println("자식 메소드입니다");
    			}
    ```
    

### Abstract Class 상속

- **abstract 키워드**
    - **Python의 pass와 유사**한 기능
        - abstract method/variable/property 등 선언 가능
        - abstract class를 만드는데도 사용가능
- **abstract Class**
    - **추상 메서드**를 포함한 클래스
    - abstract Class는 **인스턴스 생성이 불가능함**
        - abstract Class를 상속받은 **Child class는 인스턴스 생성 가능**
        - 다만 이 역시 두 가지 방법으로 abstract 문제를 해결해야 함
    - **활용**
        - 다른 class들이 상속받아서 활용하는 **prototype**
- **abstract 클래스 상속시 해결책**
    1. Child Class도 abstract로 생성하기 → 인스턴스 생성 불가
    2. abstract인 메소드 **@Override**
    
    ```java
    public abstract class Computer {
    	**abstract void typing();** //**abstract 메소드는 코드 블럭{} 선언불가**
    }
    
    public class Laptop extends Computer {
    
    	@Override //abstract인 Computer의 typing메소드 재정의 필요
    	void typing() {
    		System.out.println("Notebook에서 오버라이딩 된 메소드입니다.");	
    	}
    }
    ```