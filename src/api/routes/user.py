from fastapi import APIRouter, Depends, status, HTTPException
#from sqlalchemy.orm import Session
from api.dependencies import get_user_repository # get_db,
from application.dtos.user_dto import UserCreateDTO, UserReadDTO
from application.use_cases.cadastrar_user import CadastrarUsuarioUseCase
from domain.exceptions import DomainException

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