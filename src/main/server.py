from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.controllers.usuario_controller import router as usuarioController


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {'message': 'Hello :) Container Docker'}
app.include_router(usuarioController)
