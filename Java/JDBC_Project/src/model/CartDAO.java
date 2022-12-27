package model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import b2c_dto.CartDTO;
import dbutil.DBUtil;

public class CartDAO {
//DAO : DB와 연동해 데이터를 입력, 수정, 삭제 등을 수행하는 클래스. 여기서 본격적인 SQL 쿼리가 수행됨.
	// Insert, Update, Delete methods ...
	
	//I. 새로운 User를 DB에 추가하는 메소드
	  public static boolean insertProduct(CartDTO cart) throws SQLException {

	    Connection con = null; // Connection :: DB와 JAVA를 연결시켜주는 역할을 하는 객체이다.
	    PreparedStatement pstmt = null; // PreparedStatement :: SQL문을 실행할 때 실행을 위한 SQL을 DB에 전달하는 역할을 수행하는 객체다.
	      
	     
	    //order_id, prodnum, pname, price, quantity
	    try {

	      //1. DB 연결
	      con = DBUtil.getConnection();
	      pstmt = con.prepareStatement("INSERT INTO cart (order_id, prodnum,  pname, price, quantity) VALUES(?, ?, ?, ?, ?)"); // '?'는 아직 값이 정해지지 않은 SQL문의 변수를 의미한다.

	      //2. SQL Query 완성
	        // .setString()을 사용하여 각각의 ?위치에 값을 String으로 입력한다. (index, value)순서
	      pstmt.setString(1, cart.getuId());
	      pstmt.setInt(2, cart.getProdnum());
	      pstmt.setString(3, cart.getPname());
	      pstmt.setInt(4, cart.getPrice());
	      pstmt.setInt(5, cart.getQuantity());
	      
	      
	      
	      //3. Query 실행
	      int result = pstmt.executeUpdate(); //.executeUpdate() :: Compile된 DML문을 실행시킴. 성공적으로 수행된 경우 1, 실패한 경우 0 을 반환한다.
	      if (result == 1) {
	        return true;
	      } 
	    } finally {
	      DBUtil.close(con, pstmt); //DB connection 종료
	    } return false;
	  }
	// II. Cart 테이블의 CartDTO를 검색하는 메소드
	public static boolean searchCart(CartDTO cart) throws SQLException {
		Connection con = null;
		PreparedStatement pstmt = null;
		
		try {
			con = DBUtil.getConnection();
			pstmt = con.prepareStatement("SELECT * FROM cart WHERE cartNum = ?");
			pstmt.setInt(1, cart.getCartNum());
			
			int result = pstmt.executeUpdate();
			if(result == 1) {
				return true;
			}
		} finally {
			DBUtil.close(con, pstmt);
		} return false;
	}
		
}
