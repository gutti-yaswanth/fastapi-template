class BlogService:
    def __init__(self, repo):
        self.repo = repo

    def create_blog(self, title: str, content: str, author_id: int):
        return self.repo.create(title, content, author_id)

    def get_blog(self, blog_id: int):
        blog = self.repo.get_by_id(blog_id)
        if not blog:
            raise ValueError("Blog not found")
        return blog

    def get_all_blogs(self, skip: int = 0, limit: int = 100):
        return self.repo.get_all(skip, limit)

    def update_blog(self, blog_id: int, title: str = None, content: str = None):
        blog = self.repo.update(blog_id, title, content)
        if not blog:
            raise ValueError("Blog not found")
        return blog

    def delete_blog(self, blog_id: int):
        success = self.repo.delete(blog_id)
        if not success:
            raise ValueError("Blog not found")
        return {"message": "Blog deleted successfully"}

