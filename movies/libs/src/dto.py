import http

import pydantic


class DTO(pydantic.BaseModel):
    id: int
    title: str


class ResponseDTO(pydantic.BaseModel):
    data: DTO
    status: http.HTTPStatus
