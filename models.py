from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    name: str = None
    date_of_birth: str = None
