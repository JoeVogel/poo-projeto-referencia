import tkinter as tk

from funcionario_view import Funcionario_view

class Menu(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.criar_widgets()

    def criar_widgets(self):
        # Título
        self.container_titulo = tk.Frame(self.master)
        self.container_titulo["pady"] = 10
        self.container_titulo["padx"] = 20
        self.container_titulo.pack()

        self.titulo_dados = tk.Label(self.container_titulo, text="SELECIONE A OPÇÃO DESEJADA:")
        self.titulo_dados.pack()

        self.container_funcionario = tk.Frame(self.master)
        self.container_funcionario["pady"] = 10
        self.container_funcionario.pack()

        self.botao_funcionarios = tk.Button(self.container_funcionario)
        self.botao_funcionarios["bg"] = "green"
        self.botao_funcionarios["text"] = "CADASTRO DE FUNCIONÁRIOS"
        self.botao_funcionarios["command"] = self.abrir_cadastro_funcionarios
        self.botao_funcionarios.pack()

    def abrir_cadastro_funcionarios(self):
        self.nova_tela = tk.Toplevel(self.master)
        self.funcionario_view = Funcionario_view(self.nova_tela)

if __name__ == '__main__':

    root = tk.Tk()
    root.title("Sistema de RH")
    root.geometry("500x400")

    Menu(master=root)

    root.mainloop()
