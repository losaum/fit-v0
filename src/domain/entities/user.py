from uuid import uuid4
from datetime import datetime
from src.domain.value_objects.email import EmailVO

class User:
    def __init__(
        self,
        nome: str,
        email: EmailVO,
        senha_hash: str,
        id: str = None,
        criado_em: datetime = None
    ):
        self.id = id or str(uuid4())
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.criado_em = criado_em or datetime.utcnow()