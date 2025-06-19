from fastapi import APIRouter, Depends, HTTPException, status
from api.dependencies import get_user_repository  # get_db,
from application.dtos.auth_dto import AuthLoginDTO, AuthTokenDTO
from application.use_cases.autenticar_usuario import AutenticarUsuarioUseCase
from domain.exceptions import DomainException

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=AuthTokenDTO)
async def login(dto: AuthLoginDTO, repo=Depends(get_user_repository)):
    use_case = AutenticarUsuarioUseCase(repo)
    try:
        return use_case.execute(dto)
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
