# Descrição Funcional Detalhada do Sistema IARA
## 1. Visão e Propósito do Sistema
A IARA é uma plataforma digital concebida para ser a ponte definitiva entre profissionais da saúde – especificamente Personal Trainers e Nutricionistas – e seus respectivos clientes (Alunos). O seu propósito é transformar a prescrição e o acompanhamento de saúde e bem-estar em uma experiência contínua, personalizada e interativa, quebrando as barreiras do acompanhamento puramente presencial. A plataforma capacita os profissionais a escalar seu trabalho com eficiência e a oferecer um serviço de altíssima qualidade, ao mesmo tempo em que empodera os alunos com ferramentas claras e motivadoras para alcançar seus objetivos.
## 2. Atores do Sistema
O ecossistema IARA é composto por três tipos principais de usuários, cada um com suas próprias necessidades e jornada:
- **O Aluno**: O cliente final. Busca orientação profissional clara, um caminho estruturado para seguir, ferramentas para registrar seu progresso e um canal de comunicação direto com seus mentores de saúde. Sua maior motivação é ver resultados tangíveis e sentir-se amparado em sua jornada.
- **O Personal Trainer**: O profissional de educação física. Busca otimizar seu tempo, gerenciar múltiplos alunos de forma organizada, criar e reutilizar programas de treino de alta qualidade, e acompanhar a execução e o progresso de cada aluno de perto para fazer ajustes inteligentes.
- **O Nutricionista**: O profissional de nutrição. Busca uma ferramenta precisa para montar planos alimentares, calcular metas nutricionais, prescrever suplementos, e monitorar a adesão e o feedback de seus pacientes para promover uma reeducação alimentar eficaz.
## 3. A Jornada e as Funcionalidades do Sistema
A experiência IARA pode ser compreendida em um ciclo contínuo de planejamento, execução e acompanhamento.
### Fase I: O Início da Parceria (Onboarding e Configuração)
- **Cadastro e Identidade**: Cada usuário (Aluno, Treinador ou Nutricionista) realiza um cadastro único na plataforma, definindo seu papel principal. O sistema entende e trata cada papel de forma distinta desde o primeiro momento.
- **O Estabelecimento do Vínculo**: A relação profissional-cliente é formalizada dentro do sistema. Um profissional (Treinador ou Nutricionista) localiza um aluno na plataforma e envia um "Convite de Vínculo" para um serviço específico: Treinamento ou Nutrição. O aluno recebe a notificação e aceita o convite, selando a parceria. É fundamental entender que um aluno pode ter dois vínculos ativos e independentes simultaneamente: um com seu Personal Trainer para treinos e outro com seu Nutricionista para a dieta.
- **A Anamnese: O Ponto de Partida**: Uma vez que o vínculo é estabelecido, o profissional envia ao aluno uma anamnese completa. O profissional pode usar o modelo padrão da plataforma ou customizá-lo com suas próprias perguntas sobre histórico de saúde, lesões, hábitos, rotina e objetivos. O aluno preenche este questionário detalhado, fornecendo ao profissional todas as informações necessárias para criar um plano verdadeiramente personalizado. O profissional pode solicitar o preenchimento de uma nova anamnese a qualquer momento para reavaliar o quadro do aluno.
### Fase II: A Prescrição (O Trabalho do Profissional)
- **Para o Personal Trainer - A Criação do Plano de Treino**:
  - **Biblioteca de Exercícios**: O treinador tem acesso a uma vasta biblioteca de exercícios, cada um com vídeo demonstrativo, descrição da execução e grupos musculares trabalhados. Ele pode também adicionar seus próprios exercícios customizados, criando sua biblioteca pessoal.
  - **Montagem da Ficha**: Com base na anamnese, o treinador monta o plano de treino do aluno. Ele define a estrutura (ex: Treino A, B, C), os dias da semana, e para cada exercício, prescreve séries, repetições (ex: "8-12"), tempo de descanso, carga sugerida e observações detalhadas (ex: "focar na fase excêntrica").
  - **Templates**: Para otimizar seu tempo, o treinador pode salvar qualquer plano de treino como um "Template" para ser rapidamente adaptado e aplicado a outros alunos com perfis semelhantes no futuro.
- **Para o Nutricionista - A Criação do Plano Alimentar**:
  - **Metas Nutricionais**: O nutricionista estabelece metas diárias de calorias e macronutrientes (proteínas, carboidratos, gorduras) para o paciente.
  - **Montagem das Refeições**: Ele constrói o plano refeição por refeição (café da manhã, almoço, etc.), selecionando alimentos de uma biblioteca ou cadastrando novos. O sistema calcula automaticamente os totais nutricionais de cada refeição e do dia.
  - **Prescrição Textual**: Para suplementos, manipulados ou orientações específicas, há um campo de prescrição textual livre.
  - **Templates**: Assim como o treinador, o nutricionista pode salvar planos alimentares, refeições ou pratos específicos em sua biblioteca pessoal para reutilização.
### Fase III: A Execução (O Dia a Dia do Aluno)
- **O Diário de Treino Interativo**:
  - No dia do treino, o aluno abre seu aplicativo e visualiza a ficha prescrita.
  - Para cada exercício, ele não apenas vê o que precisa fazer, mas também registra o que de fato fez: a carga exata que utilizou e o número real de repetições em cada série.
  - Ao final da sessão, ele informa sua Percepção Subjetiva de Esforço (PSE) em uma escala (ex: 1 a 10) e pode deixar um feedback em texto para o treinador ("Senti um desconforto no ombro", "Achei o exercício fácil demais").
- **O Diário Alimentar Flexível**:
  - O aluno visualiza seu plano alimentar do dia, com todas as refeições e seus componentes.
  - Ele pode marcar cada refeição como "realizada conforme o plano".
  - Caso faça alguma alteração (ex: trocou frango por peixe), ele pode editar a refeição, substituindo ou adicionando alimentos. O sistema recalcula automaticamente os totais de calorias e macros ingeridos, mostrando o desvio em relação à meta.
### Fase IV: O Acompanhamento (Fechando o Ciclo)
- **A Visão do Profissional**: O profissional não está no escuro. Ele tem acesso a um painel de controle onde visualiza a adesão e os dados registrados por seus alunos. Ele pode ver se a carga do aluno está progredindo, se ele está cumprindo a dieta, ler seus feedbacks e usar essas informações para fazer ajustes precisos no plano para a próxima fase.
- **O Registro da Evolução Corporal**: O aluno possui uma seção dedicada para registrar seu progresso físico de forma objetiva:
  - **Peso Corporal**: Registro periódico do peso.
  - **Medidas Corporais**: Registro de circunferências (cintura, quadril, braço, etc.).
  - **Fotos de Evolução**: Upload de fotos de frente, costas e perfil para comparação visual ao longo do tempo.
  - **Visualização do Progresso**: Todos esses dados (cargas nos exercícios, peso corporal, medidas) são transformados em gráficos simples e intuitivos, tanto para o aluno quanto para o profissional, tornando o progresso e os resultados algo tangível, mensurável e motivador.

## Visão Geral da Arquitetura do Sistema IARA (Baseada em DDD)
### Parte 1: Visão Geral dos Domínios (Bounded Contexts)
A arquitetura do sistema IARA é dividida em domínios de negócio claros e independentes, cada um com suas próprias responsabilidades e linguagem. Esta abordagem garante um sistema mais organizado, manutenível e escalável.
- **Domínio de Identidade e Acesso (IAM)**
  - **Responsabilidade**: Gerenciar quem são os usuários (Alunos, Treinadores, Nutricionistas), como eles se autenticam e o que têm permissão para fazer e ver na plataforma.
- **Domínio de Treinamento**
  - **Responsabilidade**: Lidar com toda a lógica de prescrição, execução e histórico de treinos físicos. É o domínio de atuação principal do Personal Trainer.
- **Domínio de Nutrição**
  - **Responsabilidade**: Lidar com toda a lógica de prescrição, execução e histórico de planos alimentares e suplementação. É o domínio de atuação principal do Nutricionista.
- **Domínio de Avaliação e Acompanhamento**
  - **Responsabilidade**: Coletar e gerenciar dados sobre a evolução do aluno, como anamneses, avaliações físicas (medidas e fotos) e feedbacks.
- **Domínio de Conteúdo e Bibliotecas**
  - **Responsabilidade**: Gerenciar o conteúdo genérico e reutilizável da plataforma, como a biblioteca central de exercícios e de alimentos.

### Parte 2: Detalhamento do Domínio de Identidade e Acesso (IAM)
Este domínio é a fundação da plataforma, garantindo a segurança e a correta gestão dos papéis de cada usuário.

#### 1. Visão Geral e Responsabilidades
A principal função deste contexto é responder às seguintes perguntas:

- **Identificação e Autenticação**: Quem é o usuário e ele é realmente quem diz ser?
- **Autorização**: O que este usuário pode fazer e ver no sistema?
- **Gerenciamento de Perfis**: Quais são os dados específicos de um Aluno, Treinador ou Nutricionista?
- **Gerenciamento de Vínculos**: Como os profissionais (Treinadores, Nutricionistas) se conectam e se desconectam de seus Alunos?

#### 2. Linguagem Ubíqua
- **Usuário**: Indivíduo que pode se autenticar no sistema.
- **Perfil**: Conjunto de atributos de um usuário em um papel específico (Aluno, Treinador, Nutricionista).
- **Papel (Role)**: Define um conjunto de permissões. Os papéis centrais são STUDENT, TRAINER, NUTRITIONIST.
- **Vínculo**: A relação formal e ativa entre um profissional e um aluno para um serviço específico.
- **Serviço**: O tipo de atividade profissional prestada no Vínculo, sendo TRAINING ou NUTRITION.

#### 3. Agregados e Entidades (Modelo Detalhado)
A modelagem separa a Autenticação (o User) dos Perfis de Domínio.

- **Agregado User**
  - Representa a identidade de autenticação de qualquer pessoa no sistema.
  - **Propriedades**:
    - id (UUID): Identificador único universal.
    - email (Objeto de Valor): Email de login, único no sistema.
    - password (Objeto de Valor): Armazena o hash seguro da senha.
    - status (Enum): PendingVerification, Active, Inactive.
    - roles (Array de Enum): Lista de papéis do usuário (ex: ['STUDENT', 'TRAINER']).

- **Agregado TrainerProfile**
  - Armazena os dados específicos do perfil de Personal Trainer.
  - **Propriedades**:
    - id (UUID): Mesmo ID do User correspondente, formando a ligação.
    - fullName (String).
    - crefNumber (String): Registro no Conselho Regional de Educação Física.

- **Agregado NutritionistProfile**
  - Armazena os dados específicos do perfil de Nutricionista.
  - **Propriedades**:
    - id (UUID): Mesmo ID do User correspondente.
    - fullName (String).
    - crnNumber (String): Registro no Conselho Regional de Nutricionistas.
    - specializations (Array de String).

- **Agregado StudentProfile**
  - Armazena os dados específicos do perfil de Aluno.
  - **Propriedades**:
    - id (UUID): Mesmo ID do User correspondente.
    - fullName (String).
    - dateOfBirth (Date).
    - goals (String).

- **Agregado Relationship (Vínculo)**
  - Gerencia a conexão profissional, sendo um dos agregados mais importantes para a lógica de negócio.
  - **Propriedades**:
    - id (UUID): ID único do vínculo.
    - professionalId (UUID): ID do usuário Treinador ou Nutricionista.
    - studentId (UUID): ID do usuário Aluno.
    - serviceType (Enum): TRAINING ou NUTRITION. Define o propósito do vínculo.
    - status (Enum): PendingInvitation, Active, Terminated.

#### 4. Principais Casos de Uso
- **RegisterNewUser**: Cria o User e o Profile correspondente (Aluno, Treinador ou Nutricionista).
- **AuthenticateUser**: Verifica as credenciais e retorna um token de acesso (JWT) contendo o userId e seus roles.
- **EstablishRelationship**: Permite que um profissional convide um aluno para um serviço específico, criando um Vínculo com status PendingInvitation.
- **AcceptRelationship**: Permite que o aluno aceite um convite, mudando o status do Vínculo para Active.

#### 5. Decisões de Arquitetura e Implementação
- **Autenticação**: Uso de JSON Web Tokens (JWT) como padrão. O token é enviado em cada requisição para validar a sessão do usuário.
- **Autorização**:
  - Baseada em Papel (Role-Based): Verificação simples dos roles no token para acesso a áreas gerais (ex: "só TRAINER pode acessar o dashboard de treinadores").
  - Baseada em Propriedade (Ownership-Based): Verificação complexa e essencial que consulta o agregado Relationship para garantir que um profissional só acesse os dados de um aluno com quem ele tem um vínculo ativo e do tipo de serviço correto.
- **Comunicação Inter-Contextos**: Preferencialmente via arquitetura orientada a eventos. Quando um StudentProfile é atualizado, o Contexto de Identidade dispara um evento (StudentProfileUpdated) para que os outros contextos atualizem suas cópias locais de dados (ex: nome do aluno), evitando acoplamento direto.
