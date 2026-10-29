# Changelog da TechBairro


## Em desenvolvimento
### Adicionado
- Código publicado no GitHub, com histórico de versões.
# TechBairro
## v__3.2.1___ (Aula 18)
### Alterado
- O número da versão passou a ficar ___o numero da versao agora fica um unico lugar, qu e na constante versao da techbairro.py___________________________.
### Adicionado
- Script scripts/gerar_pacote.py, que _____que faz o arquivo techbairro 3.2.1 dos arquivos e tira o banco de daos e os arquivos do puthon_________________________.
- Arquivo COMO_EXECUTAR.txt, com os requisitos__e so seguir os passo a passos________________________.

## v3.2 (Aula 16)
### Alterado
- O banco agora é aberto pelo caminho completo (os.path + __file__),
  sempre na pasta do projeto, não importa de onde o programa seja executado.
### Adicionado
- Mensagem "Banco em uso" no terminal, mostrando qual arquivo de banco está sendo usado.

## v3.1 (Aula 15)
### Corrigido
- O Endereço voltou a ser obrigatório no cadastro.
- A validação de e-mail passou a recusar e-mail sem nome antes do @ ou sem ponto depois do @.
- A Consulta voltou a listar os clientes em ordem alfabética.
- A edição de um cliente passou a ser gravada no banco (faltava o commit).
- A exclusão só acontece quando o usuário responde Sim na confirmação.

## v3.0 (Aula 14)
### Alterado
- O GerenciadorClientes deixou de guardar os clientes numa lista em memória
  e passou a gravar no banco SQLite techbairro.db.
- Editar e excluir passaram a usar o id do cliente no banco (id_em_edicao),
  e não mais a posição na lista (indice_em_edicao).
- O contador de clientes passou a vir do banco ao abrir a aplicação.
### Adicionado
- Tratamento de erros do banco com try/except sqlite3.Error.

## v2.0 (Aulas 11 e 12)
### Adicionado
- Classes Cliente e GerenciadorClientes.
- Tela de Consulta com a lista de clientes e os botões Editar e Excluir.
- Confirmação antes de excluir um cliente.

## Antes da v2.0 (Aulas 5 a 10)
- Janela de cadastro com Tkinter, eventos dos botões e validação dos campos.

## v3.3.0 (Aula 20)

### Adicionado
- Modo de edição visível: o botão Salvar muda para "Salvar edição" e volta para "Salvar"
- Mensagens diferentes no botão Cancelar: "Edição cancelada" ou "Formulário limpo"
- Duplo clique na lista abre a edição do cliente
- Mensagens de aviso quando o cliente já não ta mais no banco no banco

### Corrigido
- Editar e Excluir agora usam o cliente que está visível na tela
- Atualizar verifica se o cliente ainda existe antes de alterar
- Excluir avisa quando o cliente já foi removido em outra janela
 
- Porque a gente adicionar funcionalidades novas, a gente corrigiu erros, mas tambem  aumentamos o número do meio (MINOR) não o último (PATCH).

## v3.3.2 (Aula 27)
### Adicionado
- README completo com instalação e uso
- Arquivo requirements.txt
- Manual de uso em docs/manual_de_uso.md
- Registro de testes em docs/registro_de_testes.md