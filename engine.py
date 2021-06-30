import uvicorn
from src import create_app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("engine:app", reload=True, reload_dirs=["./src"])
