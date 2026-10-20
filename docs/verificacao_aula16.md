# Verificação da integração com o banco (Aula 16)

## Matriz de verificação (tela x banco)

| ID | Tela | Banco | OK? |
|---|---|---|---|
| V01 | Clientes cadastrados: 7 | A1 = 7 | Sim |
| V02 | 7 clientes em ordem de nome, com os dados da planilha | As mesmas 7 linhas (o script lista por id) | Sim |
| V03 | Igor salvo com sucesso, contador 8 | Linha nova com id 8 | Sim |
| V04 | Igor atualizado com sucesso | Mesmo id 8 com o telefone novo, sem linha nova | Sim |
| V05 | E-mail inválido | Nenhuma linha nova | Sim |
| V06 | Nada muda | Igor continua | Sim |
| V07 | Igor excluído, contador 7 | A linha de Igor sumiu | Sim |
| V08 | Contador 7 | A1 = 7 | Sim |

## Auditoria dos dados importados da planilha antiga

| Auditoria | Antes das correções | Depois das correções |
|---|---|---|
| A1 Total de clientes | 7 | 7 |
| A2 Campos vazios | Eduarda Rocha (endereço vazio) | Nenhum problema encontrado |
| A3 Telefone com letras | Fábio Nunes (6194444ABCD) | Nenhum problema encontrado |
| A4 E-mail fora do formato | Diego Martins (diego@email) | Nenhum problema encontrado |
| A5 Telefone repetido | 61988887777 (Carlos e Gabriela) | Nenhum problema encontrado |

Os dados entraram com problemas porque a importação gravou direto no banco, sem passar pela validação do salvar(). As correções foram feitas pela própria tela (Editar), onde a validação protege o que entra.

## Teste de falha (banco travado pelo travar_banco.py)

| Ação | Tela | Terminal |
|---|---|---|
| a) Cadastrar Karina | Espera uns 5 segundos e mostra "Erro ao salvar no banco: database is locked" | Nada |
| b) Excluir na Consulta aberta | Espera uns 5 segundos e nada acontece | Traceback com sqlite3.OperationalError: database is locked |
| c) Abrir Consulta nova | Espera uns 5 segundos e a lista mostra "Erro ao ler o banco: database is locked" | Nada |
