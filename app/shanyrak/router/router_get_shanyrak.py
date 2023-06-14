from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class GetShanyrakResponse(AppModel):
    id: Any = Field(alias="_id")
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


@router.get("/", response_model=GetShanyrakResponse)
def get_shanyrak(
    id: str,
    svc: Service = Depends(get_service),
) -> GetShanyrakResponse:
    shanyrak = svc.repository.get_shanyrak(id=id)
    if shanyrak is None:
        return Response(status_code=404)
    return GetShanyrakResponse(**shanyrak)
