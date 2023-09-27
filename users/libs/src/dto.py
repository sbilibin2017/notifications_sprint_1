import http

import pydantic


class DTO(pydantic.BaseModel):
    id: int
    full_name: str
    email: str
    phone_number: str
    telegram_account: str


class ResponseDTO(pydantic.BaseModel):
    data: DTO
    status: http.HTTPStatus
