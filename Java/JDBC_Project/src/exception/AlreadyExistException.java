package exception;

public class AlreadyExistException extends Exception{

  public AlreadyExistException(String message) {
    super(message);
  }

  public AlreadyExistException() {
    super("이미 존재하는 정보입니다.");
  }
}
