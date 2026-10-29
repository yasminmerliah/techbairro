# Entrega final da TechBairro
Aluno(a): Yasmin Vitoria Silva Dos Santos
Versão entregue: 3.3.2

Por que esse número de versão:
> Porque só houve acréscimo de documentação, manual, testes e README — nenhuma função nova foi criada. Como é só ajuste de texto, soma 1 no último número: 3.3.1 → 3.3.2.

| # | Item | Evidência |
|---|---|---|
| 1 | A aplicação funciona: os 6 casos de teste passaram | docs/registro_de_testes.md  |
| 2 | A versão aparece na janela e é a mesma do CHANGELOG e do README | v3.3.2 no canto inferior esquerdo da janela  |
| 3 | O pacote foi testado numa pasta limpa | Extraído TechBairro-3.3.2.zip → executou → contador = 0 |
| 4 | Tag e release publicadas, com o .zip anexado | https://github.com/yasminmerliah/techbairro/releases/tag/v3.3.2 |
| 5 | O repositório não tem banco, __pycache__ nem dist | .gitignore protege todos os três itens  |
| 6 | O histórico tem commits com mensagens claras | https://github.com/yasminmerliah/techbairro/commits/main |
| 7 | README, manual de uso e requirements.txt estão no repositório | Arquivos na raiz e em docs/  |
| 8 | A Issue "Teste do README" está fechada | https://github.com/yasminmerliah/techbairro/issues/1  |
| 9 | O vídeo está publicado e o link abre sem pedir login | [COLOQUE O LINK DO VÍDEO AQUI] |

## Roteiro do vídeo
1. Problema e solução (30s): A Associação de Moradores usava planilhas bagunçadas. A TechBairro 3.3.2 é um sistema simples de cadastro.
2. Demonstração (1min30s): Cadastrar → validar e-mail → consultar → editar → excluir com confirmação.
3. Como foi construída (30s): Python + SQLite + GitHub + Release pronta para baixar.
4. Aprendizado (30s): Documentar é tão importante quanto programar.

## Perguntas
1. **Por que o techbairro.db não está no GitHub?**
> Porque guarda dados pessoais protegidos pela LGPD. Subir para o GitHub expõe informações de pessoas reais. O .gitignore impede o envio.

2. **Qual defeito foi encontrado e corrigido?**
> O script de geração de pacote estava incluindo a pasta .git dentro do ZIP. Corrigi 

3. **Como o voluntário instala pelo link do repositório?**
> Acessa o link  clica em <> Code → baixa ZIP ou clona → entra na pasta → executa python techbairro.py. Não precisa instalar bibliotecas extras.

## Autoavaliação
ficou bom, mas fiquei nervosa