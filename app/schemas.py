from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class User(BaseModel):
    id: int
    name: str
    email: str

class Medicine(BaseModel):
    id: int
    name: str
    description: str
    price: float

class OrderCreate(BaseModel):
    user_id: int
    medicine_id: int
    quantity: int
