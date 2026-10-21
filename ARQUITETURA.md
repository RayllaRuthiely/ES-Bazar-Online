# Arquitetura

Este documento diz onde cada parte do Bazar Online roda e como as partes conversam. Ele complementa o `PROJETO.md`, que diz de que o sistema é feito.

## Visão geral
Diagrama em `diagrams/arquitetura.mmd`.

O navegador conversa com o backend apenas pela API descrita na seção Contrato da API. Dentro do backend, as dependências seguem um sentido só: borda, domínio, persistência. O domínio não conhece requisição, resposta nem banco.

| Eixo | Pergunta | Resposta no Bazar Online |
|---|---|---|
| Decomposição | Em que partes lógicas o sistema se divide? | Frontend; backend em borda, domínio e persistência; banco |
| Distribuição | Em que máquinas cada parte executa? | Navegador do usuário, servidor da aplicação e servidor de banco |

## Responsabilidades
| Parte | Sabe | Faz |
|---|---|---|
| Frontend | apresentação e como pedir os dados | telas de login, catálogo, detalhe, novo anúncio, confirmação e meus anúncios; verificação de apoio; chama a API |
| Backend | regras do domínio | campos obrigatórios do anúncio, categorias aceitas (RN-01), transições de status (RN-02), ocultar vendidos e removidos (RN-03, CA-08.1); aplica as regras e responde |
| Banco | dados e integridade | guarda e recupera USUARIO, ANUNCIO e FOTO; chaves estrangeiras; unicidade de `email` |

Onde roda cada participante do diagrama `sequencia-publicar-anuncio.mmd`:

| Participante provisório | Parte | Por quê |
|---|---|---|
| Tela de cadastro de anúncio | Frontend | Coleta fotos e dados e mostra a recusa; não decide nada |
| Regra de validação | Backend, no domínio (Anúncio) | A D-03 isolou as regras em um módulo único, porque categorias e campos obrigatorios podem mudar |
| Repositório de anúncios | Backend, na persistência | O domínio decide gravar; a persistência e o banco apenas guardam |

O banco garante o que nunca pode ser violado (chave estrangeira, `email` único, campos não nulos). As regras que podem mudar ficam em um único módulo do backend (D-03).

## Onde cada parte roda
Diagrama em `diagrams/implantacao.mmd`.

Na primeira versão, o backend roda em um único processo (monólito modular, A-01), com um banco relacional e um armazenamento de fotos separado do banco, cujo local é decidido no Capítulo 14 (A-06).

## Contrato da API
Operações do sistema, derivadas do modelo de domínio e dos critérios de aceitação. O contrato detalhado de cada uma (entrada, regras, respostas e exemplos) vai para `contrato/operacoes.md` e `contrato/exemplos/`, ainda a fazer.

| Operação | Para quê | Origem |
|---|---|---|
| `POST /api/usuarios` | Criar conta | HU-01, CA-06.1, CA-06.2 |
| `POST /api/sessoes` | Entrar (login) | HU-01 |
| `GET /api/categorias` | Informar as categorias aceitas antes do formulário | RN-01, D-03 |
| `POST /api/anuncios` | Publicar anúncio com fotos | HU-02, CA-01.1, CA-01.2, UC-01 |
| `GET /api/anuncios?busca=&categoria=&precoMin=&precoMax=` | Catálogo, busca e filtro | HU-03, HU-05, CA-02.1, CA-02.2, CA-04.1, CA-04.2, RN-03 |
| `GET /api/anuncios/{id}` | Detalhe do produto com o contato do vendedor | HU-07, HU-04, CA-07.1, CA-07.2, CA-03.1, CA-03.2 |
| `PUT /api/anuncios/{id}/status` | Alterar o status | HU-06, CA-05.1, CA-05.2, CA-05.4 |
| `DELETE /api/anuncios/{id}` | Remover anúncio (apagamento lógico, D-01) | HU-08, CA-08.1 |
| `GET /api/usuarios/{id}/anuncios` | Meus anúncios, incluindo os inativos | UC-04, CA-08.2 |

O contrato usa nomes do domínio (`dataCriacao`), não nomes de coluna (`data_criacao`); a conversão acontece na persistência.

Códigos de status: 200 leitura ou alteração; 201 criação; 204 remoção; 404 recurso inexistente; 409 conflito com o estado atual (e-mail já cadastrado, transição de status proibida); 422 dados inválidos ou incompletos; 500 falha inesperada. 401 e 403 ficam para o Capítulo 13. Toda falha traz `erro` (código estável) e `mensagem` (texto para exibir).

## Verificações
| Verificação | Frontend | Backend |
|---|---|---|
| Campos obrigatórios do anúncio | marca e avisa | decide, 422 (CA-01.2) |
| Categoria válida | mostra só as de `GET /api/categorias` | decide, 422 (RN-01) |
| Preço maior que zero | campo numérico | decide, 422 |
| Pelo menos uma foto | avisa | decide, 422 |
| Status permitido e transição válida | mostra só as opções válidas | decide, 422 status inexistente (CA-05.2), 409 transição proibida |
| Só o dono altera ou remove | esconde os botões | decide em toda operação (403, Capítulo 13) |
| Vendido e removido fora do catálogo | não participa | filtra na consulta (RN-03, CA-08.1) |
| Data de criação | não participa | gera no servidor |
| E-mail único | não participa | decide, 409; banco garante com `UNIQUE` |
| Senha protegida | não participa | guarda só o hash (RNF-04) |

## Qualidades e custos
| Qualidade | Requisito | Decisão | Custo aceito |
|---|---|---|---|
| Desempenho | RNF-02: busca em até 3 segundos | Uma consulta única, com junção de anúncios e fotos e filtro no banco | Consulta mais complexa de escrever e testar |
| Compatibilidade | RNF-03: computador e celular | Frontend separado, que fala com o backend só pelo contrato | O contrato precisa ser mantido |
| Segurança | RNF-04: senha nunca em texto simples | Hash da senha no backend | Senha não pode ser recuperada, só redefinida |
| Confiabilidade | RNF-05 e composição Anúncio–Foto (1..*) | Gravar o anúncio e suas fotos em uma única transação | O anúncio não pode ser criado em duas chamadas |
| Manutenibilidade | D-03: categorias e campos podem mudar | Regras de validação em um módulo único do backend | Uma indireção a mais entre a tela e a regra |

## Decisões
| Id | Decisão | Motivo | Consequência aceita | Situação |
|---|---|---|---|---|
| A-01 | Monólito modular. Descartado: serviços separados | Cinco pessoas, um semestre, uma base de dados, e anúncio e fotos gravados em uma transação | Todo o sistema é implantado junto; as fronteiras dependem da disciplina do código | Aceita |
| A-02 | O backend decide toda verificação que importa; o frontend repete algumas para orientar. Descartado: validar só no frontend | O cliente pode ser contornado, e o CA-01.2 exige a recusa | Duas verificações para manter coerentes; o frontend lê as regras da API em vez de copiá-las | Aceita |
| A-03 | Contrato escrito antes da implementação, na pasta `contrato/`, alterado só por pull request revisado | Frontend e backend avançam em paralelo | Toda mudança de contrato passa por revisão das duas partes | Aceita |
| A-04 | Uma base relacional, acessada só pelo backend. Descartado: o frontend acessar o banco | Transação de anúncio e fotos; modelo de dados relacional do `PROJETO.md` | Toda consulta passa pelo backend | Aceita |
| A-05 | Data e hora geradas pelo servidor, em ISO 8601 com fuso. Descartado: data enviada pelo cliente | O relógio do cliente não é confiável, e `data_criacao` ordena o catálogo | Os testes precisam controlar o relógio | Aceita |
| A-06 | Local de guarda das fotos | Depende do ambiente de implantação | O backend é o único que conhece o local | Proposta, a decidir no Capítulo 14 |
| A-07 | Tecnologia do frontend, do backend e do banco | Em escolha pelos critérios da Tabela 7.11: conhecimento da equipe, documentação, licença, implantação gratuita e suporte a testes | — | Proposta, a decidir |

## Pontos em aberto
- Escolha da tecnologia (A-07), que depois entra no `REQUISITOS.md` como restrição RE e no `README.md`.
- Local das fotos enviadas: Capítulo 14 (A-06).
- Identificação e permissão nas operações: Capítulo 13.
- Contrato detalhado das operações em `contrato/operacoes.md`, começando por `POST /api/anuncios`, com um exemplo JSON para cada resposta em `contrato/exemplos/`.
- Confirmar se a transição Vendido -> Disponível é proibida (o diagrama de estados não tem essa seta).
- Expiração de anúncios antigos, citada no risco R2 do `DESCOBERTA.md`, ainda sem história no backlog.
- Tamanho máximo e formatos aceitos das fotos.

## Histórico de revisão
- 2026-10-21: primeira versão
