package Stream;
public class transactions {
  int id;
  String type;

  public transactions(int id, String type) {
    this.id = id;
    this.type = type;
  }
  //getter,setter for id, type:
  public int getId() {
    return id;
  }
  public void setId(int id) {
    this.id = id;
  }
  public String getType() {
    return type;
  }
  public void setType(String type) {
    this.type = type;
  }
  //toString method for id, type:
  @Override
  public String toString() {
    return "transactions [id=" + id + ", type=" + type + "]";
  }

}
