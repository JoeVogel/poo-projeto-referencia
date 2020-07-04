import sqlite3
from pessoa import Pessoa
from banco import Banco


class Funcionario(Pessoa): # Herança

    def __init__(self, cargo, id_setor, qtd_dependentes, nome, sexo, data_nascimento, salario):
        super().__init__(nome, sexo, data_nascimento)
        self.id_funcionario = None
        self.cargo = cargo
        self.id_setor = int(id_setor)
        self.salario = int(salario)
        self.qtd_dependentes = int(qtd_dependentes)
        self.banco = Banco()

    @property
    def id_funcionario(self):
        return self._id_funcionario

    @id_funcionario.setter
    def id_funcionario(self, id_funcionario):
        self._id_funcionario = id_funcionario

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def id_setor(self):
        return self._id_setor

    @id_setor.setter
    def id_setor(self, id_setor):
        self._id_setor = id_setor

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def qtd_dependentes(self):
        return self._qtd_dependentes

    @qtd_dependentes.setter
    def qtd_dependentes(self, qtd_dependentes):
        self._qtd_dependentes = qtd_dependentes

    def calcular_salario(self, horas_extras):
        valor_hora_extra = (self.salario / 30) / 8
        total_salario = (horas_extras * valor_hora_extra) + self.salario
        self.set_renda(total_salario)
        return total_salario

    def set_renda(self, valor):  # Polimorfismo
        if self.qtd_dependentes > 0:
            bonificacao = self.qtd_dependentes * 80
            self.renda = bonificacao + valor
        else:
            pass

    def insert_funcionario(self):
        try:

            c = self.banco.conexao.cursor()

            c.execute("insert into funcionarios (nome, sexo, data_nascimento, qtd_dependentes, cargo, salario, id_setor) values('" + self.nome + "', '" + self.sexo + "', '" + self.data_nascimento + "', '" + str(self.qtd_dependentes) + "', '" + self.cargo + "', '" + str(self.salario) + "', '" + str(self.id_setor) + "')")
            id_gerado = c.lastrowid

            self.banco.conexao.commit()
            c.close()

            return True, id_gerado, "Funcionário cadastrado com sucesso!"
        except sqlite3.Error as er:
            return False, 0, "Ocorreu um erro na inserção do funcionário"

    def update_funcionario(self):
        try:

            c = self.banco.conexao.cursor()

            c.execute("update funcionarios set nome = '" + self.nome + "', sexo = '" + self.sexo + "', data_nascimento = '" + self.data_nascimento + "', qtd_dependentes = '" + str(self.qtd_dependentes) + "', cargo = '" + self.cargo + "', salario = '" + str(self.salario) + "', id_setor = '" + str(self.id_setor) + "' where id_funcionario = " + str(self.id_funcionario) + " ")

            self.banco.conexao.commit()
            c.close()

            return True, "Funcionário atualizado com sucesso!"
        except sqlite3.Error as er:
            return False, "Ocorreu um erro na alteração do funcionário"

    def delete_funcionario(self):
        try:

            c = self.banco.conexao.cursor()

            c.execute("delete from funcionarios where id_funcionario = " + str(self.id_funcionario) + " ")

            self.banco.conexao.commit()
            c.close()

            return True, "Funcionário excluído com sucesso!"
        except sqlite3.Error as er:
            return False, "Ocorreu um erro na exclusão do funcionário"

    def select_funcionario(self, id_funcionario):
        try:

            c = self.banco.conexao.cursor()

            c.execute("select * from funcionarios where id_funcionario = " + id_funcionario + "  ")

            linha = c.fetchone()

            if linha is None:
                return False, "Funcionário não encontrado"

            self.id_funcionario = linha[0]
            self.nome = linha[1]
            self.sexo = linha[2]
            self.data_nascimento = linha[3]
            self.qtd_dependentes = int(linha[4])
            self.cargo = linha[5]
            self.salario = int(linha[6])
            self.id_setor = int(linha[7])

            c.close()

            return True, "Busca feita com sucesso!"
        except sqlite3.Error as er:
            return False, "Ocorreu um erro na busca do usuário"
