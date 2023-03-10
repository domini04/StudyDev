package Web.JSP.JSP_MVC_Project.src.guestbook.controller;

import java.io.IOException;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import guestbook.model.GuestBookBean;
import guestbook.model.GuestBookDAO;

@WebServlet("/guestbook.do")
public class GuestBookController extends HttpServlet {
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		
		System.out.println("일단 명령은 넘어옴");
		//	
		String command = request.getParameter("command");
		
		// 
		if(command == null){
			command = "list";
		}		
		
		if(command.equals("list")){
			list(request, response);
		}else if(command.equals("write")){
			write(request, response);
		}else if(command.equals("read")){
			read(request, response);
		}else if(command.equals("updateForm")){
			updateForm(request, response);
		}else if(command.equals("update")){
			update(request, response);
		}else if(command.equals("delete")){
			delete(request, response);
		}
	}
	private void delete(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		String strNum=request.getParameter("num");
		String password = request.getParameter("password");
		
		//유효성 검사
		if(strNum == null || strNum.trim().length() == 0 ||
			password == null || password.trim().length() == 0){
			response.sendRedirect("guestbook.do");
			return;				
		}
		//조회 없이 getContent를 사용하기 위한 flag. deleteContent가 성공적으로 실행되면 true로 변경됨.
		boolean result = false;
		try {
			result = GuestBookDAO.deleteContent(Integer.parseInt(strNum),password);
		} catch (SQLException e) {
			e.printStackTrace();
			request.setAttribute("error", "해당 게시글 삭제 실패했습니다. 재 시도 하셔요");
		}
		if(result){
			response.sendRedirect("guestbook.do"); 
			return;
		}else{
			request.setAttribute("error", "삭제하려는 게시글이 존재하지 않습니다"); // deleteContent가 실패하면 해당 게시글이 존재하지 않는다는 메시지를 띄움.
		}
		request.getRequestDispatcher("error.jsp").forward(request, response);
	}
	
	private void update(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String strNum = request.getParameter("num");
		String title = request.getParameter("title");
		String author = request.getParameter("author");				
		String email = request.getParameter("email");				
		String content = request.getParameter("content");
		String password = request.getParameter("password");
		
		// 유효성 검사
		if(strNum == null || strNum.trim().length() == 0 ||
			title == null || title.trim().length() == 0 ||
			author == null || author.trim().length() == 0 ||
			email == null || email.trim().length() == 0 ||
			content == null || content.trim().length() == 0 ||
			password == null || password.trim().length() == 0 ){
				response.sendRedirect("guestbook.do");
				return;
		}
		
		// update로 getContent를 사용하기 위할 flag
		boolean result = false;
		
		try {
			result = GuestBookDAO.updateContent(new GuestBookBean(Integer.parseInt(strNum),title,author,email,content,password));
		} catch (SQLException e) {
			e.printStackTrace();
			request.setAttribute("error", "게시글 수정 실패");
		}
		if(result){
			response.sendRedirect("guestbook.do");
			return;
		}
		request.setAttribute("error", "게시글 수정 실패");
		request.getRequestDispatcher("error.jsp").forward(request, response);
	}

	private void updateForm(HttpServletRequest request, HttpServletResponse response)  throws IOException, ServletException{
		//updateForm : 게시글 수정 폼으로 이동
		String strNum = request.getParameter("num");
		
		//num 검사후 num이 잘못된 값이면 list로 이동
		if(strNum == null || strNum.trim().length() == 0) {
			response.sendRedirect("guestbook.do");
			return;				
		}
		String url = "error.jsp";
		GuestBookBean gContent = null;
		//num이 정상적인 값이면 해당 게시글을 읽어서 update.jsp로 이동
		try {
			gContent = GuestBookDAO.getContent(Integer.parseInt(strNum), false);
		} catch (Exception e) {
			e.printStackTrace();
			request.setAttribute("error", "수정하고자 하는 게시글 검색 실패했습니다");
		}
		if(gContent == null){
			request.setAttribute("error", "수정하고자 하는 게시글이 존재하지 않습니다");
		}else{
			request.setAttribute("resultContent", gContent);
			url = "update.jsp";
		}
		request.getRequestDispatcher(url).forward(request, response);
	}

	private void read(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		String strNum=request.getParameter("num");
		if(strNum==null || strNum.length() == 0){
			response.sendRedirect("guestbook.do");
			return;
		}
		String url = "error.jsp";
		GuestBookBean gContent = null;
		try {
			gContent = GuestBookDAO.getContent(Integer.parseInt(strNum), true); //getContent로 해당 게시글의 내용을 읽어온다.
		} catch (SQLException e) {
			e.printStackTrace();
			request.setAttribute("error", "게시글 읽기 실패");
		}
		if(gContent == null){
			request.setAttribute("error", "해당 게시글이 존재하지 않습니다");
		}else{
			request.setAttribute("resultContent", gContent);	//Content가 존재한다면 resultContent라는 이름으로 request에 저장 -> read.jsp로 보냄
			url = "read.jsp";
		}
		request.getRequestDispatcher(url).forward(request, response);
	}

	private void write(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		String title=request.getParameter("title");
		String author=request.getParameter("author");				
		String email=request.getParameter("email");				
		String content=request.getParameter("content");				
		String password=request.getParameter("password");
		
		//데이터값 입력 유무만 유효성 검증
		if(title == null || title.trim().length() == 0 ||
		author == null || author.trim().length() == 0 ||
		email == null || email.trim().length() == 0 ||
		content == null || content.trim().length() == 0 ||
		password == null || password.trim().length() == 0 ){
			response.sendRedirect("write.html");
			return;//write() 메소드 종료
		}
		
		boolean result = false;
		
		try {
			result = GuestBookDAO.writeContent(new GuestBookBean(title,author,email,content,password));
		} catch (SQLException e) {
			e.printStackTrace();
			request.setAttribute("error", "게시글 저장 시도 실패 재 시도 하세요");
		}
		
		if(result){
			response.sendRedirect("guestbook.do"); 
		}else{
			request.getRequestDispatcher("error.jsp").forward(request, response);
		}
	}

	private void list(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String url = "error.jsp";
		try {
			request.setAttribute("list", GuestBookDAO.getAllContents());
			url = "list.jsp";
		} catch (SQLException e) {
			e.printStackTrace();
			request.setAttribute("error", "모두 보기 실패 재 실행 해 주세요");
		}	
		request.getRequestDispatcher(url).forward(request, response);
	}

}
