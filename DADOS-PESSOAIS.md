# Dados pessoais

Inventário dos dados pessoais que o Bazar Online trata, conforme a LGPD (Lei n.º 13.709/2018). Para cada dado, o inventário diz para que ele serve, quem o acessa, onde fica e por quanto tempo é guardado.

A equipe usa a lei para orientar decisões de projeto. As perguntas que só o controlador responde, como finalidade e retenção, estão registradas no `REQUISITOS.md` (P4 a P7) e são atualizadas aqui quando a resposta chegar.

## 1. Papéis

| Termo da LGPD | No Bazar Online |
|---|---|
| Titular | Quem cria conta: vendedores e compradores |
| Controlador | A confirmar com o professor (P7): quem decide para que os dados servem |
| Operador | A confirmar com o professor (P7): o papel da equipe em relação aos dados |
| Tratamento | Coletar o cadastro, guardar o anúncio, exibir o contato do vendedor ao comprador, desativar a conta |

O sistema não coleta **dados pessoais sensíveis** (saúde, origem racial ou étnica, religião, opinião política). As fotos dos anúncios são uma exceção possível: uma foto pode mostrar o rosto do vendedor ou o interior da casa dele (ver seção 3).

## 2. Inventário

| Dado | Finalidade | Quem acessa | Onde fica | Retenção |
|---|---|---|---|---|
| Nome | Identificar o vendedor no anúncio e no contato (HU-01, HU-04) | O próprio usuário; compradores, na página do produto | Banco, tabela `USUARIO` (`NOME_USUARIO`) | A confirmar com o professor (P5) |
| E-mail | Identificar a conta no login (HU-01) | O próprio usuário; o sistema, para autenticar | Banco, tabela `USUARIO` (`EMAIL_USUARIO`) | A confirmar com o professor (P5) |
| Senha | Autenticar o usuário (HU-01) | Ninguém: o sistema guarda só o hash e compara no login (RNF-04) | Banco, tabela `USUARIO` (`SENHA_USUARIO`, hash) | Enquanto a conta existir |
| Telefone | Permitir que o comprador combine a negociação com o vendedor (HU-04, CA-03.1) | O próprio usuário; compradores, ao pedir contato | Banco, tabela `USUARIO` (`TELEFONE_USUARIO`) | A confirmar com o professor (P5) |
| Situação da conta | Desativar a conta sem apagar o histórico (D-01) | O sistema | Banco, tabela `USUARIO` (`ATIVO_USUARIO`) | Igual à do usuário |
| Vínculo anúncio–vendedor | Saber quem publicou cada anúncio e quem pode alterá-lo (RN-04, HU-06, HU-08) | O sistema; o vendedor, em "Meus anúncios" | Banco, tabela `ANUNCIO` (`ID_USUARIO`) | A confirmar com o professor (P6) |
| Data de publicação | Ordenar o catálogo e registrar quando o anúncio foi feito | Todos, enquanto o anúncio estiver ativo; depois, só o vendedor | Banco, tabela `ANUNCIO` (`DATA_PUBLICACAO_ANUNCIO`) | Igual à do anúncio |
| Fotos do anúncio | Mostrar o produto ao comprador (HU-02, HU-07) | Todos, enquanto o anúncio estiver ativo; depois, só o vendedor | Arquivos em `static/uploads/`; caminho na tabela `FOTO` | A confirmar com o professor (P6) |
| Sessão de login | Manter o usuário conectado entre as páginas | O próprio navegador do usuário; o servidor confere a assinatura | Cookie assinado com a `SECRET_KEY` | Até o usuário sair ou fechar o navegador |

## 3. Pontos de atenção

**Telefone exposto a compradores.** Pela HU-04, o comprador vê o telefone do vendedor. Hoje não está decidido se isso vale para qualquer visitante ou só para quem tem conta (P4). A coluna "Quem acessa" precisa concordar com a política de acesso do `ARQUITETURA.md`.

**Telefone obrigatório.** A tabela `USUARIO` exige telefone (`NOT NULL`), mas a HU-04 prevê o vendedor que não disponibiliza contato (CA-03.2). Pelo princípio da necessidade, o telefone poderia ser opcional, e o sistema perderia só o contato direto com quem não quiser informar.

**Apagamento lógico guarda os dados indefinidamente.** A decisão D-01 mantém usuário e anúncio no banco depois da remoção, com `ativo = 0`. Isso atende à RN-04 (histórico do vendedor), mas a LGPD manda eliminar os dados ao fim do tratamento (art. 16). Falta definir por quanto tempo os dados de contas e anúncios desativados ficam guardados (P5 e P6).

**Fotos podem identificar o vendedor.** Uma foto pode mostrar o rosto do vendedor, outras pessoas ou o endereço. O sistema não verifica isso. Uma orientação na tela de novo anúncio ("evite fotos com pessoas ou com o endereço visível") reduz o risco sem custo técnico.

**Direito de acesso e correção.** A LGPD dá ao titular o direito de ver e corrigir os próprios dados (art. 18). Hoje o sistema não tem uma tela de perfil para isso. Fica registrado como necessidade para o backlog.

## 4. Dados pessoais fora do banco

| Onde | Regra adotada |
|---|---|
| Testes automatizados | Usam apenas dados fictícios (nomes e e-mails inventados) e banco simulado |
| Banco local de desenvolvimento | Cada integrante usa dados de teste inventados, nunca dados reais de outras pessoas |
| Mensagens de erro no terminal | As rotas imprimem o erro do banco com `print`. Um erro de duplicidade pode conter o e-mail digitado. Não registrar senha nem dados do formulário nas mensagens |
| Repositório | Nenhum dado pessoal real e nenhuma credencial (o `.env` fica fora do Git; ver `.env.example`) |

## 5. Em caso de vazamento

Se dados pessoais vazarem, a equipe avisa o professor imediatamente, informando o que vazou, desde quando e quem foi afetado. Comunicar a autoridade nacional e os titulares (LGPD, art. 48) é dever do controlador.

## 6. Histórico de revisão

- 2026-11-24: primeira versão do inventário, encontro 13
