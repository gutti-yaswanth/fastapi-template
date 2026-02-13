from domain.zan_user.repository import ZanUserRepository

class ZanCrewService:
    def __init__(self, repo, zan_user_repo):
        self.repo = repo
        self.zan_user_repo = zan_user_repo

    def create_zan_crew(self, phone: str, pan_id: str = None, adhar_id: str = None,
                       birth_date = None, city: str = None, state: str = None,
                       country: str = None, latitude: str = None, longitude: str = None,
                       martial_status: str = None, status: str = None, radius_km: float = None,
                       work_hours: str = None, kyc_verified: str = None, is_online: str = None,
                       payout_beneficiary_id: str = None, bank_account: str = None, ifsc_code: str = None,
                       home_lat: str = None, home_lng: str = None, idfy_refs: str = None,
                       pan_name: str = None, pan_number_last4: str = None, aadhaar_verified: str = None,
                       aadhaar_last4: str = None, aadhar_city: str = None, face_match_score: float = None,
                       face_verified: str = None, selfie_img_url: str = None):
        # Validate phone by finding zan_user with this phone
        zan_user = self.zan_user_repo.get_by_phone(phone)
        if not zan_user:
            raise ValueError(f"No zan_user found with phone: {phone}")
        
        # Check if zan_crew already exists for this user
        existing_crew = self.repo.get_by_zan_user_id(zan_user.user_id)
        if existing_crew:
            raise ValueError(f"ZanCrew already exists for user_id: {zan_user.user_id}")
        
        return self.repo.create(
            phone=phone,
            zan_user_id=zan_user.user_id,
            pan_id=pan_id,
            adhar_id=adhar_id,
            birth_date=birth_date,
            city=city,
            state=state,
            country=country,
            latitude=latitude,
            longitude=longitude,
            martial_status=martial_status,
            status=status,
            radius_km=radius_km,
            work_hours=work_hours,
            kyc_verified=kyc_verified,
            is_online=is_online,
            payout_beneficiary_id=payout_beneficiary_id,
            bank_account=bank_account,
            ifsc_code=ifsc_code,
            home_lat=home_lat,
            home_lng=home_lng,
            idfy_refs=idfy_refs,
            pan_name=pan_name,
            pan_number_last4=pan_number_last4,
            aadhaar_verified=aadhaar_verified,
            aadhaar_last4=aadhaar_last4,
            aadhar_city=aadhar_city,
            face_match_score=face_match_score,
            face_verified=face_verified,
            selfie_img_url=selfie_img_url
        )

    def get_zan_crew(self, zancrew_id: int):
        zan_crew = self.repo.get_by_id(zancrew_id)
        if not zan_crew:
            raise ValueError("ZanCrew not found")
        return zan_crew

    def get_zan_crew_by_phone(self, phone: str):
        zan_crew = self.repo.get_by_phone(phone)
        if not zan_crew:
            raise ValueError("ZanCrew not found")
        return zan_crew

    def get_zan_crew_by_user_id(self, zan_user_id: int):
        zan_crew = self.repo.get_by_zan_user_id(zan_user_id)
        if not zan_crew:
            raise ValueError("ZanCrew not found")
        return zan_crew

    def get_all_zan_crew(self, skip: int = 0, limit: int = 100):
        return self.repo.get_all(skip, limit)

    def get_all_zan_crew_with_user(self, skip: int = 0, limit: int = 100):
        """Get all zan_crew records with related zan_user data"""
        return self.repo.get_all_with_user(skip, limit)

    def update_zan_crew(self, zancrew_id: int, phone: str = None, pan_id: str = None,
                       adhar_id: str = None, birth_date = None, city: str = None,
                       state: str = None, country: str = None, latitude: str = None,
                       longitude: str = None, martial_status: str = None, status: str = None,
                       radius_km: float = None, work_hours: str = None, kyc_verified: str = None,
                       is_online: str = None, payout_beneficiary_id: str = None, bank_account: str = None,
                       ifsc_code: str = None, home_lat: str = None, home_lng: str = None,
                       idfy_refs: str = None, pan_name: str = None, pan_number_last4: str = None,
                       aadhaar_verified: str = None, aadhaar_last4: str = None, aadhar_city: str = None,
                       face_match_score: float = None, face_verified: str = None, selfie_img_url: str = None):
        zan_crew = self.repo.update(
            zancrew_id, phone, pan_id, adhar_id, birth_date, city, state,
            country, latitude, longitude, martial_status, status, radius_km,
            work_hours, kyc_verified, is_online, payout_beneficiary_id, bank_account,
            ifsc_code, home_lat, home_lng, idfy_refs, pan_name, pan_number_last4,
            aadhaar_verified, aadhaar_last4, aadhar_city, face_match_score, face_verified, selfie_img_url
        )
        if not zan_crew:
            raise ValueError("ZanCrew not found")
        return zan_crew

    def delete_zan_crew(self, zancrew_id: int):
        success = self.repo.delete(zancrew_id)
        if not success:
            raise ValueError("ZanCrew not found")
        return {"message": "ZanCrew deleted successfully"}

