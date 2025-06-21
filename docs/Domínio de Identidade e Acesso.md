
# Domínio de Identidade e Acesso
A separação é feita de forma elegante revisando os agregados que definimos. A estrutura se torna mais clara e robusta.

### 1. Agregado User (Revisado)
O agregado User continua sendo a base da autenticação, mas seu sistema de papéis (roles) se torna ainda mais importante.

- **Propriedades**:
  - id (UUID)
  - email
  - password
  - status
  - roles (Array de Enum): Agora pode conter ['STUDENT'], ['TRAINER'], ['NUTRITIONIST'], ou até mesmo combinações como ['TRAINER', 'NUTRITIONIST'] para o profissional com dupla certificação.

### 2. Agregados de Perfil (Agora Separados)
Em vez de um "Profile" genérico, teremos um para cada papel profissional.

- **TrainerProfile (Raiz de Agregado)**:
  - id (mesmo ID do User)
  - fullName
  - crefNumber (String)

- **NutritionistProfile (Novo Agregado)**:
  - id (mesmo ID do User)
  - fullName
  - crnNumber (String)
  - specializations (Array de String, ex: "Nutrição Esportiva")

### 3. Agregado Relationship (Vínculo - Revisão Crucial)
Este agregado se torna muito mais poderoso. Em vez de ligar um "treinador" a um "aluno", ele liga um profissional, em um determinado papel, a um aluno para um tipo específico de serviço.

- **Relationship (Raiz de Agregado - Versão 2.0)**:
  - id (UUID)
  - professionalId (UUID): O ID do usuário com o papel profissional.
  - studentId (UUID): O ID do usuário aluno.
  - serviceType (Enum): TRAINING ou NUTRITION. <-- Este campo é a chave!
  - status (Enum): PendingInvitation, Active, Terminated.
  - ...timestamps

### Impacto Prático da Nova Modelagem
Essa estrutura resolve elegantemente vários cenários complexos:

- **Cenário 1: Aluno com profissionais diferentes**.
  - O Aluno A pode ter dois Vínculos Active ao mesmo tempo:
    - Relationship { professionalId: B, studentId: A, serviceType: TRAINING, status: Active }
    - Relationship { professionalId: C, studentId: A, serviceType: NUTRITION, status: Active }
  - Isso significa que o Treinador B gerencia os treinos do Aluno A, e a Nutricionista C gerencia sua dieta. Perfeito.
- **Cenário 2: Profissional com dupla certificação**.
  - O Profissional D tem um User com roles: ['TRAINER', 'NUTRITIONIST'].
  - Ele possui ambos os perfis: TrainerProfile e NutritionistProfile.
  - Ele pode estabelecer dois Vínculos diferentes com o mesmo Aluno A: um para TRAINING e outro para NUTRITION.

### Lógica de Autorização Simplificada
- Quando um usuário tenta acessar a rota POST /api/training-plans:
  - O sistema verifica se o token do usuário contém o papel (role) TRAINER.
  - Verifica se existe um Relationship Active entre o professionalId do token e o studentId do plano com serviceType: TRAINING.
  - A lógica é idêntica e isolada para a parte de Nutrição, verificando o papel NUTRITIONIST e o serviceType: NUTRITION.

