# -*- coding: utf-8 -*-
import math
import pylab
from matplotlib import mlab
from matplotlib.figure import Figure
from label_for_graphic import Ui_MainWindow
from tab_widg import Ui_MainWindow_tab
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from main import MyWin
from main import second_window
#######################################
class Math_Part(Ui_MainWindow):
    def bilding(self, eps, n, L, I, h, x, R, w, E, secwin):
        print(L, R, I, h, x, n, E, w)
        self.progressBar.setMinimum(0)
    
        self.progressBar.setMaximum(n)
        secwin.tableWidget.setRowCount(n+1)
        secwin.label.setText("Начальное х0 = " + str(x))
        secwin.label_2.setText("Начальное I0 = " + str(I))
        secwin.label_3.setText("Коэф. самоинд. L = " + str(L))
        secwin.label_4.setText("Сопротивление R = " + str(R))
        secwin.label_5.setText("Амплитуда E0 = " + str(E))
        secwin.label_6.setText("Макс. число шагов N = " + str(n))
        secwin.label_7.setText("Шаг h = " + str(h))
        secwin.label_8.setText("Контроль ЛП = " + str(eps))
        secwin.label_9.setText("Частота w = " + str(w))
        xlist = []
        Ilist = []
        L_Elist = []
        Mark_list = []
        hlist = []
        for i in range(n+1):
            secwin.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))
        def abs_solution(x, const):
            return (((E * R * math.sin(w * x))/((L**2)*(w**2) + (R**2))) - ((E * L * w * math.cos(w * x))/((L**2)*(w**2) + (R**2))) + (const * math.exp((-(R * x)) / L)))
        def sol_const(x, I):
            return (I + (E * L * w * math.cos(w * x)/ ((L**2)*(w**2) + (R**2))) - (E * L * w * math.sin(w * x)/ ((L**2)*(w**2) + (R**2))))/ math.exp((-(R * x)) / L)
        def f(x, I):
            return (E * (math.sin(w * x)) - R * I) / L

        def loc_err(step_I, two_step_I):
            return ((two_step_I - step_I) * ((8.0) / 7.0))

        def step_func1(step, x, I):
            return step * f(x, I)

        def step_func2(step, x, I):
            return step * f(x + step / 2, I + step_func1(step, x, I) / 2)

        def step_func3(step, x, I):
            return step * f(x + step, I + 2 * step_func2(step, x, I) - step_func1(step, x, I))

        def next_point_x(step, x):
            return x + step

        def next_point_I(I, x, step):
            return I + (step_func1(step, x, I) + 4 * step_func2(step, x, I) + step_func3(step, x, I)) / 6

        ##################################################
        def new_point(step, x, I, number_r):
            nonlocal h
            new_I = next_point_I(I, x, step)
            new_x = next_point_x(step, x)

            add_I = next_point_I(I, x, step / 2)
            add_x = next_point_x(step / 2, x)

            add_I = next_point_I(add_I, add_x, step / 2)
            add_x = next_point_x(step / 2, add_x)
            S = loc_err(new_I, add_I)

            secwin.tableWidget.setItem(number_r, 3, QtWidgets.QTableWidgetItem(str(add_I)))
            secwin.tableWidget.setItem(number_r, 4, QtWidgets.QTableWidgetItem(str(abs_x)))
            secwin.tableWidget.setItem(number_r, 5, QtWidgets.QTableWidgetItem(str(h)))
            secwin.tableWidget.setItem(number_r, 6, QtWidgets.QTableWidgetItem(str(S)))

            print("S####: ", S)
            print("exp###: ", eps / 16, eps)
            print("####", h)
            if self.checkBox.isChecked():
                if abs(S) >= eps / 16 and abs(S) <= eps:
                    print("save point")
                    hlist.append(h)
                    Mark_list.append(S)
                    return new_x, new_I
                if abs(S) < eps / 16:
                    print("save point, but change step")
                    h *= 2
                    hlist.append(h)
                    Mark_list.append(S)
                    return new_x, new_I
                if abs(S) > eps:
                    print("Fail")
                    h /= 2
                    return new_point(h, x, I, number_r)
            else:
                hlist.append(h)
                Mark_list.append(S)
                return new_x, new_I

        ax = self.figure.add_subplot(111)
        if self.checkBox2.isChecked():
            ax.clear()
            ax = self.figure.add_subplot(111)
        ax.axis([-5, 5, -5, 5])
        color = '-b' if self.checkBox.isChecked() else '-g'
        const = sol_const(x, I)
        abs_x, abs_I = x, abs_solution(x, const)
        for i in range(n):
            old_abs_x, old_abs_I = abs_x, abs_I
            secwin.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(old_abs_I)))
            secwin.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(old_abs_x)))
            L_Elist.append(abs(abs_I - I))
            secwin.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(abs(abs_I - I))))
            old_x, old_I = x, I
            xlist.append(x)
            Ilist.append(I)
            secwin.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(old_I)))
            secwin.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(old_x)))
            x, I = new_point(h, old_x, old_I, i + 1)
            ax.plot([old_x, x], [old_I, I], color)
            self.progressBar.setValue(i + 1)
            abs_x = x
            abs_I = abs_solution(abs_x, const)
            ax.plot([old_abs_x, abs_x], [old_abs_I, abs_I], '-r')
        secwin.tableWidget.setItem(n, 7, QtWidgets.QTableWidgetItem(str(abs_I)))
        secwin.tableWidget.setItem(n, 8, QtWidgets.QTableWidgetItem(str(abs_x)))
        secwin.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(I)))
        secwin.tableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem(str(x)))
        secwin.tableWidget.setItem(n, 9, QtWidgets.QTableWidgetItem(str(abs(abs_I - I))))

        secwin.label_10.setText("Max I = " + str(max(Ilist)))
        secwin.label_11.setText("Max x = " + str(max(xlist)))
        secwin.label_12.setText("Max h = " + str(max(hlist)))
        secwin.label_13.setText("Max глобальная погрешность = " + str(round(max(L_Elist), 5)))
        secwin.label_14.setText("Max ОЛП = " + str(round(max(Mark_list), 5)))
        ax.grid(True)
        self.canvas.draw()
        #координата х численного решения с некоторого шага отличается от координаты х
        #точного решения из - за пересчеста чтоки с учетом ЛП, т.е. в некоторый момент
        #в ЧР ЛП в некоторый момент > чем указанная окрустность => происходит пересчет
        #с корректировкой шага, но т.к. 1 в очереди считается коорд. х ТР то она ост.
        #с со значением шага полученным на пред. итерации => коорд. х ТР и ЧР отличны
        #поэтому целесообразно использовать в качестве коорд. х ТР - коорд. х ЧР)))))