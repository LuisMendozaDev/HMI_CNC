import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow,  QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
import pyqtgraph.opengl as gl
from PyQt5.QtGui import QColor
# Taller # 1
# Autores: Luis Fernando Mendoza Cardona - José De Jesús Caro Urueta - Angel De Jesus Tuñon Cuello

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        loadUi("HMI_interfaz.ui", self)
        self.setWindowTitle("Gráfica 3D con PyQt5 y Matplotlib")
        # Configura la gráfica 3D
        self.view3D = gl.GLViewWidget()
        self.view3D.setCameraPosition(distance=30, elevation=30, azimuth=45)
        self.view3D.setBackgroundColor(QColor(250,250,228))
        self.grid0 = gl.GLGridItem()
        self.grid0.setColor(QColor(0,0,0))
        self.grid0.setSize(15,25,1)
        self.view3D.addItem(self.grid0)
        self.plotWidget.addWidget(self.view3D)

        self.iso_button.clicked.connect(self.set_isometric_view)

        # Botones para vistas desde los lados
        self.front_button.clicked.connect(self.set_front_view)

        self.side_button.clicked.connect(self.set_side_view)

        self.top_button.clicked.connect(self.set_top_view)
        # Agrega una esfera de ejemplo
        # self.plot_example_sphere()

    def plot_example_sphere(self):
        # Crear una esfera de ejemplo
        sphere = gl.MeshData.sphere(rows=10, cols=20, radius=1.0)
        sphere_mesh = gl.GLMeshItem(meshdata=sphere, color=(1.0, 0.0, 0.0, 1.0))
        sphere_mesh.translate(0, 0, 0)  # Posición de la esfera en coordenadas (x, y, z)
                # Agregar la esfera a la vista
        self.view3D.addItem(sphere_mesh)

        

    def set_isometric_view(self):
        self.view3D.setCameraPosition(distance=30, elevation=30, azimuth=45)

    def set_front_view(self):
        self.view3D.setCameraPosition(distance=30, elevation=0, azimuth=0)

    def set_side_view(self):
        self.view3D.setCameraPosition(distance=30, elevation=0, azimuth=90)

    def set_top_view(self):
        self.view3D.setCameraPosition(distance=25, elevation=90, azimuth=90)

    # def parsOBJ(self, path):
    #     print('loading', path)

    #     vertices = []
    #     texture_coordinates = []
    #     faces = []
    #     try: 
    #         f = open(path, 'r')
    #         for line in f:
    #             if line[0] != '#':
    #                 line_parts = line.replace('\n', '').split(' ')
    #                 if line_parts[0] == 'v':
    #                     vertex = [float(line_parts[1]), float(line_parts[2]), float(line_parts[3])]
    #                     vertices.append(vertex)
    #                 elif line_parts[0] == 'vt':
    #                     tex_coord = [float(line_parts[1]), float(line_parts[2])]
    #                     texture_coordinates.append(tex_coord)
    #                 elif line_parts[0] == 'f' and len(line_parts) == 5:
    #                     face = [int(line_parts[1].split('/')[0])-1, int(line_parts[2].split('/')[0])-1, int(line_parts[3].split('/')[0])-1, int(line_parts[4].split('/')[0])-1]
    #                     faces.append(face)
    #         f.close()

    #         gl_vertices = []
    #         for face in faces:
    #             gl_vertices.append(vertices[face[0]])
    #             gl_vertices.append(vertices[face[1]])
    #             gl_vertices.append(vertices[face[2]])
    #             gl_vertices.append(vertices[face[3]])
    #     except Exception as e: 
    #         print("error: " +str(e))
    #     return np.asarray(gl_vertices)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
