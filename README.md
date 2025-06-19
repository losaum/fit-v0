# fit-v0


poetry init --name fit-v0

poetry add fastapi[standard]
poetry add sqlalchemy
poetry add --group dev pytest pytest-cov taskipy pytest-mock

# pytest==7.4.3
# pytest-cov==4.1.0
# pytest-mock==3.12.0 poetry add --group dev pytest-mock

poetry add pydantic-settings
poetry add passlib
poetry add python-jose[cryptography]
### poetry add pyjwt
poetry add bcrypt


---
poetry run uvicorn main:app --reload --app-dir src