from src.domain_logic.blog_domain import BlogDomain


class BlogDomainDetail(BlogDomain):
    current_user_likes: bool
    likes_count: int
    dislikes_count: int

