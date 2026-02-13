class ZanUserService:
    def __init__(self, repo):
        self.repo = repo

    def create_zan_user(self, first_name: str, last_name: str, email: str, phone: str = None,
                       address: str = None, is_zancrew: str = "false", zancrew_id: int = None):
        # Check if email already exists
        if self.repo.get_by_email(email):
            raise ValueError("User with this email already exists")
        
        return self.repo.create(first_name, last_name, email, phone, address, is_zancrew, zancrew_id)

    def get_zan_user(self, user_id: int):
        zan_user = self.repo.get_by_id(user_id)
        if not zan_user:
            raise ValueError("ZanUser not found")
        return zan_user

    def get_zan_user_by_email(self, email: str):
        zan_user = self.repo.get_by_email(email)
        if not zan_user:
            raise ValueError("ZanUser not found")
        return zan_user

    def get_all_zan_users(self, skip: int = 0, limit: int = 100):
        return self.repo.get_all(skip, limit)

    def get_zan_users_by_zancrew(self, zancrew_id: int, skip: int = 0, limit: int = 100):
        return self.repo.get_by_zancrew_id(zancrew_id, skip, limit)

    def update_zan_user(self, user_id: int, first_name: str = None, last_name: str = None,
                       email: str = None, phone: str = None, address: str = None,
                       is_zancrew: str = None, zancrew_id: int = None):
        zan_user = self.repo.update(user_id, first_name, last_name, email, phone, 
                                    address, is_zancrew, zancrew_id)
        if not zan_user:
            raise ValueError("ZanUser not found")
        return zan_user

    def delete_zan_user(self, user_id: int):
        success = self.repo.delete(user_id)
        if not success:
            raise ValueError("ZanUser not found")
        return {"message": "ZanUser deleted successfully"}

