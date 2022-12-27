package controller;

import java.sql.SQLException;
import java.util.ArrayList;

import b2c_dto.UserDTO;
import exception.AlreadyExistException;
import exception.NotExistException;
import model.B2CService;
import view.B2CEndView;

public class B2CController {
	private static B2CController instance = new B2CController();
	private B2CService service = B2CService.getInstance();

	private B2CController() {}
	public static B2CController getInstance() {
		return instance;
	}
		
		//모든 프로젝트 검색
			// 1. Service에 getUserList()를 호출해서 ArrayList<UserDTO>를 받아온다.
			// 2. 받아온 ArrayList<UserDTO>를 EndView에게 넘겨준다.
			// 3. EndView에서는 받아온 ArrayList<UserDTO>를 출력한다.
		public void getAllUsers(){
			try {
			B2CEndView.printAllUsers(service.getUserList());
			B2CEndView.printSuccess("모든 프로젝트 검색 성공! ( ͡° ͜ʖ ͡°)♥");
			} catch (SQLException e) {
				e.printStackTrace();
				B2CEndView.printError("getAllUsers()에서 오류 발생! Σ(っ °Д °;)っ");
			}
		}
		
		//특정 프로젝트 검색
			// 1. Service에 getUser()를 호출해서 UserDTO를 받아온다.
			// 이하 동일
		public void getUser(String id){
			try{
			B2CEndView.printUser(service.getUser(id));
			B2CEndView.printSuccess("특정 프로젝트 검색 성공! ( ͡° ͜ʖ ͡°)♥");
			} catch (SQLException | NotExistException e) {
				e.printStackTrace();
				B2CEndView.printError("getUser()에서 오류 발생! Σ(っ °Д °;)っ");
			}
		}

		//프로젝트 추가
			// 1. Service에 addUser()를 호출해서 추가한다.
			// 2. 추가가 완료되면 EndView에게 알려준다.
			// 3. EndView에서는 추가가 완료되었다는 메시지를 출력한다.
		public void insertUser(UserDTO user) {
			try {
			Boolean b = service.insertUser(user); //작업이 성공적으로 완료되었다면 b == true를 반환함
			if (b) { 
				B2CEndView.printSuccess("프로젝트 추가 성공! ( ͡° ͜ʖ ͡°)♥");
			}
			} catch (SQLException | AlreadyExistException e) {
				B2CEndView.printError(e.getMessage());
			}	
		}
		//프로젝트 삭제
			// 1. Service에 deleteUser()를 호출해서 삭제한다.
			// 2. 삭제가 완료되면 EndView에게 알려준다.
			// 3. EndView에서는 삭제가 완료되었다는 메시지를 출력한다.
		public void deleteUser(String id) {
			try {
			Boolean b = service.deleteUser(id);
			if (b) {
				B2CEndView.printSuccess("프로젝트 삭제 성공! ( ͡° ͜ʖ ͡°)♥");
			} 
			} catch (SQLException | NotExistException e) {
				B2CEndView.printError(e.getMessage());
			}
		}

		//프로젝트 수정
			// 1. Service에 updateUser()를 호출해서 수정한다.
			// 2. 수정이 완료되면 EndView에게 알려준다.
			// 3. EndView에서는 수정이 완료되었다는 메시지를 출력한다.
		public void updateUser(UserDTO user) {
			try {
			Boolean b = service.updateUser(user);
			if (b) {
				B2CEndView.printSuccess("프로젝트 수정 성공! ( ͡° ͜ʖ ͡°)♥");
			}
			} catch (SQLException | NotExistException e) {
				e.printStackTrace();
				B2CEndView.printError(e.getMessage());
				// B2CEndView.printError("updateUser()에서 오류 발생! Σ(っ °Д °;)っ");
			}
		}
		
}


