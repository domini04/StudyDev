package Web.JSP.JSP_MVC_Project.src.guestbook.model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import util.DBUtil;

public class GuestBookDAO {
	
	// 게시물 등록
	public static boolean writeContent(GuestBookBean vo) throws SQLException{
		Connection con = null;	
		PreparedStatement pstmt = null;
		boolean result = false;
		
		try {
			con = DBUtil.getConnection();
			//gbook table에 num, title, author, email, content, password를 입력. 이 때 num은 auto_increment이므로 입력하지 않음.
				//writeday는 현재 시간이므로 now()를 입력.
				//readnum은 조회 수이므로 0을 입력.
			System.out.println("테스트용. 실행됨"); //여기까지 안감
			pstmt = con.prepareStatement("Insert Into gbook (title, author, email, content, password, writeday, readnum) Values (?,?,?,?,?, now(), 0)");

	        pstmt.setString(1, vo.getTitle());
	        pstmt.setString(2, vo.getAuthor());
	        pstmt.setString(3, vo.getEmail());
	        pstmt.setString(4, vo.getContent());
	        pstmt.setString(5, vo.getPassword());
	        
			int count = pstmt.executeUpdate();			
			if(count != 0){
				result = true;
			}
		}finally{
			DBUtil.close(con, pstmt);
		}
		return result;		
	}
	
	// 게시물 조회 - boolean flag 값 = read인 경우 true, update인 경우  false
	public static GuestBookBean getContent(int  num, boolean flag) throws SQLException{		
		Connection con = null;	
		PreparedStatement pstmt = null;
		ResultSet rset = null;
		GuestBookBean vo  = null;
		//flag가 true인 경우 
				
			//sql1 : num에 해당하는 게시물을 찾아 readnum을 1 증가시킴. read(flag=true)인 경우만 조회수 증가.
			//sql2 : num에 해당하는 게시물을 조회. read & update 두 경우 모두 수행되므로 if문 밖에 위치.
		String sql1="Update gbook Set readnum=readnum+1 Where num=?";	
		String sql2="Select * From gbook Where num=?";

		try {
			con = DBUtil.getConnection();
			if(flag){
				//1. 먼저 read할꺼니까 조회수를 1 증가시킴.
				pstmt = con.prepareStatement(sql1);
				pstmt.setInt(1, num);
				int count = pstmt.executeUpdate();
				if(count == 0){
					return vo;
				}
			}
			
			//2. gbook에서 num에 해당하는 게시물을 검색해서 rset -> vo에 저장.
			pstmt = con.prepareStatement(sql2);
			pstmt.setInt(1, num);	
			rset = pstmt.executeQuery();
			System.out.println("read : 여기까진 실행됨");
			if(rset.next()){
				vo = new GuestBookBean();
				vo.setNum(rset.getInt("num"));
				vo.setTitle(rset.getString("title"));
				vo.setAuthor(rset.getString("author"));
				vo.setEmail(rset.getString("email"));
				vo.setContent(rset.getString("content"));
				vo.setPassword(rset.getString("password"));
				vo.setWriteday(rset.getString("writeday"));
				vo.setReadnum(rset.getInt("readnum"));
				// vo = new GuestBookBean(num,rset.getString(1),
				// 		rset.getString(2),rset.getString(3),rset.getString(4).replaceAll("</n>","<br>"),
				// 		rset.getString(5),rset.getString(6),rset.getInt(7));
				System.out.println("read : vo 객체가 존재함");
			}
		}finally{
			DBUtil.close(con, pstmt);
		}
		return vo;
	}
	
	//게시물 삭제
	public  static boolean deleteContent(int num, String password) throws SQLException{
		Connection con = null;	
		PreparedStatement pstmt = null;
		boolean result = false;
		
		String sql = "Delete From gbook Where num=? And password=?";
		
		try {
			con = DBUtil.getConnection();

			pstmt = con.prepareStatement(sql);

			pstmt.setInt(1,num);
	        pstmt.setString(2,password);

			int count = pstmt.executeUpdate();
			
			if(count != 0){
				result = true;
			}
		}finally{
			DBUtil.close(con, pstmt);
		}
		return result;
	}
	
	// 게시물 수정
	public  static boolean updateContent(GuestBookBean vo) throws SQLException{
		Connection con = null;	
		PreparedStatement pstmt = null;
		boolean result = false;
		
		try {
			con = DBUtil.getConnection();
			//num으로 검색해서 password가 일치하면 수정.
			pstmt = con.prepareStatement("update gbook set title=?, author=?, email=?, content=? where num=? and password=?");
			pstmt.setString(1,vo.getTitle());
		    pstmt.setString(2,vo.getAuthor());
		    pstmt.setString(3, vo.getEmail());
		    pstmt.setString(4, vo.getContent());
		    pstmt.setInt(5, vo.getNum());
		    pstmt.setString(6, vo.getPassword());

			int count = pstmt.executeUpdate();
			
			if(count != 0){
				result = true;
			}
		}finally{
			DBUtil.close(con, pstmt);
		}
		return result;
	}
	
	// 모든 게시물 조회
	public  static ArrayList<GuestBookBean> getAllContents() throws SQLException{
		Connection con = null;	
		PreparedStatement pstmt = null;
		ResultSet rset = null;
		ArrayList<GuestBookBean> alist = null;
		String sql="";	
		try {
			con = DBUtil.getConnection();
			pstmt = con.prepareStatement("select * from gbook order by num asc");
			rset = pstmt.executeQuery();
			alist = new ArrayList<GuestBookBean>();
			while(rset.next()){
				alist.add(new GuestBookBean(rset.getInt(1),rset.getString(2),
						rset.getString(3),rset.getString(4),rset.getString(5)
		 				,rset.getString(6),rset.getString(7),rset.getInt(8)));
			}
		}finally{
			DBUtil.close(con, pstmt, rset);
		}
		return alist;
	}
}
