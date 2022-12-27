package blood.transfusion.model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import blood.transfusion.dto.DonorDTO;
import blood.transfusion.util.DBUtil;

public class DonorDAO { //DonorDAO : DonorDTO 객체를 DB에 저장하고, DB에서 DonorDTO 객체를 가져오는 기능을 지원하는 클래스
	public static boolean addDonor(DonorDTO donor) throws SQLException{ //addDonor() : DonorDTO 객체를 DB에 저장하는 메소드
		Connection con = null;
		PreparedStatement pstmt = null;
		try {
			con = DBUtil.getConnection();
			pstmt = con.prepareStatement("insert into Donor values(?, ?, ?, ?, ?, ?)");
			pstmt.setString(1, donor.getId());
			pstmt.setString(2, donor.getName());
			pstmt.setInt(3, donor.getAge());
			pstmt.setString(4, donor.getSex());
			pstmt.setString(5, donor.getBloodType());
			pstmt.setString(6, donor.getPurposeDonation());
			
			int result = pstmt.executeUpdate();
		
			if(result == 1){
				return true;
			}
		}finally{
			DBUtil.close(con, pstmt); //PreparedStatement는 Statement를 상속받으므로 Statement를 close()할 때 PreparedStatement도 close()됨
		}
		return false;
	}

	// 수정
	// 헌혈자 id로 주요 기부 내용 수정하기
	public static boolean updateDonor(String donorId, String purposeDonation) throws SQLException { //updateDonor() : donorId기준으로 purposeDonation을 수정하는 메소드
		Connection con = null;
		PreparedStatement pstmt = null;
		try {
			con = DBUtil.getConnection();

			pstmt = con.prepareStatement("update Donor set purpose_donation=? where Donor_id=?");
			pstmt.setString(1, purposeDonation);
			pstmt.setString(2, donorId);

			int result = pstmt.executeUpdate();
			if (result == 1) {
				return true;
			}
		} finally {
			DBUtil.close(con, pstmt);
		}
		return false;
	}

	// sql - delete from donor where donor_id=?
	public static boolean deleteDonor(String donorId) throws SQLException { //deleteDonor() : donorId를 기준으로 DonorDTO 객체를 삭제하는 메소드
		Connection con = null;
		PreparedStatement pstmt = null;
		try {
			con = DBUtil.getConnection();
			pstmt = con.prepareStatement("delete from donor where donor_id=?");
			pstmt.setString(1, donorId);
			int result = pstmt.executeUpdate();
			if (result == 1) {
				return true;
			}
		} finally {
			DBUtil.close(con, pstmt);
		}
		return false;
	}

	// id로 해당 헌혈자의 모든 정보 반환
	public static DonorDTO getDonor(String donorId) throws SQLException { //getDonor() : donorId를 기준으로 DonorDTO 객체를 가져오는 메소드
		Connection con = null;
		PreparedStatement pstmt = null;
		ResultSet rset = null;
		DonorDTO Donor = null;

		try {
			con = DBUtil.getConnection();
			pstmt = con.prepareStatement("select * from donor where Donor_id=?");
			pstmt.setString(1, donorId);
			rset = pstmt.executeQuery();
			if (rset.next()) {
				Donor = new DonorDTO(rset.getString(1), rset.getString(2), rset.getInt(3), rset.getString(4), rset.getString(5), rset.getString(6));
			}
		} finally {
			DBUtil.close(con, pstmt, rset);
		}
		return Donor;
	}

	// 모든 헌혈자 검색해서 반환
	// sql - select * from donor
	public static  ArrayList<DonorDTO> getAllDonors() throws SQLException { //getAllDonors() : 모든 DonorDTO 객체를 가져오는 메소드
		Connection con= null;
		PreparedStatement pstmt = null;
		ResultSet rset = null;
		ArrayList<DonorDTO> list = null;
		try {
			con = DBUtil.getConnection();
			pstmt = con.prepareStatement("select * from donor");
			rset = pstmt.executeQuery();
			
			list = new ArrayList<DonorDTO>();
			while(rset.next()) {
				list.add(new DonorDTO(rset.getString(1), rset.getString(2), rset.getInt(3), rset.getString(4), rset.getString(5), rset.getString(6) ));
			}
		}finally {
			DBUtil.close(con, pstmt, rset);
		}
		return list;
	}
}
