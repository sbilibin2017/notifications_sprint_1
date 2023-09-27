import fastapi
import libs.src as libs_src
from libs.src import db
from libs.utils.generate_data import generate_data


class Application:
    def __init__(self) -> None:
        pass

    def create_app(self) -> fastapi.FastAPI:
        app = fastapi.FastAPI(
            title="default",
            description="default",
            version="0.1.0",
            docs_url="/api/openapi",
            openapi_url="/api/openapi.json",
            default_response_class=fastapi.responses.ORJSONResponse,
        )
        app.include_router(
            libs_src.handler.router, prefix="/api/v1/movies", tags=["movies"]
        )

        @app.on_event("startup")
        async def startup_event():
            db.db = generate_data()

        return app


__all__ = ["Application"]
