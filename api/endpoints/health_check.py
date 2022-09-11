from typing import Any
from fastapi import APIRouter
from dotenv import dotenv_values

from db.crud import highlow

config = dotenv_values(".env")

router = APIRouter()


@router.get("/fastapi")
def health_check_fastapi() -> Any:
    return {"msg": "FastAPI OK"}


@router.get("/upbit")
def health_check_fastapi() -> Any:
    print(config.get("UPBIT_ACCESS_KEY"))

    return {"msg": "UpBit OK"}


@router.get("/db")
def health_check_db() -> Any:
    highlow.read("KRW-EOS")

    return {"msg": "FireStore OK"}
