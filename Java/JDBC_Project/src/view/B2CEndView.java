package view;

import java.util.ArrayList;

import b2c_dto.UserDTO;

public class B2CEndView {

	public static void main(String[] args) {

	}

  public static void printAllUsers(ArrayList<UserDTO> list) {
		for (UserDTO user : list) {
			System.out.println(user);
		}
  }

	public static void printUser(UserDTO user) {
		System.out.println(user);
	}

	public static void printMessage(String string) {
		System.out.println(string);
	}

  public static void printError(String string) {
		System.out.println("작업이 실패하였습니다. (꒪⌓꒪)");
		System.out.println(string);
  }

  public static void printSuccess(String string) {
		System.out.println("작업이 성공적으로 완료되었습니다.  (๑•̀ㅂ•́)و✧");
		System.out.println(string);
  }

}
