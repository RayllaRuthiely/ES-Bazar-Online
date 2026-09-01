# Descoberta do problema

# Problema
A compra e venda de produtos usados ou novos entre moradores de Palmas é frequentemente realizada por meio de redes sociais e aplicativos de mensagens. Entretanto, essas ferramentas não são especificamente voltadas para a organização de anúncios, o que pode dificultar a busca por produtos disponíveis na cidade.

Além disso, os anúncios podem ficar dispersos entre diferentes grupos, páginas e conversas, tornando mais difícil encontrar produtos específicos, comparar opções e entrar em contato com os vendedores.

# Partes interessadas

| Parte | Categoria | Interesse | Poder | Contato |
|---|---|---|---|---|
| Comprador Local | Usa e é afetado | Encontrar itens na região, visualizar detalhes e falar com vendedores facilmente | Alto | Suporte / Canal do Usuário |
| Vendedor Local | Usa e é afetado | Publicar, gerenciar anúncios e alcançar compradores locais sem burocracia | Alto | Suporte / Canal do Usuário |
| Equipe de Desenvolvimento | Constroi e mantém | Cumprir o escopo do MVP, entregar incrementos a cada 2 semanas e manter revisões de PR | Alto | Equipe do Projeto |
| Provedores de Hospedagem | Afetado e suporta | Manter o ambiente do sistema funcional para o MVP | Baixo | Painel da Plataforma |

# Personas

## Persona 1: Mariana

* Perfil: Mariana, 22 anos, estudante e estagiária.
* Contexto: Com orçamento justo, prefere comprar itens usados em bom estado para economizar.
* Necessidade: Encontrar produtos seminovos anunciados na cidade com preços acessíveis, podendo retirar a compra no mesmo dia e negociar diretamente com o vendedor.

* Origem dos traços : fretes abusivos, busca por preços acessíveis e medo de comprar itens usados na internet e receber algo danificado ou diferente das fotos sem poder conferir antes, com base na fonte E1.

## Persona 2: Carlos
* Perfil: Carlos, 28 anos, profissional autônomo morando em Palmas.
* Contexto: Acuula itens em casa e deseja uma forma rápida e sem burocracia para vende-los.
* Origem dos traços (Carlos): Necessidade de cadastro rápido e frustração com mensagens repetitivas, com base na fonte E1.

# Fontes Consultadas

| Fonte Consultada | Data da Consulta | Duração / Extensão |
| :--- | :--- | :--- |
| E1- Grupos locais de comércio e aplicativos de revenda(OLX e Facebook MarketPlace) | 2026-08-31 | 30 minutos de observação |
| E2- Repositório Git da Equipe (`ES-Bazar-Online`) | 2026-08-19 a 2026-09-01 | Acompanhamento contínuo |

# Necessidades levantadas

| Id | Necessidade | Parte | Fonte | Situação |
|---|---|---|---|---|
| N1 | Visualizar catálogo de produtos disponíveis na região | Comprador Local | E1 | Confirmada |
| N2 | Cadastrar e gerenciar anúncios de itens usados com fotos e descrição | Vendedor Local | E1 | Confirmada |
| N3 | Filtrar produtos por categorias e faixas de preço | Comprador Local | E1 | Confirmada |
| N4 | Entrar em contato direto com o vendedor para negociar e combinar a entrega | Comprador Local | E1 | Confirmada |
| N5 | Controlar o status dos anúncios (ex: disponível, reservado, vendido) | Vendedor Local | E1 | Confirmada |

# Conflitos resolvidos

Não foi registrado nenhum conflito, tudo de acordo entre as partes e o cumprimento de prazo do MVP.

# Cenários

## Cenário Atual
Um morador de Palmas decide vender um item usado. Ele publica fotos em grupos abertos de redes sociais ou aplicativos de revenda. O anúncio rapidamente perde visibilidade no feed, atrai mensagens repetitivas de pessoas sem interesse real e exige repostagem para tentar novamente a venda. Do lado do comprador, encontrar um item específico exige buscar em vários grupos e apps sem garantia de disponibilidade, além de não ter certeza da condição do produto.

## Cenário Pretendido
O vendedor acessa o sistema e cadastra seu anúncio informando fotos, descrição, preço e categoria em um catálogo. O comprador acessa a plataforma, pesquisa o produto por palavra-chave ou categoria e visualiza apenas itens da sua região. Ao se interessar, clica no botão de contato direto do vendedor para combinar a retirada e o pagamento. Ao fechar o negócio, o vendedor altera o status do anúncio para "Vendido" ou "Reservado".

# Escopo

## Entra nesta versão
- Cadastro e login de usuários.
- Cadastro, edição e remoção de anúncios de produtos com fotos, descrição, preço e categoria.
- Visualização do catálogo de produtos disponíveis na região.
- Busca e filtragem de produtos por palavra-chave, categoria e faixa de preço.
- Exibição das informações de contato do vendedor para combinar entrega e pagamento.
- Gestão de status do anúncio (disponível, reservado ou vendido).

## Fora de escopo nesta versão
- Sistema de pagamento online — Motivo: Reduzir complexidade e riscos financeiros do MVP.
- Cálculo automático de frete — Motivo: O foco do sistema no momento é o comércio local em Palmas com entrega presencial.
- Sistema de avaliação de usuários — Motivo: Funcionalidade secundária que será implementada em iterações futuras após a validação do fluxo principal.
- Chat na própria plataforma em tempo real — Motivo: O contato inicial será redirecionado para canais de fora (ex: WhatsApp).

# MVP

A fatia escolhida para o MVP abrange o cadastro de anúncios pelo vendedor, a busca de itens pelo comprador e a exibição clara do contato para fechamento do negócio.

* Critério 1: Permite que compradores encontrem itens baratos na cidade e vendedores anunciem seus desapegos sem burocracia.
* Critério 2: Escopo viável para implementação em ciclos de 2 semanas.

Contagem de iterações: O MVP será entregue e validado ao longo de 3 iterações até a consolidação para o Encontro 9.

# Riscos iniciais

| Id | Risco | Prob. | Impacto | Ação e responsável |
|---|---|---|---|---|
| R1 | Baixa adesão inicial de vendedores cadastrando anúncios | Média | Alto | Divulgar a plataforma em grupos locais de Palmas. Responsável: Equipe de Marketing |
| R2 | Anúncios desatualizados permanecendo no catálogo | Alta | Médio | Implementar funcionalidade de alteração de status para "Vendido" e expiração de anúncios antigos. Responsável: Equipe de desenvolvimento |
| R3 | Tentativas de golpes | Média | Alto | Exigir validação de e-mail no cadastro e adicionar avisos de segurança sobre entregas presenciais. Responsável: Equipe de desenvolvimento |

# Histórico de revisão

- 2026-09-01: Escopo, detalhamento do MVP e alinhamento dos riscos iniciais.