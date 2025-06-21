from sqlalchemy.orm import Session
from src.infrastructure.db.models import UserModel
from src.domain.IAM.entities.user import User
from src.domain.IAM.value_objects.email import EmailVO
from src.domain.IAM.repositories.user_repository import UserRepository


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def exists_by_email(self, email: EmailVO) -> User | None:
        row = (
            self.session.query(UserModel)
            .filter(UserModel.email == email.value)
            .first()
        )
        if not row:
            return None

        return User(
            id=row.id,
            nome=row.nome,
            email=EmailVO(row.email),
            senha_hash=row.senha_hash,
            criado_em=row.criado_em,
        )

    def save(self, user: User) -> None:
        model = UserModel(
            id=user.id,
            nome=user.nome,
            email=user.email.value,
            senha_hash=user.senha_hash,
            criado_em=user.criado_em,
        )
        self.session.merge(model)
        self.session.commit()

        return user

    def get_by_id(self, id: str) -> User | None:
        """Busca um usuário pelo ID

        Args:
            id (str): ID do usuário

        Returns:
            User | None: Usuário encontrado ou None se não existir
        """
        row = (
            self.session.query(UserModel)
            .filter(UserModel.id == id)
            .first()
        )
        if not row:
            return None

        return User(
            id=row.id,
            nome=row.nome,
            email=EmailVO(row.email),
            senha_hash=row.senha_hash,
            criado_em=row.criado_em,
        )
