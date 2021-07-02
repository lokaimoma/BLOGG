from . import prefix
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import starlette.status as status_code
from src.domain_logic.user_domain import UserDomain
from src.domain_logic.user_domain import User
from src.util.mappers.user_domain_mapper import map_user_domain_to_user_base_model as mapper
from src.usecases.insert.insert_user import insert_user


user_router = APIRouter(prefix=f"{prefix}/user", tags=["users"])


@user_router.post(path="/register", response_model=User,
                  status_code=status_code.HTTP_201_CREATED)
async def register(user_info: UserDomain):
    is_successfull = await insert_user(user_domain=user_info)
    if is_successfull:
        user = mapper(user_domain=user_info)
        return JSONResponse(content=user, media_type="application/json")
    error = {
        "ERROR": "A user with similar email or user name already exists.",
        "status code": status_code.HTTP_409_CONFLICT
    }
    return JSONResponse(content=error, status_code=status_code.HTTP_409_CONFLICT, media_type="application/json")

@user_router.post(path="/login", )
