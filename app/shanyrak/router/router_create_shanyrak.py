from fastapi import Depends, HTTPException, status

from app.utils import AppModel
from typing import Any
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from . import router
from ..service import Service, get_service


class CreateShanyrakRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


class CreateShanyrakResponse(AppModel):
    id: Any = Field(alias="_id")


@router.post("/", response_model=CreateShanyrakResponse)
def create_shanyrak(
    input: CreateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> CreateShanyrakResponse:
    shanyrak_id = svc.repository.create_shanyrak(jwt_data.user_id, data=input.dict())
    return CreateShanyrakResponse(id=shanyrak_id)
