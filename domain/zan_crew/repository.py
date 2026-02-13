from infrastructure.db.models import ZanCrew
from datetime import datetime

class ZanCrewRepository:
    def __init__(self, db):
        self.db = db

    def get_by_id(self, zancrew_id: int):
        return self.db.query(ZanCrew).filter(ZanCrew.zancrew_id == zancrew_id).first()

    def get_by_phone(self, phone: str):
        return self.db.query(ZanCrew).filter(ZanCrew.phone == phone).first()

    def get_by_zan_user_id(self, zan_user_id: int):
        return self.db.query(ZanCrew).filter(ZanCrew.zan_user_id == zan_user_id).first()

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(ZanCrew).offset(skip).limit(limit).all()

    def get_all_with_user(self, skip: int = 0, limit: int = 100):
        """Get all zan_crew records with joined zan_user data"""
        from sqlalchemy.orm import joinedload
        return self.db.query(ZanCrew).options(joinedload(ZanCrew.zan_user)).offset(skip).limit(limit).all()

    def create(self, phone: str, zan_user_id: int, pan_id: str = None, adhar_id: str = None,
               birth_date: datetime = None, city: str = None, state: str = None,
               country: str = None, latitude: str = None, longitude: str = None,
               martial_status: str = None, status: str = None, radius_km: float = None,
               work_hours: str = None, kyc_verified: str = None, is_online: str = None,
               payout_beneficiary_id: str = None, bank_account: str = None, ifsc_code: str = None,
               home_lat: str = None, home_lng: str = None, idfy_refs: str = None,
               pan_name: str = None, pan_number_last4: str = None, aadhaar_verified: str = None,
               aadhaar_last4: str = None, aadhar_city: str = None, face_match_score: float = None,
               face_verified: str = None, selfie_img_url: str = None):
        zan_crew = ZanCrew(
            phone=phone,
            pan_id=pan_id,
            adhar_id=adhar_id,
            birth_date=birth_date,
            city=city,
            state=state,
            country=country,
            latitude=latitude,
            longitude=longitude,
            martial_status=martial_status,
            zan_user_id=zan_user_id,
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
        self.db.add(zan_crew)
        self.db.commit()
        self.db.refresh(zan_crew)
        return zan_crew

    def update(self, zancrew_id: int, phone: str = None, pan_id: str = None,
               adhar_id: str = None, birth_date: datetime = None, city: str = None,
               state: str = None, country: str = None, latitude: str = None,
               longitude: str = None, martial_status: str = None, status: str = None,
               radius_km: float = None, work_hours: str = None, kyc_verified: str = None,
               is_online: str = None, payout_beneficiary_id: str = None, bank_account: str = None,
               ifsc_code: str = None, home_lat: str = None, home_lng: str = None,
               idfy_refs: str = None, pan_name: str = None, pan_number_last4: str = None,
               aadhaar_verified: str = None, aadhaar_last4: str = None, aadhar_city: str = None,
               face_match_score: float = None, face_verified: str = None, selfie_img_url: str = None):
        zan_crew = self.get_by_id(zancrew_id)
        if not zan_crew:
            return None
        
        if phone is not None:
            zan_crew.phone = phone
        if pan_id is not None:
            zan_crew.pan_id = pan_id
        if adhar_id is not None:
            zan_crew.adhar_id = adhar_id
        if birth_date is not None:
            zan_crew.birth_date = birth_date
        if city is not None:
            zan_crew.city = city
        if state is not None:
            zan_crew.state = state
        if country is not None:
            zan_crew.country = country
        if latitude is not None:
            zan_crew.latitude = latitude
        if longitude is not None:
            zan_crew.longitude = longitude
        if martial_status is not None:
            zan_crew.martial_status = martial_status
        if status is not None:
            zan_crew.status = status
        if radius_km is not None:
            zan_crew.radius_km = radius_km
        if work_hours is not None:
            zan_crew.work_hours = work_hours
        if kyc_verified is not None:
            zan_crew.kyc_verified = kyc_verified
        if is_online is not None:
            zan_crew.is_online = is_online
        if payout_beneficiary_id is not None:
            zan_crew.payout_beneficiary_id = payout_beneficiary_id
        if bank_account is not None:
            zan_crew.bank_account = bank_account
        if ifsc_code is not None:
            zan_crew.ifsc_code = ifsc_code
        if home_lat is not None:
            zan_crew.home_lat = home_lat
        if home_lng is not None:
            zan_crew.home_lng = home_lng
        if idfy_refs is not None:
            zan_crew.idfy_refs = idfy_refs
        if pan_name is not None:
            zan_crew.pan_name = pan_name
        if pan_number_last4 is not None:
            zan_crew.pan_number_last4 = pan_number_last4
        if aadhaar_verified is not None:
            zan_crew.aadhaar_verified = aadhaar_verified
        if aadhaar_last4 is not None:
            zan_crew.aadhaar_last4 = aadhaar_last4
        if aadhar_city is not None:
            zan_crew.aadhar_city = aadhar_city
        if face_match_score is not None:
            zan_crew.face_match_score = face_match_score
        if face_verified is not None:
            zan_crew.face_verified = face_verified
        if selfie_img_url is not None:
            zan_crew.selfie_img_url = selfie_img_url
        
        self.db.commit()
        self.db.refresh(zan_crew)
        return zan_crew

    def update_phone_by_user_id(self, zan_user_id: int, phone: str):
        """Update phone in zan_crew when phone is updated in zan_user"""
        zan_crew = self.get_by_zan_user_id(zan_user_id)
        if zan_crew:
            zan_crew.phone = phone
            self.db.commit()
            self.db.refresh(zan_crew)
            return True
        return False

    def delete(self, zancrew_id: int):
        zan_crew = self.get_by_id(zancrew_id)
        if not zan_crew:
            return False
        
        self.db.delete(zan_crew)
        self.db.commit()
        return True

