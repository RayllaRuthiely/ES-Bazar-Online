# Como contribuir com o Bazar Online

Este documento explica como a equipe trabalha no projeto e o que precisa ser feito para uma alteração entrar na `main`. O Bazar Online é um trabalho da disciplina de Engenharia de Software, então tentamos manter as regras simples.

Antes de mexer em qualquer coisa, vale ler o `README.md` e o `PROCESSO.md`. O primeiro explica o que o projeto é e o segundo explica como a gente se organiza (iterações, revisão e definição de pronto). Os requisitos estão no `REQUISITOS.md`.

## Código de conduta

Seja respeitoso e profissional. Críticas devem ser construtivas e focadas no código ou na ideia, nunca na pessoa. Comportamentos ofensivos, discriminatórios ou de assédio não serão tolerados. Como a equipe possui diferentes níveis de experiência, dúvidas e erros devem ser tratados com respeito. Todos devem ter liberdade para perguntar, aprender e contribuir.

## Como posso ajudar?

- **Reportando bugs** — abra uma *issue* descrevendo o problema.
- **Sugerindo melhorias** — novas funcionalidades, ajustes de usabilidade ou de visual.
- **Escrevendo casos de teste** — ajudam a garantir a qualidade do sistema.
- **Melhorando a documentação** — README, comentários, este guia.
- **Enviando código** — correções e novas funcionalidades via Pull Request.

## Trabalhando com Git

Ninguém faz commit direto na `main`. O caminho é sempre este:

1. Atualize a main local com `git pull`.
2. Crie uma branch a partir da main atualizada.
3. Faça as alterações e registre commits na branch criada.
4. Envie a branch ao repositório remoto com `git push`.
5. Abra um Pull Request para a main.
6. Aguarde a revisão e a aprovação de outra pessoa da equipe.
7. Após a aprovação, integre a alteração à main e remova a branch quando não for mais necessária.

## Prefixos que usamos nas branches

- `feat/`: para novas funcionalidades.
- `fix/`: para correções de defeitos.
- `docs/`: para alterações na documentação.
- `test/`: para criação ou modificação de testes.

### Mensagens de commit

Escreva o que foi feito de forma curta, começando com o tipo da alteração:

```text
feat: adiciona listagem de produtos
fix: corrige filtro por categoria
docs: atualiza requisitos
```

Os tipos mais usados são `feat`, `fix`, `docs`, `test` e `refactor`. Tente fazer commits pequenos, um por mudança, para facilitar a revisão.


## Pull Requests

Toda alteração destinada à `main` deverá ser proposta por meio de um Pull Request (PR).

Antes de abrir um PR, o autor deverá verificar se:

- A alteração está relacionada a uma issue ou tarefa do projeto.
- O PR contempla apenas um item do backlog.
- O código está organizado e a mudança é coerente.
- Os testes pertinentes foram executados.
- A documentação foi atualizada, quando necessário.
- A descrição explica o que mudou e como testar.
- Não foram incluídos segredos, senhas, tokens ou dados pessoais reais no repositório.

### Descrição do Pull Request

A descrição deverá informar:

- O objetivo da alteração.
- A issue ou tarefa relacionada.
- As principais mudanças realizadas.
- Os passos necessários para testar o resultado.

O repositório disponibiliza o modelo `.github/pull_request_template.md` para orientar o preenchimento dessas informações.

## Revisão de código

Todo PR deverá ser revisado e aprovado por pelo menos uma pessoa diferente de seu autor. Não é permitido aprovar o próprio PR.

A pessoa responsável pela revisão deverá responder em até 24 horas após a abertura do PR, informando se iniciará a análise ou se existe algum impedimento. Caso não consiga realizar a revisão nesse prazo, deverá comunicar a equipe para que outro integrante possa assumir.

A aprovação somente deverá ocorrer depois que os problemas que bloqueiam a integração forem resolvidos.

### Lista de verificação para revisão

A pessoa responsável pela revisão deverá utilizar a lista abaixo para avaliar as alterações antes da aprovação:

- **Critérios de aceitação:** a alteração atende ao que foi solicitado na tarefa?
- **Requisitos:** a implementação está de acordo com os requisitos do projeto?
- **Organização:** o código respeita a estrutura e a organização existentes?
- **Responsabilidades:** cada classe, função ou módulo possui uma responsabilidade clara?
- **Contratos:** as interfaces e os parâmetros utilizados estão corretos e são compatíveis com o restante do sistema?
- **Legibilidade:** os nomes de variáveis, funções e classes são claros? O código é fácil de compreender?
- **Manutenibilidade:** existem repetições desnecessárias ou trechos que poderiam ser simplificados?
- **Casos de uso e multiplicidade:** foram considerados os casos de ausência de dados, apenas um registro e vários registros, quando aplicável?
- **Segurança:** foram evitados problemas relacionados à exposição de dados, credenciais e informações sensíveis?
- **Testes:** os testes pertinentes foram executados e os resultados estão corretos?
- **Documentação:** a documentação foi atualizada quando necessário?
- **Rastreabilidade:** o PR está relacionado à issue, tarefa e requisito correspondente?

### Classificação dos comentários da revisão

Ao realizar comentários no código ou no PR, a equipe deverá classificá-los da seguinte maneira:

- **Bloqueia:** aponta um problema que precisa ser corrigido antes da aprovação.
- **Sugere:** apresenta uma melhoria recomendada, mas que não impede a integração.
- **Pergunta:** solicita esclarecimento sobre alguma decisão ou implementação.
- **Elogia:** reconhece uma solução ou prática bem realizada.

Os comentários devem ser objetivos, respeitosos e acompanhados de explicações quando necessário. A classificação ajuda a equipe a identificar o que precisa ser corrigido e o que representa apenas uma sugestão de melhoria.

### Resolução de divergências

Quando o autor e o revisor discordarem sobre alguma alteração, deverão apresentar suas justificativas de forma respeitosa e fundamentada nos requisitos, critérios de aceitação e padrões do projeto.

Caso a divergência não seja resolvida entre os dois integrantes, a questão deverá ser discutida com a equipe. A decisão deverá ser discutida e registrada no PR para manter a rastreabilidade.

Enquanto existir um problema classificado como **Bloqueia** sem solução, o PR não deverá ser aprovado.

## Quando uma tarefa está pronta

Seguimos a definição de pronto do `PROCESSO.md`. Resumindo, a tarefa só é fechada quando:

- O requisito foi implementado e o critério de aceitação foi atendido;
- A funcionalidade foi testada e está integrada ao resto do sistema;
- Outra pessoa revisou e o PR foi aprovado e integrado à `main`;
- A documentação necessária foi atualizada;
- O item do backlog foi encerrado.

## Encontrou um bug?

Abra uma issue contando o que aconteceu, o que você esperava que acontecesse e os passos para reproduzir. Se tiver print ou mensagem de erro, anexe também.

## Convivência e Colaboração

- Critique o código e as ideias, nunca a pessoa.
- Mantenha uma comunicação respeitosa e construtiva, independentemente do nível de experiência de cada integrante.
- Dúvidas, erros e dificuldades fazem parte do processo de aprendizagem e devem ser tratados com respeito, sem ofensas ou constrangimentos.
- Utilize o grupo da equipe ou as reuniões para esclarecer dúvidas, compartilhar conhecimentos e buscar soluções em conjunto.

## Licença

O projeto utiliza a licença MIT, e as contribuições devem respeitar os termos dessa licença. Consulte o arquivo `LICENSE` na raiz do repositório para conhecer as condições aplicáveis.
