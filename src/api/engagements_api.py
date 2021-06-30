from . import prefix
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import starlette.status as StatusCode
from src.domain_logic.engagement_domain import EngagementDomain
from src.usecases.insert.insert_engagement import insertEngagement
from ..usecases.update.update_engagement import update_engagement

engagement_router = APIRouter(
    prefix=f"{prefix}/engagement", tags=["engagements"])


@engagement_router.post(path="/insert",
                        response_model=EngagementDomain,
                        status_code=StatusCode.HTTP_201_CREATED)
async def insert(engagement: EngagementDomain):
    await insert(engagementDomain=engagement)
    return JSONResponse(content=engagement.__dict__, media_type="application/json")


@engagement_router.post(path="/update", response_model=EngagementDomain, status_code=StatusCode.HTTP_201_CREATED)
async def update(engagement: EngagementDomain):
    await update_engagement(engagement_domain=engagement)
    return JSONResponse(content=engagement.__dict__, media_type="application/json")
