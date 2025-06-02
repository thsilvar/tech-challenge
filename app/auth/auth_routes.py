from fastapi import APIRouter, HTTPException
from app.model.user import UserCreate, UserRepository
from app.auth.jwt_handler import create_access_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    if UserRepository.find_by_username(user.username):
        raise HTTPException(status_code=400, detail="Usuário já existe.")
    
    UserRepository.create_user(user.username, user.password)
    return {"message": "Usuário criado com sucesso!"}

@router.post("/login")
def login(user: UserCreate):
    db_user = UserRepository.find_by_username(user.username)
    if not db_user or not UserRepository.verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Credenciais inválidas.")

    access_token = create_access_token(data={"sub": db_user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
