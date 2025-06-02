from fastapi import FastAPI
from app.routes.produto_routes import router as produto_router
from app.routes.importacao_routes import router as importacao_router
from app.routes.exportacao_routes import router as exportacao_router
from app.auth import auth_routes
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI(
        title="Tech Challenge API",
        description="API para acessar dados da Embrapa",
        version="1.0",
        contact={
            "name": "Alexandre Lima, Thiago Ramos, Lucas Caique de Lima, Eduardo Barbosa",
            "email": "ale_and5@hotmail.com"
        }
    )

    origins = [
    "http://localhost",
    "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    # Inclui os routers com prefixo /api
    app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
    app.include_router(produto_router, prefix="/api/produtos", tags=["Produtos"])
    app.include_router(importacao_router, prefix="/api/dados", tags=["Importação"])
    app.include_router(exportacao_router, prefix="/api/dados", tags=["Exportação"])

    return app
