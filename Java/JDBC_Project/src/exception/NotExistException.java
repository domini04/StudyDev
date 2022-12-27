package exception;

public class NotExistException extends Exception {

  public NotExistException(String message) {
    super(message); // super()를 통해 Exception 클래스의 생성자를 호출하고, 매개변수로 message를 넘겨준다.
                                                    //Exception클래스는 String을 매개변수로 받을 경우 해당 String을 에러메세지로 출력한다.
  }  
  public NotExistException() {
    super("해당하는 정보가 존재하지 않습니다."); //String을 매개변수로 받지 않는 경우, 기본적으로 "해당하는 정보가 존재하지 않습니다."를 출력한다.
  }
}
