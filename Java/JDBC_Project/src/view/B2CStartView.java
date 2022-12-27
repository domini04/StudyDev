package view;

import b2c_dto.UserDTO;
import controller.B2CController;

public class B2CStartView {

	public static void main(String[] args) {
		B2CController controller = B2CController.getInstance();
		
		System.out.println("====================모든 User 검색====================");
		controller.getAllUsers();

		System.out.println("====================User 검색====================");
		controller.getUser("user1");

//		System.out.println("====================User 추가====================");
//		controller.insertUser(new UserDTO("user3", "1234", "user1", "user1", "010-1111-1111", "123456-1234567", "서울시 강남구", "123-45-67890", "C"));
	
		System.out.println("====================User 수정====================");
		controller.updateUser(new UserDTO("user2", "1234", "밍키", "최민기", "010-1111-1111", "123456-1234567", "서울시 강남구", "123-45-67890", "C"));

		System.out.println("====================User 삭제====================");
		controller.deleteUser("user3");

		System.out.println("====================모든 User 검색====================");
		controller.getAllUsers();
	}


}
