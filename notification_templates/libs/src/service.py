import http

import fastapi
import pandas as pd
from libs.src.db import get_db
from libs.src.dto import DTO, ResponseDTO


class Service:
    def __init__(self, db: pd.DataFrame | None):
        self.db = db

    async def get_by_id(self, id: int, dto: DTO | None) -> ResponseDTO | None:
        try:
            data = dto(**self.db.query("id==@id").iloc[0].to_dict())
            return ResponseDTO(data=data, status=http.HTTPStatus.OK)
        except Exception:
            return ResponseDTO(data=None, status=http.HTTPStatus.NOT_FOUND)


def get_service(db: pd.DataFrame = fastapi.Depends(get_db)) -> Service:
    return Service(db)
