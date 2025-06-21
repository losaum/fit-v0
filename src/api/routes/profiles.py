from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID
from src.api.dependencies import get_user_repository
from src.application.dtos.user_dto import UserReadDTO
from src.application.dtos.add_nutritionist_profile_dto import AddNutritionistProfileDTO
from src.application.use_cases.adicionar_perfil_nutricionista import AdicionarPerfilNutricionistaUseCase
from src.domain.IAM.shared.exceptions.domain_exceptions import DomainException

router = APIRouter(prefix="/profiles", tags=["Profiles"])

@router.post("/users/{user_id}/nutritionist", response_model=UserReadDTO, status_code=status.HTTP_200_OK)
async def add_nutritionist_profile(
    user_id: UUID,
    dto: AddNutritionistProfileDTO,
    user_repository=Depends(get_user_repository)
):
    try:
        use_case = AdicionarPerfilNutricionistaUseCase(user_repository)
        user = use_case.execute(user_id, dto)
        return UserReadDTO.model_validate(user)
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))