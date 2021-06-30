from . import prefix
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import starlette.status as StatusCode
from src.domain_logic.blog_domain import BlogDomain
from src.usecases.insert_blog import insert_blog
from src.util.mappers.blog_domain_to_json import blog_domain_json as convertor

blog_router = APIRouter(prefix=f"{prefix}/blog", tags=["blogs"])


@blog_router.post(path="/insert", response_model=BlogDomain, status_code=StatusCode.HTTP_201_CREATED)
async def insertBlog(blogInfo: BlogDomain):
    await insert_blog(blogDomain=blogInfo)

    return JSONResponse(content=convertor(blogDomain=blogInfo), media_type="application/json")
