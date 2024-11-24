import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI import Ui_MainWindow  # Importar la clase generada de tu archivo UI
import secrets
import string
from DB_Conection import get_connection
from ventana2 import Ventana2
from utils import encriptar


class PswGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Instancia de la clase de UI
        self.ui.setupUi(self)  # Configura la UI en esta ventana

        # Conectar el botón "Generar Nueva Contrasena" a la función generar_contrasena
        self.ui.pushButton.clicked.connect(self.generar_contrasena)
        # Conectar el botón "Guardar Contrasena" a la función guardar_contrasena
        self.ui.pushButton_3.clicked.connect(self.guardar_contrasena)
        # Conectar el botón "Ver Contrasenas Guardadas" a la función abrir_ventana2
        self.ui.pushButton_2.clicked.connect(self.abrir_ventana2)

    # Lógica para generar contraseña segura
    def logica_contrasena(self, longitud=12):
        # Definir el conjunto de caracteres que se usarán en la contraseña
        caracteres = string.ascii_letters + string.digits + string.punctuation
        # Generar la contraseña segura
        password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        return password

    def generar_contrasena(self):
        # Generar una nueva contraseña y mostrarla en el QLineEdit (self.ui.lineEdit)
        psw = self.logica_contrasena(16)  # Puedes ajustar la longitud aquí
        self.ui.lineEdit.setText(psw)  # Muestra la contraseña en el campo de texto
        self.psw_guardada = psw  # Guarda la contraseña para poder usarla en la función guardar_contrasena

    
    # Guardar la contraseña en la base de datos
    def guardar_contrasena(self):
        psw = self.psw_guardada  # Obtenemos la contraseña generada en la función generar_contrasena
        usuario = self.ui.lineEdit_2.text()  # Lo que el usuario escribió en lineEdit_2
        correo = self.ui.lineEdit_3.text()   # Lo que el usuario escribió en lineEdit_3

        # Encriptar la contraseña antes de guardarla
        psw_encriptada = encriptar(psw)

        connection = get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Guardar la contraseña encriptada en la base de datos
                cursor.execute(
                    "INSERT INTO dbo.contrasenas (contrasena, usuario, correo) VALUES (?,?,?)",
                    (psw_encriptada, usuario, correo)
                )
                connection.commit()  # Confirmar los cambios
                print("Contraseña guardada exitosamente")
                
                # Mostrar alerta en la interfaz de usuario
                self.mostrar_alerta("Éxito", "Contraseña guardada exitosamente.")
            except Exception as e:
                print(f"Error al guardar la contraseña: {e}")
                self.mostrar_alerta("Error", "Hubo un problema al guardar la contraseña.")
            finally:
                connection.close()  # Cerrar la conexión
        else:
            print("No se pudo conectar a la base de datos para guardar la contraseña")
        

    # Función para mostrar alertas en la interfaz
    def mostrar_alerta(self, titulo, mensaje):
        alert = QMessageBox(self)
        alert.setIcon(QMessageBox.Information)  # Icono de información
        alert.setWindowTitle(titulo)  # Título de la ventana
        alert.setText(mensaje)  # Mensaje que se mostrará
        alert.setStandardButtons(QMessageBox.Ok)  # Botón de OK
        alert.exec_()  # Mostrar el cuadro de mensaje

    def abrir_ventana2(self):
        # Crear instancia de Ventana2
        ventana = Ventana2()
        ventana.cargar_contrasenas()
        ventana.exec_()  # Mostrar la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PswGenerator()
    window.show()
    sys.exit(app.exec_())
