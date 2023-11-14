# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HMI_interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1353, 1021)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.mni_subir_gcode = QAction(MainWindow)
        self.mni_subir_gcode.setObjectName(u"mni_subir_gcode")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(409, 192))
        self.frame_5.setMaximumSize(QSize(430, 192))
        self.frame_5.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cb_list_ports = QComboBox(self.frame_5)
        self.cb_list_ports.setObjectName(u"cb_list_ports")

        self.verticalLayout_3.addWidget(self.cb_list_ports)

        self.bt_conectar = QPushButton(self.frame_5)
        self.bt_conectar.setObjectName(u"bt_conectar")
        self.bt_conectar.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.verticalLayout_3.addWidget(self.bt_conectar)

        self.bt_actualizar = QPushButton(self.frame_5)
        self.bt_actualizar.setObjectName(u"bt_actualizar")
        self.bt_actualizar.setStyleSheet(u"background-color: rgb(76, 151, 227);")

        self.verticalLayout_3.addWidget(self.bt_actualizar)

        self.bt_desconectar = QPushButton(self.frame_5)
        self.bt_desconectar.setObjectName(u"bt_desconectar")
        self.bt_desconectar.setStyleSheet(u"background-color: rgb(234, 0, 0);")

        self.verticalLayout_3.addWidget(self.bt_desconectar)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.etiqueta_estado = QLabel(self.frame_6)
        self.etiqueta_estado.setObjectName(u"etiqueta_estado")
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Text"])
        font.setPointSize(18)
        font.setBold(True)
        self.etiqueta_estado.setFont(font)
        self.etiqueta_estado.setLayoutDirection(Qt.RightToLeft)
        self.etiqueta_estado.setStyleSheet(u"color: #fff;\n"
"")
        self.etiqueta_estado.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.etiqueta_estado)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(434, 414))
        self.frame_2.setMaximumSize(QSize(434, 414))
        self.frame_2.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(414, 0))
        self.progressBar.setMaximumSize(QSize(414, 16777215))
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setMinimumSize(QSize(414, 0))
        self.textEdit.setMaximumSize(QSize(377, 16777215))
        self.textEdit.setStyleSheet(u"background:rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.limpiar_consola = QPushButton(self.frame_2)
        self.limpiar_consola.setObjectName(u"limpiar_consola")
        self.limpiar_consola.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: #FFF;")

        self.verticalLayout_2.addWidget(self.limpiar_consola)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.bt_x_retrocede = QPushButton(self.frame_3)
        self.bt_x_retrocede.setObjectName(u"bt_x_retrocede")
        self.bt_x_retrocede.setMinimumSize(QSize(75, 75))
        self.bt_x_retrocede.setMaximumSize(QSize(75, 75))
        self.bt_x_retrocede.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"img/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_x_retrocede.setIcon(icon)
        self.bt_x_retrocede.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.bt_x_retrocede, 2, 0, 1, 1)

        self.bt_home = QPushButton(self.frame_3)
        self.bt_home.setObjectName(u"bt_home")
        self.bt_home.setMinimumSize(QSize(75, 75))
        self.bt_home.setMaximumSize(QSize(75, 75))
        self.bt_home.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"img/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_home.setIcon(icon1)
        self.bt_home.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.bt_home, 2, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 1, 2, 1, 1)

        self.bt_z_avanza = QPushButton(self.frame_3)
        self.bt_z_avanza.setObjectName(u"bt_z_avanza")
        self.bt_z_avanza.setMinimumSize(QSize(75, 75))
        self.bt_z_avanza.setMaximumSize(QSize(75, 75))
        self.bt_z_avanza.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"img/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_z_avanza.setIcon(icon2)
        self.bt_z_avanza.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.bt_z_avanza, 0, 5, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 2, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 2, 1, 1, 1)

        self.bt_x_avanza = QPushButton(self.frame_3)
        self.bt_x_avanza.setObjectName(u"bt_x_avanza")
        self.bt_x_avanza.setMinimumSize(QSize(75, 75))
        self.bt_x_avanza.setMaximumSize(QSize(75, 75))
        self.bt_x_avanza.setLayoutDirection(Qt.RightToLeft)
        self.bt_x_avanza.setStyleSheet(u"background: rgb(255, 255, 255)")
        icon3 = QIcon()
        icon3.addFile(u"img/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_x_avanza.setIcon(icon3)
        self.bt_x_avanza.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.bt_x_avanza, 2, 4, 1, 1)

        self.bt_z_retrocede = QPushButton(self.frame_3)
        self.bt_z_retrocede.setObjectName(u"bt_z_retrocede")
        self.bt_z_retrocede.setMinimumSize(QSize(75, 75))
        self.bt_z_retrocede.setMaximumSize(QSize(75, 75))
        self.bt_z_retrocede.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u"img/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_z_retrocede.setIcon(icon4)
        self.bt_z_retrocede.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.bt_z_retrocede, 4, 5, 1, 1)

        self.bt_y_retrocede = QPushButton(self.frame_3)
        self.bt_y_retrocede.setObjectName(u"bt_y_retrocede")
        self.bt_y_retrocede.setMinimumSize(QSize(75, 75))
        self.bt_y_retrocede.setMaximumSize(QSize(75, 75))
        self.bt_y_retrocede.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.bt_y_retrocede.setIcon(icon4)
        self.bt_y_retrocede.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.bt_y_retrocede, 4, 2, 1, 1)

        self.bt_y_avanza = QPushButton(self.frame_3)
        self.bt_y_avanza.setObjectName(u"bt_y_avanza")
        self.bt_y_avanza.setMinimumSize(QSize(75, 75))
        self.bt_y_avanza.setMaximumSize(QSize(75, 75))
        self.bt_y_avanza.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.bt_y_avanza.setIcon(icon2)
        self.bt_y_avanza.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.bt_y_avanza, 0, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 3, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_7.addWidget(self.frame_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(831, 721))
        self.frame.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(701, 691))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.plotWidget = QGridLayout()
        self.plotWidget.setObjectName(u"plotWidget")

        self.horizontalLayout_7.addLayout(self.plotWidget)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.x_coord = QLCDNumber(self.frame)
        self.x_coord.setObjectName(u"x_coord")
        self.x_coord.setMinimumSize(QSize(75, 50))
        self.x_coord.setMaximumSize(QSize(75, 50))
        self.x_coord.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.x_coord)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.y_coord = QLCDNumber(self.frame)
        self.y_coord.setObjectName(u"y_coord")
        self.y_coord.setMinimumSize(QSize(75, 50))
        self.y_coord.setMaximumSize(QSize(75, 50))
        self.y_coord.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.y_coord)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.z_coord = QLCDNumber(self.frame)
        self.z_coord.setObjectName(u"z_coord")
        self.z_coord.setMinimumSize(QSize(75, 50))
        self.z_coord.setMaximumSize(QSize(75, 50))
        self.z_coord.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.z_coord)

        self.verticalSpacer_5 = QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.iso_button = QPushButton(self.frame)
        self.iso_button.setObjectName(u"iso_button")
        self.iso_button.setMinimumSize(QSize(75, 75))
        self.iso_button.setMaximumSize(QSize(75, 75))
        self.iso_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u"img/isometric.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iso_button.setIcon(icon5)
        self.iso_button.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.iso_button)

        self.side_button = QPushButton(self.frame)
        self.side_button.setObjectName(u"side_button")
        self.side_button.setMinimumSize(QSize(75, 75))
        self.side_button.setMaximumSize(QSize(75, 75))
        self.side_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u"img/Lateral.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_button.setIcon(icon6)
        self.side_button.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.side_button)

        self.top_button = QPushButton(self.frame)
        self.top_button.setObjectName(u"top_button")
        self.top_button.setMinimumSize(QSize(75, 75))
        self.top_button.setMaximumSize(QSize(75, 75))
        self.top_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u"img/top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.top_button.setIcon(icon7)
        self.top_button.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.top_button)

        self.front_button = QPushButton(self.frame)
        self.front_button.setObjectName(u"front_button")
        self.front_button.setMinimumSize(QSize(75, 75))
        self.front_button.setMaximumSize(QSize(75, 75))
        self.front_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u"img/Front.png", QSize(), QIcon.Normal, QIcon.Off)
        self.front_button.setIcon(icon8)
        self.front_button.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.front_button)


        self.verticalLayout_6.addLayout(self.verticalLayout)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_6 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_8.addWidget(self.frame)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(831, 141))
        self.frame_4.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_5.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_5.addWidget(self.radioButton_2)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(250, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(100, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.potencia = QLCDNumber(self.frame_7)
        self.potencia.setObjectName(u"potencia")
        self.potencia.setMinimumSize(QSize(75, 50))
        self.potencia.setMaximumSize(QSize(16777215, 50))
        self.potencia.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.potencia)


        self.horizontalLayout_8.addWidget(self.frame_7)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_5)

        self.lcdNumber = QLCDNumber(self.frame_10)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(75, 50))
        self.lcdNumber.setMaximumSize(QSize(16777215, 50))
        self.lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.lcdNumber)


        self.horizontalLayout_8.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.horizontalSpacer_2 = QSpacerItem(457, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.setHome = QPushButton(self.frame_4)
        self.setHome.setObjectName(u"setHome")
        self.setHome.setMinimumSize(QSize(80, 80))
        self.setHome.setMaximumSize(QSize(80, 80))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Heavy"])
        font1.setPointSize(11)
        self.setHome.setFont(font1)
        self.setHome.setStyleSheet(u"background:rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.setHome)

        self.horizontalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.blink = QPushButton(self.frame_4)
        self.blink.setObjectName(u"blink")
        self.blink.setMinimumSize(QSize(80, 80))
        self.blink.setMaximumSize(QSize(80, 80))
        self.blink.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon9 = QIcon()
        icon9.addFile(u"img/off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.blink.setIcon(icon9)
        self.blink.setIconSize(QSize(60, 60))

        self.horizontalLayout_2.addWidget(self.blink)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.start = QPushButton(self.frame_4)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(80, 80))
        self.start.setMaximumSize(QSize(80, 80))
        self.start.setAcceptDrops(False)
        self.start.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon10 = QIcon()
        icon10.addFile(u"img/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start.setIcon(icon10)
        self.start.setIconSize(QSize(70, 70))

        self.horizontalLayout_2.addWidget(self.start)

        self.horizontalSpacer = QSpacerItem(10, 30, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.stop = QPushButton(self.frame_4)
        self.stop.setObjectName(u"stop")
        self.stop.setMinimumSize(QSize(80, 80))
        self.stop.setMaximumSize(QSize(80, 80))
        self.stop.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addFile(u"img/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop.setIcon(icon11)
        self.stop.setIconSize(QSize(90, 90))

        self.horizontalLayout_2.addWidget(self.stop)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_8.addWidget(self.frame_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1353, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.mni_subir_gcode)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mni_subir_gcode.setText(QCoreApplication.translate("MainWindow", u"Subir GCODE", None))
#if QT_CONFIG(shortcut)
        self.mni_subir_gcode.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.bt_conectar.setText(QCoreApplication.translate("MainWindow", u"CONECTAR", None))
        self.bt_actualizar.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.bt_desconectar.setText(QCoreApplication.translate("MainWindow", u"DESCONECTAR", None))
        self.etiqueta_estado.setText(QCoreApplication.translate("MainWindow", u"ESTADO", None))
        self.limpiar_consola.setText(QCoreApplication.translate("MainWindow", u"Limpiar Consola", None))
        self.bt_x_retrocede.setText("")
        self.bt_home.setText("")
        self.bt_z_avanza.setText("")
        self.bt_x_avanza.setText("")
        self.bt_z_retrocede.setText("")
        self.bt_y_retrocede.setText("")
        self.bt_y_avanza.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.iso_button.setText("")
        self.side_button.setText("")
        self.top_button.setText("")
        self.front_button.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"HERRAMIENTA", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"LASER", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RUTEADORA", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"POTENCIA", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"VELOCIDAD", None))
        self.setHome.setText(QCoreApplication.translate("MainWindow", u"SET HOME", None))
        self.blink.setText("")
#if QT_CONFIG(tooltip)
        self.start.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.start.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.start.setText("")
#if QT_CONFIG(shortcut)
        self.start.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+Return", None))
#endif // QT_CONFIG(shortcut)
        self.stop.setText("")
#if QT_CONFIG(shortcut)
        self.stop.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X, Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

