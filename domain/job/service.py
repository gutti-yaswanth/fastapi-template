from domain.zan_user.repository import ZanUserRepository

class JobService:
    def __init__(self, repo, zan_user_repo=None):
        self.repo = repo
        self.zan_user_repo = zan_user_repo

    def create_job(self, user_id: int, task_title: str, polished_task: str, location_address: str,
                   latitude: str, longitude: str, scheduled_at, duration_hours: int, duration_minutes: int,
                   estimated_cost_pence: int, people_required: int, actions: str, tags: str,
                   payment_mode: str, payment_status: str, currency: str, pickup_adress: str,
                   pickup_latitude: str, pickup_longitude: str, assigned_zancrew_user_id: int = None,
                   short_title: str = None, imp_notes: str = None, bucket: str = None,
                   chat_room_id: str = None):
        # Validate user_id exists in zan_user table
        if self.zan_user_repo:
            zan_user = self.zan_user_repo.get_by_id(user_id)
            if not zan_user:
                raise ValueError(f"User with user_id {user_id} not found in zan_user table")
        
        return self.repo.create(
            user_id, task_title, polished_task, location_address, latitude, longitude,
            scheduled_at, duration_hours, duration_minutes, estimated_cost_pence,
            people_required, actions, tags, payment_mode, payment_status, currency,
            pickup_adress, pickup_latitude, pickup_longitude, assigned_zancrew_user_id,
            short_title, imp_notes, bucket, chat_room_id
        )

    def get_job(self, job_id: int):
        job = self.repo.get_by_id(job_id)
        if not job:
            raise ValueError("Job not found")
        return job

    def get_all_jobs(self, skip: int = 0, limit: int = 100):
        return self.repo.get_all(skip, limit)

    def get_jobs_by_user(self, user_id: int, skip: int = 0, limit: int = 100):
        # Validate user_id exists in zan_user table
        if self.zan_user_repo:
            zan_user = self.zan_user_repo.get_by_id(user_id)
            if not zan_user:
                raise ValueError(f"User with user_id {user_id} not found in zan_user table")
        
        return self.repo.get_by_user_id(user_id, skip, limit)

    def update_job(self, job_id: int, task_title: str = None, polished_task: str = None,
                   location_address: str = None, latitude: str = None, longitude: str = None,
                   scheduled_at = None, duration_hours: int = None, duration_minutes: int = None,
                   estimated_cost_pence: int = None, assigned_zancrew_user_id: int = None,
                   short_title: str = None, people_required: int = None, imp_notes: str = None,
                   actions: str = None, tags: str = None, bucket: str = None,
                   payment_mode: str = None, payment_status: str = None, currency: str = None,
                   chat_room_id: str = None, pickup_adress: str = None,
                   pickup_latitude: str = None, pickup_longitude: str = None):
        job = self.repo.update(
            job_id, task_title, polished_task, location_address, latitude, longitude,
            scheduled_at, duration_hours, duration_minutes, estimated_cost_pence,
            assigned_zancrew_user_id, short_title, people_required, imp_notes,
            actions, tags, bucket, payment_mode, payment_status, currency,
            chat_room_id, pickup_adress, pickup_latitude, pickup_longitude
        )
        if not job:
            raise ValueError("Job not found")
        return job

    def delete_job(self, job_id: int):
        success = self.repo.delete(job_id)
        if not success:
            raise ValueError("Job not found")
        return {"message": "Job deleted successfully"}
