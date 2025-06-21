class DomainException(Exception):
    """
    Exceção genérica para erros de regra de negócio
    (camada de domínio). Deve ser capturada nos Use Cases
    e traduzida em respostas HTTP adequadas.
    """

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
