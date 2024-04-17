from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    is_active: bool = True

    model_config = {
        "json_schema_extra": {"examples": [{"name": "Santiago Ortiz", "age": 15}]}
    }


class UserIn(User):
    password: str


class UserOut(User):
    pass


class UserInDB(User):
    hashed_password: str
