from fastapi import APIRouter, Depends, status, HTTPException
#from sqlalchemy.orm import Session
from src.api.dependencies import get_user_repository # get_db,
from src.application.dtos.user_dto import UserCreateDTO, UserReadDTO, UserPasswordChangeDTO
from src.application.use_cases.cadastrar_user import CadastrarUsuarioUseCase
from src.application.use_cases.trocar_senha import TrocarSenhaUseCase
from src.domain.IAM.shared.exceptions.domain_exceptions import DomainException

router = APIRouter(prefix="/usuario", tags=["Usuario"])

@router.post("/", 
             response_model=UserReadDTO, 
             status_code=status.HTTP_201_CREATED,
             summary="Cadastrar um novo usuário",
             description="Registra um usuário fornecendo nome, login (e‑mail) e senha.")
async def criar_usuario(
    dto: UserCreateDTO,
    repo=Depends(get_user_repository)
):
    use_case = CadastrarUsuarioUseCase(repo)
    try:
        return use_case.execute(dto)
    except DomainException as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.post("/trocar-senha",
             status_code=status.HTTP_200_OK,
             summary="Trocar senha do usuário",
             description="Altera a senha do usuário mediante confirmação da senha atual.")
async def trocar_senha(
    dto: UserPasswordChangeDTO,
    repo=Depends(get_user_repository)
):
    use_case = TrocarSenhaUseCase(repo)
    try:
        use_case.execute(dto)
        return {"message": "Senha alterada com sucesso"}
    except DomainException as e:
        raise HTTPException(status_code=400, detail=str(e))