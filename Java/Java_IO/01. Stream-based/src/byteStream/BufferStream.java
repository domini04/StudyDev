package byteStream;

import java.io.*;

public class BufferStream {
  // FileInput/OutputStream을 사용할 때, 파일을 읽고 쓰는 속도가 느리다
  // 이를 해결하기 위해 BufferedInputStream/BufferedOutputStream을 사용한다
  FileInputStream fis = null;
  FileOutputStream fos = null;
  BufferedInputStream bis = null;
  BufferedOutputStream bos = null;
  // 인스턴스 생성시 filename이라는 변수를 받아서 파일을 IO할때 활용
  private String filename;
  public BufferStream(String filename) {
    this.filename = filename;
  }
  // String을 입력받아서 filename이라는 파일에 저장하는 메소드
  public void write(String str) {
    try {
      fos = new FileOutputStream(filename + ".txt"); // 파일을 쓰기위한 스트림 생성
      bos = new BufferedOutputStream(fos); // 파일을 쓰기위한 스트림 생성
      bos.write(str.getBytes()); // 파일에 str을 바이트로 변환하여 쓰기
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      try {
        bos.close(); // 스트림 닫기
      } catch (Exception e) {
        e.printStackTrace();
      }
    }
  }
  // filename이라는 파일을 읽어서 String으로 반환하는 메소드
  public String read() {
    String str = "";
    try {
      fis = new FileInputStream(filename + ".txt"); // 파일을 읽기위한 스트림 생성
      bis = new BufferedInputStream(fis); // 파일을 읽기위한 스트림 생성
      byte[] b = new byte[1024]; // 파일을 읽어올 바이트 배열 생성  (1024byte = 1kb)
      int len = 0; // 파일을 읽어올 길이
      while ((len = bis.read(b)) != -1) { // 파일을 읽어올 길이가 -1이 아닐때까지 반복
        str += new String(b, 0, len); // 파일을 읽어온 바이트를 String으로 변환하여 str에 저장
      }
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      try {
        bis.close(); // 스트림 닫기
      } catch (Exception e) {
        e.printStackTrace();
      }
    }
    return str;
  }
}
