package Stream;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class stream {
  // Q1. 해당 SQL 쿼리문을 java Stream을 통해 구현해보세요
	// - transactions이란 class에 'id', 'type'등의 정보가 멤버벼수로 들어있음.
	// - id는 int, type은 string
// SELECT id FROM transactions WHERE type = 'GROCERY' ORDER BY value DESC;

  // Q2. 2. 위 쿼리문을 ArrayList로 반환해보세요



//답안.
  public static void main(String[] args) {
    //I. 초기 설정
      // 01. transactions 인스턴스를 생성하고, transactions 값 넣기
    transactions t1 = new transactions(1, "GROCERY");
    transactions t2 = new transactions(2, "GROCERY"); 
    transactions t3 = new transactions(3, "DINING");
    transactions t4 = new transactions(4, "EDUCATION");
    transactions t5 = new transactions(5, "GROCERY");

      // 02. List에 transactions 인스턴스를 넣기
    List<transactions> tList = new ArrayList<>();
    tList.add(t1);
    tList.add(t2);
    tList.add(t3);
    tList.add(t4);
    tList.add(t5);

    //II. Stream 생성
    Stream<transactions> tStream = tList.stream();

    //III. Stream을 통해 원하는 값 추출하기
    tStream.filter(t -> t.getType().equals("GROCERY"))
              .sorted(Comparator.comparing(transactions::getId).reversed())
              .forEach(System.out::println);

    //IV. Stream을 List로 반환하기
    List<transactions> tList2 = tList.stream()
                                    .filter(t -> t.getType().equals("GROCERY"))
                                    .sorted(Comparator.comparing(transactions::getId).reversed())
                                    .collect(Collectors.toList());
    System.out.println(tList2);
  }
}
