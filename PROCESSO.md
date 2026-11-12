# PROCESSO DE DESENVOLVIMENTO

O projeto Bazar Online utilizará um processo iterativo e incremental, com iterações de duas semanas. A escolha foi realizada considerando os cinco fatores apresentados por Boehm e Turner: tamanho, criticidade, dinamismo, pessoal e cultura.

# 1. Escolha e justificativa

## 1.1 Tamanho

A equipe é composta inicialmente por cinco integrantes. Por se tratar de uma equipe pequena, uma abordagem ágil é adequada, pois facilita a comunicação entre os integrantes e permite uma divisão simples das tarefas.

**Tendência: ágil.**

## 1.2 Criticidade

O sistema não possui, inicialmente, requisitos de criticidade elevada. Por se tratar de um projeto acadêmico, os riscos associados à sua utilização são relativamente baixos.

**Tendência: ágil.**

## 1.3 Dinamismo

O projeto apresenta alto dinamismo porque os requisitos podem ser alterados durante o desenvolvimento. Novas funcionalidades poderão ser identificadas a partir dos testes e das avaliações da equipe.

**Tendência: ágil.**

## 1.4 Pessoal

A equipe é composta por estudantes que podem possuir diferentes níveis de experiência em desenvolvimento de sistemas e trabalho colaborativo. Esse fator apresenta uma tendência parcialmente plano-dirigida, pois os diferentes níveis de experiência podem exigir maior acompanhamento, orientação e padronização das atividades.

**Tendência: plano-dirigida.**

## 1.5 Cultura

A equipe está disposta a trabalhar de forma colaborativa e aceitar alterações nos requisitos durante o desenvolvimento, desde que essas mudanças sejam registradas e avaliadas.

**Tendência: ágil.**

## 1.6 Resultado da avaliação

| Fator | Característica do projeto | Tendência |
|---|---|---|
| Tamanho | Equipe pequena, com 5 integrantes | Ágil |
| Criticidade | Projeto acadêmico sem alta criticidade | Ágil |
| Dinamismo | Requisitos podem sofrer alterações | Ágil |
| Pessoal | Diferentes níveis de experiência | Plano-dirigida |
| Cultura | Equipe colaborativa e aberta a mudanças | Ágil |

## 1.7 Compensação para o fator pessoal

Como o fator pessoal apresentou uma tendência para uma abordagem plano-dirigida, a equipe adotará medidas para reduzir os riscos relacionados aos diferentes níveis de experiência e à falta de experiência conjunta.

Serão utilizadas as seguintes compensações:

- Documentação das decisões importantes;
- Revisão obrigatória dos Pull Requests;
- Definição clara das responsabilidades;
- Critérios de aceitação para as tarefas;
- Registro das alterações relevantes;
- Reuniões de planejamento e retrospectiva;
- Atualização da documentação quando necessário.

Dessa forma, o projeto mantém a flexibilidade de uma abordagem ágil sem deixar de possuir mecanismos de organização e controle.

# 2. Iterações

## 2.1 Duração

Cada iteração terá duração de duas semanas. O ciclo será composto pelas seguintes atividades:

- Planejamento;
- Desenvolvimento;
- Acompanhamento;
- Revisão;
- Demonstração;
- Retrospectiva.

## 2.2 Planejamento

Será realizado no início de cada iteração, com duração aproximada de 30 minutos.

Durante o planejamento, serão selecionadas as tarefas do backlog que deverão ser realizadas na iteração. Cada item selecionado deverá possuir uma descrição compreensível, critérios de aceitação e estimativa de esforço.

A seleção deverá considerar a capacidade disponível da equipe e as prioridades do projeto.

## 2.3 Acompanhamento

Cada integrante deverá informar diariamente o andamento de suas tarefas por meio do canal definido pela equipe.

Dificuldades, atrasos e impedimentos deverão ser comunicados para que possam ser avaliados e tratados coletivamente.

## 2.4 Demonstração

Ao final da iteração será realizada uma demonstração das funcionalidades desenvolvidas.

A demonstração será realizada preferencialmente na sexta-feira da segunda semana. Sua condução será realizada em sistema de rodízio entre os integrantes.

## 2.5 Retrospectiva

Após a demonstração será realizada uma retrospectiva de aproximadamente 15 minutos.

A equipe deverá discutir:

- O que funcionou bem;
- O que apresentou problemas;
- Quais evidências foram observadas durante a iteração;
- O que deverá ser melhorado na próxima iteração.

As melhorias identificadas deverão ser registradas para acompanhamento nas iterações seguintes.

# 3. Papéis

## 3.1 Responsável pelo backlog

A equipe será responsável coletivamente por identificar, discutir, organizar e priorizar os itens do backlog. A atualização dos registros será realizada em conjunto pelos integrantes.

## 3.2 Responsável pela demonstração

A demonstração será realizada em sistema de rodízio entre os integrantes.

## 3.3 Revisores

Todo Pull Request deverá ser revisado por pelo menos um integrante diferente daquele que realizou a implementação.

A escolha do revisor deverá considerar sua disponibilidade e seu conhecimento sobre a alteração.

# 4. Definição de pronto

Uma tarefa será considerada pronta somente quando:

- O requisito estiver implementado;
- O critério de aceitação estiver atendido;
- A funcionalidade tiver sido testada;
- O código estiver integrado ao restante do sistema;
- O código apresentar organização, legibilidade e facilidade de manutenção;
- A alteração estiver relacionada à issue ou tarefa correspondente;
- Não houver exposição indevida de senhas, tokens, credenciais ou dados pessoais reais;
- Outro integrante tiver revisado o código;
- O Pull Request tiver sido aprovado;
- O Pull Request tiver sido integrado à branch `main`;
- A documentação necessária tiver sido atualizada;
- O item do backlog tiver sido encerrado.

# 5. Revisão de código

Todo Pull Request deverá passar por uma revisão realizada por pelo menos um integrante diferente de seu autor.

A revisão deverá utilizar a lista de verificação definida no `CONTRIBUTING.md` e disponibilizada no arquivo `.github/pull_request_template.md`.

Durante a revisão, deverão ser observados os seguintes aspectos:

- Atendimento aos critérios de aceitação;
- Conformidade com os requisitos;
- Organização e responsabilidades do código;
- Compatibilidade das interfaces e dos parâmetros;
- Legibilidade e manutenibilidade;
- Tratamento dos diferentes casos de uso e multiplicidade;
- Segurança e proteção dos dados;
- Execução dos testes pertinentes;
- Atualização da documentação;
- Rastreabilidade entre o Pull Request, a tarefa e o requisito correspondente.

O revisor deverá responder em até 24 horas após a abertura do PR, informando o andamento da revisão ou eventuais impedimentos. Caso não consiga realizar a análise nesse prazo, deverá comunicar a equipe para que outro integrante possa assumir.

A aprovação deverá ocorrer somente após a resolução dos problemas que bloqueiam a integração.

## 5.1 Classificação dos comentários

Os comentários realizados durante as revisões deverão ser classificados em quatro categorias:

- **Bloqueia:** problemas que precisam ser corrigidos antes da aprovação do Pull Request.
- **Sugere:** melhorias recomendadas, mas que não impedem a integração.
- **Pergunta:** dúvidas ou solicitações de esclarecimento sobre a implementação.
- **Elogia:** reconhecimento de soluções ou práticas bem realizadas.

Os comentários deverão ser objetivos e respeitosos, priorizando a melhoria do código e evitando críticas pessoais.

## 5.2 Resolução de divergências

Quando houver divergência entre o autor e o revisor, ambos deverão apresentar suas justificativas com base nos requisitos, critérios de aceitação e padrões estabelecidos pelo projeto.

Caso não seja possível chegar a um consenso, a questão deverá ser discutida com a equipe. A decisão deverá ser registrada no Pull Request para manter a rastreabilidade.

# 6. Gerenciamento da dívida técnica

Durante o desenvolvimento, poderão ser identificados problemas ou soluções provisórias que facilitem a implementação imediata, mas que possam gerar dificuldades futuras de manutenção e evolução do sistema.

Esses problemas deverão ser registrados no backlog como dívida técnica, mesmo quando não forem corrigidos imediatamente.

## 6.1 Registro da dívida técnica

Cada dívida técnica deverá apresentar os seguintes campos:

- **Localização:** arquivo, classe, função ou parte do sistema onde o problema foi identificado.
- **Origem:** motivo pelo qual a dívida foi gerada.
- **Custo de carregar:** esforço ou dificuldade adicional causada pela manutenção da dívida.
- **Custo de pagar:** estimativa do esforço necessário para corrigir o problema, expressa em pontos.
- **Gatilho:** situação ou condição que indicará o momento adequado para resolver a dívida.

Os custos deverão ser estimados pela equipe e registrados nas issues correspondentes.

## 6.2 Reserva técnica

A partir da Iteração 3, a equipe destinará uma reserva de 2 pontos por iteração para a resolução de dívidas técnicas.

A seleção dos itens deverá considerar:

- O custo de carregar a dívida;
- O custo de pagar a dívida;
- Os gatilhos registrados;
- Os riscos para a manutenção e evolução do sistema;
- A capacidade disponível da equipe.

Os pontos destinados ao trabalho técnico deverão ser considerados no planejamento da capacidade total da iteração, não sendo tratados como capacidade adicional.

As dívidas não selecionadas permanecerão registradas no backlog para avaliação nas próximas iterações.

# 7. Características de qualidade do produto

A equipe utilizará características de qualidade para orientar as decisões de desenvolvimento e avaliar o produto ao longo das iterações.

As características prioritárias para o Bazar Online serão:

| Característica | Aplicação no projeto | Evidência de avaliação |
|---|---|---|
| Segurança | Proteger os dados dos usuários e evitar exposição de informações sensíveis. | Revisão de código e testes relacionados à proteção de dados. |
| Manutenibilidade | Facilitar correções, alterações e inclusão de novas funcionalidades. | Organização do código, responsabilidades claras e revisão de código. |
| Eficiência de desempenho | Permitir consultas e buscas de produtos sem demora desnecessária. | Testes de busca e observação do tempo de resposta. |
| Capacidade de interação | Facilitar a utilização do sistema por compradores e vendedores. | Testes de utilização e avaliação das funcionalidades. |

## 7.1 Decisões e custos de qualidade

A equipe deverá considerar que decisões de desenvolvimento podem favorecer determinadas características de qualidade e exigir esforço adicional em outras.

Por exemplo:

- Priorizar a segurança pode exigir mais tempo para implementar validações e controles de acesso.
- Melhorar a manutenibilidade pode exigir refatoração e reorganização do código.
- Melhorar o desempenho das buscas pode exigir otimizações e estruturas adicionais.
- Melhorar a capacidade de interação pode exigir avaliações e ajustes na interface.

Esses custos deverão ser considerados durante o planejamento e registrados quando representarem decisões importantes para o projeto.

A equipe deverá buscar equilíbrio entre as características, considerando os requisitos, os riscos e a capacidade disponível.

# 8. Medição da qualidade do processo

A equipe utilizará o método GQM (Goal-Question-Metric), que relaciona objetivos, perguntas e métricas, para acompanhar a qualidade do processo de desenvolvimento.

As medições serão utilizadas para identificar problemas, avaliar resultados e orientar melhorias nas próximas iterações.

## 8.1 Objetivos, perguntas e métricas

| Objetivo | Pergunta | Métrica |
|---|---|---|
| Melhorar o processo de revisão | Quanto tempo os Pull Requests levam para ser integrados? | Tempo entre a abertura e a integração dos PRs. |
| Identificar problemas encontrados nas revisões | Quantos problemas classificados como bloqueadores são identificados? | Quantidade de comentários classificados como Bloqueia. |
| Avaliar a qualidade das entregas | Quantos defeitos são identificados após a integração? | Quantidade de defeitos registrados em issues após a integração. |
| Verificar a aderência ao processo | As atividades e regras estabelecidas estão sendo cumpridas? | Verificação dos itens de planejamento, revisão e definição de pronto. |
| Avaliar a eficácia do processo | As entregas estão atendendo aos requisitos e critérios de aceitação? | Quantidade de itens concluídos que atendem aos critérios de aceitação. |

## 8.2 Coleta e análise dos dados

Os dados serão obtidos a partir das issues, Pull Requests, testes e registros das iterações no repositório.

A equipe deverá acompanhar:

- Datas de abertura, revisão e integração dos Pull Requests;
- Comentários registrados durante as revisões;
- Defeitos identificados após a integração;
- Itens planejados e efetivamente concluídos;
- Resultados dos testes e critérios de aceitação.

Os resultados serão discutidos durante as retrospectivas.

As métricas deverão ser analisadas em conjunto, considerando o tamanho das alterações e o contexto de cada iteração. A quantidade de comentários bloqueadores, por exemplo, não deverá ser interpretada isoladamente como uma medida de desempenho individual ou como prova de baixa qualidade.

## 8.3 Aderência e eficácia do processo

A equipe avaliará duas dimensões:

- **Aderência:** verifica se as práticas definidas no processo estão sendo seguidas, como a utilização de branches, a revisão dos PRs e o cumprimento da definição de pronto.
- **Eficácia:** verifica se o processo está contribuindo para a entrega de funcionalidades que atendem aos requisitos, com funcionamento adequado e quantidade controlada de defeitos.

Quando forem identificados desvios ou resultados insatisfatórios, a equipe deverá registrar as dificuldades e definir melhorias para as próximas iterações.

# 9. Histórico de revisão do processo

| Data | Versão | Alteração |
|---|---|---|
| 2026-08-20 | 1.0 | Versão inicial do processo. |
| 2026-11-11 | 1.1 | Inclusão dos procedimentos de revisão de código, classificação dos comentários e gerenciamento da dívida técnica. |
| 2026-11-12 | 1.2 | Inclusão das regras de resolução de divergências, características de qualidade do produto, medição pelo método GQM e avaliação da aderência e eficácia do processo. |







