from typing import Annotated

from fastapi import APIRouter, HTTPException, Header

from ..models.users import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# Dummy data for users
users_data: list[User] = [User(name="santiago", age=1), User(name="alex", age=2)]


@router.get("/")
def get_users(
    data_partition: Annotated[str, Header()] = "shared",
) -> dict[str, list[User]]:
    """Read operation - Get all users"""
    return {data_partition: users_data}


@router.get("/{user_name}")
def get_user(user_name: str):
    """Read operation - Get a specific user by ID"""
    for user in users_data:
        if user.name == user_name:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post("/")
def create_user(user: User) -> User:
    """Create operation - Add a new user"""
    users_data.append(user)
    return user


@router.put("/{user_name}")
def update_user(user_name: str, updated_user: User):
    """Update operation - Update a user by ID"""
    for user in users_data:
        if user.name == user_name:
            index = users_data.index(user)
            users_data[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{user_name}")
def delete_user(user_name: str):
    """Delete operation - Delete a user by ID"""
    for user in users_data:
        if user.name == user_name:
            index = users_data.index(user)
            deleted_user = users_data.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User not found")
