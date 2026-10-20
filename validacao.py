# VALIDAÇÃO (Aula 21)
# ============================================================
#
# Responsabilidade: as regras de negócio do cadastro (RF01 a RF03).
# Este arquivo não sabe nada de janela nem de banco.
# Classe responsável por conferir se um cliente pode ser gravado
class ValidadorCliente:

    # Confere todas as regras do cliente.
    #
    # Retorna a mensagem do primeiro problema encontrado,
    # ou None se o cliente estiver válido.
    def validar(self, cliente):

        # RF01: lista com os campos vazios, com o nome que aparece na tela
        vazios = []
        if cliente.nome == "":
            vazios.append("Nome")
        # COMPLETE: os mesmos testes para telefone, email e endereço
        # (na tela, os nomes são "Telefone", "E-mail" e "Endereço")
        if cliente.telefone == "":
            vazios.append("Telefone")
        if cliente.email == "":
            vazios.append("E-mail")
        if cliente.endereco == "":
            vazios.append("Endereço")

        # Se houver algum campo vazio
        if vazios:
            return f"Preencha o(s) campo(s): {', '.join(vazios)}"

        # RF02: o telefone precisa ter somente números
        if not cliente.telefone.isdigit():
            return "Telefone inválido: use somente números."

        # RF03: o e-mail precisa estar no formato nome@dominio.com
        if not self.email_parece_valido(cliente.email):
            return "E-mail inválido: use o formato nome@dominio.com."

        # Nenhum problema encontrado
        return None

    # MUDOU NA AULA 21: era uma função solta no techbairro.py,
    # agora é um método do ValidadorCliente
    def email_parece_valido(self, email):
        # COMPLETE: copie o corpo da função email_parece_valido do techbairro.py
        if "@" not in email:
            return False
        usuario, _, dominio = email.partition("@")
        if usuario == "" or "." not in dominio:
            return False
        return True