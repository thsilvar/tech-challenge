from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt_handler import verify_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not verify_token(credentials.credentials):
                raise HTTPException(status_code=403, detail="Token inválido ou expirado.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Token de autenticação ausente.")
