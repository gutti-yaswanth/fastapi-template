class UserService:
    def __init__(self, repo):
        self.repo = repo

    def create_user(self, email: str, name: str = None, mobile: str = None):
        if self.repo.get_by_email(email):
            raise ValueError("User already exists")

        return self.repo.create(email, name, mobile)
