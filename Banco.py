#Importando o adaptador do SQL Server para python
import pyodbc

#Configurando conexão
server = 'localhost'
database= 'Cognitiva'
username = 'GuiiLuiss'
password= 'dnr@2016'
driver = '{ODBC Driver 17 for SQL Server}'
port = '1433'

#Conexão
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT='+port+';DATABASE='+database+';UID='+username+';pwd='+password)

#Abrindo o cursor
cursor = conn.cursor()

conn.commit()
