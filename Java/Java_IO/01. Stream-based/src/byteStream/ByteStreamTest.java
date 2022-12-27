package byteStream;

public class ByteStreamTest {

	public static void main(String[] args) {
	    ByteStream bs = new ByteStream("test");
	    bs.write("Hello World!");
	    System.out.println(bs.read());
	    }
}
