from typing import Any

from fastapi import Depends
from pydantic import Field

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class GetMyAccountResponse(AppModel):
    id: Any = Field(alias="_id")
    email: str
    phone: str | None = None
    name: str | None = None
    city: str | None = None


@router.get("/users/me", response_model=GetMyAccountResponse)
def get_my_account(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> GetMyAccountResponse:
    dict = svc.repository.get_user_by_id(jwt_data.user_id)
    return GetMyAccountResponse(
        id=dict["_id"],
        email=dict["email"],
        phone=dict.get("phone", None),
        name=dict.get("name", None),
        city=dict.get("city", None),
    )
