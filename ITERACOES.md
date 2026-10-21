# Iterações — Bazar Online
O projeto Bazar Online utilizará um processo iterativo e incremental, com iterações de duas semanas. Cada iteração terá planejamento, desenvolvimento, acompanhamento, revisão, demonstração e retrospectiva.
A equipe é composta inicialmente por cinco integrantes. No início de cada iteração, será realizado um planejamento de aproximadamente 30 minutos para selecionar os itens do backlog, definir as responsabilidades e estimar o trabalho.
Durante o desenvolvimento, cada integrante deverá informar diariamente o andamento de suas tarefas. Ao final da iteração, será realizada uma demonstração das funcionalidades desenvolvidas, seguida de uma retrospectiva de aproximadamente 15 minutos.
Todo Pull Request deverá ser revisado e aprovado por pelo menos um integrante diferente de seu autor antes de ser integrado à branch main.

# Iteração 1 — Cadastro e publicação de anúncios
Duração: duas semanas.


  Objetivo

Implementar a base do sistema, permitindo que o usuário crie uma conta e que o vendedor cadastrado publique e gerencie anúncios de produtos no Bazar Online.



  Capacidade da equipe

- Integrantes: 5.
- Capacidade estimada: 100 horas.
- Pontos planejados: 8 pontos.


Itens selecionados do backlog
| Item | Descrição | Prioridade | Estimativa |
| --- | --- | --- | --- |
| HU-01 | Cadastro e login de usuário | Must | 3 |
| HU-02 | Cadastrar e gerenciar anúncio | Must | 5 |


Critérios de aceitação a verificar
- O sistema deve criar uma conta quando os dados obrigatórios forem informados corretamente.
- O sistema deve recusar cadastros com dados obrigatórios inválidos ou incompletos e informar o problema.
- O vendedor cadastrado deve conseguir publicar um anúncio com fotos, descrição, preço e categoria.
- O anúncio cadastrado deve permanecer disponível nas consultas posteriores, enquanto não for alterado, removido ou tiver seu status modificado.


Resultados da iteração
- Itens concluídos:
- Itens parcialmente concluídos:
- Itens não concluídos e devolvidos ao backlog:
- Pontos planejados:
- Pontos concluídos:
- Pull Requests integrados à main:
- Testes realizados:

Retrospectiva
- O que funcionou bem:
- O que apresentou problemas:
- Evidências analisadas:
- Melhorias para a próxima iteração:

  
Riscos e impedimentos
- Dificuldades na implementação do cadastro e da autenticação.
- Problemas na validação dos dados dos anúncios.

 #  Iteração 2 — Busca e visualização de produtos
 Duração: duas semanas.

Objetivo

Permitir que os compradores consultem os produtos anunciados, realizem buscas e visualizem as informações necessárias para avaliar os itens de interesse.

Capacidade da equipe
- Integrantes: 5.
- Capacidade estimada: 100 horas.
- Pontos planejados: 8 pontos.

Itens selecionados do backlog
| Item | Descrição | Prioridade | Estimativa |
| --- | --- | --- | --- |
| HU-03 | Buscar produtos | Must | 5 |
| HU-07 | Visualizar detalhes do produto | Should | 3 |

Critérios de aceitação a verificar
- O sistema deve apresentar anúncios correspondentes à pesquisa realizada.
- Quando não houver resultados, deve informar que nenhum produto foi encontrado.
- O comprador deve conseguir selecionar um anúncio e visualizar fotos, descrição, preço e categoria.
- Se um anúncio não estiver mais disponível para negociação, o sistema deve informar.

Resultados da iteração
- Itens concluídos:
- Itens parcialmente concluídos:
- Itens não concluídos e devolvidos ao backlog:
- Pontos planejados:
- Pontos concluídos:
- Pull Requests integrados à main:
- Testes realizados:

Retrospectiva
- O que funcionou bem:
- O que apresentou problemas:
- Evidências analisadas:
- Melhorias para a próxima iteração:

Riscos e impedimentos
- Busca retornando resultados incorretos ou incompletos.
- Anúncios vendidos ou indisponíveis aparecendo como disponíveis para negociação.

# Iteração 3 — Contato e consolidação do MVP

Duração: duas semanas.

Objetivo

Concluir o fluxo principal de negociação entre comprador e vendedor, consolidar as funcionalidades essenciais e validar o MVP do Bazar Online.

Capacidade da equipe
- Integrantes: 5.
- Capacidade estimada: 100 horas.
- Pontos planejados: 14 pontos.

Itens selecionados do backlog
| Item | Descrição | Prioridade | Estimativa |
| --- | --- | --- | --- |
| HU-04 | Entrar em contato com vendedor | Must | 3 |
| HU-05 | Filtrar produtos | Should | 3 |
| HU-06 | Gerenciar status do anúncio | Should | 5 |
| HU-08 | Remover anúncio | Must | 3 |

Critérios de aceitação a verificar

- O comprador deve conseguir visualizar a forma de contato disponibilizada pelo vendedor.
- Quando não houver forma de contato cadastrada, o sistema deve informar essa condição.
- O comprador deve conseguir filtrar produtos por categoria e faixa de preço.
- O vendedor deve conseguir alterar o status do anúncio para disponível, reservado ou vendido.
- O sistema deve impedir estados inválidos.
- Na parte de remoção de anúncios, o anúncio removido deverá deixar de aparecer no catálogo e nas buscas, permanecendo identificado como inativo no histórico do vendedor.

Resultados da iteração
- Itens concluídos:
- Itens parcialmente concluídos:
- Itens não concluídos e devolvidos ao backlog:
- Pontos planejados:
- Pontos concluídos:
- Pull Requests integrados à main:
- Testes realizados:

Retrospectiva
- O que funcionou bem:
- O que apresentou problemas:
- Evidências analisadas:
- Melhorias para a próxima iteração:

Riscos e impedimentos
- Contato do vendedor não ser exibido corretamente.
- Anúncios vendidos continuando disponíveis para negociação.

# Definição de pronto
Um item somente será considerado concluído quando:
- O requisito estiver implementado.
- O critério de aceitação estiver atendido.
- A funcionalidade tiver sido testada.
- O código estiver integrado ao restante do sistema.
- Outro integrante tiver revisado e aprovado o Pull Request.
- O Pull Request tiver sido integrado à branch main.
- A documentação necessária tiver sido atualizada.
- O item do backlog tiver sido encerrado.
























