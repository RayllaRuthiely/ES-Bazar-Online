# PROCESSO DE DESENVOLVIMENTO

O projeto Bazar Online utilizará um processo iterativo e incremental, com iterações de duas semanas.
A escolha foi realizada considerando os cinco fatores apresentados por Boehm e Turner: tamanho, criticidade, dinamismo, pessoal e cultura.



# 1.Escolha e justificativa

1.1 Tamanho

A equipe é composta inicialmente por cinco integrantes.
Por se tratar de uma equipe pequena, uma abordagem ágil é adequada, pois facilita a comunicação entre os integrantes e permite uma divisão simples das tarefas.
Tendência: ágil.

1.2 Criticidade

Baixa, o sistema não possui, inicialmente, requisitos de criticidade elevada.
Tendência: ágil.

1.3 Dinamismo

O projeto apresenta alto dinamismo porque os requisitos podem ser alterados durante o desenvolvimento.
Novas funcionalidades poderão ser identificadas a partir dos testes e das avaliações da equipe.
Tendência: ágil.

1.4 Pessoal

A equipe é composta por estudantes e os integrantes podem possuir diferentes níveis de experiência em desenvolvimento de sistemas e trabalho colaborativo.
Esse fator apresenta uma tendência parcialmente plano-dirigida, pois a falta de experiência conjunta pode gerar problemas de organização e integração.
Tendência: plano-dirigida.

1.5 Cultura

A equipe está disposta a trabalhar de forma colaborativa e aceitar alterações nos requisitos durante o desenvolvimento, desde que essas mudanças sejam registradas e avaliadas.
Tendência: ágil.

1.6 Resultado da avaliação   

| Fator | Característica do projeto | Tendência |
| --- | --- | --- |
| Tamanho | Equipe pequena, com 5 integrantes | Ágil |
| Criticidade | Projeto acadêmico sem alta criticidade | Ágil |
| Dinamismo | Requisitos podem sofrer alterações | Ágil |
| Pessoal | Diferentes níveis de experiência | Plano-dirigido |
| Cultura | Equipe colaborativa e aberta a mudanças | Ágil |

1.7 Compensação para o fator pessoal

Como o fator "pessoal" apresentou uma tendência para uma abordagem plano-dirigida, a equipe adotará algumas medidas para reduzir os riscos relacionados à falta de experiência conjunta.
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

2.1 Duração

Cada iteração terá duração de duas semanas.
O ciclo será:

- Planejamento;
- Desenvolvimento;
- Acompanhamento;
- Revisão;
- Demonstração;
- Retrospectiva.

2.2 Planejamento

Será realizado no início de cada iteração, com duração aproximada de 30 minutos.
Durante o planejamento serão escolhidas as tarefas do backlog que deverão ser realizadas na iteração.

2.3 Acompanhamento

Cada integrante deverá informar diariamente o andamento de suas tarefas por meio do canal definido pela equipe.

2.4 Demonstração

Ao final da iteração será realizada uma demonstração das funcionalidades desenvolvidas.
A demonstração será realizada preferencialmente na sexta-feira da segunda semana.
A condução da demonstração será realizada em sistema de rodízio entre os integrantes.

2.5 Retrospectiva

Após a demonstração será realizada uma retrospectiva de aproximadamente 15 minutos.
A equipe deverá discutir:

- O que funcionou bem;
- O que apresentou problemas;
- O que deverá ser melhorado na próxima iteração.



# 3. Papéis
   
3.1 Responsável pelo backlog

Será responsável por organizar e priorizar as funcionalidades que deverão ser desenvolvidas.
Responsável: Todos

 3.2 Responsável pela demonstração

A demonstração será realizada em sistema de rodízio.

 3.3 Revisores

Todo Pull Request deverá ser revisado por pelo menos um integrante diferente daquele que realizou a implementação.



# 4. Definição de pronto

Uma tarefa será considerada pronta somente quando:

- O requisito estiver implementado;
- O critério de aceitação estiver atendido;
- A funcionalidade tiver sido testada;
- O código estiver integrado ao restante do sistema;
- Outro integrante tiver revisado o código;
- O Pull Request tiver sido aprovado;
- O Pull Request tiver sido integrado à main;
- A documentação necessária tiver sido atualizada;
- O item do backlog tiver sido encerrado.



# 5. Revisão de código

Todo Pull Request deverá passar por uma revisão realizada por pelo menos um integrante diferente de seu autor.

A revisão deverá utilizar a lista de verificação definida no CONTRIBUTING.md e disponibilizada no arquivo .github/pull_request_template.md.

Durante a revisão, deverão ser observados os seguintes aspectos:

- Atendimento aos critérios de aceitação;
- Conformidade com os requisitos;
- Organização e responsabilidades do código;
- Compatibilidade das interfaces e dos parâmetros;
- Legibilidade e manutenibilidade;
- Tratamento dos diferentes casos de uso;
- Execução dos testes pertinentes;
- Atualização da documentação;
- Rastreabilidade entre o Pull Request e a tarefa correspondente.

5.1 Classificação dos comentários

Os comentários realizados durante as revisões deverão ser classificados em quatro categorias:

- **Bloqueia:** problemas que precisam ser corrigidos antes da aprovação do Pull Request.
- **Sugere:** melhorias recomendadas, mas que não impedem a integração.
- **Pergunta:** dúvidas ou solicitações de esclarecimento sobre a implementação.
- **Elogia:** reconhecimento de soluções ou práticas bem realizadas.

Os comentários deverão ser objetivos e respeitosos, priorizando a melhoria do código e evitando críticas pessoais.



# 6. Gerenciamento da dívida técnica

Durante o desenvolvimento, poderão ser identificados problemas ou soluções provisórias que facilitem a implementação imediata, mas que possam gerar dificuldades futuras de manutenção e evolução do sistema.

Esses problemas deverão ser registrados no backlog como dívida técnica, mesmo quando não forem corrigidos imediatamente.

6.1 Registro da dívida técnica

Cada dívida técnica deverá apresentar os seguintes campos:

- **Localização:** arquivo, classe, função ou parte do sistema onde o problema foi identificado.
- **Origem:** motivo pelo qual a dívida foi gerada.
- **Custo de carregar:** esforço ou dificuldade adicional causada pela manutenção da dívida.
- **Custo de pagar:** estimativa do esforço necessário para corrigir o problema, expressa em pontos.
- **Gatilho:** situação ou condição que indicará o momento adequado para resolver a dívida.

6.2 Reserva técnica da iteração 3

Na iteração 3, a equipe deverá avaliar as dívidas técnicas registradas e selecionar aquelas que poderão ser resolvidas utilizando a reserva técnica disponível.

Os itens selecionados deverão ser identificados no backlog, considerando sua estimativa em pontos e a capacidade disponível da equipe.

A seleção deverá priorizar problemas que possam comprometer a manutenção, a organização ou a evolução do sistema.


# 7. Histórico de revisão do processo

| Data       | Versão | Alteração |
|------------|--------|-----------|
| 2026-08-20 | 1.0    | Versão inicial do processo |
| 2026-11-12 | 1.1    | Inclusão dos procedimentos de revisão de código, classificação dos comentários e gerenciamento da dívida técnica |







