# NOME ALTERADO V32, que sera alterado para outro nome depois.

# Importa a biblioteca Tkinter
import tkinter as tk

# Importa o messagebox para exibir mensagens e confirmações
from tkinter import messagebox

# NOVO NA AULA 14: importa o módulo do SQLite (já vem com o Python)
import sqlite3

# NOVO NA AULA 16: usado para montar o caminho completo do banco
import os

# NOVO NA AULA 21: importa os módulos separados
from cliente import Cliente
from banco import GerenciadorClientes
from validacao import ValidadorCliente

# NOVO NA AULA 18: a versão fica num único lugar.
# Para publicar uma versão nova, basta mudar aqui
# (e registrar a mudança no CHANGELOG).
VERSAO = "3.3.2"

# ============================================================
# JANELA PRINCIPAL
# ============================================================

# Cria a janela principal da aplicação
janela = tk.Tk()

# Define o título da janela
janela.title("TechBairro — Cadastro de Cliente")

# Define o tamanho da janela
janela.geometry("480x460")

# Impede que a janela seja redimensionada
janela.resizable(False, False)


# ============================================================
# OBJETO GERENCIADOR
# ============================================================

# Cria o objeto responsável por gerenciar os clientes
# (e cria o arquivo techbairro.db, se ele ainda não existir)
# MUDOU NA AULA 16: __file__ é o caminho deste arquivo .py.
# Assim o techbairro.db fica SEMPRE na mesma pasta do projeto,
# não importa de onde o VS Code rodar o programa.
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")

# Mostra no terminal qual banco está em uso
print(f"Banco em uso: {CAMINHO_BANCO}")

gerenciador = GerenciadorClientes(CAMINHO_BANCO)
validador = ValidadorCliente()


# Guarda o id do cliente que está sendo editado.
#
# None significa que estamos cadastrando um cliente novo.
#
# MUDOU NA AULA 14: antes era indice_em_edicao.
id_em_edicao = None


# ============================================================
# CABEÇALHO DA INTERFACE
# ============================================================

# Cria um Frame para funcionar como cabeçalho
cabecalho = tk.Frame(
    janela,
    bg="#2c3e50"
)

cabecalho.pack(
    side="top",
    fill="x"
)


# Cria o título do sistema
tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    fg="white",
    bg="#2c3e50",
    font=("Arial", 14, "bold"),
    pady=12
).pack()


# ============================================================
# FORMULÁRIO
# ============================================================

# Cria um Frame para organizar os campos
form = tk.Frame(janela)

form.pack(
    pady=20
)

# Lista com os nomes dos campos
campos = [
    "Nome",
    "Telefone",
    "E-mail",
    "Endereço"
]


# Dicionário que armazenará os campos Entry
entradas = {}


# Percorre os campos para criar os Labels e Entrys
for i, campo in enumerate(campos):

    # Cria o Label
    tk.Label(
        form,
        text=f"{campo}:"
    ).grid(
        row=i,
        column=0,
        sticky="e",
        padx=5,
        pady=6
    )


    # Cria o campo de entrada
    entrada = tk.Entry(
        form,
        width=30
    )

    entrada.grid(
        row=i,
        column=1,
        padx=5,
        pady=6
    )


    # Guarda o Entry no dicionário
    entradas[campo] = entrada


# ============================================================
# STATUS
# ============================================================

# Label utilizada para mostrar mensagens ao usuário
status = tk.Label(
    janela,
    text="Nenhum cliente cadastrado ainda",
    fg="gray",
    wraplength=440,
    justify="left"
)

status.pack(
    pady=(0, 5)
)


# Mostra a quantidade de clientes cadastrados
#
# MUDOU NA AULA 14: o total já vem do banco ao abrir a aplicação
contador = tk.Label(
    janela,
    text=f"Clientes cadastrados: {gerenciador.total()}"
)

contador.pack()


# ============================================================
# LIMPAR CAMPOS
# ============================================================

def limpar_campos():

    global id_em_edicao

    # Percorre todos os campos
    for entrada in entradas.values():

        # Apaga o conteúdo do campo
        entrada.delete(
            0,
            tk.END
        )

    # Sai do modo de edição
    id_em_edicao = None
    botao_salvar.config(text="Salvar")


# ============================================================
# SALVAR
# ============================================================

def salvar():

    global id_em_edicao


    # Pega os valores digitados nos campos
    valores = {
        campo: entradas[campo].get().strip()
        for campo in campos
    }


    # Cria um novo objeto Cliente
    cliente = Cliente(
        valores["Nome"],
        valores["Telefone"],
        valores["E-mail"],
        valores["Endereço"]
    )

    # MUDOU NA AULA 21: as regras saíram daqui e foram
    # para o ValidadorCliente (validacao.py).
    # A tela só pergunta e mostra a resposta.
    erro = validador.validar(cliente)
    if erro is not None:
        status.config(
            text=erro,
            fg="red"
        )
        return


    # ========================================================
    # CADASTRAR OU ATUALIZAR?
    # ========================================================

    # NOVO NA AULA 14: try/except captura qualquer erro do banco
    try:

        # Se não existe um id em edição,
        # significa que estamos cadastrando um cliente novo.
        if id_em_edicao is None:

            gerenciador.adicionar(cliente)

            status.config(
                text=f"Cliente '{cliente.nome}' salvo com sucesso!",
                fg="green"
            )

        # Caso contrário, estamos editando um cliente existente.
        else:
            # MUDOU NA AULA 20: guardamos a resposta do atualizar()
            alterou = gerenciador.atualizar(id_em_edicao, cliente)
            
            # NOVO NA AULA 20: avisa se o cliente foi excluído enquanto editava
            if not alterou:
                status.config(
                    text="Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.",
                    fg="red"
                )
                limpar_campos()
                return
            
            status.config(
                text=f"Cliente '{cliente.nome}' atualizado com sucesso!",
                fg="green"
            )

    except sqlite3.Error as erro:

        status.config(
            text=f"Erro ao salvar no banco: {erro}",
            fg="red"
        )

        return


    # Atualiza o contador
    contador.config(
        text=f"Clientes cadastrados: {gerenciador.total()}"
    )


    # Limpa o formulário
    limpar_campos()


# ============================================================
# CANCELAR
# ============================================================

def cancelar():
    # NOVO NA AULA 20: antes de limpar, descobre se estava editando
    estava_editando = id_em_edicao is not None

    # Limpa os campos
    limpar_campos()

    # Atualiza a mensagem de status
    #
    # MUDOU NA AULA 20: mensagem diferente para quem cancela uma edição
    if estava_editando:
        status.config(
            text="Edição cancelada. Nada foi alterado.",
            fg="gray"
        )
    else:
        status.config(
            text="Formulário limpo",
            fg="gray"
        )


# ============================================================
# CONSULTA DE CLIENTES
# ============================================================

def abrir_consulta():

    # Cria uma nova janela
    consulta = tk.Toplevel(janela)

    consulta.title(
        "Consulta de Clientes"
    )

    # Define um tamanho fixo para que os botões
    # fiquem sempre visíveis
    consulta.geometry(
        "500x380"
    )

    # Impede o redimensionamento
    consulta.resizable(
        False,
        False
    )

    # NOVO NA AULA 20: guarda os clientes que estão aparecendo na Listbox,
    # na mesma ordem das linhas.
    #
    # Assim, Editar e Excluir usam o cliente que o usuário VIU,
    # e não buscam o banco de novo pela posição.
    clientes_na_tela = []

    # ========================================================
    # LISTBOX
    # ========================================================

    # Cria a lista de clientes
    lista = tk.Listbox(
        consulta,
        width=65,
        height=12
    )

    # Não utilizamos expand=True ou fill="both".
    # Dessa forma, a Listbox não ocupa todo o espaço
    # e os botões permanecem visíveis.
    lista.pack(
        padx=10,
        pady=10
    )

    # ========================================================
    # BARRA DE ROLAGEM
    # ========================================================

    # Cria a barra de rolagem
    scrollbar = tk.Scrollbar(
        consulta
    )

    scrollbar.pack(
        side="right",
        fill="y",
        pady=10
    )


    # Liga a Listbox à barra de rolagem
    lista.config(
        yscrollcommand=scrollbar.set
    )

    scrollbar.config(
        command=lista.yview
    )


    # ========================================================
    # ATUALIZAR LISTA
    # ========================================================
    def atualizar_lista():

        # Remove todos os itens da Listbox
        lista.delete(
            0,
            tk.END
        )

        # NOVO NA AULA 20: esvazia também a lista da tela
        clientes_na_tela.clear()

        # Busca os clientes cadastrados no banco
        try:

            clientes_cadastrados = gerenciador.listar()

        except sqlite3.Error as erro:

            lista.insert(
                tk.END,
                f"Erro ao ler o banco: {erro}"
            )

            return


        # Verifica se existem clientes
        if not clientes_cadastrados:

            lista.insert(
                tk.END,
                "Nenhum cliente cadastrado"
            )

            return


        # Percorre os clientes
        for cliente in clientes_cadastrados:

            # Adiciona o resumo do cliente na Listbox
            lista.insert(
                tk.END,
                cliente.resumo()
            )

            # NOVO NA AULA 20: guarda o cliente na mesma posição da linha
            clientes_na_tela.append(cliente)

    # NOVO NA AULA 20: duplo clique numa linha também abre a edição.
    #
    # O bind passa um "evento" para a função;
    # o lambda recebe esse evento e chama editar_cliente() sem ele.
    lista.bind(
        "<Double-1>",
        lambda evento: editar_cliente()
    )

    # Preenche a Listbox
    atualizar_lista()


    # ========================================================
    # CLIENTE SELECIONADO
    # ========================================================
    # NOVO NA AULA 20: devolve o cliente da linha selecionada,
    # ou None se nenhuma linha válida estiver selecionada.
    #
    # Editar e Excluir usam esta função, e não mais
    # gerenciador.listar()[indice].
    def cliente_selecionado(acao):
        # Descobre qual linha foi selecionada
        selecionado = lista.curselection()

        # Verifica se alguma linha foi selecionada
        #
        # A segunda condição protege as linhas de aviso,
        # como "Nenhum cliente cadastrado", que não são clientes.
        if not selecionado or selecionado[0] >= len(clientes_na_tela):
            messagebox.showwarning(
                "Atenção",
                f"Selecione um cliente antes de {acao}."
            )
            return None

        # Pega o cliente que está na mesma posição da linha
        return clientes_na_tela[selecionado[0]]


    # ========================================================
    # EDITAR CLIENTE
    # ========================================================

    def editar_cliente():

        # MUDOU NA AULA 20: pega o cliente que está na tela
        cliente = cliente_selecionado("editar")
        if cliente is None:
            return
        
        # Guarda o id do cliente que é fixo, e não a posição dele na lista.
        id_em_edicao = cliente.id

        # ====================================================
        # COLOCA OS DADOS NO FORMULÁRIO
        # ====================================================

        # Nome
        entradas["Nome"].delete(
            0,
            tk.END
        )

        entradas["Nome"].insert(
            0,
            cliente.nome
        )


        # Telefone
        entradas["Telefone"].delete(
            0,
            tk.END
        )

        entradas["Telefone"].insert(
            0,
            cliente.telefone
        )


        # E-mail
        entradas["E-mail"].delete(
            0,
            tk.END
        )

        entradas["E-mail"].insert(
            0,
            cliente.email
        )


        # Endereço
        entradas["Endereço"].delete(
            0,
            tk.END
        )

        entradas["Endereço"].insert(
            0,
            cliente.endereco
        )


        # Informa que estamos editando
        status.config(
            text=f"Editando cliente: {cliente.nome}",
            fg="blue"
        )
        botao_salvar.config(text="Salvar edição")
        # Fecha a janela de consulta
        consulta.destroy()


    # ========================================================
    # EXCLUIR CLIENTE
    # ========================================================

    def excluir_cliente():

        # MUDOU NA AULA 20: pega o cliente que está na tela
        cliente = cliente_selecionado("excluir")
        if cliente is None:
            return

        # ====================================================
        # CONFIRMAÇÃO
        # ====================================================
        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja excluir o cadastro de "
            f"{cliente.nome}?\n\n"
            f"Essa ação não pode ser desfeita."
        )

        if confirmar:
            # Remove pelo id do cliente
            try:
                # MUDOU NA AULA 20: guardamos a resposta do remover()
                removeu = gerenciador.remover(cliente.id)
            except sqlite3.Error as erro:
                messagebox.showerror(
                    "Erro no banco",
                    f"Não foi possível excluir o cliente.\n{erro}"
                )
                return

            # NOVO NA AULA 20: o cliente já tinha sido excluído
            if not removeu:
                messagebox.showwarning(
                    "Cliente não encontrado",
                    f"{cliente.nome} já não está mais no banco.\n"
                    f"A lista será atualizada."
                )
                atualizar_lista()
                return

            # Atualiza a lista
            atualizar_lista()

            # Atualiza o contador da janela principal
            contador.config(
                text=f"Clientes cadastrados: {gerenciador.total()}"
            )

            # Atualiza o status
            status.config(
                text=f"Cliente '{cliente.nome}' excluído com sucesso!",
                fg="green"
            )


    # ========================================================
    # BOTÕES DA CONSULTA
    # ========================================================

    # Frame para organizar os botões
    botoes_consulta = tk.Frame(
        consulta
    )

    botoes_consulta.pack(
        pady=10
    )


    # Botão Editar
    tk.Button(
        botoes_consulta,
        text="Editar selecionado",
        width=18,
        command=editar_cliente
    ).grid(
        row=0,
        column=0,
        padx=5
    )


    # Botão Excluir
    tk.Button(
        botoes_consulta,
        text="Excluir selecionado",
        width=18,
        command=excluir_cliente
    ).grid(
        row=0,
        column=1,
        padx=5
    )


    # Preenche a Listbox
    atualizar_lista()


# ============================================================
# BOTÕES DA JANELA PRINCIPAL
# ============================================================

botoes = tk.Frame(
    janela
)

botoes.pack(
    pady=10
)


# Botão Salvar
botao_salvar = tk.Button(
    botoes,
    text="Salvar",
    width=13,
    command=salvar
)
botao_salvar.grid(
    row=0,
    column=0,
    padx=5
)


# Botão Cancelar
tk.Button(
    botoes,
    text="Cancelar",
    width=12,
    command=cancelar
).grid(
    row=0,
    column=1,
    padx=5
)


# Botão Consultar
#
# A edição e a exclusão ficam dentro
# da tela de consulta.
tk.Button(
    botoes,
    text="Consultar",
    width=12,
    command=abrir_consulta
).grid(
    row=0,
    column=2,
    padx=5
)


# ============================================================
# VERSÃO
# ============================================================

# Exibe a versão do sistema no canto inferior direito
#
# MUDOU NA AULA 16: v3.2 (banco aberto pelo caminho completo)
# MUDOU NA AULA 17: o arquivo passou a se chamar techbairro.py;
# MUDOU NA AULA 18: o rótulo usa a constante VERSAO

# a versão fica aqui no rótulo e no CHANGELOG, não no nome do arquivo
tk.Label(
    janela,
    text=f"v{VERSAO}",
    fg="black"
).place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)


# ============================================================
# INICIALIZAÇÃO
# ============================================================

# Mantém a aplicação aberta
janela.mainloop()