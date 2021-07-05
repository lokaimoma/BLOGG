from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5000",
]

__app: Optional[FastAPI] = None


def create_app() -> FastAPI:
    """
    This function creates the app and
    include all routers from different
    end points. App configurations are
    also done here.

    ARGS
    ----
    None

    Return type
    -----------
    FastAPI object
    """
    global __app

    if not __app:
        __app = FastAPI(title="BLOGG API",
                        description="An api backend for a blogging app.", version="0.1.0")

        from src.views.index import router as pagesRouter
        from src.api.blogs_api import blog_router
        from src.api.users_api import user_router
        from src.api.engagements_api import engagement_router

        __app.include_router(router=pagesRouter)
        __app.include_router(router=user_router)
        __app.include_router(router=blog_router)
        __app.include_router(router=engagement_router)

        __app.add_middleware(
            middleware_class=CORSMiddleware,
            allow_origins=origins,
            allow_origin_regex="http://localhost:*",
            allow_methods=["*"],
            allow_headers=["*"],
        )

    return __app
