from fastapi import APIRouter
from fastapi import responses

router = APIRouter()


@router.get("/", include_in_schema=False)
def index():
    return responses.FileResponse(path="src/pages/index.html",
                                  media_type="text/html")
