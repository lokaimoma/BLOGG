from . import prefix
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import starlette.status as StatusCode
from src.domain_logic.engagement_domain import EngagementDomain
from src.usecases.insert.insert_engagement import insertEngagement


engagement_router = APIRouter(
    prefix=f"{prefix}/engagement", tags=["engagements"])


@engagement_router.post(path="/insert",
                        response_model=EngagementDomain,
                        status_code=StatusCode.HTTP_201_CREATED)
async def insert_Engagement(engagement: EngagementDomain):
    await insertEngagement(engagementDomain=engagement)
    return JSONResponse(content=engagement.__dict__, media_type="application/json")
