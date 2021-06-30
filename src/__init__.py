from typing import Optional
from fastapi import FastAPI


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
        from src.api.users_api import user_router
        __app.include_router(router=pagesRouter)
        __app.include_router(router=user_router)

    return __app
