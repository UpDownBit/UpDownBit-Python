from typing import Any
from fastapi import APIRouter
from dotenv import dotenv_values

from db import init as db_init

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
    db = db_init.main()
    print(db)

    return {"msg": "FireStore OK"}
