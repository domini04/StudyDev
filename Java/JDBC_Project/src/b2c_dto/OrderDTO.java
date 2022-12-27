package b2c_dto;

import java.sql.Date;
import java.sql.SQLException;

import exception.NotExistException;


public class OrderDTO {
   
   public enum Result {
      배송미출발(0), // 0을 넣을 시 배송미출발 출력
      배송출발(1); // 1을 넣을 시 배송출발 출력
         //※주의사항 : Result enum객체를 사용시 안의 num 값을 꺼내려면 .num을 붙여야 한다.
      int num;
      
      Result() {};
      Result(int num) {
         this.num = num; // Result 인스턴스 생성시 0 또는 1을 받아서 num에 저장
      }
      
      public int getNum() {
         return num;
      }
      public void setNum(int num) { //이 부분 추가. 우리가 구하고자 하는 값이 
         this.num = num;
      }
      }
   
   private int orderNum; 
   private String orderId; //주문자 id. UserDTO의 id를 FK로 받아온다.
   private int totalPrice;
   private Date indate;
   private Result result;

   public OrderDTO() {
      this.result = Result.배송미출발; // default result is 배송미출발
   }
   
   public OrderDTO(int orderNum, String orderId, int totalPrice,
         Date indate, String label){

      this.orderId = orderId;
      this.totalPrice = totalPrice;
      this.indate = indate;
      
      // 
      switch(label) {
      case "배송미출발":
         this.result = Result.배송미출발;
         break;
      case "배송출발":
         this.result = Result.배송출발;
         break;
      default:
         this.result = Result.배송미출발;
         break;
      }
      
   }

   public int getOrderNum() {
      return orderNum;
   }

   public void setOrderNum(int orderNum) {
      this.orderNum = orderNum;
   }

   public String getOrderId() {
      return orderId;
   }

   public void setOrderId(String orderId) throws SQLException, NotExistException {
      this.orderId = orderId;
   }

   public int getTotalPrice() {
      return totalPrice;
   }

   public void setTotalPrice(int totalPrice) {
      this.totalPrice = totalPrice;
   }

   public Date getIndate() {
      return indate;
   }

   public void setIndate(Date indate) {
      this.indate = indate;
   }

   public Result getResult() {
      return result;
   }

   public void setResult(Result result) {
      this.result = result;
   }

   @Override
   public String toString() {
      return "OrderDTO [orderNum=" + orderNum + ", orderId=" + orderId + ", totalPrice=" + totalPrice + ", indate="
            + indate + ", result=" + result + "]";
   }
}