# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label_for_graphic.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1202, 1000))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 440, 151, 25))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(640, 30, 381, 101))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.Widget = QtWidgets.QWidget(self.centralwidget)
        self.Widget.setGeometry(QtCore.QRect(540, 190, 571, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Widget.sizePolicy().hasHeightForWidth())
        self.Widget.setSizePolicy(sizePolicy)
        self.Widget.setObjectName("Widget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(540, 10, 571, 21))
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 10, 160, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.textEdit_11 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_11.setObjectName("textEdit_11")
        self.verticalLayout_5.addWidget(self.textEdit_11)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.textEdit_10 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_10.setAcceptDrops(False)
        self.textEdit_10.setWhatsThis("")
        self.textEdit_10.setObjectName("textEdit_10")
        self.verticalLayout_5.addWidget(self.textEdit_10)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.textEdit_8 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_8.setAcceptDrops(False)
        self.textEdit_8.setWhatsThis("")
        self.textEdit_8.setObjectName("textEdit_8")
        self.verticalLayout_4.addWidget(self.textEdit_8)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.textEdit_9 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_9.setAcceptDrops(False)
        self.textEdit_9.setWhatsThis("")
        self.textEdit_9.setObjectName("textEdit_9")
        self.verticalLayout_4.addWidget(self.textEdit_9)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.textEdit_6 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_6.setAcceptDrops(False)
        self.textEdit_6.setWhatsThis("")
        self.textEdit_6.setObjectName("textEdit_6")
        self.verticalLayout_4.addWidget(self.textEdit_6)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.textEdit_3 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_4.addWidget(self.textEdit_3)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.textEdit_5 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_5.setObjectName("textEdit_5")
        self.verticalLayout_4.addWidget(self.textEdit_5)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(350, 10, 160, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.textEdit_7 = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit_7.setAcceptDrops(False)
        self.textEdit_7.setWhatsThis("")
        self.textEdit_7.setObjectName("textEdit_7")
        self.verticalLayout_6.addWidget(self.textEdit_7)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.textEdit_4 = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_6.addWidget(self.textEdit_4)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(180, 220, 161, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox2.setGeometry(QtCore.QRect(180, 240, 161, 31))
        self.checkBox2.setObjectName("checkBox2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 470, 521, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Построить"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">L dI/dx + R*I = E</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; vertical-align:sub;\">0</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">*sin(</span><span style=\" font-family:\'arial,sans-serif\'; font-size:10pt; color:#545454; background-color:#ffffff;\">ω</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">x); I(x</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; vertical-align:sub;\">0</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">) = I</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; vertical-align:sub;\">0</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">E</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; vertical-align:sub;\">0</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">*sin(</span><span style=\" font-family:\'arial,sans-serif\'; font-size:10pt; color:#545454; background-color:#ffffff;\">ω</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">x) - ЭДС; R - сопротивление; x - время.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">L - коэффициент самоиндукции; I(x) - сила тока;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Постановка задачи</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Максимальное</p><p>число шагов <span style=\" font-size:12pt; font-weight:600;\">N</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">max</span></p></body></html>"))
        self.textEdit_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>Шаг <span style=\" font-size:12pt; font-weight:600;\">h</span></p></body></html>"))
        self.textEdit_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.01</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Коэффициент </p><p>самоиндукции <span style=\" font-size:12pt; font-weight:600;\">L</span></p></body></html>"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Сопротивление <span style=\" font-size:12pt; font-weight:600;\">R</span></p></body></html>"))
        self.textEdit_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Амплитутда <span style=\" font-size:12pt; font-weight:600;\">E</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>Частота <span style=\" font-family:\'arial,sans-serif\'; font-size:16px; font-weight:600; color:#222222; background-color:#ffffff;\">Ѡ</span>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>Контроль ЛП <span style=\" font-family:\'arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222; background-color:#ffffff;\">Ɛ</span><span style=\" font-size:12pt; font-weight:600;\""))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.0001</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>Начальное значение </p><p>времени <span style=\" font-size:12pt; font-weight:600;\">x</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0</span></p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Начальное значение </p><p>силы тока <span style=\" font-size:12pt; font-weight:600;\">I</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5</p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Контроль ЛП"))
        self.checkBox2.setText(_translate("MainWindow", "Очищать график"))

