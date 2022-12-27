package blood.transfusion.model;

import java.sql.SQLException;
import java.util.ArrayList;

import blood.transfusion.dto.BTProjectDTO;
import blood.transfusion.dto.DonorDTO;
import blood.transfusion.dto.RecipientDTO;
import blood.transfusion.exception.NotExistException;

public class BTService { //BTService : 
			
	private static BTService instance = new BTService(); //싱글톤 패턴을 사용하여 객체를 하나만 생성하도록 함
	
	private BTService(){}
	
	public static BTService getInstance(){
		return instance;
	}
	
	//BTProject - CRUD
	public void notExistBTProject(String btProjectId) throws NotExistException, SQLException{ //프로젝트 검색시, 프로젝트가 존재하지 않을 경우 예외처리
		BTProjectDTO btProject = BTProjectDAO.getBTProject(btProjectId);
		if(btProject == null){
			throw new NotExistException("검색하진 수혈 정보가 없습니다.");
		}
	}
	
	//모든 BTProject 정보 반환
	public ArrayList<BTProjectDTO> getAllBTProjects() throws SQLException{ //
		return BTProjectDAO.getAllBTProjects();
	}
	
	//BTProject id로 검색
	public BTProjectDTO getBTProject(String btProjectName) throws SQLException, NotExistException{
		
		return BTProjectDAO.getBTProject(btProjectName); //getBTProject 반환값으로 BTProjectDTO 객체하나를 반환한다
	}
	
	//새로운 BTProject 저장
	public boolean addBTProject(BTProjectDTO btProject) throws SQLException{
		return BTProjectDAO.addBTProject(btProject);
	}
	
	//기존 BTProject projectID로 검색하여 정보 수정
		// BTProjectDTo의 properties : btProjectName, btProjectId, donorId, recipientId, btContent.
		// 일단 DAO에 update 메소드가 존재하는 recipientId, btContent, donorId만 수정 가능하도록 함. -> 나중에는 DTO를 받아서 모든 property를 수정 할 수 있어야 함.
	public boolean updateBTProject(String btProjectId, String changeContent, String btProjectField) throws SQLException, NotExistException{
		notExistBTProject(btProjectId); //프로젝트가 존재하지 않을 경우 예외처리
		if (btProjectField.equals("recipientId") {
			return BTProjectDAO.updateBTProjectReceive(btProjectId, changeContent);
		} 
		else if (btProjectField.equals("btContent")) {
			return BTProjectDAO.updateBTProjectContent(btProjectId, changeContent);
		} 
		else if (btProjectField.equals("donorId")) {
			return BTProjectDAO.updateBTProjectdonor(btProjectId, changeContent);
		} 
		else {
			return false;
		}
	}
	
	//BTProject 삭제
	public boolean deleteBTProject(String btProjectId) throws SQLException, NotExistException{
		notExistBTProject(btProjectId);
		return BTProjectDAO.deleteBTProject(btProjectId);
	}
	
	
	//Donor - CRUD
	// Service의 메소드 호출시 DAO의 동일이름 메소드 호출하고 결과 반환. 에러처리는 Service에서 함.
	public void notExistDonor(String donorId) throws NotExistException, SQLException {
		DonorDTO Donor = DonorDAO.getDonor(donorId);
		if (Donor == null) {
			throw new NotExistException("검색한  헌혈자가 미 존재합니다.");
		}
	}

	public boolean addDonor(DonorDTO donor) throws SQLException {
		return DonorDAO.addDonor(donor);
	}

	public boolean updateDonor(String donorId, String purposeDonation) throws SQLException, NotExistException {
		notExistDonor(donorId);
		return DonorDAO.updateDonor(donorId, purposeDonation);
	}

	public boolean deleteDonor(String donorId) throws SQLException, NotExistException {
		notExistDonor(donorId);
		return DonorDAO.deleteDonor(donorId);
	}

	public DonorDTO getDonor(String donorId) throws SQLException, NotExistException {
		DonorDTO donor = DonorDAO.getDonor(donorId);
		if (donor == null) {
			throw new NotExistException("검색한 헌혈자가 미 존재합니다.");
		}
		return donor;
	}

	public ArrayList<DonorDTO> getAllDonors() throws SQLException {
		return DonorDAO.getAllDonors();
	}

	// Recipient - CRUD
	public static void notExistRecipient(String recipientId) throws NotExistException, SQLException {
		RecipientDTO recipient = RecipientDAO.getRecipient(recipientId);
		if (recipient == null) {
			throw new NotExistException("검색한  수혈자가 미 존재합니다.");
		}
	}

	public static boolean addRecipient(RecipientDTO recipient) throws SQLException {
		return RecipientDAO.addRecipient(recipient);
	}

	public static boolean updateRecipient(String recipientId, String purposeTransfusion)
			throws SQLException, NotExistException {
		notExistRecipient(recipientId);
		return RecipientDAO.updateRecipient(recipientId, purposeTransfusion);
	}

	public boolean deleteRecipient(String recipientId) throws SQLException, NotExistException {
		notExistRecipient(recipientId);
		return RecipientDAO.deleteRecipient(recipientId);
	}

	public static RecipientDTO getRecipient(String recipientId) throws SQLException {
		return RecipientDAO.getRecipient(recipientId);
	}

	public static ArrayList<RecipientDTO> getAllRecipients() throws SQLException {
		return RecipientDAO.getAllRecipients();
	}
}
