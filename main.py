# -*- coding: utf-8 -*-
import sys
import math
# Импортируем наш интерфейс из файла
from label_for_graphic import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from MyMplCanc import MtMplCanv
import Math_Part
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets, QtGui, QtCore
from MyMplCanc import MtMplCanv
from matplotlib.figure import Figure
from tab_widg import *
class MyWin(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.sec_win = None
        self.figure = Figure()

        # добавление шаблона размещения на виджет
        self.companovka_for_mpl = QtWidgets.QVBoxLayout(self.Widget)
        # получение объекта класса холста с нашим рисунком

        self.canvas = MtMplCanv(self.figure)
        # Размещение экземпляра класса холста в шаблоне размещения
        self.companovka_for_mpl.addWidget(self.canvas)
        # получение объекта класса панели управления холста
        self.toolbar = NavigationToolbar(self.canvas, self)
        # Размещение экземпляра класса панели управления в шаблоне размещения
        self.companovka_for_mpl.addWidget(self.toolbar)
        # Здесь прописываем событие нажатия на кнопку
        self.pushButton.clicked.connect(self.MyFunction)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def MyFunction(self):
        L = float(self.textEdit_8.toPlainText())
        R = float(self.textEdit_9.toPlainText())
        I0 = float(self.textEdit_4.toPlainText())
        h = float(self.textEdit_10.toPlainText())
        x0 = float(self.textEdit_7.toPlainText())
        n = int(self.textEdit_11.toPlainText())
        E = float(self.textEdit_6.toPlainText())
        w = float(self.textEdit_3.toPlainText())
        eps = float(self.textEdit_5.toPlainText())
        self.sec_win = second_window(self)
        Math_Part.Math_Part.bilding(self, eps, n, L, I0, h, x0, R, w, E, self.sec_win)
        self.sec_win.show()

class second_window(QMainWindow, Ui_MainWindow_tab):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
