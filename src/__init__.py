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
        __app = FastAPI()

    return __app
