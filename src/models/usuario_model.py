from datetime import date
from pydantic import BaseModel, validator
from typing import Optional
class UsuarioModel(BaseModel):
    nome: str
    nascimento: date

    @validator('nome')
    def nome_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Nome is empty')
        return v.title()
