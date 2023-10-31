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
    QHBoxLayout, QLCDNumber, QLabel, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1293, 944)
        self.actionSubir_GCODE = QAction(MainWindow)
        self.actionSubir_GCODE.setObjectName(u"actionSubir_GCODE")
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
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cb_portlist = QComboBox(self.frame_5)
        self.cb_portlist.setObjectName(u"cb_portlist")

        self.verticalLayout_3.addWidget(self.cb_portlist)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_11 = QPushButton(self.frame_5)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_3.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_5)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_3.addWidget(self.pushButton_12)

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

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
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
        self.textEdit.setMinimumSize(QSize(414, 0))
        self.textEdit.setMaximumSize(QSize(377, 16777215))

        self.verticalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_21 = QPushButton(self.frame_3)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(75, 75))
        self.pushButton_21.setMaximumSize(QSize(75, 75))
        icon = QIcon()
        icon.addFile(u"img/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon)
        self.pushButton_21.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.pushButton_21, 0, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.frame_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(75, 75))
        self.pushButton_19.setMaximumSize(QSize(75, 75))
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.pushButton_19, 0, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(75, 75))
        self.pushButton_3.setMaximumSize(QSize(75, 75))
        icon1 = QIcon()
        icon1.addFile(u"img/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(75, 75))
        self.pushButton_2.setMaximumSize(QSize(75, 75))
        self.pushButton_2.setLayoutDirection(Qt.RightToLeft)
        icon2 = QIcon()
        icon2.addFile(u"img/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(75, 75))
        self.pushButton_10.setMaximumSize(QSize(75, 75))
        icon3 = QIcon()
        icon3.addFile(u"img/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.pushButton_10, 1, 1, 1, 1)

        self.pushButton_20 = QPushButton(self.frame_3)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(75, 75))
        self.pushButton_20.setMaximumSize(QSize(75, 75))
        icon4 = QIcon()
        icon4.addFile(u"img/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_20.setIcon(icon4)
        self.pushButton_20.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.pushButton_20, 2, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(75, 75))
        self.pushButton_4.setMaximumSize(QSize(75, 75))
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.pushButton_4, 2, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_7.addWidget(self.frame_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(831, 721))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 701, 691))
        self.plotWidget = QGridLayout(self.layoutWidget)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotWidget.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(740, 10, 79, 691))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lcdNumber = QLCDNumber(self.widget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(75, 50))
        self.lcdNumber.setMaximumSize(QSize(75, 50))

        self.verticalLayout_5.addWidget(self.lcdNumber)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.lcdNumber_2 = QLCDNumber(self.widget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setMinimumSize(QSize(75, 50))
        self.lcdNumber_2.setMaximumSize(QSize(75, 50))

        self.verticalLayout_5.addWidget(self.lcdNumber_2)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.lcdNumber_3 = QLCDNumber(self.widget)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setMinimumSize(QSize(75, 50))
        self.lcdNumber_3.setMaximumSize(QSize(75, 50))

        self.verticalLayout_5.addWidget(self.lcdNumber_3)

        self.verticalSpacer_5 = QSpacerItem(20, 120, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.iso_button = QPushButton(self.widget)
        self.iso_button.setObjectName(u"iso_button")
        self.iso_button.setMinimumSize(QSize(75, 75))
        self.iso_button.setMaximumSize(QSize(75, 75))
        icon5 = QIcon()
        icon5.addFile(u"img/isometric.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iso_button.setIcon(icon5)
        self.iso_button.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.iso_button)

        self.side_button = QPushButton(self.widget)
        self.side_button.setObjectName(u"side_button")
        self.side_button.setMinimumSize(QSize(75, 75))
        self.side_button.setMaximumSize(QSize(75, 75))
        icon6 = QIcon()
        icon6.addFile(u"img/Lateral.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_button.setIcon(icon6)
        self.side_button.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.side_button)

        self.top_button = QPushButton(self.widget)
        self.top_button.setObjectName(u"top_button")
        self.top_button.setMinimumSize(QSize(75, 75))
        self.top_button.setMaximumSize(QSize(75, 75))
        icon7 = QIcon()
        icon7.addFile(u"img/top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.top_button.setIcon(icon7)
        self.top_button.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.top_button)

        self.front_button = QPushButton(self.widget)
        self.front_button.setObjectName(u"front_button")
        self.front_button.setMinimumSize(QSize(75, 75))
        self.front_button.setMaximumSize(QSize(75, 75))
        icon8 = QIcon()
        icon8.addFile(u"img/Front.png", QSize(), QIcon.Normal, QIcon.Off)
        self.front_button.setIcon(icon8)
        self.front_button.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.front_button)


        self.verticalLayout_6.addLayout(self.verticalLayout)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(831, 141))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.widget1 = QWidget(self.frame_4)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(590, 30, 191, 91))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.widget1)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_2.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.widget1)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_2.addWidget(self.pushButton_14)


        self.verticalLayout_8.addWidget(self.frame_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1293, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionSubir_GCODE)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSubir_GCODE.setText(QCoreApplication.translate("MainWindow", u"Subir GCODE", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"CONECTAR", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"DESCONECTAR", None))
        self.etiqueta_estado.setText(QCoreApplication.translate("MainWindow", u"ESTADO", None))
        self.pushButton_21.setText("")
        self.pushButton_19.setText("")
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton_10.setText("")
        self.pushButton_20.setText("")
        self.pushButton_4.setText("")
        self.iso_button.setText("")
        self.side_button.setText("")
        self.top_button.setText("")
        self.front_button.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"EMPEZAR", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"DETENER", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

