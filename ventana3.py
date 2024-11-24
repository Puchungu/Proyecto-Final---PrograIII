from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QMessageBox
from DB_Conection import editar_contrasena
from utils import encriptar


class VentanaEditar(QDialog):
    def __init__(self, id_contrasena, contrasena, usuario, correo, fecha_guardado):
        super().__init__()

        self.setWindowTitle("Editar Contraseña")
        self.setGeometry(250, 250, 400, 300)  # Ajusta el tamaño y la posición de la ventana

        # Almacenar los valores originales
        self.id_contrasena = id_contrasena
        self.contrasena_actual = contrasena

        # Crear los campos de texto para la edición
        self.txtContrasena = QLineEdit(self)
        self.txtContrasena.setText(contrasena)
        self.txtUsuario = QLineEdit(self)
        self.txtUsuario.setText(usuario)
        self.txtCorreo = QLineEdit(self)
        self.txtCorreo.setText(correo)

        # Crear el botón para guardar los cambios
        self.btnGuardar = QPushButton("Guardar Cambios", self)
        self.btnGuardar.clicked.connect(self.guardar_cambios)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Contraseña:"))
        layout.addWidget(self.txtContrasena)
        layout.addWidget(QLabel("Usuario:"))
        layout.addWidget(self.txtUsuario)
        layout.addWidget(QLabel("Correo:"))
        layout.addWidget(self.txtCorreo)
        layout.addWidget(self.btnGuardar)

        self.setLayout(layout)

    def guardar_cambios(self):
        # Obtener los nuevos valores de los campos de texto
        nueva_contrasena = self.txtContrasena.text()
        nuevo_usuario = self.txtUsuario.text()
        nuevo_correo = self.txtCorreo.text()

        # Encriptar la contraseña antes de guardarla
        nueva_contrasena_encriptada = encriptar(nueva_contrasena)

        # Llamar a la función editar_contrasena con la contraseña encriptada
        if editar_contrasena(self.id_contrasena, nueva_contrasena_encriptada, nuevo_usuario, nuevo_correo):
            self.mostrar_alerta("Éxito", "Contraseña actualizada exitosamente.")
            self.accept()  # Cerrar la ventana de edición
        else:
            self.mostrar_alerta("Error", "Hubo un problema al actualizar la contraseña.")



    def mostrar_alerta(self, titulo, mensaje):
        alert = QMessageBox(self)
        alert.setIcon(QMessageBox.Information)
        alert.setWindowTitle(titulo)
        alert.setText(mensaje)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()
