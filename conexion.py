import pyodbc

# Establece los detalles de conexión a tu base de datos SQL Server
server = 'sistemasoperativosupc.database.windows.net'
database = 'SO-Project'
username = 'KarimS21'
password = 'SOupc2024'

# Construye la cadena de conexión
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
# Intenta establecer la conexión
def connect():
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print(f"No se pudo conectar a la base de datos: {e}")
