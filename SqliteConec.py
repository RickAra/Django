import sqlite3
#criar uma conexao com o banco de dados
conn = sqlite3.connect('mydatabase.db')
#criar uma tabela
conn.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
#salvar as alterações
conn.commit()
#fechar a conexão com o banco de dados
conn.close()

print("conexão realizada com sucesso")