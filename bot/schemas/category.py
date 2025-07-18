from pydantic import BaseModel


class Category(BaseModel):
    name: str
    description: str
    image: str
    parent: int
