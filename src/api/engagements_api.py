from . import prefix
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import starlette.status as status_code
from src.domain_logic.engagement_domain import EngagementDomain
from src.usecases.insert.insert_engagement import insert_engagement
from ..usecases.update.update_engagement import update_engagement

engagement_router = APIRouter(
    prefix=f"{prefix}/engagement", tags=["engagements"])


@engagement_router.post(path="/insert",
                        response_model=EngagementDomain,
                        status_code=status_code.HTTP_201_CREATED)
async def insert(engagement: EngagementDomain):
    result = await insert_engagement(engagement_domain=engagement)
    if result:
        return JSONResponse(content=engagement.__dict__, media_type="application/json")

    error = {
        "ERROR": f"The blog with id {engagement.blog_id} was not found"
    }
    return JSONResponse(content=error, media_type="application/json",
                        status_code=status_code.HTTP_422_UNPROCESSABLE_ENTITY)


@engagement_router.post(path="/update", response_model=EngagementDomain, status_code=status_code.HTTP_201_CREATED)
async def update(engagement: EngagementDomain):
    result = await update_engagement(engagement_domain=engagement)
    if result:
        return JSONResponse(content=engagement.__dict__, media_type="application/json")

    error = {
        "ERROR": f"No engagement was found"
    }
    return JSONResponse(content=error, media_type="applicatoin/json",
                        status_code=status_code.HTTP_422_UNPROCESSABLE_ENTITY)
