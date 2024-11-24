from cryptography.fernet import Fernet
import os

# Nombre del archivo donde se guarda la clave
ARCHIVO_CLAVE = "clave.key"

def generar_clave():
    """Genera una clave y la guarda en un archivo si no existe."""
    if not os.path.exists(ARCHIVO_CLAVE):  # Verificar si el archivo ya existe
        clave = Fernet.generate_key()
        with open(ARCHIVO_CLAVE, "wb") as file:
            file.write(clave)
        print(f"Clave generada y guardada en '{ARCHIVO_CLAVE}'")
    else:
        print(f"La clave ya existe en '{ARCHIVO_CLAVE}'. No es necesario generarla nuevamente.")

def cargar_clave():
    """Carga la clave desde el archivo."""
    if not os.path.exists(ARCHIVO_CLAVE):
        raise FileNotFoundError(f"No se encontró el archivo '{ARCHIVO_CLAVE}'. Genera una clave primero.")
    with open(ARCHIVO_CLAVE, "rb") as file:
        return file.read()

# Generar o cargar la clave
try:
    clave = cargar_clave()
    print("Clave cargada correctamente.")
except FileNotFoundError:
    print("Archivo de clave no encontrado. Ejecuta 'generar_clave()' para crearlo.")
    clave = None

# Inicializar el objeto Fernet
fernet = Fernet(clave) if clave else None

def encriptar(texto):
    """Encripta un texto plano."""
    if not fernet:
        raise ValueError("La clave no está disponible. Asegúrate de generar y cargar la clave.")
    return fernet.encrypt(texto.encode()).decode()

def desencriptar(texto_encriptado):
    """Desencripta un texto cifrado."""
    if not fernet:
        raise ValueError("La clave no está disponible. Asegúrate de generar y cargar la clave.")
    return fernet.decrypt(texto_encriptado.encode()).decode()


