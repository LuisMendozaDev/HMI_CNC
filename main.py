import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow,  QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from pyqtgraph.opengl import GLLinePlotItem
import pyqtgraph.opengl as gl
from PyQt5.QtGui import QColor
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import time
# Taller # 1
# Autores: Luis Fernando Mendoza Cardona - José De Jesús Caro Urueta - Angel De Jesus Tuñon Cuello

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        loadUi("HMI_interfaz.ui", self)
        global distancia
        global velocidad
        global cone_mesh
        global cone
        global prev_x
        global prev_y
        global prev_Z
        self.resolucion = 0.5
        distancia = 35

        self.portList = []

        # Se iniciala la variable que nos permitirá acceder al puerto serial
        self.serial = QSerialPort()
        self.setWindowTitle("Gráfica 3D con PyQt5 y Matplotlib")

        # Se vinculan los botones de actualizar, conectar y desconectar con las respectivas funciones
        self.bt_actualizar.clicked.connect(self.read_ports)
        self.bt_conectar.clicked.connect(self.serial_connect)
        self.bt_desconectar.clicked.connect(self.serial_disconnect)

        # Se vinculan los botones de avance de cada eje con sus respectivas funciones
        self.bt_y_avanza.clicked.connect(self.avanza_y)
        self.bt_y_retrocede.clicked.connect(self.retrocede_y)
        self.bt_x_avanza.clicked.connect(self.avanza_x)
        self.bt_x_retrocede.clicked.connect(self.retrocede_x)
        self.bt_z_avanza.clicked.connect(self.avanza_z)
        self.bt_z_retrocede.clicked.connect(self.retrocede_z)

        # Se vincula accion para agregar archivo GCODE
        self.mni_subir_gcode.triggered.connect(self.subir_archivo)
        #  Se vinculan los botones de start y stop
        self.start.clicked.connect(self.comenzar)
        self.stop.clicked.connect(self.parar)

        # Se vincula boton de home con su funcion
        self.bt_home.clicked.connect(self.home)
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

        self.X = 0
        self.Y = 0
        self.Z = 0

        velocidad = 200

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

        # Crear un cono de ejemplo
        cone = gl.MeshData.cylinder(rows=10, cols=20, radius=[0.0, 0.5], length=2.0)
        cone_mesh = gl.GLMeshItem(meshdata=cone, color=(1.0, 0.0, 0.0, 1.0))
        cone_mesh.translate(-10+self.X, -14+self.Y, 0+self.Z)  # Posición del cono en coordenadas (x, y, z)
        
        # Agregar el cono a la vista 3D
        self.view3D.addItem(cone_mesh)

        # Inicializar una lista para rastrear el camino del cono
        self.path_points = []

        # Crear un objeto GLLinePlotItem para el camino
        self.path_item = gl.GLLinePlotItem()

        # Agregar el objeto GLLinePlotItem a la vista 3D
        self.view3D.addItem(self.path_item)
    

    def set_isometric_view(self):
        self.view3D.setCameraPosition(distance=distancia, elevation=30, azimuth=225)

    def set_front_view(self):
        self.view3D.setCameraPosition(distance=distancia, elevation=0, azimuth=90+180)

    def set_side_view(self):
        self.view3D.setCameraPosition(distance=distancia, elevation=0, azimuth=180)

    def set_top_view(self):
        self.view3D.setCameraPosition(distance=distancia, elevation=90, azimuth=-90)
    
    def subir_archivo(self):
        archivo = QFileDialog.getOpenFileName(self, 'Subir GCODE', 'C:\\', 'Archivo GCODE (*.gcode)')
        # Abre el archivo .gcode
        with open(archivo[0], 'r') as gcode_file:
            self.datos = gcode_file.read()
            self.textEdit.setText(self.datos)

    def read_ports(self):
        # Funcion para leer puertos
        ports = QSerialPortInfo.availablePorts()
        for i in ports:
            self.portList.append(i.portName())
        print(self.portList)
        self.cb_list_ports.clear()
        self.cb_list_ports.addItems(self.portList)

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
            try:
                self.serial.write(data.encode())
                self.serial.flush()
                time.sleep(1)
            except Exception as e:
                print(f"Error: {e}")
    
    def grafica_punto(self):
        # Actualizar el objeto GLLinePlotItem con los nuevos puntos
        self.path_points.append([-10 + self.X, -14 + self.Y, 0 + self.Z])
        if len(self.path_points) >= 2:
            path_array = np.array(self.path_points)
            self.path_item.setData(pos=path_array, color=(1, 0, 0, 1), width=2) 

    def avanza_y(self):
        
        prev_y = self.Y
        self.Y+=self.resolucion
        self.send_data(f"G1 Y{self.Y} F{velocidad}")
        cone_mesh.translate(0, self.Y - prev_y, 0)
        self.grafica_punto()
    
    def retrocede_y(self):
        prev_y = self.Y
        self.Y-=self.resolucion
        self.send_data(f"G1 Y{self.Y} F{velocidad}")
        cone_mesh.translate(0, self.Y - prev_y,0)
        self.grafica_punto()
    
    def avanza_x(self):
        prev_x = self.X
        self.X+=self.resolucion
        self.send_data(f"G1 X{self.Y} F{velocidad}")
        cone_mesh.translate(self.X - prev_x, 0, 0)
        self.grafica_punto()
    
    def retrocede_x(self):
        prev_x = self.X
        self.X-=self.resolucion
        self.send_data(f"G1 X{self.Y} F{velocidad}")
        cone_mesh.translate(self.X - prev_x, 0, 0)
        self.grafica_punto()
    
    def avanza_z(self):
        prev_z = self.Z
        self.Z+=self.resolucion
        self.send_data(f"G1 Z{self.Y} F{velocidad}")
        cone_mesh.translate(0, 0, self.Z - prev_z)
        self.grafica_punto()
    
    def retrocede_z(self):
        prev_z = self.Z
        self.Z-=self.resolucion
        self.send_data(f"G1 Z{self.Y} F{velocidad}")
        cone_mesh.translate(0, 0, self.Z - prev_z)
        self.grafica_punto()

    def home(self):
        prev_x = self.X
        prev_y = self.Y
        prev_z = self.Z
        self.X = self.Y = self.Z = 0
        self.send_data(f"G1 X0 Y0 Z0 F{velocidad}")
        cone_mesh.translate(self.X - prev_x,self.Y -prev_y, self.Z - prev_z)

        # Reiniciar la lista de puntos del camino
        self.path_points = []

        # Actualizar el objeto GLLinePlotItem con la lista vacía para borrar el camino
        self.path_item.setData(pos=np.array(self.path_points), color=(1, 0, 0, 1), width=2)
        self.grafica_punto()
    def comenzar(self):
        dato = self.textEdit.toPlainText()
        print(dato)
        self.send_data(dato)

        self.obtener_coordenada()
        pass
    def parar(self):
        self.send_data('M0;')

    def show_message_dialog(self, mensaje):
        "Funcion para mostrar mensaje en una panel de dialogo"
        message_box = QMessageBox()
        message_box.setWindowTitle("Mensaje de PyQt5")
        message_box.setText(mensaje)
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    def subir(self):
        pass
    
    def obtener_coordenada(self):
        prev_x = self.X
        prev_y = self.Y
        prev_z = self.Z
        lines = [line for line in self.datos]
        print(lines)
        # cone_mesh.translate(self.X - prev_x, 0, 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
