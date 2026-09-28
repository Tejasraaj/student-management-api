from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    course: str = Field(..., min_length=1)
    age: int


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    course: str
    age: int

    class Config:
        from_attributes = True