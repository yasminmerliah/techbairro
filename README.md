# TechBairro

Sistema de cadastro de clientes da TechBairro.

(README completo na Aula 26.)
# TechBairro

Sistema de cadastro e gerenciamento de clientes desenvolvido para a Associação de Moradores. Permite cadastrar, consultar, editar e excluir pessoas atendidas, substituindo planilhas por uma interface simples.

**Versão atual:** 3.3.2 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades
- Cadastrar clientes com nome, telefone, e-mail e endereço
- Visualizar, alterar e excluir cadastros com confirmação antes de apagar
- Validação de campos obrigatórios e formato de e-mail

## Requisitos para execução
| Item | Requisito |
|---|---|
| Sistema operacional | Windows 10 ou superior, Linux ou macOS |
| Python | 3.10 ou superior (versão testada: 3.12.0) |
| Tkinter | Já incluso com a instalação padrão do Python |
| Bibliotecas externas | Nenhuma — usa só a biblioteca padrão |
| Internet | Não é necessária depois de instalado |

## Instalação

### Com Git
1. Baixe o projeto: `git clone https://github.com/yasminmerliah/techbairro.git`
2. Entre na pasta: `cd techbairro`
3. Execute: `python techbairro.py`

### Pelo arquivo ZIP
1. Acesse https://github.com/yasminmerliah/techbairro
2. Clique em **<> Code** → **Download ZIP** e extraia os arquivos
3. Abra o terminal na pasta extraída e digite: `python techbairro.py`

> Ao abrir, aparece a janela do programa e no terminal: **Banco em uso: techbairro.db**

## Configuração do banco de dados
O banco fica na mesma pasta do programa com o nome `techbairro.db` e é criado automaticamente na primeira vez que o sistema é aberto. No terminal aparece o caminho do banco em uso. Ele não é enviado para o repositório porque pode conter dados pessoais protegidos pela LGPD. Para fazer cópia de segurança, basta copiar o arquivo `techbairro.db` e colar em outro local; para restaurar, coloque o arquivo de volta na pasta do programa.

## Como usar
O passo a passo completo está no [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto
- `techbairro.py` — programa principal com a tela de cadastro
- `banco.py` — conexão e operações com o banco de dados
- `validacao.py` — regras de verificação dos dados digitados
- `cliente.py` — estrutura dos dados de cada cliente
- `docs/` — manuais, documentação e registros
- `scripts/` — ferramentas auxiliares
- `techbairro.db` — banco de dados (criado automaticamente)

## Autor
Yasmin Vitoria Silva Dos Santos
Curso Técnico em Desenvolvimento de Sistemas — Senac DF