import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow,  QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
from pyqtgraph.opengl import GLLinePlotItem
import pyqtgraph.opengl as gl
from PyQt5.QtGui import QColor
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
# Taller # 1
# Autores: Luis Fernando Mendoza Cardona - José De Jesús Caro Urueta - Angel De Jesus Tuñon Cuello

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        loadUi("HMI_interfaz.ui", self)
        global distancia
        distancia = 35

        # Se iniciala la variable que nos permitirá acceder al puerto serial
        self.serial = QSerialPort()
        self.setWindowTitle("Gráfica 3D con PyQt5 y Matplotlib")

        # Se vinculan los botones de actualizar, conectar y desconectar con las respectivas funciones
        self.bt_actualizar.clicked.connect(self.read_ports)
        self.bt_conectar.clicked.connect(self.serial_connect)
        self.bt_desconectar.clicked.connect(self.serial_disconnect)

        # Dado que se conecte el puerto serial, se leen los datos que hay en él
        self.serial.readyRead.connect(self.read_data)

        # Se leen los puertos
        self.read_ports()

        # Configura la gráfica 3D
        self.view3D = gl.GLViewWidget()
        self.view3D.setCameraPosition(distance=distancia, elevation=30, azimuth=225)

        # self.view3D.setBackgroundColor(QColor(179,226,255))
        self.view3D.setBackgroundColor(QColor(0,0,0))
        self.grid0 = gl.GLGridItem()
        self.grid0.setColor(QColor(255,255,255))
        self.grid0.setSize(20,28,1)
        self.view3D.addItem(self.grid0)
        # Crear ejes X, Y, Z personalizados
        axis_width = 5  # Puedes ajustar este valor según tu preferencia

        # Eje X (rojo)
        x_axis_points = np.array([[-10, 14, 0], [-9, 14, 0]])
        x_axis = GLLinePlotItem(pos=x_axis_points, color=(1, 0, 0, 1), width=axis_width)

        # Eje Y (verde)
        y_axis_points = np.array([[-10, 14, 0], [-10, 13, 0]])
        y_axis = GLLinePlotItem(pos=y_axis_points, color=(0, 1, 0, 1), width=axis_width)

        # Eje Z (azul)
        z_axis_points = np.array([[-10, 14, 0], [-10, 14, 1]])
        z_axis = GLLinePlotItem(pos=z_axis_points, color=(0, 0, 1, 1), width=axis_width)

        # Agregar ejes a la vista 3D
        self.view3D.addItem(x_axis)
        self.view3D.addItem(y_axis)
        self.view3D.addItem(z_axis)
        self.plotWidget.addWidget(self.view3D)

        self.iso_button.clicked.connect(self.set_isometric_view)

        # Botones para vistas desde los lados
        self.front_button.clicked.connect(self.set_front_view)

        self.side_button.clicked.connect(self.set_side_view)

        self.top_button.clicked.connect(self.set_top_view)
        # Agrega una esfera de ejemplo
        self.plot_example_cone()

    def plot_example_cone(self):
        # Crear un cono de ejemplo
        cone = gl.MeshData.cylinder(rows=10, cols=20, radius=[0.0, 0.5], length=2.0)
        cone_mesh = gl.GLMeshItem(meshdata=cone, color=(1.0, 0.0, 0.0, 1.0))
        cone_mesh.translate(-10, 14, 0)  # Posición del cono en coordenadas (x, y, z)
        
        # Agregar el cono a la vista 3D
        self.view3D.addItem(cone_mesh)

    def set_isometric_view(self):
        self.view3D.setCameraPosition(distance=distancia, elevation=30, azimuth=225)

    def set_front_view(self):
        self.view3D.setCameraPosition(distance=distancia, elevation=0, azimuth=90+180)

    def set_side_view(self):
        self.view3D.setCameraPosition(distance=distancia, elevation=0, azimuth=180)

    def set_top_view(self):
        self.view3D.setCameraPosition(distance=distancia, elevation=90, azimuth=-90)

    def read_ports(self):
        # Funcion para leer puertos
        ports = QSerialPortInfo.availablePorts()
        for i in ports:
            self.portList.append(i.portName())
        print(self.portList)
        self.cb_list_ports.clear()
        self.cb_list_baudrates.clear()
        self.cb_list_ports.addItems(self.portList)
        self.cb_list_baudrates.setCurrentText("9600")

    def serial_connect(self):
        # Funcion para conectar el puerto serial
        self.etiqueta_estado.setStyleSheet("color:#00FF00;")
        self.etiqueta_estado.setText("CONECTADO")
        print("Puerto Serial Conectado")
        self.serial.waitForReadyRead(10)
        self.port = self.cb_list_ports.currentText()
        self.baudrates = 115200
        self.serial.setBaudRate(int(self.baudrates))
        self.serial.setPortName(self.port)
        self.serial.open(QIODevice.ReadWrite)

    def serial_disconnect(self):
        # Funcion para desconectar el puerto serial
        self.etiqueta_estado.setStyleSheet("color:#FF0000;")
        self.etiqueta_estado.setText("DESCONECTADO")
        print("Puerto serial desconectado")
        self.serial.close()

    def read_data(self):
        # Funcion para leer los datos que viene del canal serial
        if not self.serial.canReadLine():
            return
        rx = self.serial.readLine()
        self.x = str(rx, 'utf-8').strip()

    def send_data(self, data):
        # Funcion para enviar datos
        data = data + "\n"
        print(data)
        if (self.serial.isOpen):
            self.serial.write(data.encode())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
