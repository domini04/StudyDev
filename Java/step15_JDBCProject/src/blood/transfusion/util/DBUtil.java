package blood.transfusion.util;

import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

public class DBUtil { //DB 접속, 해제, 쿼리 실행 등의 기본기능을 지원하는 클래스
	// DB 설정
	static Properties propertiesInfo = new Properties();	//Properties : DB 설정 정보를 저장할 객체
	static {
		try {
			propertiesInfo.load( new FileInputStream("db.properties") ); //db.properties 파일을 읽어서 propertiesInfo에 저장
			Class.forName(propertiesInfo.getProperty("jdbc.driver"));	//jdbc.driver에 저장된 클래스를 로드
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static Connection getConnection() throws SQLException { //getConnection() : DB 접속 메소드
		return DriverManager.getConnection(propertiesInfo.getProperty("jdbc.url"), //jdbc.url에 저장된 DB 접속 정보를 이용하여 DB 접속
											propertiesInfo.getProperty("jdbc.id"), // jdbc.id에 저장된 DB 접속 정보를 이용하여 DB 접속
											propertiesInfo.getProperty("jdbc.pw")); // jdbc.pw에 저장된 DB 접속 정보를 이용하여 DB 접속
	}

	// 자원반환
	public static void close(Connection con, Statement stmt, ResultSet rset) {
		try {
			if (rset != null) {
				rset.close();
				rset = null;
			}
			if (stmt != null) {
				stmt.close();
				stmt = null;
			}
			if (con != null) {
				con.close();
				con = null;
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	// 자원반환
	public static void close(Connection con, Statement stmt) { //close() 메소드 오버로딩 -> argument가 2개인 close() 메소드 가능하도록
		try {
			if (stmt != null) {
				stmt.close();
				stmt = null;
			}
			if (con != null) {
				con.close();
				con = null;
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
