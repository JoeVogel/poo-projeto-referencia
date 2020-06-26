import tkinter as tk

from funcionario import Funcionario
from tkcalendar import DateEntry

class Funcionario_view(tk.Frame):

    def __init__(self, master=None):
        self.funcionarios = []
        super().__init__(master)
        self.master = master
        self.pack()
        self.criar_widget_funcionario()

    def criar_widget_funcionario(self):
        # Título
        self.container_titulo = tk.Frame(self.master)
        self.container_titulo["pady"] = 10
        self.container_titulo["padx"] = 20
        self.container_titulo.pack()

        self.titulo_dados = tk.Label(self.container_titulo, text="CADASTRAR NOVO FUNCIONÁRIO")
        self.titulo_dados.pack()

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
        funcionario = Funcionario(self.cargo.get(), "", int(self.qtde_dependetes.get()), self.nome.get(), self.sexo.get(), self.nascimento.get())
        self.funcionarios.append(funcionario)

        self.mensagem["text"] = "Novo funcionário criado!"

        self.limpar_tela()

    def limpar_tela(self):
        self.nome.delete(0, tk.END)
        self.nascimento.delete(0, tk.END)
        self.cargo.delete(0, tk.END)
        self.sexo.set("")
        self.qtde_dependetes.set("0")
        self.mensagem["text"] = ""
