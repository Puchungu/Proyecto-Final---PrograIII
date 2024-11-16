import pyodbc

def get_connection():
    SERVER = 'localhost'
    DATABASE = 'contrasena'
    try:
        connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes"
        )
        print("Conexión exitosa")
        return connection
    except Exception as e:
        print("Error al conectar:", e)
        return None

# Llamamos a la función para ver si todo está funcionando
get_connection()



def obtener_contrasenas():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id, contrasena FROM dbo.contrasenas")  # Consulta SQL
            contrasenas = cursor.fetchall()  # Obtener todas las contraseñas
            return contrasenas
        except Exception as e:
            print(f"Error al obtener las contraseñas: {e}")
            return []
        finally:
            connection.close()  # Cerrar la conexión
    else:
        return []
    


    

