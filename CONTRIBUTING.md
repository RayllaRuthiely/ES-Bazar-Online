# Como contribuir com o Bazar Online

Este documento explica como a equipe trabalha no projeto e o que precisa ser feito para uma alteração entrar na `main`. O Bazar Online é um trabalho da disciplina de Engenharia de Software, então tentamos manter as regras simples.

Antes de mexer em qualquer coisa, vale ler o `README.md` e o `PROCESSO.md`. O primeiro explica o que o projeto é e o segundo explica como a gente se organiza (iterações, revisão e definição de pronto). Os requisitos estão no `REQUISITOS.md`.

## Código de conduta
 
Seja respeitoso e profissional. Críticas devem ser construtivas e focadas no código ou na ideia, nunca na pessoa. Comportamentos ofensivos, discriminatórios ou de assédio não serão tolerados.
 
## Como posso ajudar?
 
- 🐛 **Reportando bugs** — abra uma *issue* descrevendo o problema.
- 💡 **Sugerindo melhorias** — novas funcionalidades, ajustes de usabilidade ou de visual.
- 🧪 **Escrevendo casos de teste** — ajudam a garantir a qualidade do sistema.
- 📝 **Melhorando a documentação** — README, comentários, este guia.
- 💻 **Enviando código** — correções e novas funcionalidades via Pull Request.

## Trabalhando com Git

Ninguém faz commit direto na `main`. O caminho é sempre este:

1. Atualize sua `main` local com `git pull`.
2. Crie uma branch a partir dela, com um nome que diga o que está sendo feito, por exemplo `feature/cadastro-usuario` ou `fix/busca-produtos`.
3. Faça seus commits na branch.
4. Dê push da branch e abra um Pull Request para a `main`.

Prefixos que usamos nas branches: `feature/`, `fix/`, `docs/` e `test/`.

### Mensagens de commit

Escreva o que foi feito de forma curta, começando com o tipo da alteração:

```
feat: adiciona listagem de produtos
fix: corrige filtro por categoria
docs: atualiza requisitos
```

Os tipos mais usados são `feat`, `fix`, `docs`, `test` e `refactor`. Tente fazer commits pequenos, um por mudança, para facilitar a revisão.

## Pull Requests

Todo Pull Request precisa ser revisado por pelo menos uma pessoa que não seja quem fez o código. Não vale aprovar o próprio PR.

Na descrição do PR, conte o que foi feito, qual tarefa ou issue ele resolve e como testar. Se mudou alguma tela, coloque um print.

Quem for revisar deve olhar se o critério de aceitação da tarefa foi atendido, testar se der e comentar o que achar que pode melhorar. Se estiver tudo certo, aprova. Se não, deixa o comentário e o autor ajusta.

Se a sua alteração mudar algum requisito ou o jeito de rodar o projeto, atualize o arquivo de documentação no mesmo PR.

## Quando uma tarefa está pronta

Seguimos a definição de pronto do `PROCESSO.md`. Resumindo, a tarefa só é fechada quando:

- o requisito foi implementado e o critério de aceitação foi atendido;
- a funcionalidade foi testada e está integrada ao resto do sistema;
- outra pessoa revisou e o PR foi aprovado e integrado à `main`;
- a documentação necessária foi atualizada;
- o item do backlog foi encerrado.

## Encontrou um bug?

Abra uma issue contando o que aconteceu, o que você esperava que acontecesse e os passos para reproduzir. Se tiver print ou mensagem de erro, anexa também.

## Convivência

Critique o código, não a pessoa. Como o grupo tem níveis diferentes de experiência, ninguém deve ser chamado de burro por perguntar ou errar. Dúvidas podem ser tiradas no grupo ou nas reuniões.

## Licença

O projeto usa a licença MIT, e as contribuições entram sob a mesma licença.
