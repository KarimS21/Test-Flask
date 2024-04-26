import pymssql

# Establece los detalles de conexión a tu base de datos SQL Server
server = 'sistemasoperativosupc.database.windows.net'
database = 'SO-Project'
username = 'KarimS21'
password = 'SOupc2024'

# Intenta establecer la conexión
def connect():
    try:
        conn = pymssql.connect(server=server, user=username, password=password, database=database)
        return conn
    except Exception as e:
        print(f"No se pudo conectar a la base de datos: {e}")
