import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow  # Importar la clase generada de tu archivo UI
import secrets
import string

class PswGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Instancia de la clase de UI
        self.ui.setupUi(self)  # Configura la UI en esta ventana

        # Conectar el botón "Generar Nueva Contrasena" a la función generar_contrasena
        self.ui.pushButton.clicked.connect(self.generar_contrasena)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PswGenerator()
    window.show()
    sys.exit(app.exec_())
