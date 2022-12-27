package b2c_dto;



public class UserDTO {
  // user가 갖는 속성 : id, pw, nickname, name, phonenumber, ssn, address, business_number, user_type(enum "C" or "S")

  public enum UserType{C, S} //enum : 열거형, 상수를 정의하는데 사용되는 데이터 타입

  private String id;
  private String pw;
  private String nickname;
  private String name;
  private String phonenumber;
  private String ssn;
  private String address;
  private String business_number; 
  private UserType userType;  //enum타입의 userType변수 선언
  
  public UserDTO() {
    this.userType = UserType.C; //default userType is C
  }
  public UserDTO(String id, String pw, String nickname, String name, String phonenumber, String ssn, String address,
      String business_number, String label) {
    this.id = id;
    this.pw = pw;
    this.nickname = nickname;
    this.name = name;
    this.phonenumber = phonenumber;
    this.ssn = ssn;
    this.address = address;
    this.business_number = business_number;

    // 생성자에서 String타입의 label을 받아서, enum타입의 userType변수에 대입
       //UserType의 default값은 C로, label이 S이면 userType을 S로 바꿔준다.
    switch(label) {
      case "C":
        this.userType = UserType.C;
        break;
      case "S":
        this.userType = UserType.S;
        break;
      default:
        this.userType = UserType.C;
        break;
    }
    //this.userType = UserType.valueOf(label); //UserType.valueOf() :: String을 enum으로 변환
  }

  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }

  public String getPw() {
    return pw;
  }

  public void setPw(String pw) {
    this.pw = pw;
  }

  public String getNickname() {
    return nickname;
  }

  public void setNickname(String nickname) {
    this.nickname = nickname;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getPhonenumber() {
    return phonenumber;
  }

  public void setPhonenumber(String phonenumber) {
    this.phonenumber = phonenumber;
  }

  public String getSSN() {
    return ssn;
  }

  public void setSSN(String ssn) {
    this.ssn = ssn;
  }

  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }

  public String getBusiness_number() {
    return business_number;
  }

  public void setBusiness_number(String business_number) {
    this.business_number = business_number;
  }

  public String getSsn() {
    return ssn;
  }

  public void setSsn(String ssn) {
    this.ssn = ssn;
  }

  public UserType getUserType() {
    return userType;
  }

  public void setUserType(UserType userType) {
    this.userType = userType;
  }

  @Override
  public String toString() {
    return "UserDTO [id=" + id + ", pw=" + pw + ", nickname=" + nickname + ", name=" + name + ", phonenumber="
        + phonenumber + ", ssn=" + ssn + ", address=" + address + ", business_number=" + business_number + ", userType="
        + userType + "]";
  }
}
