import sqlite3

conn = sqlite3.connect("aula.db")

conn.execute('''
CREATE table IF NOT EXISTS aluno(
  nome string,
  sobrenome string,
  idade integer
)
''')

conn.execute('''insert INTO aluno values("Layza", "Souza", 20)''')
conn.commit()

cursor = conn.execute('''SELECT * from aluno''')

print(cursor.fetchall())
for row in cursor:
  print(row)