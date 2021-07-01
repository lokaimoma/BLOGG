from typing import List, Optional

from . import prefix
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import starlette.status as StatusCode
from src.domain_logic.blog_domain import BlogDomain
from src.usecases.insert.insert_blog import insert_blog
from src.util.mappers.blog_domain_to_json import blog_domain_json as convertor
from ..domain_logic.blog_domain_detailed import BlogDomainDetail
from ..usecases.getters.get_blog_details import get_blog_details
from ..usecases.getters.get_blogs_by_user_id import get_blogs_by_user_id
from ..usecases.update.update_blog import update_blog
from ..util.mappers.blog_model_to_blog_domain_json import blog_model_list_to_blog_domain_json

blog_router = APIRouter(prefix=f"{prefix}/blog", tags=["blogs"])


@blog_router.post(path="/insert", response_model=BlogDomain, status_code=StatusCode.HTTP_201_CREATED)
async def insert(blogInfo: BlogDomain):
    await insert_blog(blogDomain=blogInfo)

    return JSONResponse(content=convertor(blogDomain=blogInfo), media_type="application/json")


@blog_router.post(path="/update/{blog_id}", response_model=BlogDomain,
                  status_code=StatusCode.HTTP_201_CREATED)
async def update(blog_id: int, blog_info: BlogDomain):
    await update_blog(blog_id=blog_id, blog_info=blog_info)
    return JSONResponse(content=convertor(blogDomain=blog_info),
                        media_type="application/json")


@blog_router.get(path="/user_blogs/{user_id}", response_model=List[BlogDomain],
                 status_code=StatusCode.HTTP_200_OK)
async def get_user_blogs(user_id: int):
    blog_list = await get_blogs_by_user_id(user_id=user_id)
    data = await blog_model_list_to_blog_domain_json(blog_list=blog_list)
    return JSONResponse(content=data, media_type="application/json")


@blog_router.get(path="/{blog_id}", response_model=BlogDomainDetail,
                 status_code=StatusCode.HTTP_200_OK)
async def blog_details(blog_id: int, current_user_id: Optional[int] = None):
    result = await get_blog_details(blog_id=blog_id,
                                    current_user_id=current_user_id)
    if result:
        return JSONResponse(content=convertor(blogDomain=result),
                            media_type="application/json")

    return JSONResponse(content="")
