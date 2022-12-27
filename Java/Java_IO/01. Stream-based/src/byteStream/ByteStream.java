package byteStream;

import java.io.FileInputStream;
import java.io.FileOutputStream;



public class ByteStream {
  //인스턴스 생성시 filename이라는 변수를 받아서 파일을 IO할때 활용
  private String filename;
  public ByteStream(String filename) {
    this.filename = filename;
  }
  //String을 입력받아서 filename이라는 파일에 저장하는 메소드
  public void write(String str) {
    FileOutputStream fos = null; //파일을 쓰기위한 스트림 초기화
    try {
      fos = new FileOutputStream(filename + ".txt"); //파일을 쓰기위한 스트림 생성
      fos.write(str.getBytes()); //파일에 str을 바이트로 변환하여 쓰기
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      try {
        fos.close(); //스트림 닫기
      } catch (Exception e) {
        e.printStackTrace();
      }
    }
  } 
  //filename.txt라는 파일을 읽어서 String으로 반환하는 메소드
  public String read() {
    FileInputStream fis = null; //파일을 읽기위한 스트림 초기화
    String str = "";
    try {
      fis = new FileInputStream(filename + ".txt"); //파일을 읽기위한 스트림 생성
      int data = 0; //읽어온 데이터를 저장할 변수
      while ((data = fis.read()) != -1) { //파일을 읽어서 data에 저장. 파일의 끝이면 -1을 반환
        str += (char) data; //data를 char로 변환하여 str에 저장
      } return str;
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      try {
        fis.close(); //스트림 닫기
      } catch (Exception e) {
        e.printStackTrace();
      } 
    }
	return null;
  }
}
