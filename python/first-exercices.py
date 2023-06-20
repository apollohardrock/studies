from datetime import date

print("Let's Go!")

hoje = date.today()

print(hoje)

nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']

qtd_letras = {}

for nome in nomes:
    qtd_letras[nome] = len(nome)

print(type(nomes))
print(type(qtd_letras))