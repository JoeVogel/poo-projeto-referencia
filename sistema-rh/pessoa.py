import datetime


class Pessoa:
    renda = None

    def __init__(self, nome,  sexo, data_nascimento):  # Construtor / Visbilidade (atributos publicos)
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    def get_idade(self):
        idade = int(datetime.datetime.now().year) - int(datetime.date.replace(self.data_nascimento).year)
        return idade

    def set_renda(self, valor):
        self.renda = valor
