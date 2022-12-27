package b2c_dto;

import java.sql.Date;

public class ProductDTO {
   //product가 갖는 속성 : prodNum int, pname var, kind var,
   //price int, content var, useyn var, regdate date
   
   public enum UseYN{Y,N}
   
   private int prodNum; // 상품 등록시 자동 ++
   private String pname; // 상품 이름
   private String kind; // 상품 종류
   private int price; // 상품 종류
   private String content; // 상품 설명
   private UseYN useyn; // 상품 재고 유무
   private Date regdate; // 상품 등록 날짜
   
   public ProductDTO() {};
   
   public ProductDTO(String pname, String kind, int price, String content,String label) {
      this.pname = pname;
      this.kind = kind;
      this.price = price;
      this.content = content;
      
      switch(label) {
         case "Y":
           this.useyn = UseYN.Y;
           break;
         case "N":
           this.useyn = UseYN.N;
           break;
         default:
           this.useyn = UseYN.Y;
           break;
       }
   }

   public int getProdNum() {
      return prodNum;
   }

   public void setProdNum(int prodNum) {
      this.prodNum = prodNum;
   }

   public String getPname() {
      return pname;
   }

   public void setPname(String pname) {
      this.pname = pname;
   }

   public String getKind() {
      return kind;
   }

   public void setKind(String kind) {
      this.kind = kind;
   }

   public int getPrice() {
      return price;
   }

   public void setPrice(int price) {
      this.price = price;
   }

   public String getContent() {
      return content;
   }

   public void setContent(String content) {
      this.content = content;
   }

   public UseYN getUseyn() {
      return useyn;
   }

   public void setUseyn(UseYN useyn) {
      this.useyn = useyn;
   }

   public Date getRegdate() {
      return regdate;
   }

   public void setRegdate(Date regdate) {
      this.regdate = regdate;
   }

   @Override
   public String toString() {
      return "ProductDTO [prodNum = " + prodNum + ", 상품이름 = " + pname + ", 상품종류 = " + kind + ", 금액 = " + price
            + ", 상품 설명 = " + content + ", 주문 가능 여부 = " + useyn + ", 상품 등록 날짜 = " + regdate + " ]";
   }
   
   
   
   
}