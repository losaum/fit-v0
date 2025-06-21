from fastapi import APIRouter, Depends, HTTPException, status
from src.api.dependencies import get_user_repository, get_password_service
from src.application.dtos.user_dto import UserReadDTO
from src.application.dtos.fitness_profile_dto import FitnessProfileCreateDTO
from src.application.dtos.trainer_profile_dto import TrainerProfileCreateDTO
from src.application.dtos.nutritionist_profile_dto import NutritionistProfileCreateDTO
from src.application.use_cases.cadastrar_fitness_user import CadastrarFitnessUserUseCase
from src.application.use_cases.cadastrar_trainer_user import CadastrarTrainerUserUseCase
from src.application.use_cases.cadastrar_nutritionist_user import CadastrarNutritionistUserUseCase
from src.domain.IAM.shared.exceptions.domain_exceptions import DomainException

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/fitness", response_model=UserReadDTO, status_code=status.HTTP_201_CREATED)
async def create_fitness_user(
    dto: FitnessProfileCreateDTO,
    user_repository=Depends(get_user_repository),
    password_service=Depends(get_password_service)
):
    try:
        use_case = CadastrarFitnessUserUseCase(user_repository, password_service)
        return use_case.execute(dto)
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/trainer", response_model=UserReadDTO, status_code=status.HTTP_201_CREATED)
async def create_trainer_user(
    dto: TrainerProfileCreateDTO,
    user_repository=Depends(get_user_repository),
    password_service=Depends(get_password_service)
):
    try:
        use_case = CadastrarTrainerUserUseCase(user_repository, password_service)
        return use_case.execute(dto)
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/nutritionist", response_model=UserReadDTO, status_code=status.HTTP_201_CREATED)
async def create_nutritionist_user(
    dto: NutritionistProfileCreateDTO,
    user_repository=Depends(get_user_repository),
    password_service=Depends(get_password_service)
):
    try:
        use_case = CadastrarNutritionistUserUseCase(user_repository, password_service)
        return use_case.execute(dto)
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))