from pydantic import BaseModel, EmailStr, Field

# Base schema with shared fields
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="User password")

class UserResponse(UserBase):
    userid: int

    class Config:
        from_attributes = True  