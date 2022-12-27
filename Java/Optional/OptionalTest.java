import java.util.Optional; 

public class OptionalTest {

	public static void main(String[] args) {
		// Optional
			// empty() : 빈 Optional 객체 생성
		Optional<String> opt1 = Optional.empty();
		System.out.println(opt1);
		
			// of(value / null) : null이 아닌 데이터 생성 /NPE 발생.null값 못받음
		Optional<String> opt2 = Optional.of("Java");
		System.out.println(opt2);
		System.out.println(opt2.get());
		
			//ofNullable(value / null) : null값 받을 수 있음. null값 받으면 비어 있는 Optional객체 생성됨 
		Optional<String> opt3 = Optional.ofNullable(null);
		System.out.println(opt3); //Optional.empty로 출력됨
//		System.out.println(opt3.get()); //null을 가져오려고 하기에 에러. 다만 NPE가 아닌 NSE에러가 발생
		
			//ifPresent() : Optional안에 데이터가 있는 경우에만 반환
		opt3.ifPresent(v -> System.out.println(v));
		Optional<String> opt4 = Optional.ofNullable("Java");
		opt4.ifPresent(v -> System.out.println(v));
		
			//orElse() : Optional객체가  비어있는 경우 대신 지정값을 반환
		System.out.println(opt3.orElse("대신 출력"));
		System.out.println(opt4.orElse("대신 출력"));
	
	
			//orElseThrow() : paramter를 Exception 객체로 받음. 만약 null이 아닌 경우 해당 보유 객채값을 반환하고, null이면 지정된 Exception을 일으킴/ 
		try {
		System.out.println(opt3.orElseThrow(IllegalArgumentException::new));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
