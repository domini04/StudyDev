# I/O

### 개요

![Untitled](I%20O%20eca046025595456fb2d8a927c3f806b0/Untitled.png)

- [https://terianp.tistory.com/19](https://terianp.tistory.com/19)
- **주요 개념**
    - **Stream & Buffer**
    - **InputStream & OutputStream**
    - **Byte Stream & char Stream**
- **Stream**
    - **데이터를 byte 형태로 운반**하는데 사용되는 연결통로
    - **단방향 통신**
    - **Queue**의 구조를 가짐(**FIFO)**
    - 입출력을 위해선 input & output stream 두개가 필요
    
    ![Untitled](I%20O%20eca046025595456fb2d8a927c3f806b0/Untitled%201.png)
    
    - **데이터의 흐름**
        - **Source → input Stream → (File) → Output Stream → Java System(Sink)**
- **Buffer Stream**
    
    ![Untitled](I%20O%20eca046025595456fb2d8a927c3f806b0/Untitled%202.png)
    

### **ByteStream**

*파일을 거친다고 가정*

- **Write**
    1. **FileOutputStream** 인스턴스(**fos**) 생성
        - 생성시 **파일이름** 지정
    2. fos의 메소드를 통해 원하는 데이터를 파일에 write
        - **데이터를 byte로 변환**하여 write
    3. 에러처리 해주기
        - FileNotFoundException
        - IOException
    4. 사용한 자원 반납
        - **.close()**를 통해 열린 스트림 닫기
- **Read**
    1. **FileInputStream** 인스턴스(**fis**) 생성
        - 생성시 읽어올 파일 지정
    2. 데이터를 읽어오기
        - byte형태의 **데이터를 저장할 매개변수** 사용하여, Byte단위로 최종 리턴값append
    3. 에러처리 해주기
        - FileNotFoundException
        - IOException
- **CharStream**
    - **String을 Char단위별 Byte로 자동으로 변환**해주는 프로세스 추가
    - **FileReader, FileWriter**를 사용

### Buffer

- **Buffer**
    - **입/출력 에 대한 임시 저장공간**(8192Byte 배열)
    - 입력받은 값이 버퍼에 저장되었다가, **일정 조건**이 만족되면 버퍼의 내용이 전송됨
- **Buffer 전송 조건**
    - Buffer가 가득 차거나
    - **newline**(개행문자)가 나타나면 버퍼의 값이 전송되면서 비워짐
- **장점**
    - **속도가 빠름**
        - 하나의 Byte단위로 I/O하지 않고, 모아서 한꺼번에 하므로 빠름

### Buffered Stream

- **사용법**
    - 기존의 Input & Output Stream에 **Buffered Reader & Buffered Writer을 덧씌워서 사용**
    
    ```java
    public void write(String str) {
        try {
          fos = new FileOutputStream(filename + ".txt"); // 파일을 쓰기위한 스트림 생성
          **bos = new BufferedOutputStream(fos);** // 파일을 쓰기위한 스트림 생성
    ****      **bos.write(str.getBytes());** // 파일에 str을 바이트로 변환하여 쓰기
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
    ```