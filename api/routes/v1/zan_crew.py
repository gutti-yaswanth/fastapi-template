from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from domain.zan_crew.schemas import ZanCrewCreate, ZanCrewResponse, ZanCrewUpdate, ZanCrewWithUserResponse
from core.dependencies import get_zan_crew_service

router = APIRouter(prefix="/zan-crew", tags=["ZanCrew"])

@router.post("", response_model=ZanCrewResponse, status_code=201)
def create_zan_crew(
    data: ZanCrewCreate,
    service = Depends(get_zan_crew_service)
):
    try:
        return service.create_zan_crew(
            data.phone,
            data.pan_id,
            data.adhar_id,
            data.birth_date,
            data.city,
            data.state,
            data.country,
            data.latitude,
            data.longitude,
            data.martial_status,
            data.status,
            data.radius_km,
            data.work_hours,
            data.kyc_verified,
            data.is_online,
            data.payout_beneficiary_id,
            data.bank_account,
            data.ifsc_code,
            data.home_lat,
            data.home_lng,
            data.idfy_refs,
            data.pan_name,
            data.pan_number_last4,
            data.aadhaar_verified,
            data.aadhaar_last4,
            data.aadhar_city,
            data.face_match_score,
            data.face_verified,
            data.selfie_img_url
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=List[ZanCrewResponse])
def get_all_zan_crew(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    service = Depends(get_zan_crew_service)
):
    return service.get_all_zan_crew(skip, limit)

@router.get("/with-user", response_model=List[ZanCrewWithUserResponse])
def get_all_zan_crew_with_user(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    service = Depends(get_zan_crew_service)
):
    """Get all zan_crew records with related zan_user data"""
    return service.get_all_zan_crew_with_user(skip, limit)

@router.get("/phone/{phone}", response_model=ZanCrewResponse)
def get_zan_crew_by_phone(
    phone: str,
    service = Depends(get_zan_crew_service)
):
    try:
        return service.get_zan_crew_by_phone(phone)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/user/{zan_user_id}", response_model=ZanCrewResponse)
def get_zan_crew_by_user_id(
    zan_user_id: int,
    service = Depends(get_zan_crew_service)
):
    try:
        return service.get_zan_crew_by_user_id(zan_user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{zancrew_id}", response_model=ZanCrewResponse)
def get_zan_crew(
    zancrew_id: int,
    service = Depends(get_zan_crew_service)
):
    try:
        return service.get_zan_crew(zancrew_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{zancrew_id}", response_model=ZanCrewResponse)
def update_zan_crew(
    zancrew_id: int,
    data: ZanCrewUpdate,
    service = Depends(get_zan_crew_service)
):
    try:
        return service.update_zan_crew(
            zancrew_id,
            data.phone,
            data.pan_id,
            data.adhar_id,
            data.birth_date,
            data.city,
            data.state,
            data.country,
            data.latitude,
            data.longitude,
            data.martial_status,
            data.status,
            data.radius_km,
            data.work_hours,
            data.kyc_verified,
            data.is_online,
            data.payout_beneficiary_id,
            data.bank_account,
            data.ifsc_code,
            data.home_lat,
            data.home_lng,
            data.idfy_refs,
            data.pan_name,
            data.pan_number_last4,
            data.aadhaar_verified,
            data.aadhaar_last4,
            data.aadhar_city,
            data.face_match_score,
            data.face_verified,
            data.selfie_img_url
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{zancrew_id}", status_code=204)
def delete_zan_crew(
    zancrew_id: int,
    service = Depends(get_zan_crew_service)
):
    try:
        service.delete_zan_crew(zancrew_id)
        return None
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

