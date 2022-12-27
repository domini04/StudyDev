package model;

import java.sql.SQLException;
import java.util.ArrayList;

import b2c_dto.UserDTO;
import b2c_dto.OrderDTO;
import exception.NotExistException;
import exception.AlreadyExistException;


public class B2CService {

	// B2CService를 싱글톤으로 구현하기 위한 코드
	private static B2CService instance = new B2CService(); 
	private B2CService() {}
	public static B2CService getInstance() {
		return instance;
	}

	//CRUD

	//에러처리를 위한 메소드
		//1.User가 존재하지 않을 경우
	public  void notExistUser(String uid) throws SQLException, NotExistException {
		//DB에서 uid와 일치하는 user를 가져온다. 해당하는 user가 없으면 NotExistException을 발생시킨다.
		UserDTO user = UserDAO.getUser(uid); 
		if(user == null) {
			throw new NotExistException("존재하지 않는 사용자입니다.  Σ(っ °Д °;)っ");
		}
	}
	//2.User가 이미 존재하는 경우
	public  void alreadyExistUser(String uid) throws SQLException, AlreadyExistException { 
		//DB에서 uid를 가진 user가 있는지 확인한다. 있으면 AlreadyExistException을 발생시킨다.
		UserDTO user = UserDAO.getUser(uid);
		if(user != null) {
			throw new AlreadyExistException("이미 존재하는 사용자입니다.  Σ(っ °Д °;)っ");
		}
	}

	// ------------------------				
	// DAO에게 일 시키는 기능 + 일 시키기 전에 에러처리를 합친 메소드들을 Service에 구현

	// I. User 테이블 관련 메소드
	//1. User검색을 위한 메소드.
	public  UserDTO getUser(String uid) throws SQLException, NotExistException {
		notExistUser(uid); // 1. 에러처리
		return UserDAO.getUser(uid); //2.DAO에 일 시키기
	}

	//2. User목록을 가져오는 메소드
	public  ArrayList<UserDTO> getUserList() throws SQLException {
		return UserDAO.getAllUsers();
	}

	//3. User추가를 위한 메소드
	public  boolean insertUser(UserDTO user) throws SQLException, AlreadyExistException {
		alreadyExistUser(user.getId());
		return UserDAO.insertUser(user); //성공적으로 추가되면 true, 실패하면 false 반환
	}

	//4. User삭제를 위한 메소드
	public  boolean deleteUser(String uid) throws SQLException, NotExistException {
		notExistUser(uid); // 1. 에러처리
		return UserDAO.deleteUser(uid); //2.DAO에 일 시키기
	}

	//5. User수정을 위한 메소드
	public  boolean updateUser(UserDTO user) throws SQLException, NotExistException {
		notExistUser(user.getId()); // 1. 에러처리
		return UserDAO.updateUser(user); //2.DAO에 일 시키기
	}

	// II. Order 테이블 관련 메소드

	//1. Order 테이블에 OrderDTO를 insert하는 메소드
		// OrderDTO의 컬림 : orderNum, orderId, totalPrice, indate, label
		// ※주의점 : orderId는 UserDTO의 id를 참조하는 왜래키이므로 UserDTO의 id가 존재하는지 확인해야 한다.
	public  boolean insertOrder(OrderDTO order) throws SQLException, NotExistException {
		//1. 에러처리
		notExistUser(order.getOrderId());
		//2. DAO에 일 시키기
		return OrderDAO.insertOrder(order);
	}
}
