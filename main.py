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
from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QThread, QIODevice, QCoreApplication
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

import speech_recognition as sr
from pydub.playback import play
from pydub import AudioSegment
from gtts import gTTS
import keyboard
import os


class PlayAudio(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def play_audio(self, string):
        # Funcion para pasar texto a audio
        tts = gTTS(text=string, lang='es')
        # Guarda el audio como un archivo temporal
        tts.save("tmp/temp.mp3")      
        file_path=os.path.abspath("tmp/temp.mp3")
        print(file_path)
        
        if os.path.exists(file_path):
            audio = AudioSegment.from_file(file_path)
            play(audio)
        else:
            print(f"El archivo {file_path} no existe.")

    def reproduce(self, file_path):
        if os.path.exists(file_path):
            audio = AudioSegment.from_file(file_path)
            play(audio)
        else:
            print(f"El archivo {file_path} no existe.")
        # Reproducir el audio
        play(audio)


class SerialHandler(QObject):
    error_occurred = pyqtSignal(int)
    connected = pyqtSignal(bool)
    data_received = pyqtSignal(str)

    def __init__(self, parent=None):

        super().__init__(parent)
        self.serial = QSerialPort()
        self.is_connected = False
        self.serial.errorOccurred.connect(self.handle_error)

    def get_serial_port(self):
        return self.serial

    def handle_error(self, error):
        self.error_occurred.emit(error)
        print(
            f"Error en el puerto serial: {error}, {self.serial.errorString()}")
        if error == QSerialPort.ResourceError:
            self.connected.emit(False)

    @pyqtSlot()
    def connect_serial(self, port_name, baud_rate):
        self.serial.setPortName(port_name)
        self.serial.setBaudRate(baud_rate)
        self.is_connected = self.serial.open(QIODevice.ReadWrite)
        if self.is_connected:
            self.connected.emit(True)
            self.send_data("\r\n\r\n")
        else:
            self.connected.emit(False)

    @pyqtSlot()
    def clear_serial_input(self):
        self.serial.clear(QSerialPort.Input)

    @pyqtSlot()
    def disconnect_serial(self):
        if self.is_connected:
            self.serial.close()
            self.connected.emit(False)

    @pyqtSlot(str)
    def send_data(self, data):
        data = data + "\n"
        if self.serial.isOpen():
            self.serial.write(data.encode())

    @pyqtSlot()
    def read_data(self):
        if not self.serial.canReadLine():
            return
        rx = self.serial.readLine()
        self.data_received.emit(str(rx, 'utf-8').strip())
        print(str(rx, 'utf-8').strip())

# Autores: Luis Fernando Mendoza Cardona - José De Jesús Caro Urueta - Angel De Jesus Tuñon Cuello


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
        global width
        global height
        
        self.imprimir_linea_actual=0
        self.numero_linea_actual=0
        self.numero_total_lineas=0

        self.serial_handler = SerialHandler()
        self.serial_thread = QThread()
        self.serial_handler.moveToThread(self.serial_thread)
        self.serial_thread.start()

        self.audio_player = PlayAudio()
        self.audio_player_thread = QThread()
        self.audio_player.moveToThread(self.audio_player_thread)
        self.audio_player_thread.start()

        self.listening = False

        # Se inicializa las variables para reconocer voz y activar microfono
        self.recognizer = sr.Recognizer()
        self.microphone = None

        # Dado que se precione la tecla espaciadora se ejecuta la funcion toggle_listening()
        keyboard.add_hotkey('j', lambda: self.toggle_listening())

        # Conecta la señal error_occurred a una función específica
        self.serial_handler.error_occurred.connect(self.handle_serial_error)
        self.audio_player

        self.is_connect = False
        self.archivo = []
        self.gcode = ""
        milisegundos = 200
        width = 17
        height = 27
        self.resolucion = 0.5
        self.slider_pasos.valueChanged.connect(self.pasos)
        distancia = 40
        comandos_g = "codigo_g.txt"
        # Variable para controlar la pausa/detención del proceso
        self.detener_proceso = False
        self.boton_parar_presionado = False
        self.pausar_proceso = False

        self.port_line = ""

        self.portList = []

        self.line_port = ""

        self.setWindowTitle("interfaz CNC modular")

        # Se vinculan los botones de actualizar, conectar y desconectar con las respectivas funciones
        self.bt_actualizar.clicked.connect(self.read_ports)
        self.bt_conectar.clicked.connect(self.serial_connect)
        self.bt_desconectar.clicked.connect(self.serial_disconnect)

        # Se vinculan los botones de avance de cada eje con sus respectivas 
        self.bt_y_avanza.clicked.connect(self.avanza_y)
        self.bt_y_retrocede.clicked.connect(self.retrocede_y)
        self.bt_x_avanza.clicked.connect(self.avanza_x)
        self.bt_x_retrocede.clicked.connect(self.retrocede_x)
        self.bt_z_avanza.clicked.connect(self.avanza_z)
        self.bt_z_retrocede.clicked.connect(self.retrocede_z)
        # handler para manejar hilo
        self.serial_handler.connected.connect(self.update_connection_status)
        # Boton set home
        self.setHome.clicked.connect(self.set_home)
        self.setHome.setToolTip("Establecer casa")

        # Se vincula accion para agregar archivo GCODE
        self.mni_subir_gcode.triggered.connect(self.subir_archivo)
        #  Se vinculan los botones de start y stop
        self.start.clicked.connect(self.comenzar)
        self.start.setToolTip("Comenzar proceso")
        self.stop.clicked.connect(self.parar)
        self.stop.setToolTip("Parada de emergencia")
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
        self.grid0.setSize(width, height, 1)
        self.view3D.addItem(self.grid0)

        self.X = 0
        self.Y = 0
        self.Z = 0

        self.velocidad_actual = 0
        self.potencia_actual = 0

        velocidad = 100
        # Crear ejes X, Y, Z personalizados
        axis_width = 5  # Puedes ajustar este valor según tu preferencia

        # Eje X (rojo)
        x_axis_points = np.array([[-width/2, height/2, 0], [-4.5, height/2, 0]])
        x_axis = GLLinePlotItem(
            pos=x_axis_points, color=(1, 0, 0, 1), width=axis_width)

        # Eje Y (verde)
        y_axis_points = np.array([[-width/2, height/2, 0], [-width/2, 6.5, 0]])
        y_axis = GLLinePlotItem(
            pos=y_axis_points, color=(0, 1, 0, 1), width=axis_width)

        # Eje Z (azul)
        z_axis_points = np.array([[-width/2, height/2, 0], [-width/2, height/2, 1]])
        z_axis = GLLinePlotItem(
            pos=z_axis_points, color=(0, 0, 1, 1), width=axis_width)

        # Agregar ejes a la vista 3D
        self.view3D.addItem(x_axis)
        self.view3D.addItem(y_axis)
        self.view3D.addItem(z_axis)
        self.plotWidget.addWidget(self.view3D)

        self.iso_button.clicked.connect(self.set_isometric_view)
        self.iso_button.setToolTip("Vista isometrica")

        # Botones para vistas desde los lados
        self.front_button.clicked.connect(self.set_front_view) 
        self.front_button.setToolTip("Vista frontal")

        self.side_button.clicked.connect(self.set_side_view)
        self.side_button.setToolTip("Vista lateral")

        self.top_button.clicked.connect(self.set_top_view)
        self.top_button.setToolTip("Vista superior")

        # Conecta las señales del botón
        self.blink.installEventFilter(self)
        self.blink.setToolTip("Blink")

        # Crear un cono de ejemplo
        cone = gl.MeshData.cylinder(
            rows=10, cols=20, radius=[0.0, 0.5], length=2.0)
        cone_mesh = gl.GLMeshItem(meshdata=cone, color=(1.0, 0.0, 0.0, 1.0))
        # Posición del cono en coordenadas (x, y, z)
        cone_mesh.translate(-width/2+self.X, -height/2+self.Y, 0+self.Z)

        # Agregar el cono a la vista 3D
        self.view3D.addItem(cone_mesh)

        # Inicializar una lista para rastrear el camino del cono
        self.path_points = []

        # Crear un objeto GLLinePlotItem para el camino
        # self.path_item = gl.GLLinePlotItem()

        self.path_item = gl.GLScatterPlotItem()
        # Agregar el objeto GLLinePlotItem a la vista 3D
        self.view3D.addItem(self.path_item)

        self.progressBar.setValue(0)
    
    def pasos(self, valor):
        self.resolucion = valor/10
        self.n_pasos.setText("Paso: " + str(self.resolucion))


    def toggle_listening(self):
        # funcion que se encarga de activar o desactivar el micro
        if self.listening:
            self.stop_listening()
        else:
            self.start_listening()

    def start_listening(self):
        # Funcion para activar el micro
        if not self.listening:
            self.microphone = sr.Microphone()
            self.listening = True
            with self.microphone as source:
                self.audio_player.play_audio("Escuchando")
                print('Escuchando...')
                audio = self.recognizer.listen(source, phrase_time_limit=5)
                self.print_transcription(audio)
                self.listening = False

    def stop_listening(self):
        # Funcion para desactivar el micro
        if self.listening and self.microphone is not None:
            self.listening = False
            self.microphone.__exit__(None, None, None)  # Cerrar el micrófono
            self.microphone = None  # Restablecer el micrófono a None

    def print_transcription(self, audio):
        # Funcion donde se ejecuta el reconocimiento de voz 
        try:
            n_puertos = len(self.portList)
            text = self.recognizer.recognize_google(audio, language='es-ES')
            print('Texto Escuchado: ' + text)
            if (("dame" in text or "Dame" in text or "dime" in text) and ("lista" in text or "listado" in text) and ("puerto" in text or "puertos" in text)):
                puerto = ""
                # Da el listado de puertos disponibles
                if (n_puertos != 0):
                    for i in range(n_puertos):
                        puerto = puerto + str(self.portList[i]) + ", "
                        print(puerto)
                    self.audio_player.play_audio("el listado de puerto es: " + puerto)
                else:
                    self.audio_player.play_audio("No hay puertos disponibles")
            elif ("conectar" in text and not ("des" in text) or "conectarse" in text):
                    # Conecta el puerto serial
                    self.serial_connect()
            elif ("desconectar" in text or "desconectarse" in text):
                    # Conecta el puerto serial
                    self.serial_disconnect()
            elif ("ir" in text and "casa" in text):
                self.audio_player.play_audio(string="Yendo a casa")
                self.home()
                self.audio_player.reproduce("audio_done.mp3")
            elif (("setear" in text or "establecer" in text) and ("casa" in text or "home" in text)):
                self.audio_player.play_audio(string="Seteando casa")
                self.set_home()
                self.audio_player.reproduce("audio_done.mp3")
            elif(("comenzar" in text or "empezar" in text) and "proceso" in text):
                self.comenzar()
            elif (("parar" in text or "detener" in text) and "emergencia" in text):
                self.parar()
            else:
                print('Comando no reconocido.')
                self.audio_player.play_audio("Comando no reconocido.")
        except Exception as e:  
            print(e)
    
    @pyqtSlot(int)
    def handle_serial_error(self, error_code):
        if error_code == QSerialPort.ResourceError:
            # Acciones específicas para manejar ResourceError
            self.serial_handler.connected.connect(self.update_connection_status)
            self.serial_handler.connected.disconnect(self.update_connection_status)
            self.audio_player.reproduce("alarm.mp3")
            self.audio_player.play_audio("el equipo se desconectó de manera imprevista")
            self.show_message_dialog("Error de recurso en el puerto serial. Desconectando...")
            

        elif error_code == QSerialPort.NoError:
            self.show_message_dialog("Conectado Correctamente")
        else:
            # Acciones genéricas para otros tipos de errores
            self.show_message_dialog("Error en el puerto serial (Código {}): {}".format(
                error_code, self.serial_handler.get_serial_port().errorString()))
        

    def read_ports(self):
        self.portList = [p.portName()
                         for p in QSerialPortInfo.availablePorts()]
        self.cb_list_ports.clear()
        self.cb_list_ports.addItems(self.portList)

    def send_data(self, data):
        self.serial_handler.send_data(data)

    def serial_connect(self):
        port_name = self.cb_list_ports.currentText()
        baud_rate = 115200
        # Envia la señal para que el hilo maneje la conexión
        self.serial_handler.connect_serial(port_name, baud_rate)
        self.serial_handler.connected.connect(self.update_connection_status)
        

    def update_connection_status(self, isConnect):
        self.is_connect = isConnect
        print(self.is_connect)
        if self.is_connect:
            self.bt_actualizar.setEnabled(False)
            self.bt_conectar.setEnabled(False)
            self.etiqueta_estado.setStyleSheet("color:#00FF00;")
            self.etiqueta_estado.setText("CONECTADO")
            self.audio_player.play_audio(string="Se conectó correctamente")
        else:
            self.bt_actualizar.setEnabled(True)
            self.bt_conectar.setEnabled(True)
            self.etiqueta_estado.setStyleSheet("color:#FF0000;")
            self.etiqueta_estado.setText("DESCONECTADO")
            self.audio_player.play_audio(string="Se desconectó correctamente")
        self.serial_handler.connected.disconnect(self.update_connection_status)

    def serial_disconnect(self):
        # Funcion para desconectar el puerto serial

        # Envia la señal para que el hilo maneje la desconexión
        self.serial_handler.disconnect_serial()
        self.serial_handler.connected.connect(self.update_connection_status)
        print("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    def obtener_coordenadas_velocidad_potencia(self, linea):
        coordenadas = {'X': self.X, 'Y': self.Y, 'Z': self.Z}
        velocidad = self.velocidad_actual
        potencia = self.potencia_actual

        # Eliminar comentarios
        linea = linea.split(";")[0].strip()

        # Asegurarse de que la línea sea un comando G-code válido
        if linea:
            partes = linea.split()

            for parte in partes:
                if parte[0] == 'G':
                    # Comando G, verificar si es movimiento lineal (G0 o G1)
                    if parte == 'G0' or parte == 'G1':
                        for componente in partes[1:]:
                            match = re.match(r"([XYZ])([+-]?\d+(\.\d+)?)", componente)
                            if match:
                                coordenada, valor = match.group(1), float(match.group(2))
                                setattr(self, coordenada, valor)
                                coordenadas[coordenada] = valor
                elif parte.startswith('F'):
                    # Velocidad (Feed Rate)
                    velocidad = float(parte[1:])
                elif parte[0] == 'S':
                    # Potencia
                    potencia = float(parte[1:])
        
        self.velocidad_actual = velocidad
        self.potencia_actual = potencia
        self.X, self.Y, self.Z = coordenadas['X'], coordenadas['Y'], coordenadas['Z']

        return coordenadas, velocidad, potencia
    
    # def grafica_punto(self, potencia = 0):
    #     # Actualizar el objeto GLLinePlotItem con los nuevos puntos
    #     try:
    #         self.path_points.append([-10 + self.X, -14 + self.Y, 0 + self.Z])
    #         if len(self.path_points) >= 2:
    #             path_array = np.array(self.path_points)
    #             self.path_item.setData(
    #             pos=path_array, color=(1, 0, 0, 1), width=2)
    #     except Exception as e:
    #         print(f"Error: {e}")

    # def grafica_punto(self, potencia=0):
    #     try:
    #         # Solo agregar puntos y graficar si la potencia está dentro de un rango adecuado
    #         if 100 <= self.potencia_actual <= 1000:
    #             # Obtener el punto actual
    #             current_point = np.array([[-width/2 + self.X, -height/2 + self.Y, 0 + self.Z]])

    #             # Agregar el punto actual a la lista de todos los puntos
    #             self.path_points.append(current_point)

    #             # Configurar la apariencia de todos los puntos
    #             all_points_array = np.concatenate(self.path_points)
    #             self.path_item.setData(pos=all_points_array, color=(1, 0, 0, 1), size=4)

    #     except Exception as e:
    #         print(f"Error: {e}")

    def grafica_punto(self, potencia=0):
        try:
            # Solo agregar puntos y graficar si la potencia está dentro de un rango adecuado
            if 100 <= potencia <= 1000:
                # Obtener el punto actual
                current_point = np.array([[-width/2 + self.X, -height/2 + self.Y, 0 + self.Z]])

                # Agregar el punto actual a la lista de todos los puntos
                self.path_points.append(current_point)

                # Configurar la apariencia de todos los puntos
                all_points_array = np.concatenate(self.path_points)
                self.path_item.setData(pos=all_points_array, color=(1, 0, 0, 1), size=4)

            # Actualizar potencia actual
            self.potencia_actual = potencia

        except Exception as e:
            print(f"Error: {e}")
    
    def stream_gcode(self, gcode_path):
        # Reads the G-code file
        with open(gcode_path, 'r') as gcodeFile:
            gcode = gcodeFile.readlines()
            
        self.numero_total_lineas=len(gcode)

        # Executes each line of the G-code
        for line in gcode:
            print(line)
            # Removes comments and end-of-line characters
            line = self.remove_comment(self.remove_eol_chars(line))

            # Makes sure the line is a valid command
            if line and line != "\n":
                # Writes the G-code to the printer
                self.send_data(line)
                coordenadas, velocidad, potencia = self.obtener_coordenadas_velocidad_potencia(line)
                #cone_mesh.translate(self.X - self.X_prev, self.Y - self.Y_prev, self.Z - self.Z_prev)
                #self.grafica_punto
                self.x_coord.display(coordenadas['X'])
                self.y_coord.display(coordenadas['Y'])
                self.z_coord.display(coordenadas['Z'])
                self.potencia.display(potencia)
                self.velocidad.display(velocidad)
                self.grafica_punto(potencia=potencia)

                # Waits for the "OK" response from the printer
                response = self.wait_for_ok_response()

                # Do something with the response if needed
                print(response)
                if self.detener_proceso or not(self.is_connect):
                    break

    def start_serial_reading(self):
        # Conectar la señal readyRead para manejar la llegada de nuevos datos
        self.serial_handler.get_serial_port().readyRead.connect(self.read_data_non_blocking)

    def read_data_non_blocking(self):
        # Manejar los datos disponibles de manera no bloqueante
        while self.serial_handler.get_serial_port().bytesAvailable() > 0:
            self.serial_handler.data_received.connect(
                self.data_received_from_port)
            response = self.port_line
            self.data_received_from_port(response)

    def wait_for_ok_response(self):
        response = ''

        while response.count("ok") == 0:
            # No uses waitForReadyRead aquí, ya que es bloqueante
            # Asegúrate de que esta función lea de manera no bloqueante
            self.serial_handler.read_data()
            self.serial_handler.data_received.connect(
                self.data_received_from_port)

            # Si deseas esperar un poco antes de verificar nuevamente, puedes usar un temporizador
            # QCoreApplication.processEvents() permite que la interfaz siga respondiendo
            QCoreApplication.processEvents()
            # Puedes ajustar el tiempo de espera según tus necesidades
            QThread.msleep(180)

            response += self.port_line
            if "ok" in response:
                break
        self.numero_linea_actual+=1
        self.numero_total_lineas
        self.imprimir_linea_actual=((self.numero_linea_actual/self.numero_total_lineas)*100)
        self.progressBar.setValue(int(self.imprimir_linea_actual))
        
        return response

    def calculate_percentage(total_lines, processed_lines):
        if total_lines == 0:
            return 100  # To avoid division by zero
        return (processed_lines / total_lines) * 100

    def limpiar(self):
        self.textEdit.setText("")
        self.textEdit.setReadOnly(False)
        self.limpiar_progreso()

    def eventFilter(self, obj, event):
        if obj == self.blink and event.type() == QEvent.MouseButtonPress:
            # Cambia el icono cuando se presiona el botón
            if self.is_connect:
                self.blink.setIcon(QIcon('img\on.png'))
                gcode = "M3 S100\n G1 F1000\n M5 S0"
                self.send_data(gcode)
            else:
                self.show_message_dialog("El Puerto Serial No Está Conectado")

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
            self, 'Subir GCODE', 'C:\\', 'Archivo GCODE (*.gcode);;Archivos NC (*.nc);;Archivos TXT (*.txt)')
        # Abre el archivo .gcode
        with open(self.archivo[0], 'r') as gcode_file:
            print(self.archivo[0])
            self.datos = gcode_file.read()
            self.textEdit.setText(self.datos)
        self.textEdit.setReadOnly(True)

    def remove_comment(self, string: str):
        if (string.find(';') == -1):
            return string
        else:
            return string[:string.index(';')]

    def remove_eol_chars(self, string: str):
        # removed \n or traling spaces
        return string.strip()

    def set_home(self):
        if self.is_connect:
            self.send_data("G92 X0 Y0 Z0")
            self.home()
        else:
            self.show_message_dialog("El Puerto Serial No Está Conectado")

    def avanza_y(self):
        if self.is_connect:
            prev_y = self.Y
            self.Y += self.resolucion
            self.send_data(f"G1 Y{self.Y} F{velocidad}")
            cone_mesh.translate(0, self.Y - prev_y, 0)
            self.grafica_punto()
        else:
            self.show_message_dialog("El Puerto Serial No Está Conectado")

    def retrocede_y(self):
        if self.is_connect:
            prev_y = self.Y
            self.Y -= self.resolucion
            self.send_data(f"G1 Y{self.Y} F{velocidad}")
            cone_mesh.translate(0, self.Y - prev_y, 0)
            self.grafica_punto()
        else:
            self.show_message_dialog("El Puerto Serial No Está Conectado")

    def avanza_x(self):
        if self.is_connect:
            prev_x = self.X
            self.X += self.resolucion
            self.send_data(f"G1 X{self.X} F{velocidad}")
            cone_mesh.translate(self.X - prev_x, 0, 0)
            self.grafica_punto()
        else:
            self.show_message_dialog("El Puerto Serial No Está Conectado")

    def retrocede_x(self):
        if self.is_connect:
            prev_x = self.X
            self.X -= self.resolucion
            self.send_data(f"G1 X{self.X} F{velocidad}")
            cone_mesh.translate(self.X - prev_x, 0, 0)
            self.grafica_punto()
        else:
            self.show_message_dialog("El Puerto Serial No Está Conectado")

    def avanza_z(self):
        if self.is_connect:
            prev_z = self.Z
            self.Z -= self.resolucion
            self.send_data(f"G1 Z{self.Z} F{velocidad}")
            cone_mesh.translate(0, 0, self.Z - prev_z)
            self.grafica_punto()
        else:
            self.show_message_dialog("El Puerto Serial No Está Conectado")

    def retrocede_z(self):
        if self.is_connect:
            prev_z = self.Z
            self.Z += self.resolucion
            self.send_data(f"G1 Z{self.Z} F{velocidad}")
            cone_mesh.translate(0, 0, self.Z - prev_z)
            self.grafica_punto()
        else:
            self.show_message_dialog("El Puerto Serial No Está Conectado")

    def home(self):
        if self.is_connect:
            prev_x = self.X
            prev_y = self.Y
            prev_z = self.Z
            self.X = self.Y = self.Z = 0.0
            self.send_data(f"G1 X0 Y0 Z0 F{velocidad}")
            cone_mesh.translate(self.X - prev_x, self.Y -
                                prev_y, self.Z - prev_z)

            # Reiniciar la lista de puntos del camino
            self.path_points = []
            try:
                # Actualizar el objeto GLLinePlotItem con la lista vacía para borrar el camino
                self.path_item.setData(pos=np.array(
                    self.path_points), color=(1, 0, 0, 1), width=2)
                self.grafica_punto()
            except Exception as e:
                print(f"Error: {e}")
        else:
            self.show_message_dialog("El Puerto Serial No Está Conectado")
        
    def limpiar_progreso(self):
        self.numero_linea_actual=0
        self.numero_total_lineas=0
        self.imprimir_linea_actual=0
        self.progressBar.setValue(self.imprimir_linea_actual)

    def comenzar(self):
        self.audio_player.play_audio(string="Iniciar proceso. 3..., 2..., 1")
        if self.is_connect:
            self.limpiar_progreso()
            self.boton_parar_presionado = False
            dato = self.textEdit.toPlainText()

            with open(comandos_g, "w") as archivo:
                archivo.write(dato)
            
            self.limpiar_consola.setEnabled(False)
            self.stream_gcode("codigo_g.txt")
            self.limpiar_consola.setEnabled(True)
            self.audio_player.reproduce("audio_done.mp3")
        else:
            self.show_message_dialog("El Puerto Serial No Está Conectado")

    @pyqtSlot(str)
    def data_received_from_port(self, data):
        self.port_line = data

    def parar(self):
        if self.is_connect:
            self.boton_parar_presionado = True
            if (self.boton_parar_presionado and not (self.detener_proceso)):
                self.detener_proceso = True
                self.send_data("M2")
                self.audio_player.play_audio(string="Se detuvo el proceso")
        else:
            self.show_message_dialog("El Puerto Serial No Está Conectado")

    def show_message_dialog(self, mensaje):
        "Funcion para mostrar mensaje en una panel de dialogo"
        message_box = QMessageBox()
        message_box.setWindowTitle("GRBL Sender")
        message_box.setText(mensaje)
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
