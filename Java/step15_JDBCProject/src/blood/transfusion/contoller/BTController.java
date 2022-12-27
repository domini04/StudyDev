package blood.transfusion.contoller;

import java.sql.SQLException;
import java.util.ArrayList;

import blood.transfusion.dto.BTProjectDTO;
import blood.transfusion.dto.DonorDTO;
import blood.transfusion.model.BTProjectDAO;
import blood.transfusion.model.BTService;
import blood.transfusion.model.DonorDAO;
import blood.transfusion.view.RunningEndView;
import blood.transfusion.view.RunningSuccessView;

public class BTController {
	private static BTController instance = new BTController();
	private BTService service = BTService.getInstance();
	
	private BTController() {}
	
	public static BTController getInstance() {
		return instance;
	}
	
	// 모든 프로젝트 검색
	public void allBTProjects(){
		try{
			RunningEndView.projectListView(service.getAllBTProjects());
			RunningSuccessView.showSuccess("모든 프로젝트 검색 성공");
		}catch(SQLException s){
			s.printStackTrace();
			RunningEndView.showError("모든 프로젝트 검색시 에러 발생");
		}
	
	}
	
	// 특정 프로젝트 검색
	public void BTProject(String pname){
			try{
				RunningEndView.projectView(service.getBTProject(pname));
				RunningSuccessView.showSuccess("특정 프로젝트 검색 성공");
			}catch(SQLException s){
				s.printStackTrace();
				RunningEndView.showError("특정 프로젝트 검색시 에러 발생");
			}
		
		}
	
	// 새로운 프로젝트 저장 로직
	public void insertBTProject(BTProjectDTO dto){
			try{
				service.addBTProject(dto);
				RunningSuccessView.showSuccess("새로운 프로젝트 등록 성공");
			}catch(SQLException s){
				s.printStackTrace();
				RunningEndView.showError("새로운 프로젝트 등록시 에러 발생");
			}
	}
	
	// 특정 프로젝트 업데이트
	public void updateBTProject(String btProjectId, String changeContent, String btProjectField){
			try{
				service.updateBTProject(btProjectId, changeContent, btProjectField);
				RunningSuccessView.showSuccess("프로젝트 수정 성공");
			}catch(SQLException s){
				s.printStackTrace();
				RunningEndView.showError("프로젝트 수정 시 에러 발생");
			}
	}
	
	// 특정 프로젝트 삭제
	
	
	// 모든 헌혈자 검색 로직
	public static ArrayList<DonorDTO> getAllDonors(){
		ArrayList<DonorDTO> allProject = null;
		try{
			RunningEndView.projectListView(DonorDAO.getAllDonors());
			RunningSuccessView.showSuccess("모든  헌혈자 검색 성공");
		}catch(SQLException s){
			s.printStackTrace();
			RunningEndView.showError("모든  헌혈자 검색시 에러 발생");
		}
		return allProject;
	}
	
}
