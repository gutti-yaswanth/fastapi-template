from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=True)
    mobile = Column(String, nullable=True)
    
    # Relationship to blogs
    blogs = relationship("Blog", back_populates="author")

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationship to user
    author = relationship("User", back_populates="blogs")

class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("zan_user.user_id"), nullable=False)
    task_title = Column(String, nullable=False)
    polished_task = Column(Text, nullable=False)
    location_address = Column(Text, nullable=False)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    scheduled_at = Column(DateTime, nullable=False)
    duration_hours = Column(Integer, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    estimated_cost_pence = Column(Integer, nullable=False)
    assigned_zancrew_user_id = Column(Integer, nullable=True)
    short_title = Column(String, nullable=True)
    people_required = Column(Integer, nullable=False)
    imp_notes = Column(Text, nullable=True)
    actions = Column(String, nullable=False)
    tags = Column(String, nullable=False)
    bucket = Column(String, nullable=True)
    payment_mode = Column(String, nullable=False)
    payment_status = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    chat_room_id = Column(String, nullable=True)
    pickup_adress = Column(Text, nullable=False)
    pickup_latitude = Column(String, nullable=False)
    pickup_longitude = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationship to zan_user
    zan_user = relationship("ZanUser", back_populates="jobs")

class ZanUser(Base):
    __tablename__ = "zan_user"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    phone = Column(String, nullable=False)
    address = Column(Text, nullable=True)
    is_zancrew = Column(String, nullable=True, default="false")
    zancrew_id = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationship to zan_crew
    zan_crew = relationship("ZanCrew", back_populates="zan_user", uselist=False)
    # Relationship to jobs
    jobs = relationship("Job", back_populates="zan_user")

class ZanCrew(Base):
    __tablename__ = "zan_crew"

    zancrew_id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)
    pan_id = Column(String, nullable=True)
    adhar_id = Column(String, nullable=True)
    birth_date = Column(DateTime, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)
    martial_status = Column(String, nullable=True)
    zan_user_id = Column(Integer, ForeignKey("zan_user.user_id"), nullable=False)
    status = Column(String, nullable=True)
    radius_km = Column(Float, nullable=True)
    work_hours = Column(String, nullable=True)
    kyc_verified = Column(String, nullable=True)
    is_online = Column(String, nullable=True)
    payout_beneficiary_id = Column(String, nullable=True)
    bank_account = Column(String, nullable=True)
    ifsc_code = Column(String, nullable=True)
    home_lat = Column(String, nullable=True)
    home_lng = Column(String, nullable=True)
    idfy_refs = Column(Text, nullable=True)
    pan_name = Column(String, nullable=True)
    pan_number_last4 = Column(String, nullable=True)
    aadhaar_verified = Column(String, nullable=True)
    aadhaar_last4 = Column(String, nullable=True)
    aadhar_city = Column(String, nullable=True)
    face_match_score = Column(Float, nullable=True)
    face_verified = Column(String, nullable=True)
    selfie_img_url = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationship to zan_user
    zan_user = relationship("ZanUser", back_populates="zan_crew")
