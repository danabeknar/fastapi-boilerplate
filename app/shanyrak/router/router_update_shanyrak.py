from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class UpdateShanyrakRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


@router.patch("/")
def update_shanyrak(
    id: str,
    input: UpdateShanyrakRequest,
    svc: Service = Depends(get_service),
) -> Response:
    svc.repository.update_shanyrak(id, data=input.dict())
    return Response(status_code=200)
