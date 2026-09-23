# Projeto

## Modelo de domínio

Diagrama em `diagrams/dominio.mmd`.

| Classe | Origem no REQUISITOS.md | Observação |
|---|---|---|
| Usuário | HU-06 | Cadastro e login; `contato` fica aqui, não por anúncio — a confirmar (ver Decisões, D-02) |
| Anúncio | CA-01.1, CA-05.1, CA-07.1 | Reúne o que o glossário separa em "Anúncio" e "Produto"; RN-01 e RN-02 justificam `categoria` e `status` |
| Foto | CA-01.1 | Anúncio tem "fotos" no plural — composição, não existe fora do anúncio |

Substantivos do glossário descartados do modelo, com motivo:

| Substantivo | Decisão | Motivo |
|---|---|---|
| Comprador / Vendedor | Papel do usuário, não classe | Mesma pessoa pode comprar e vender; nenhum atributo extra exigido só por um dos papéis |
| Produto | Absorvido em Anúncio | Glossário e CA-01.1 tratam produto e anúncio como a mesma publicação |
| Categoria | Atributo de valor restrito de Anúncio | RN-01 lista um conjunto fechado (roupas, calçados, acessórios, outros) |
| Catálogo | Fora do modelo de domínio | É a consulta sobre os anúncios, não um conceito com dado próprio |
| Status do anúncio | Atributo restrito de Anúncio | RN-02: disponível / reservado / vendido |
| Localização | Fora do modelo, por ora | RE-01 fixa Palmas-TO como restrição do sistema inteiro, não um dado por anúncio |

## Modelo de dados

Diagrama em `diagrams/dados.mmd`.

Estratégia de identidade: chave artificial (`id`) em todas as tabelas; `email` como restrição de unicidade em `USUARIO`, não como chave primária.

Apagamento: lógico, com coluna `ativo` em `USUARIO` e `ANUNCIO` — decisão sujeita a discussão (ver D-01).

Tempo: `data_criacao` em timestamp, não texto, para permitir ordenação e comparação (RNF-02 exige busca em até 3s).

Arquivo: `FOTO` guarda apenas a URL/caminho da imagem; o arquivo em si fica fora do banco.

Segurança: `senha_hash`, nunca senha em texto simples (RNF-04).

## Comportamento

Sequência do fluxo principal (UC-01) em `diagrams/sequencia-publicar-anuncio.mmd`.
Estados do anúncio em `diagrams/estados-anuncio.mmd`.

Lacunas encontradas pelo diagrama de estados, levadas ao `REQUISITOS.md`:
Ambas as lacunas foram resolvidas: viraram CA-05.4 (cancelamento de reserva) e HU-08 (remoção de anúncio) no `REQUISITOS.md`.

1. Transição Reservado → Disponível (cancelar reserva) não tem CA correspondente.
2. Remoção de anúncio (qualquer estado → Removido) não tem CA própria; UC-04 só cita "remover" sem descrever o efeito (some do catálogo? fica visível no histórico do vendedor?).

## Distribuição de responsabilidades

| Parte | Sabe | Faz |
|---|---|---|
| Anúncio | próprio status, próprias fotos | decide transições de status permitidas; valida-se antes de publicar |
| Regra de validação | campos obrigatórios do anúncio | aprova ou recusa o cadastro, isolada da tela |

## Decisões de projeto

| Id | Decisão | Motivo | Consequência aceita |
|---|---|---|---|
| D-01 | Apagamento lógico (`ativo`) em Usuário e Anúncio | RN-04: vendedor é responsável pelo que anunciou; histórico deve sobreviver à remoção | Uma condição a mais em cada consulta |
| D-02 | Contato fica em Usuário, não em Anúncio | CA-03.1 fala em "forma de contato disponibilizada pelo vendedor", no singular ligado ao vendedor | Vendedor não pode ter contato diferente por anúncio |
| D-03 | Regras de validação do anúncio isoladas da tela, em módulo único | Teste de Parnas: categorias e campos obrigatórios têm chance real de mudar durante o semestre | Uma indireção a mais entre tela e regra |

## Protótipo

Telas do fluxo principal (UC-01) em `prototipo/`:
1. Meus anúncios (lista + botão "novo anúncio")
2. Novo anúncio (formulário: fotos, descrição, preço, categoria)
3. Anúncio publicado (confirmação, status Disponível)

Recusas por dados incompletos (A1) e inválidos (A2) aparecem como mensagem na tela 2, preservando o preenchimento.

## Conferência cruzada

| Pergunta | Verificado | Resultado |
|---|---|---|
| CA-03.1 exige mostrar a forma de contato do vendedor — a tela de detalhe lê `contato` de Usuário? | Pendente | — |
| RN-03 exige que anúncio Vendido não apareça como disponível — a tela de catálogo filtra por `status`? | Pendente | — |

## Histórico de revisão

- 2026-09-21: primeira versão, encontro 6.
