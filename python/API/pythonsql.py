import pyodbc
from datetime import date

def conecta_ao_banco(driver='SQL Server', server='SKVM08\SQLEXPRESS', database='VolpeSkyglass', username='dashboard', password='%Skygl@ss2023$', trusted_connection='no'):

    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database}; UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

    conexao = pyodbc.connect(string_conexao)
    cursor = conexao.cursor()

    return conexao, cursor

conexao, cursor = conecta_ao_banco()

hoje = date.today()

visitantes_parque = cursor.execute(f"SELECT COUNT(PK_ID) FROM pq_catraca WHERE dh_inclusao BETWEEN '{hoje} 00:00:00' AND '{hoje} 23:59:59' AND FK_ATRACAO ='6';").fetchone()

visitantes_plataforma = cursor.execute(f"SELECT COUNT(PK_ID) FROM pq_catraca WHERE dh_inclusao BETWEEN '{hoje} 00:00:00' AND '{hoje} 23:59:59' AND FK_ATRACAO ='7';").fetchone()

visitantes_abusado = cursor.execute(f"SELECT COUNT(PK_ID) FROM pq_catraca WHERE dh_inclusao BETWEEN '{hoje} 00:00:00' AND '{hoje} 23:59:59' AND FK_ATRACAO ='8';").fetchone()

a = visitantes_parque[0]
b = visitantes_plataforma[0]
c = visitantes_abusado[0]

print(a,b,c)

