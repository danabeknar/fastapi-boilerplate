from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.utils import AppModel

from ..service import Service, get_service
from . import router


@router.delete("/")
def delete_shanyrak(
    id: str,
    svc: Service = Depends(get_service),
) -> Response:
    svc.repository.delete_shanyrak(id=id)
    return Response(status_code=200)
