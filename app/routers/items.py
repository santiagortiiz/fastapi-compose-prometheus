from fastapi import APIRouter, HTTPException

from ..models.users import User
from .users import users_data

router = APIRouter(
    prefix="/{user_name}/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_user_items(user_name: str) -> User:
    print(user_name)
    for user in users_data:
        if user.name == user_name:
            return user

    raise HTTPException(status_code=404, detail="User not found")


@router.get("/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
