package b2c_dto;

public class OrderDetailDTO {
   // OrderDetail가 갖는 속성 : cartNum int, orderId var, prodnum int,
   // pname var, price int, quantity int 
   
   private int cartNum; // cartnum
   private String orderId; // 사용자id
   private int prodnum; // 상품번호
   private String pname; // 상품이름
   private int price; // 상품가격
   private int quantity; // 상품양
   
   public OrderDetailDTO(int cartNum, String orderId,
         int prodnum, String pname, int price, int quantity) {
      this.cartNum = cartNum;
      this.orderId = orderId;
      this.prodnum = prodnum;
      this.pname = pname;
      this.price = price;
      this.quantity = quantity;
      
   }

   public int getCartNum() {
      return cartNum;
   }

   public void setCartNum(int cartNum) {
      this.cartNum = cartNum;
   }

   public String getOrderId() {
      return orderId;
   }

   public void setOrderId(String orderId) {
      this.orderId = orderId;
   }

   public int getProdnum() {
      return prodnum;
   }

   public void setProdnum(int prodnum) {
      this.prodnum = prodnum;
   }

   public String getPname() {
      return pname;
   }

   public void setPname(String pname) {
      this.pname = pname;
   }

   public int getPrice() {
      return price;
   }

   public void setPrice(int price) {
      this.price = price;
   }

   public int getQuantity() {
      return quantity;
   }

   public void setQuantity(int quantity) {
      this.quantity = quantity;
   }

   @Override
   public String toString() {
      return "OrderDetailDTO [cartNum=" + cartNum + ", orderId=" + orderId + ", prodnum=" + prodnum + ", pname="
            + pname + ", price=" + price + ", quantity=" + quantity + "]";
   }
   
}