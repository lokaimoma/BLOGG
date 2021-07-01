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
    await insert_engagement(engagement_domain=engagement)
    return JSONResponse(content=engagement.__dict__, media_type="application/json")


@engagement_router.post(path="/update", response_model=EngagementDomain, status_code=status_code.HTTP_201_CREATED)
async def update(engagement: EngagementDomain):
    await update_engagement(engagement_domain=engagement)
    return JSONResponse(content=engagement.__dict__, media_type="application/json")
