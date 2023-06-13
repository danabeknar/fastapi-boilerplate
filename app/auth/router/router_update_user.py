from typing import Any

from fastapi import Depends
from pydantic import Field

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class UpdateUserRequest(AppModel):
    phone: str
    name: str
    city: str


class UpdateUserResponse(AppModel):
    phone: str
    name: str
    city: str


@router.patch("/users/me", response_model=UpdateUserResponse)
def update_account(
    input: UpdateUserRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> UpdateUserResponse:
    user = svc.repository.get_user_by_id(jwt_data.user_id)
    return input
