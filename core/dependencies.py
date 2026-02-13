from fastapi import Depends
from infrastructure.db.session import SessionLocal
from domain.user.repository import UserRepository
from domain.user.service import UserService
from domain.blog.repository import BlogRepository
from domain.blog.service import BlogService
from domain.job.repository import JobRepository
from domain.job.service import JobService
from domain.zan_user.repository import ZanUserRepository
from domain.zan_user.service import ZanUserService
from domain.zan_crew.repository import ZanCrewRepository
from domain.zan_crew.service import ZanCrewService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_service(db=Depends(get_db)):
    repo = UserRepository(db)
    return UserService(repo)

def get_blog_service(db=Depends(get_db)):
    repo = BlogRepository(db)
    return BlogService(repo)

def get_job_service(db=Depends(get_db)):
    repo = JobRepository(db)
    zan_user_repo = ZanUserRepository(db)
    return JobService(repo, zan_user_repo)

def get_zan_user_service(db=Depends(get_db)):
    repo = ZanUserRepository(db)
    zan_crew_repo = ZanCrewRepository(db)
    return ZanUserService(repo, zan_crew_repo)

def get_zan_crew_service(db=Depends(get_db)):
    zan_crew_repo = ZanCrewRepository(db)
    zan_user_repo = ZanUserRepository(db)
    return ZanCrewService(zan_crew_repo, zan_user_repo)
