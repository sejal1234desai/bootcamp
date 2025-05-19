# schemas.py
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float

class ProductOut(ProductCreate):
    class Config:
        orm_mode = True

class UserProfile(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True

class DepartmentCreate(BaseModel):
    name: str

class DepartmentOut(DepartmentCreate):
    id: int
    class Config:
        orm_mode = True

class EmployeeCreate(BaseModel):
    name: str
    department_id: int

class EmployeeOut(EmployeeCreate):
    id: int
    class Config:
        orm_mode = True
