from typing import Annotated

from fastapi import APIRouter, Depends

from ..models.items import Message

router = APIRouter(
    prefix="/hello",
    tags=["hello world"],
    # dependencies=[Depends(get_token_header)],
)


def common_parameters() -> dict:
    return {"msg": "hello world"}


@router.get("/")
def read_item(greetings: Annotated[dict, Depends(common_parameters)]):
    print("do something")
    return greetings


@router.post("/")
def log_message(message: Message) -> str:
    """Create operation - Add a new user"""
    print(message)
    return "status saved"
