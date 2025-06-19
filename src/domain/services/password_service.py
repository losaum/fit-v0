from passlib.context import CryptContext

class PasswordService:
    """Serviço para gerenciamento de senhas"""
    
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verifica se a senha em texto plano corresponde ao hash"""
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def get_password_hash(self, password: str) -> str:
        """Gera um hash para a senha fornecida"""
        return self.pwd_context.hash(password)