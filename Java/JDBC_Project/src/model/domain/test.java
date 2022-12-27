package model.domain;

import b2c_dto.ProductDTO;

public class test {

  public static void main(String[] args) {
    ProductDTO dto = new ProductDTO("sellerId", "pname", 1000, "kind", "content");
    System.out.println(dto);
  }

}
