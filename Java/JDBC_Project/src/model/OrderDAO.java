package model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;

import b2c_dto.OrderDTO;
import b2c_dto.ProductDTO;
import dbutil.DBUtil;

public class OrderDAO {
	//DAO : DB와 연동해 데이터를 입력, 수정, 삭제 등을 수행하는 클래스. 여기서 본격적인 SQL 쿼리가 수행됨.
		// Insert, Update, Delete methods ...
		
		//I. 새로운 Order를 DB에 추가하는 메소드
		  public static boolean insertOrder(OrderDTO order) throws SQLException {

		    Connection con = null; // Connection :: DB와 JAVA를 연결시켜주는 역할을 하는 객체이다.
		    PreparedStatement pstmt = null; // PreparedStatement :: SQL문을 실행할 때 실행을 위한 SQL을 DB에 전달하는 역할을 수행하는 객체다.
		     
		    //  order가 갖는 속성 : ordernum, order_id, total_price, indate, result
        try {
          con = DBUtil.getConnection(); // DBUtil.getConnection() :: DB와 연결시켜주는 메소드
          pstmt = con.prepareStatement("INSERT INTO orders VALUES(?, ?, ?, ?, ?)"); // SQL문을 실행할 때 실행을 위한 SQL을 DB에 전달하는 역할을 수행하는 객체다.

          pstmt.setInt(1, order.getOrderNum()); // 1번째 ?에 orderNum을 넣는다.
          pstmt.setString(2, order.getOrderId()); // 2번째 ?에 orderId를 넣는다.
          pstmt.setInt(3, order.getTotalPrice()); // 3번째 ?에 totalPrice를 넣는다.
          pstmt.setString(4, order.getIndate().toString()); // 4번째 ?에 indate를 넣는다.  indate는 LocalDate 타입이므로 toString()을 이용해 String으로 변환한다.
          pstmt.setInt(5, order.getResult().getNum()); // 5번째 ?에 result를 넣는다.  result는 enum 타입이므로 getNum()을 이용해 int로 변환한다.

          if (pstmt.executeUpdate() == 1) { // executeUpdate() :: SQL문을 실행시키는 메소드. 1이 반환되면 성공, 0이 반환되면 실패
            return true;
          } else {
            return false;
          }
        } finally {
          DBUtil.close(con, pstmt); // DBUtil.close() :: DB와 연결을 끊는 메소드
        } 
		  }
}
