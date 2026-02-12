from infrastructure.db.models import Blog

class BlogRepository:
    def __init__(self, db):
        self.db = db

    def get_by_id(self, blog_id: int):
        return self.db.query(Blog).filter(Blog.id == blog_id).first()

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Blog).offset(skip).limit(limit).all()

    def create(self, title: str, content: str, author_id: int):
        blog = Blog(title=title, content=content, author_id=author_id)
        self.db.add(blog)
        self.db.commit()
        self.db.refresh(blog)
        return blog

    def update(self, blog_id: int, title: str = None, content: str = None):
        blog = self.get_by_id(blog_id)
        if not blog:
            return None
        
        if title is not None:
            blog.title = title
        if content is not None:
            blog.content = content
        
        self.db.commit()
        self.db.refresh(blog)
        return blog

    def delete(self, blog_id: int):
        blog = self.get_by_id(blog_id)
        if not blog:
            return False
        
        self.db.delete(blog)
        self.db.commit()
        return True

