# fit-v0


poetry init --name fit-v0

poetry add fastapi[standard]
poetry add sqlalchemy
poetry add --group dev pytest pytest-cov taskipy pytest-mock
poetry add --group dev httpx pytest-asyncio
poetry add pydantic-settings
poetry add passlib
poetry add python-jose[cryptography]
poetry add bcrypt



# run = 'uvicorn main:app --reload --app-dir src'

---
poetry run uvicorn main:app --reload --app-dir src 