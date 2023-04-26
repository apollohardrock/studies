import pyodbc

def conecta_ao_banco(driver='SQL Server', server='SGTI00\SQLEXPRESS', database='Nome_Banco_Dados', username=None, password=None, trusted_connection='yes'):

    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database}; UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

    conexao = pyodbc.connect(string_conexao)
    cursor = conexao.cursor()

    return conexao, cursor

conexao, cursor = conecta_ao_banco()

clientes = cursor.execute('SELECT * FROM Numeros').fetchall()

atracao_parque = clientes[0]
atracao_plataforma = clientes[1]
atracao_abusado = clientes[2]

a = atracao_parque[0]
b = atracao_parque[1]
c = atracao_plataforma[0]
d = atracao_plataforma[1]
e = atracao_abusado[0]
f = atracao_abusado[1]

print(a,b,c,d,e,f)