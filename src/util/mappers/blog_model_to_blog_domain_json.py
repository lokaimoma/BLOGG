from typing import List

from src.domain_logic.blog_domain import BlogDomain
from src.model.blog import Blog
from src.util.mappers.blog_domain_to_json import blog_domain_json


async def __map_blog_model_to_blog_domain(blog_model: Blog) -> BlogDomain:
    blog_domain_data = {
        "title": blog_model.title,
        "body": blog_model.body,
        "created_date": blog_model.created_date,
        "last_updated": blog_model.last_updated,
        "user_id": blog_model.user_id
    }
    return BlogDomain(**blog_domain_data)


async def blog_model_to_blog_domain_json(blog_model: Blog) -> str:
    result = await __map_blog_model_to_blog_domain(blog_model=blog_model)
    return blog_domain_json(blogDomain=result)


async def blog_model_list_to_blog_domain_json(blog_list: List[Blog]) -> List[str]:
    result = [await blog_model_to_blog_domain_json(blog) for blog in blog_list]
    return result
