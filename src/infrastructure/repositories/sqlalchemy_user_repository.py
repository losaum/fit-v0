from sqlalchemy.orm import Session
from infrastructure.db.models import UserModel
from domain.entities.user import User
from domain.value_objects.email import EmailVO
from domain.repositories.user_repository import UserRepository


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
        self.session.add(model)
        self.session.commit()
        # Atualiza entidade a partir da ORM
        user.id = model.id
        user.criado_em = model.criado_em
