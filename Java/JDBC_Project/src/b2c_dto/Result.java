package b2c_dto;

public enum Result {
   배송미출발(0), // '배송미출발'이라는 이름의 enum 상수를 생성
   배송출발(1); // '배송출발'이라는 이름의 enum 상수를 생성
   
   int num;
   
   Result() {};
   Result(int num) {  // enum 상수를 생성할 때, num을 매개변수로 받아서 
      this.num = num; //
   }
   
   public int getNum() {
      return num;
   }
}