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
import re
import pyautogui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QEvent, QThread
from threading import Event
import serial
import serial.tools.list_ports
# Taller # 1
# Autores: Luis Fernando Mendoza Cardona - José De Jesús Caro Urueta - Angel De Jesus Tuñon Cuello


class stream_gcode_Thread(QThread):
    def __init__(self):
        super().__init__()

    def stream_gcode(self, gcode_path):
        # with contect opens file/connection and closes it if function(with) scope is left
        with open(gcode_path, "r") as file, window.serial as ser:
            self.send_wake_up(ser)
            self.total_lines = 5
            self.processed_lines = 0
            for line in file:
                # cleaning up gcode from file
                cleaned_line = self.remove_eol_chars(
                    self.remove_comment(line))
                if cleaned_line:  # checks if string is empty
                    print("Sending gcode:" + str(cleaned_line))
                    # converts string to byte encoded string and append newline
                    command = str.encode(line + '\n')
                    ser.write(command)  # Send g-code

                    self.wait_for_movement_completion(ser, cleaned_line)

                    # processed_lines += 1
                    # percentage = (processed_lines / total_lines) * 100
                    # self.progreso(int(percentage))

                    grbl_out = ser.readline()  # Wait for response with carriage return
                    print(" : ", grbl_out.strip().decode('utf-8'))

            print('End of gcode')
            window.textEdit.setReadOnly(False)
    
    def remove_comment(self, string):
        if (string.find(';') == -1):
            return string
        else:
            return string[:string.index(';')]

    def remove_eol_chars(self, string):
        # removed \n or traling spaces
        return string.strip()

    def send_wake_up(self, ser):
        # Wake up
        # Hit enter a few times to wake the Printrbot
        ser.write(str.encode("\r\n\r\n"))
        time.sleep(2)   # Wait for Printrbot to initialize
        ser.flushInput()  # Flush startup text in serial input

    def wait_for_movement_completion(self, ser, cleaned_line):
        Event().wait(1)

        if cleaned_line != '$X' or '$$':
            idle_counter = 0

            while True:
                ser.reset_input_buffer()
                command = str.encode('?' + '\n')
                ser.write(command)
                
                start_time = time.time()
                timeout = 1.0  # Set the timeout to 1 second (adjust as needed)

                while time.time() - start_time < timeout:
                    grbl_out = ser.readline()
                    if grbl_out:
                        break  # Exit the inner loop if data is received

                print(grbl_out)
                grbl_response = grbl_out.strip().decode('utf-8')

                if grbl_response != 'ok':
                    if grbl_response.find('Idle') > 0:
                        idle_counter += 1

                if idle_counter > 10:
                    break
        return


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        loadUi("HMI_interfaz.ui", self)
        global comandos_g
        global distancia
        global velocidad
        global milisegundos
        global cone_mesh
        global cone
        global prev_x
        global prev_y
        global prev_Z
        self.archivo = []
        self.gcode = ""
        milisegundos = 200
        self.resolucion = 0.5
        distancia = 40
        comandos_g = "codigo_g.txt"
        # Variable para controlar la pausa/detención del proceso
        self.detener_proceso = False
        self.boton_parar_presionado = False
        self.pausar_proceso = False

        self.portList = []

        # Se iniciala la variable que nos permitirá acceder al puerto serial
        self.serial = None
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
        # Boton set home
        self.setHome.clicked.connect(self.set_home)

        # Se vincula accion para agregar archivo GCODE
        self.mni_subir_gcode.triggered.connect(self.subir_archivo)
        #  Se vinculan los botones de start y stop
        self.start.clicked.connect(self.comenzar)
        self.stop.clicked.connect(self.parar)
        # boton para limpiar consola
        self.limpiar_consola.clicked.connect(self.limpiar)

        # Se vincula boton de home con su funcion
        self.bt_home.clicked.connect(self.home)

        # Se leen los puertos
        self.read_ports()

        # Configura la gráfica 3D
        self.view3D = gl.GLViewWidget()
        self.view3D.setCameraPosition(
            distance=distancia, elevation=30, azimuth=225)

        # self.view3D.setBackgroundColor(QColor(179,226,255))
        self.view3D.setBackgroundColor(QColor(0, 0, 0))
        self.grid0 = gl.GLGridItem()
        self.grid0.setColor(QColor(255, 255, 255))
        self.grid0.setSize(20, 28, 1)
        self.view3D.addItem(self.grid0)

        self.X = 0
        self.Y = 0
        self.Z = 0

        velocidad = 150
        # Crear ejes X, Y, Z personalizados
        axis_width = 5  # Puedes ajustar este valor según tu preferencia

        # Eje X (rojo)
        x_axis_points = np.array([[-10, 14, 0], [-9, 14, 0]])
        x_axis = GLLinePlotItem(
            pos=x_axis_points, color=(1, 0, 0, 1), width=axis_width)

        # Eje Y (verde)
        y_axis_points = np.array([[-10, 14, 0], [-10, 13, 0]])
        y_axis = GLLinePlotItem(
            pos=y_axis_points, color=(0, 1, 0, 1), width=axis_width)

        # Eje Z (azul)
        z_axis_points = np.array([[-10, 14, 0], [-10, 14, 1]])
        z_axis = GLLinePlotItem(
            pos=z_axis_points, color=(0, 0, 1, 1), width=axis_width)

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

        # Conecta las señales del botón
        self.blink.installEventFilter(self)

        # Crear un cono de ejemplo
        cone = gl.MeshData.cylinder(
            rows=10, cols=20, radius=[0.0, 0.5], length=2.0)
        cone_mesh = gl.GLMeshItem(meshdata=cone, color=(1.0, 0.0, 0.0, 1.0))
        # Posición del cono en coordenadas (x, y, z)
        cone_mesh.translate(-10+self.X, -14+self.Y, 0+self.Z)

        # Agregar el cono a la vista 3D
        self.view3D.addItem(cone_mesh)

        # Inicializar una lista para rastrear el camino del cono
        self.path_points = []

        # Crear un objeto GLLinePlotItem para el camino
        self.path_item = gl.GLLinePlotItem()

        # Agregar el objeto GLLinePlotItem a la vista 3D
        self.view3D.addItem(self.path_item)

        self.progreso(0)

    # def remove_comment(self, string):
    #     if (string.find(';') == -1):
    #         return string
    #     else:
    #         return string[:string.index(';')]

    # def remove_eol_chars(self, string):
    #     # removed \n or traling spaces
    #     return string.strip()

    # def send_wake_up(self, ser):
    #     # Wake up
    #     # Hit enter a few times to wake the Printrbot
    #     ser.write(str.encode("\r\n\r\n"))
    #     time.sleep(2)   # Wait for Printrbot to initialize
    #     ser.flushInput()  # Flush startup text in serial input

    # def wait_for_movement_completion(self, ser, cleaned_line):

    #     Event().wait(1)

    #     if cleaned_line != '$X' or '$$':

    #         idle_counter = 0

    #         while True:

    #             # Event().wait(0.01)
    #             ser.reset_input_buffer()
    #             command = str.encode('?' + '\n')
    #             ser.write(command)
    #             grbl_out = ser.readline()
    #             print(grbl_out)
    #             grbl_response = grbl_out.strip().decode('utf-8')

    #             if grbl_response != 'ok':

    #                 if grbl_response.find('Idle') > 0:
    #                     idle_counter += 1

    #             if idle_counter > 10:
    #                 break
    #     return

    def calculate_percentage(total_lines, processed_lines):
        if total_lines == 0:
            return 100  # To avoid division by zero
        return (processed_lines / total_lines) * 100

    # def stream_gcode(self, gcode_path):
    #     # with contect opens file/connection and closes it if function(with) scope is left
    #     with open(gcode_path, "r") as file, self.serial as ser:
    #         self.send_wake_up(ser)
    #         total_lines = 5
    #         processed_lines = 0
    #         for line in file:
    #             # cleaning up gcode from file
    #             cleaned_line = self.remove_eol_chars(self.remove_comment(line))
    #             if cleaned_line:  # checks if string is empty
    #                 print("Sending gcode:" + str(cleaned_line))
    #                 # converts string to byte encoded string and append newline
    #                 command = str.encode(line + '\n')
    #                 ser.write(command)  # Send g-code

    #                 self.wait_for_movement_completion(ser,cleaned_line)

    #                 # processed_lines += 1
    #                 # percentage = (processed_lines / total_lines) * 100
    #                 # self.progreso(int(percentage))

    #                 grbl_out = ser.readline()  # Wait for response with carriage return
    #                 print(" : " , grbl_out.strip().decode('utf-8'))

    #         print('End of gcode')
    #         self.textEdit.setReadOnly(False)

    def limpiar(self):
        self.textEdit.setText("")

    def eventFilter(self, obj, event):
        if obj == self.blink and event.type() == QEvent.MouseButtonPress:
            # Cambia el icono cuando se presiona el botón
            self.blink.setIcon(QIcon('img\on.png'))
            gcode = "M3 S100\n G1 F1000\n M5 S0"
            self.button_sender(gcode)

        elif obj == self.blink and event.type() == QEvent.MouseButtonRelease:
            # Restaura el icono original cuando se suelta el botón
            self.blink.setIcon(QIcon('img\off.png'))

        return super().eventFilter(obj, event)

    def set_isometric_view(self):
        self.view3D.setCameraPosition(
            distance=distancia, elevation=30, azimuth=225)

    def set_front_view(self):
        self.view3D.setCameraPosition(
            distance=distancia, elevation=0, azimuth=90+180)

    def set_side_view(self):
        self.view3D.setCameraPosition(
            distance=distancia, elevation=0, azimuth=180)

    def set_top_view(self):
        self.view3D.setCameraPosition(
            distance=distancia+5, elevation=90, azimuth=-90)

    def subir_archivo(self):
        self.archivo = QFileDialog.getOpenFileName(
            self, 'Subir GCODE', 'C:\\', 'Archivo GCODE (*.gcode)')
        # Abre el archivo .gcode
        with open(self.archivo[0], 'r') as gcode_file:
            print(self.archivo[0])
            self.datos = gcode_file.read()
            self.textEdit.setText(self.datos)
        self.textEdit.setReadOnly(True)

    def read_ports(self):
        # Limpiar la lista actual de puertos
        self.cb_list_ports.clear()

        # Obtener la lista de puertos disponibles
        ports = [port.device for port in serial.tools.list_ports.comports()]

        # Agregar puertos a la lista
        self.cb_list_ports.addItems(ports)

    def serial_connect(self):
        # Funcion para conectar el puerto serial
        self.etiqueta_estado.setStyleSheet("color:#00FF00;")
        self.etiqueta_estado.setText("CONECTADO")
        port_name = self.cb_list_ports.currentText()

        try:
            # Intentar abrir el puerto serial
            self.serial = serial.Serial(port=port_name, baudrate=115200)
            print(f"Puerto serial {port_name} conectado.")
        except serial.SerialException as e:
            print(f"Error al conectar el puerto serial {port_name}: {e}")

    def serial_disconnect(self):
        # Funcion para desconectar el puerto serial
        self.etiqueta_estado.setStyleSheet("color:#FF0000;")
        self.etiqueta_estado.setText("DESCONECTADO")
        print("Puerto serial desconectado")
        if self.serial and self.serial.is_open:
            self.serial.close()
            print("Puerto serial desconectado.")

    def button_sender(self, datos):
        if self.serial and self.serial.is_open:
            try:
                # Convertir la cadena a bytes antes de enviarla
                datos_codificados = datos.encode()

                # Enviar datos
                self.serial.write(datos_codificados)
                print(f"Datos enviados: {datos}")
            except Exception as e:
                QMessageBox.warning(
                    self, "Error", f"Error al enviar datos: {e}")
        else:
            QMessageBox.warning(
                self, "Error", "El puerto serial no está conectado.")

    def button_sender(self, dato):
        with open(comandos_g, "w") as archivo:
            archivo.write(dato)

        stream_thread = self.stream_gcode_Thread()
        stream_thread.stream_gcode("codigo_g.txt")

        # Abrir el archivo en modo escritura, esto borrará el contenido existente
        with open(comandos_g, 'w') as archivo:
            pass  # No necesitas escribir nada, solo abrir el archivo en modo escritura lo limpiará

    def grafica_punto(self):
        # Actualizar el objeto GLLinePlotItem con los nuevos puntos
        try:
            self.path_points.append([-10 + self.X, -14 + self.Y, 0 + self.Z])
            if len(self.path_points) >= 2:
                path_array = np.array(self.path_points)
                self.path_item.setData(
                    pos=path_array, color=(1, 0, 0, 1), width=2)
        except Exception as e:
            print(f"Error: {e}")

    def set_home(self):
        self.button_sender("G10 L20 P1 X0 Y0 Z0")
        self.home()

    def avanza_y(self):

        prev_y = self.Y
        self.Y += self.resolucion
        self.button_sender(f"G1 Y{self.Y} F{velocidad}")
        cone_mesh.translate(0, self.Y - prev_y, 0)
        self.grafica_punto()

    def retrocede_y(self):
        prev_y = self.Y
        self.Y -= self.resolucion
        self.button_sender(f"G1 Y{self.Y} F{velocidad}")
        cone_mesh.translate(0, self.Y - prev_y, 0)
        self.grafica_punto()

    def avanza_x(self):
        prev_x = self.X
        self.X += self.resolucion
        self.button_sender(f"G1 X{self.X} F{velocidad}")
        cone_mesh.translate(self.X - prev_x, 0, 0)
        self.grafica_punto()

    def retrocede_x(self):
        prev_x = self.X
        self.X -= self.resolucion
        self.button_sender(f"G1 X{self.X} F{velocidad}")
        cone_mesh.translate(self.X - prev_x, 0, 0)
        self.grafica_punto()

    def avanza_z(self):
        prev_z = self.Z
        self.Z -= self.resolucion
        self.button_sender(f"G1 Z{self.Z} F{velocidad}")
        cone_mesh.translate(0, 0, self.Z - prev_z)
        self.grafica_punto()

    def retrocede_z(self):
        prev_z = self.Z
        self.Z += self.resolucion
        self.button_sender(f"G1 Z{self.Z} F{velocidad}")
        cone_mesh.translate(0, 0, self.Z - prev_z)
        self.grafica_punto()

    def home(self):
        prev_x = self.X
        prev_y = self.Y
        prev_z = self.Z
        self.X = self.Y = self.Z = 0.0
        self.button_sender(f"G1 X0 Y0 Z0 F{velocidad}")
        cone_mesh.translate(self.X - prev_x, self.Y - prev_y, self.Z - prev_z)

        # Reiniciar la lista de puntos del camino
        self.path_points = []
        try:
            # Actualizar el objeto GLLinePlotItem con la lista vacía para borrar el camino
            self.path_item.setData(pos=np.array(
                self.path_points), color=(1, 0, 0, 1), width=2)
            self.grafica_punto()
        except Exception as e:
            print(f"Error: {e}")

    def calcular_progreso_gcode(self, archivo_gcode):
        # Inicializa las variables para el seguimiento de coordenadas y progreso.
        longitud_total = 0
        distancia_actual = 0
        coordenadas_actuales = {'X': 0, 'Y': 0, 'Z': 0}
        print(coordenadas_actuales)
        # Expresiones regulares para buscar comandos G, X, Y y Z en el archivo G-code.
        patron_g = re.compile(r'G\d+(\.\d+)?')
        patron_x = re.compile(r'X[+-]?\d+(\.\d+)?')
        patron_y = re.compile(r'Y[+-]?\d+(\.\d+)?')
        patron_z = re.compile(r'Z[+-]?\d+(\.\d+)?')

        with open(archivo_gcode, 'r') as f:
            for linea in f:
                # Busca comandos G, X, Y y Z en la línea.
                comando_g = patron_g.search(linea)
                comando_x = patron_x.search(linea)
                comando_y = patron_y.search(linea)
                comando_z = patron_z.search(linea)

                if comando_g:
                    # Procesa el comando G encontrado.
                    codigo_g = comando_g.group()
                    # Aquí puedes realizar acciones específicas según el comando G encontrado si es necesario.

                if comando_x:
                    # Procesa el comando X encontrado.
                    valor_x = float(comando_x.group()[1:])
                    distancia_actual += abs(
                        coordenadas_actuales['X'] - valor_x)
                    coordenadas_actuales['X'] = valor_x

                if comando_y:
                    # Procesa el comando Y encontrado.
                    valor_y = float(comando_y.group()[1:])
                    distancia_actual += abs(
                        coordenadas_actuales['Y'] - valor_y)
                    coordenadas_actuales['Y'] = valor_y

                if comando_z:
                    # Procesa el comando Z encontrado.
                    valor_z = float(comando_z.group()[1:])
                    # Actualiza la coordenada Z si es necesario.

        # Devuelve el progreso en porcentaje.
        if longitud_total > 0:
            progreso = (distancia_actual / longitud_total) * 100
        else:
            # Si no se puede determinar la longitud total, se asume que el progreso es del 100%.
            progreso = 100

        return progreso

    def progreso(self, porcentaje):
        self.progressBar.setValue(porcentaje)

    def comenzar(self):
        self.boton_parar_presionado = False
        dato = self.textEdit.toPlainText()

        with open(comandos_g, "w") as archivo:
            archivo.write(dato)

        self.stream_thread = stream_gcode_Thread()
        self.stream_thread.stream_gcode("codigo_g.txt")

        # self.stream_gcode("codigo_g.txt")

    def parar(self):
        self.boton_parar_presionado = True
        if (self.boton_parar_presionado and not (self.detener_proceso)):
            self.detener_proceso = True
            self.button_sender("M2")

    def show_message_dialog(self, mensaje):
        "Funcion para mostrar mensaje en una panel de dialogo"
        message_box = QMessageBox()
        message_box.setWindowTitle("Mensaje de PyQt5")
        message_box.setText(mensaje)
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    def obtener_coordenada(self):
        prev_x = self.X
        prev_y = self.Y
        prev_z = self.Z
        # lines = [line for line in self.datos]
        # print(lines)
        # cone_mesh.translate(self.X - prev_x, 0, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
