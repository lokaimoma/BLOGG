from . import prefix
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import starlette.status as status_code
from src.domain_logic.user_domain import UserDomain, UserLogin
from src.domain_logic.user_domain import User
from src.util.mappers.user_domain_mapper import map_user_domain_to_user_base_model as mapper
from src.usecases.insert.insert_user import insert_user
from ..usecases.login_user import login_user

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


@user_router.post(path="/login", response_model=UserLogin, status_code=status_code.HTTP_200_OK)
async def login(email: str, password: str):
    result = await login_user(email=email, password=password)
    if not result:
        error = {
            "ERROR": "User may not be registered, or credentials are incorrect"
        }
        return JSONResponse(content=error, status_code=status_code.HTTP_404_NOT_FOUND)

    user_data = result.__dict__
    del user_data["password"]
    user = UserLogin(**user_data)
    return JSONResponse(content=user)
