# Registro de testes da TechBairro
Versão testada: _3.3.2___ · Data: _26/10/2026___ · Responsável: yasmin vitoria silva dos santos
Sistema operacional e versão do Python: __3.12.0__
| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar um cliente com todos os campos certos: cadastrar nome= "alice lima", telefone "619812341241", email= alicesantos@gmail.com, endereço= rua 54. passos: mensagem de sucesso. cliente aparece na lista e passou.| preencher o nome, endereço, telefone, email_: precisa preencher__ | ____ | ____ |
| CT02 | RF01 | Salvar com Nome e Endereço vazios. preencher o nome, endereço, telefone, email. passou_ | ____ |
| CT03 | RF02 | Telefone 61 9999 0000 (com espaços) | informa que precisa prencher todos os campos, passou__ | ____ | ____ |
| CT04 | RF03 | E-mail ana@email (sem ponto) | informa que precisa preencher com  o .com_ passou__ | ____ | ____ |
| CT05 | RF05 | Editar um cliente, trocar o telefone e salvar | __funciona normalmente.  passou_ | ____ | ____ |
| CT06 | RF06 | Excluir um cliente: responder Não, depois Sim | _se clicar em sim acaba excluindo e se apertar em nao nao vai excluir, poassou | ____ | ____ |
## Testes automáticos
Saída do `python testar_validacao.py`: _funcionou tudo__
## Defeitos encontrados
_nenhum__ (o que falhou, como foi corrigido e em qual commit; ou "nenhum")