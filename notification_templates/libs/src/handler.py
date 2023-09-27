import http
import typing

import fastapi
from libs.src.dto import DTO, ResponseDTO
from libs.src.service import Service, get_service

router = fastapi.APIRouter()


@router.get(
    "/{id}",
    summary="Returns item by id",
    description="",
    status_code=http.HTTPStatus.OK,
)
async def get_by_id(
    id: int,
    service: Service = fastapi.Depends(get_service),
) -> ResponseDTO:
    return await service.get_by_id(id, DTO)
