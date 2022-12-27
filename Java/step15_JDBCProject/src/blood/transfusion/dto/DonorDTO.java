package blood.transfusion.dto;

public class DonorDTO extends PeopleDTO{ //DonorDTO 클래스는 PeopleDTO 클래스를 상속받음
	private String purposeDonation; // 헌혈목적 추가
	
	public DonorDTO() {}
	public DonorDTO(String purposeDonation) {
		super();
		this.purposeDonation = purposeDonation;
	}
	public DonorDTO(String id, String name, int age, String sex, String bloodType, String purposeDonation) { //DonorDTO를 직접 생성할 때 사용
		super(id, name, age, sex, bloodType);
		this.purposeDonation = purposeDonation;
	}
	public String getPurposeDonation() {
		return purposeDonation;
	}
	public void setPurposeDonation(String purposeDonation) {
		this.purposeDonation = purposeDonation;
	}
	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append(super.toString());
		builder.append(", 헌혈 목적 : ");
		builder.append(purposeDonation);		
		builder.append("]");
		return builder.toString();
	}
}
