from typing import List, Optional

from starlette.responses import JSONResponse

from . import prefix
from fastapi import APIRouter
from fastapi.responses import Response
import starlette.status as status_code
from src.domain_logic.blog_domain import BlogDomain
from src.usecases.insert.insert_blog import insert_blog
from src.util.mappers.blog_domain_to_json import blog_domain_json as convertor
from ..domain_logic.blog_domain_detailed import BlogDomainDetail
from ..usecases.getters.get_all_blogs import get_all_blogs
from ..usecases.getters.get_blog_details import get_blog_details
from ..usecases.getters.get_blogs_by_user_id import get_blogs_by_user_id
from ..usecases.update.update_blog import update_blog
from ..util.mappers.blog_model_to_blog_domain_json import blog_model_list_to_blog_domain_json

blog_router = APIRouter(prefix=f"{prefix}/blog", tags=["blogs"])


@blog_router.get("/", response_model=List[BlogDomain], status_code=status_code.HTTP_200_OK)
async def get_all():
    blog_list = await get_all_blogs()
    blog_list_serialized = [blog.to_dict() for blog in blog_list]
    return JSONResponse(content=blog_list_serialized)


@blog_router.post(path="/insert", response_model=BlogDomain, status_code=status_code.HTTP_201_CREATED)
async def insert(blog_info: BlogDomain):
    result = await insert_blog(blog_domain=blog_info)
    if result:
        return Response(content=convertor(blog_domain=blog_info),
                        media_type="application/json")
    error = {
        "ERROR": f"No user with the id {blog_info.user_id} was found.",
        "Status Code": status_code.HTTP_422_UNPROCESSABLE_ENTITY
    }
    return JSONResponse(content=error, media_type="application/json",
                        status_code=status_code.HTTP_422_UNPROCESSABLE_ENTITY)


@blog_router.post(path="/update/{blog_id}", response_model=BlogDomain,
                  status_code=status_code.HTTP_201_CREATED)
async def update(blog_id: int, blog_info: BlogDomain):
    await update_blog(blog_id=blog_id, blog_info=blog_info)
    return Response(content=convertor(blog_domain=blog_info),
                    media_type="application/json")


@blog_router.get(path="/user_blogs/{user_id}", response_model=List[BlogDomain],
                 status_code=status_code.HTTP_200_OK)
async def get_user_blogs(user_id: int):
    blog_list = await get_blogs_by_user_id(user_id=user_id)
    data = await blog_model_list_to_blog_domain_json(blog_list=blog_list)
    return Response(content=data, media_type="application/json")


@blog_router.get(path="/{blog_id}", response_model=BlogDomainDetail,
                 status_code=status_code.HTTP_200_OK)
async def blog_details(blog_id: int, current_user_id: Optional[int] = None):
    result = await get_blog_details(blog_id=blog_id,
                                    current_user_id=current_user_id)
    if result:
        return Response(content=convertor(blog_domain=result),
                        media_type="application/json")

    return JSONResponse(content="")
