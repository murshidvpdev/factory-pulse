from pydantic import BaseModel, EmailStr


# Shared fields
class UserBase(BaseModel):
    email: EmailStr
    username: str


# What user sends during registration
class UserCreate(UserBase):
    password: str


# What user sends during login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# What we return to frontend
class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True  # for ORM compatibility


# JWT Token response
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"