from pydantic import EmailStr, TypeAdapter, ValidationError


class EmailVO:
    """
    Value Object que representa e valida um endereço de e-mail.
    Imutável e validado via Pydantic.
    """

    def __init__(self, value: str):
        # Remove espaços e normaliza para minúsculas
        value_normalized = value.strip().lower()

        try:
            adapter = TypeAdapter(EmailStr)
            self._value = adapter.validate_python(value_normalized)            
        except ValidationError:
            raise ValueError(f"E-mail inválido: {value}")

    @property
    def value(self) -> str:
        return str(self._value)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, EmailVO):
            return self.value == other.value
        return False

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"EmailVO({self.value})"
