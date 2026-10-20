# Testes da TechBairro (Aula 15)

Rodada de testes da versão entregue na Aula 15 e correções que geraram a v3.1.

## Defeitos encontrados

| Bug | Requisito | Como reproduzir | Esperado | Obtido | Severidade |
|---|---|---|---|---|---|
| BUG 1 | RF01 | Preencher tudo, menos o Endereço, e clicar em Salvar | "Preencha o(s) campo(s): Endereço" | Cliente salvo sem endereço | Média |
| BUG 2 | RF03 | Preencher o e-mail sem ponto depois do @ (ana@email) e clicar em Salvar | "E-mail inválido" | Cliente salvo | Média |
| BUG 3 | RF04 | Cadastrar Zeca, depois Ana, depois Maria e abrir a Consulta | Ana, Maria, Zeca | Zeca, Ana, Maria | Baixa |
| BUG 4 | RF05 e RF07 | Editar um cliente, trocar o telefone, salvar e abrir a Consulta de novo | Telefone novo na Consulta | Status diz "atualizado com sucesso", mas a Consulta mostra o telefone antigo | Alta |
| BUG 5 | RF06 | Selecionar um cliente, clicar em Excluir e responder Não | Cliente continua na lista | Cliente excluído | Alta |

## Correções (marcadas no código com "CORRIGIDO (BUG n)")

| Bug | Onde | Correção |
|---|---|---|
| BUG 1 | salvar() | Conferir todos os campos (campos, e não campos[:3]) |
| BUG 2 | email_parece_valido() | Trocar and por or |
| BUG 3 | listar() | Acrescentar ORDER BY nome |
| BUG 4 | atualizar() | Acrescentar conexao.commit() antes do close() |
| BUG 5 | excluir_cliente() da Consulta | Guardar a resposta do askyesno e só remover se for Sim |

## Regressão

Depois das correções, RF02 (telefone só com números) e o cadastro e a exclusão de RF07, que já funcionavam, foram testados de novo e continuaram passando.
