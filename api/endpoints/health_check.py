from typing import Any
from fastapi import APIRouter
from dotenv import dotenv_values

config = dotenv_values(".env")

router = APIRouter()


@router.get("/fastapi")
def health_check_fastapi() -> Any:
    return {"msg": "FastAPI OK"}


@router.get("/upbit")
def health_check_fastapi() -> Any:
    print(config.get("UPBIT_ACCESS_KEY"))
    return {"msg": "UpBit OK"}
