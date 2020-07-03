import sqlite3

conexao = sqlite3.connect('banco.db')
c = conexao.cursor()

c.execute("select * from funcionarios")

rows = c.fetchall()

for row in rows:
    print(row)

c.close()
