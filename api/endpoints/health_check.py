from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/fastapi")
def health_check_fastapi() -> Any:
    return {"msg": "FastAPI OK"}
