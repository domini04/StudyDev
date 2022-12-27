package model;

import dbutil.DBUtil;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import b2c_dto.UserDTO;


public class UserDAO { //DAO : DB와 연동해 데이터를 입력, 수정, 삭제 등을 수행하는 클래스. 여기서 본격적인 SQL 쿼리가 수행됨.
  // Insert, Update, Delete methods ...

  //I. 새로운 User를 DB에 추가하는 메소드
  public static boolean insertUser(UserDTO user) throws SQLException {

    Connection con = null; // Connection :: DB와 JAVA를 연결시켜주는 역할을 하는 객체이다.
    PreparedStatement pstmt = null; // PreparedStatement :: SQL문을 실행할 때 실행을 위한 SQL을 DB에 전달하는 역할을 수행하는 객체다.
      
     
        //user가 갖는 속성 : id, pw, nickname, name, phonenumber, ssn, address, business_number, user_type(enum "C" or "S")
    try {

      //1. DB 연결
      con = DBUtil.getConnection();
      pstmt = con.prepareStatement("INSERT INTO user VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"); // '?'는 아직 값이 정해지지 않은 SQL문의 변수를 의미한다.


      //2. SQL Query 완성
        // .setString()을 사용하여 각각의 ?위치에 값을 String으로 입력한다. (index, value)순서
        // id, pw, nickname, name, phonenumber, ssn, address, business_number, user_type(enum "C" or "S") 순서로 입력한다.
      pstmt.setString(1, user.getId());
      pstmt.setString(2, user.getPw());
      pstmt.setString(3, user.getNickname());
      pstmt.setString(4, user.getName());
      pstmt.setString(5, user.getPhonenumber());
      pstmt.setString(6, user.getSsn());
      pstmt.setString(7, user.getAddress());
      pstmt.setString(8, user.getBusiness_number());
      pstmt.setString(9, user.getUserType().toString());
      
      //3. Query 실행
      int result = pstmt.executeUpdate(); //.executeUpdate() :: Compile된 DML문을 실행시킴. 성공적으로 수행된 경우 1, 실패한 경우 0 을 반환한다.
      if (result != 1) {
        return true;
      }  else {
        return false;
      }
      }
    finally {
      DBUtil.close(con, pstmt); //DB connection 종료
    } 
  }


  //II. DB에 있는 User를 삭제하는 메소드
  public static boolean deleteUser(String uid) throws SQLException {
    Connection con = null;
    PreparedStatement pstmt = null;
    try {
      con = DBUtil.getConnection();
      pstmt = con.prepareStatement("DELETE FROM user WHERE id = ?");
      pstmt.setString(1, uid);
      int result = pstmt.executeUpdate();
      if (result != 1) {
        return true;
      } else {
        return false;
      }
    } finally {
      DBUtil.close(con, pstmt);
    }
  }

  //III. User 테이블의 모든 정보를 가져오는 메소드
  public static ArrayList<UserDTO> getAllUsers() throws SQLException {
    Connection con = null;
    PreparedStatement pstmt = null;
    ResultSet rs = null;  //ResultSet :: select 문을 실행했을 경우 데이터베이스에서 결과를 받아와 저장하는 객체이다.
    ArrayList<UserDTO> list = new ArrayList<UserDTO>(); //반환할 모든 Seller객체 정보를 담을 ArrayList 생성
    try {
      con = DBUtil.getConnection();
      pstmt = con.prepareStatement("SELECT * FROM user");
      rs = pstmt.executeQuery();
      while (rs.next()) { // .next() : 수행결과로 ResultSet객체에서 하나의 Row를 반환한다. 더이상 결과가 없을 경우 false를 반환하면서 리턴
                          // next()메소드를 한번 호출할때마다 한개의 레코드를 아이템으로 가진 객체를 반환한다.

        UserDTO user = new UserDTO(
            rs.getString("id"), //ResultSet에서 getString()을 사용하여 각각의 컬럼의 값을 가져온다.
            rs.getString("pw"),
            rs.getString("nickname"),
            rs.getString("name"),
            rs.getString("phonenumber"),
            rs.getString("ssn"),
            rs.getString("address"),
            rs.getString("business_number"),
            rs.getString("user_type")
        );
        list.add(user); //각 User객체를 ArrayList에 추가
      }
    } finally {
      DBUtil.close(con, pstmt, rs);
    } return list;
  }

  // IV. DB에 있는 User를 검색하는 메소드
  public static UserDTO getUser(String uid) throws SQLException {
    Connection con = null;
    PreparedStatement pstmt = null;
    ResultSet rs = null;
    try {
      con = DBUtil.getConnection();
      pstmt = con.prepareStatement("SELECT * FROM user WHERE id = ?");
      pstmt.setString(1, uid);
      rs = pstmt.executeQuery();
      if (rs.next()) {
        UserDTO user = new UserDTO(
            rs.getString("id"),
            rs.getString("pw"),
            rs.getString("nickname"),
            rs.getString("name"),
            rs.getString("phonenumber"),
            rs.getString("ssn"),
            rs.getString("address"),
            rs.getString("business_number"),
            rs.getString("user_type")
        );
        return user;
      }
    } finally {
      DBUtil.close(con, pstmt, rs);
    } return null;
  }
  
  // V. DB에 있는 User를 수정하는 메소드
    // 수정할 User의 id를 받아와서 해당 User의 정보를 수정한다.
  public static boolean updateUser(UserDTO user) throws SQLException {
    String uid = user.getId();
    Connection con = null;
    PreparedStatement pstmt = null;

    try {
      con = DBUtil.getConnection();
      pstmt = con.prepareStatement("UPDATE user SET pw = ?, nickname = ?, name = ?, phonenumber = ?, ssn = ?, address = ?, business_number = ?, user_type = ? WHERE id = ?");
      pstmt.setString(1, user.getPw());
      pstmt.setString(2, user.getNickname());
      pstmt.setString(3, user.getName());
      pstmt.setString(4, user.getPhonenumber());
      pstmt.setString(5, user.getSsn());
      pstmt.setString(6, user.getAddress());
      pstmt.setString(7, user.getBusiness_number());
      pstmt.setString(8, user.getUserType().toString());
      pstmt.setString(9, uid);
      int result = pstmt.executeUpdate();
      if (result != 1) {
        return true;
      }
    } finally {
      DBUtil.close(con, pstmt);
    } return false;
  }
}

