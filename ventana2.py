from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QMessageBox
from DB_Conection import obtener_contrasenas, eliminar_contrasena
from ventana3 import VentanaEditar



class Ventana2(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ver Contraseñas")
        self.setGeometry(300, 300, 900, 500)  # Ajusta el tamaño y posición de la ventana

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(6)  # ID, Contraseña, Usuario, Correo, Acciones, Fecha de Guardado
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Contraseña', 'Usuario', 'Correo', 'Fecha de Guardado', 'Acciones'])

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def cargar_contrasenas(self):
        # Obtener las contraseñas de la base de datos
        contrasenas = obtener_contrasenas()
        # Recibir las contraseñas y mostrar en la tabla
        self.tableWidget.setRowCount(len(contrasenas))  # Ajustar las filas

        for row_num, row_data in enumerate(contrasenas):
            for col_num, data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))
        
        self.agregar_botones()

    def agregar_botones(self):  # Agregar los botones a la tabla
        self.tableWidget.setColumnWidth(5, 160)  # Ajusta el ancho de la columna "Acciones"

        for row_num in range(self.tableWidget.rowCount()):
            # Crear botones
            btnEditar = QPushButton("Editar")
            btnEliminar = QPushButton("Eliminar")
            btnEliminar.setMinimumSize(60, 25)

            # Conectar botones con las funciones
            btnEditar.clicked.connect(lambda _, row=row_num: self.editar_contrasena(row))
            btnEliminar.clicked.connect(lambda _, row=row_num: self.eliminar_contrasena(row))

            # Crear un contenedor para los botones
            widgetAcciones = QWidget()
            layoutAcciones = QHBoxLayout()
            layoutAcciones.addWidget(btnEditar)
            layoutAcciones.addWidget(btnEliminar)
            layoutAcciones.setContentsMargins(5, 0, 5, 0)  # Sin márgenes
            layoutAcciones.setSpacing(8)  # Espaciado entre botones
            widgetAcciones.setLayout(layoutAcciones)

            # Añadir el widget con los botones a la columna "Acciones"
            self.tableWidget.setCellWidget(row_num, 5, widgetAcciones)  # Asegúrate de que las "Acciones" estén en la columna 4

    def eliminar_contrasena(self, row):
        # Obtener el ID de la contraseña que se desea eliminar
        id_contrasena = self.tableWidget.item(row, 0).text()
        # Eliminar la contraseña de la base de datos llamando a la función de DB_Connection
        if eliminar_contrasena(id_contrasena):
            self.mostrar_alerta("Éxito", "Contraseña eliminada exitosamente.")
            self.cargar_contrasenas()  # Recargar la tabla después de la eliminación
        else:
            self.mostrar_alerta("Error", "Hubo un problema al eliminar la contraseña.")

    def editar_contrasena(self, row):
        # Obtener los datos de la contraseña seleccionada
        id_contrasena = self.tableWidget.item(row, 0).text()
        contrasena = self.tableWidget.item(row, 1).text()
        usuario = self.tableWidget.item(row, 2).text()
        correo = self.tableWidget.item(row, 3).text()
        fecha_guardado = self.tableWidget.item(row, 4).text()

        # Abrir la ventana de edición pasando los datos seleccionados
        ventana_editar = VentanaEditar(id_contrasena, contrasena, usuario, correo, fecha_guardado)
        ventana_editar.exec_()
        self.cargar_contrasenas()  # Recargar las contraseñas después de editar

    # Función para mostrar alertas en la interfaz
    def mostrar_alerta(self, titulo, mensaje):
        alert = QMessageBox(self)
        alert.setIcon(QMessageBox.Information)  # Icono de información
        alert.setWindowTitle(titulo)  # Título de la ventana
        alert.setText(mensaje)  # Mensaje que se mostrará
        alert.setStandardButtons(QMessageBox.Ok)  # Botón de OK
        alert.exec_()  # Mostrar el cuadro de mensaje

