from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from passlib.context import CryptContext
from app.db.mongo import db

# Para lidar com ObjectId no Pydantic
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("ID inválido")
        return ObjectId(v)

# Schema de entrada (registro/login)
class UserCreate(BaseModel):
    username: str
    password: str

# Schema de saída (sem senha)
class UserOut(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True

# Repositório Mongo + utilitários
class UserRepository:
    collection = db["users"]
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def find_by_username(cls, username: str) -> Optional[dict]:
        return cls.collection.find_one({"username": username})

    @classmethod
    def verify_password(cls, plain: str, hashed: str) -> bool:
        return cls.pwd_context.verify(plain, hashed)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def create_user(cls, username: str, password: str) -> str:
        hashed = cls.hash_password(password)
        result = cls.collection.insert_one({"username": username, "password": hashed})
        return str(result.inserted_id)
