import pyodbc
from utils import encriptar, desencriptar


def get_connection():
    SERVER = 'localhost'
    DATABASE = 'contrasenas'
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
            cursor.execute("SELECT id, contrasena, usuario, correo, fecha_guardado FROM dbo.contrasenas")
            contrasenas = cursor.fetchall()
            # Desencriptar cada contraseña antes de devolverla
            contrasenas_desencriptadas = []
            for contrasena in contrasenas:
                id_, contrasena_encriptada, usuario, correo, fecha_guardado = contrasena
                try:
                    # Desencriptar la contraseña si está en formato adecuado
                    contrasena_desencriptada = desencriptar(contrasena_encriptada)
                    contrasenas_desencriptadas.append((id_, contrasena_desencriptada, usuario, correo, fecha_guardado))
                except Exception as e:
                    print(f"Error al desencriptar la contraseña con ID {id_}: {e}")
                    contrasenas_desencriptadas.append((id_, "Error al desencriptar", usuario, correo, fecha_guardado))
            return contrasenas_desencriptadas
        except Exception as e:
            print(f"Error al obtener las contraseñas: {e}")
            return []
        finally:
            connection.close()  # Cerrar la conexión
    else:
        return []

    
def eliminar_contrasena(id_contrasena):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM dbo.contrasenas WHERE id = ?", (id_contrasena,))
            connection.commit()  # Confirmar los cambios
            print(f"Contraseña con ID {id_contrasena} eliminada exitosamente.")
            return True  # Éxito
        except Exception as e:
            print(f"Error al eliminar la contraseña: {e}")
            return False  # Error
        finally:
            connection.close()  # Cerrar la conexión
    else:
        print("No se pudo conectar a la base de datos para eliminar la contraseña")
        return False  # Error
    
def editar_contrasena(id_contrasena, contrasena, usuario, correo):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE dbo.contrasenas SET contrasena = ?, usuario = ?, correo = ? WHERE id = ?",
                (contrasena, usuario, correo, id_contrasena)  # No encriptar de nuevo aquí
            )
            connection.commit()  # Confirmar los cambios
            print(f"Contraseña con ID {id_contrasena} actualizada exitosamente.")
            return True  # Éxito
        except Exception as e:
            print(f"Error al actualizar la contraseña: {e}")
            return False  # Error
        finally:
            connection.close()  # Cerrar la conexión
    else:
        print("No se pudo conectar a la base de datos para actualizar la contraseña")
        return False  # Error



    

