import tkinter as tk

from funcionario import Funcionario
from tkcalendar import DateEntry

class Funcionario_view(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.criar_widget_funcionario()
        self.funcionario = Funcionario("", 0, 0, "", "", "", 0)

    def criar_widget_funcionario(self):
        # Título
        self.container_titulo = tk.Frame(self.master)
        self.container_titulo["pady"] = 10
        self.container_titulo["padx"] = 20
        self.container_titulo.pack()

        self.titulo_dados = tk.Label(self.container_titulo, text="CADASTRAR NOVO FUNCIONÁRIO")
        self.titulo_dados.pack()

        # Campo id
        self.container_id = self.criar_container_padrao()

        self.id_label = tk.Label(self.container_id, text="Id")
        self.id_label["width"] = 20
        self.id_label["anchor"] = tk.NW
        self.id_label.pack(side=tk.LEFT)

        self.id = tk.Entry(self.container_id)
        self.id["width"] = 10
        self.id.pack(side=tk.LEFT)

        self.botao_buscar = tk.Button(self.container_id)
        self.botao_buscar["text"] = "Buscar"
        self.botao_buscar["command"] = self.buscar_funcionario
        self.botao_buscar.pack(side=tk.LEFT)

        # Campo nome
        self.container_nome = self.criar_container_padrao()

        self.nome_label = tk.Label(self.container_nome, text="Nome")
        self.nome_label["width"] = 20
        self.nome_label["anchor"] = tk.NW
        self.nome_label.pack(side=tk.LEFT)

        self.nome = tk.Entry(self.container_nome)
        self.nome["width"] = 20
        self.nome.pack(side=tk.LEFT)

        # Campo nascimento
        self.container_nascimento = self.criar_container_padrao()

        self.nascimento_label = tk.Label(self.container_nascimento, text="Data de nascimento")
        self.nascimento_label["width"] = 20
        self.nascimento_label["anchor"] = tk.NW
        self.nascimento_label.pack(side=tk.LEFT)

        self.nascimento = DateEntry(self.container_nascimento, width=18, background='darkblue',
                                    foreground='white', borderwidth=2)
        self.nascimento.pack(side=tk.LEFT)

        # Campo sexo
        self.container_sexo = self.criar_container_padrao()

        self.sexo_label = tk.Label(self.container_sexo, text="Sexo")
        self.sexo_label["width"] = 20
        self.sexo_label["anchor"] = tk.NW
        self.sexo_label.pack(side=tk.LEFT)

        self.sexo = tk.StringVar(self.container_sexo)
        self.sexo.set("")  # default value
        self.sexo_combo = tk.OptionMenu(self.container_sexo, self.sexo, "Masculino", "Feminino", "")
        self.sexo_combo["width"] = 15
        self.sexo_combo.pack(side=tk.LEFT)

        # Campo cargo
        self.container_cargo = self.criar_container_padrao()

        self.cargo_label = tk.Label(self.container_cargo, text="Cargo")
        self.cargo_label["width"] = 20
        self.cargo_label["anchor"] = tk.NW
        self.cargo_label.pack(side=tk.LEFT)

        self.cargo = tk.Entry(self.container_cargo)
        self.cargo["width"] = 20
        self.cargo.pack(side=tk.LEFT)

        # Campo qtde dependentes
        self.container_qtde_dependetes = self.criar_container_padrao()

        self.qtde_dependetes_label = tk.Label(self.container_qtde_dependetes, text="Dependentes")
        self.qtde_dependetes_label["width"] = 20
        self.qtde_dependetes_label["anchor"] = tk.NW
        self.qtde_dependetes_label.pack(side=tk.LEFT)

        self.qtde_dependetes = tk.StringVar(self.container_qtde_dependetes)
        self.qtde_dependetes.set("0")  # default value
        self.qtde_dependetes_combo = tk.OptionMenu(self.container_qtde_dependetes, self.qtde_dependetes, "0", "1", "2", "3", "4", "5")
        self.qtde_dependetes_combo["width"] = 15
        self.qtde_dependetes_combo.pack(side=tk.LEFT)

        # Botões
        self.container_botoes = self.criar_container_padrao()

        self.botao_criar = tk.Button(self.container_botoes)
        self.botao_criar["text"] = "Criar"
        self.botao_criar["command"] = self.add_funcionario
        self.botao_criar["bg"] = "blue"
        self.botao_criar["fg"] = "white"
        self.botao_criar.pack(side=tk.LEFT)

        self.botao_atualizar = tk.Button(self.container_botoes)
        self.botao_atualizar["text"] = "Atualizar"
        self.botao_atualizar["command"] = self.atualizar_funcionario
        self.botao_atualizar["bg"] = "green"
        self.botao_atualizar["fg"] = "white"
        self.botao_atualizar["state"] = "disabled"
        self.botao_atualizar.pack(side=tk.LEFT)

        self.botao_excluir = tk.Button(self.container_botoes)
        self.botao_excluir["text"] = "Excluir"
        self.botao_excluir["command"] = self.excluir_funcionario
        self.botao_excluir["bg"] = "red"
        self.botao_excluir["fg"] = "white"
        self.botao_excluir["state"] = "disabled"
        self.botao_excluir.pack(side=tk.LEFT)

        self.botao_limpar = tk.Button(self.container_botoes)
        self.botao_limpar["text"] = "Limpar"
        self.botao_limpar["command"] = self.limpar_tela
        self.botao_limpar.pack()

        # Mensagem
        self.container_mensagem = self.criar_container_padrao()

        self.mensagem = tk.Label(self.container_mensagem, text="")
        self.mensagem.pack()

    def criar_container_padrao(self):
        container = tk.Frame(self.master)
        container["padx"] = 20
        container["pady"] = 5
        container.pack()

        return container

    def add_funcionario(self):
        self.funcionario.nome = self.nome.get()
        self.funcionario.cargo = self.cargo.get()
        self.funcionario.id_setor = 0
        self.funcionario.qtd_dependentes = self.qtde_dependetes.get()
        self.funcionario.sexo = self.sexo.get()
        self.funcionario.data_nascimento = self.nascimento.get()
        self.funcionario.salario = 950

        status, id_gerado, mensagem = self.funcionario.insert_funcionario()

        if status:
            self.id.insert(0, id_gerado)
            self.botao_criar.config(state="disabled")
            self.botao_excluir.config(state="normal")
            self.botao_atualizar.config(state="normal")

        self.mensagem["text"] = mensagem

    def limpar_tela(self):
        self.id.delete(0, tk.END)
        self.nome.delete(0, tk.END)
        self.nascimento.delete(0, tk.END)
        self.cargo.delete(0, tk.END)
        self.sexo.set("")
        self.qtde_dependetes.set("0")
        self.mensagem["text"] = ""
        self.funcionario = Funcionario("", 0, 0, "", "", "", 0)

        self.botao_criar.config(state="normal")
        self.botao_excluir.config(state="disabled")
        self.botao_atualizar.config(state="disabled")

    def buscar_funcionario(self):
        status, mensagem = self.funcionario.select_funcionario(self.id.get())

        if status:
            self.nome.insert(0, self.funcionario.nome)
            self.nascimento.set_date(self.funcionario.data_nascimento)
            self.cargo.insert(0, self.funcionario.cargo)
            self.sexo.set(self.funcionario.sexo)
            self.qtde_dependetes.set(self.funcionario.qtd_dependentes)

            self.botao_criar.config(state="disabled")
            self.botao_excluir.config(state="normal")
            self.botao_atualizar.config(state="normal")
        else:
            self.limpar_tela()

        self.mensagem["text"] = mensagem

    def atualizar_funcionario(self):
        self.funcionario.nome = self.nome.get()
        self.funcionario.cargo = self.cargo.get()
        self.funcionario.id_setor = 0
        self.funcionario.qtd_dependentes = self.qtde_dependetes.get()
        self.funcionario.sexo = self.sexo.get()
        self.funcionario.data_nascimento = self.nascimento.get()
        self.funcionario.salario = 950

        status, mensagem = self.funcionario.update_funcionario()

        if status:
            self.limpar_tela()

        self.mensagem["text"] = mensagem

    def excluir_funcionario(self):
        self.funcionario.id_funcionario = self.id.get()
        status, mensagem = self.funcionario.delete_funcionario()

        if status:
            self.limpar_tela()

        self.mensagem["text"] = mensagem
