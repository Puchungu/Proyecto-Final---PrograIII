from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout
from DB_Conection import obtener_contrasenas

class Ventana2(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ver Contraseñas")
        self.setGeometry(200, 200, 600, 400)  # Ajusta el tamaño y posición de la ventana
        
        # Crear un QTableWidget para mostrar las contraseñas
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(2)  # Suponiendo que tienes dos columnas: ID y Contraseña
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Contraseña'])

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

