from . import prefix
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import starlette.status as StatusCode
from src.domain_logic.user_domain import UserDomain
from src.usecases.insert_user import insert_user


user_router = APIRouter(prefix=f"{prefix}/user", tags=["user"])


@user_router.post(path="/register", response_model=UserDomain,
                  status_code=StatusCode.HTTP_201_CREATED)
async def register(userInfo: UserDomain):
    isSuccessfull = await insert_user(userDomain=userInfo)
    if isSuccessfull:
        return JSONResponse(content=userInfo, media_type="application/json")
    error = {
        "ERROR": "A user with similar email or user name already exists.",
        "status code": StatusCode.HTTP_409_CONFLICT
    }
    return JSONResponse(content=error, status_code=StatusCode.HTTP_409_CONFLICT, media_type="application/json")
