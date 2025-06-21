from src.domain.IAM.exceptions import DomainException
from src.domain.IAM.repositories.user_repository import UserRepository
from src.application.dtos.user_dto import UserPasswordChangeDTO
from src.domain.IAM.services.password_service import PasswordService

class TrocarSenhaUseCase:
    """Caso de uso para troca de senha do usuário"""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.password_service = PasswordService()

    def execute(self, dto: UserPasswordChangeDTO) -> bool:
        """Executa a troca de senha do usuário

        Args:
            dto (UserPasswordChangeDTO): DTO contendo o ID do usuário, senha atual e nova senha

        Raises:
            DomainException: Quando a senha atual está incorreta
            DomainException: Quando o usuário não é encontrado

        Returns:
            bool: True se a senha foi alterada com sucesso
        """
        # Busca o usuário pelo ID
        user = self.user_repository.get_by_id(dto.id)
        if not user:
            raise DomainException("Usuário não encontrado")

        # Verifica se a senha atual está correta
        if not self.password_service.verify_password(dto.senha_atual, user.senha_hash):
            raise DomainException("Senha atual incorreta")

        # Gera o hash da nova senha
        new_hashed_password = self.password_service.get_password_hash(dto.nova_senha)

        # Atualiza a senha do usuário
        user.senha_hash = new_hashed_password
        self.user_repository.save(user)

        return True