from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPen, QColor
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QLineEdit
from PyQt5.QtCore import pyqtSignal, Qt, QPointF
import sys

class pictures(QWidget):
    clicked = pyqtSignal()

    def __init__(self, dosyaYolu, x, y, width, height, parent=None):
        super().__init__(parent)
        self.id = None
        self.resim = QPixmap(dosyaYolu).scaled(35, 35)

        self.etiket = QLabel(self)
        self.etiket.setPixmap(self.resim)
        self.etiket.setGeometry(x, y, width, height)

        self.idLabel = QLabel(self)
        self.idLabel.setGeometry(x, y + 70, width, 70)
        self.idLabel.setAlignment(Qt.AlignCenter)

        self.kapsamaAlan = QVBoxLayout(self)
        self.kapsamaAlan.addWidget(self.etiket)
        self.kapsamaAlan.addWidget(self.idLabel)
        
        self.setFixedSize(100, 100)
        self.sabitlikDurum = True

    def referans(self):
        return self

    def setID(self, id):
        self.id = id
        self.idLabel.setText(f"ID: {self.id}") 

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.sabitlikDurum:
            widget_pos = self.mapToParent(event.pos() - self.offset)
            self.move(widget_pos)
            
    def mouseDoubleClickEvent(self, event):
        if self.sabitlikDurum:
            self.sabitlikDurum=False
        else:
            self.sabitlikDurum=True


class notGate(pictures):
    def evaluate(self, inputs):
        return int(not inputs[0])

class buffer(pictures):
    def evaluate(self, inputs):
        return inputs[0]

class nandGate(pictures):
    def evaluate(self, inputs):

        if len(inputs)==inputs.count(True):
            return 0
        else:
            return 1

        

class nor(pictures):
    def evaluate(self, inputs):

        if 1  in inputs:
            return 0

        else:
            return 1

class andGate(pictures):
    def evaluate(self, inputs):

        if len(inputs)==inputs.count(True):
            return 1
        else:
            return 0

class xnor(pictures):
    def evaluate(self, inputs):
        if inputs.count(1)==1:
            return 0
        else:
            return 1

class xor(pictures):
    def evaluate(self, inputs):

        if inputs.count(1)==1:
            return 1
        else:
            return 0       

class orGate(pictures):
    def evaluate(self, inputs):

        if 1  in inputs:
            return 1

        else:
            return 0

        
class led(pictures):
    def evaluate(self, inputs):
        if inputs[0] == 0:
            self.etiket.setPixmap(QPixmap("resimler/pasifled.png").scaled(35, 35))
        else:
            self.etiket.setPixmap(QPixmap("resimler/aktifled.png").scaled(35, 35))

        return inputs[0]
    
class stop(pictures):
    def evaluate(self, inputs):
        if inputs[0] == 1:
            self.etiket.setPixmap(QPixmap("resimler/pasifled.png").scaled(35, 35))


class cikisKutu(pictures):
    def evaluate(self, inputs):
        return inputs[0]

class girisKutu(pictures):
    def __init__(self, dosyaYolu, x, y, width, height, parent=None):
        super().__init__(dosyaYolu, x, y, width, height, parent)
        self.inputDeger = QLineEdit(self)
        self.inputDeger.setGeometry(0, 90, 55, 20)
        self.kapsamaAlan.addWidget(self.inputDeger)

    def get_value(self):
        try:
            return int(self.inputDeger.text())
        except ValueError:
            return 0
        
class dugum(pictures):
    def __init__(self, dosyaYolu, x, y, width, height, parent=None):
        super().__init__(dosyaYolu, x, y, width, height, parent)
        self.inputs = []

    def add_input(self, kapi):
        self.inputs.append(kapi)

    def evaluate(self, inputs):
        if inputs:
            return inputs[0]  
        return 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 843)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.notkapiRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.notkapiRadio.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.notkapiRadio.setObjectName("notkapiRadio")

        self.bufferRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.bufferRadio.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.bufferRadio.setObjectName("bufferRadio")

        self.andkapiRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.andkapiRadio.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.andkapiRadio.setObjectName("andkapiRadio")

        self.orkapiRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.orkapiRadio.setGeometry(QtCore.QRect(10, 100, 82, 17))
        self.orkapiRadio.setObjectName("orkapiRadio")

        self.nandkapiRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.nandkapiRadio.setGeometry(QtCore.QRect(10, 130, 82, 17))
        self.nandkapiRadio.setObjectName("nandkapiRadio")

        self.norRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.norRadio.setGeometry(QtCore.QRect(10, 160, 82, 17))
        self.norRadio.setObjectName("norRadio")

        self.xorRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.xorRadio.setGeometry(QtCore.QRect(10, 190, 82, 17))
        self.xorRadio.setObjectName("xorRadio")

        self.xnorRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.xnorRadio.setGeometry(QtCore.QRect(10, 220, 82, 17))
        self.xnorRadio.setObjectName("xnorRadio")

        self.girisKutusuRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.girisKutusuRadio.setGeometry(QtCore.QRect(10, 250, 82, 17))
        self.girisKutusuRadio.setObjectName("girisKutusuRadio")

        self.cikisKapisiRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.cikisKapisiRadio.setGeometry(QtCore.QRect(10, 280, 82, 17))
        self.cikisKapisiRadio.setObjectName("cikisKapisiRadio")

        self.ledRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.ledRadio.setGeometry(QtCore.QRect(10, 310, 82, 17))
        self.ledRadio.setObjectName("ledRadio")

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(440, 770, 75, 23))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.start_simulation)

        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(630, 770, 75, 23))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.clicked.connect(self.stopButonu)

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(820, 770, 75, 23))
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.reset_simulation)

        self.ekleButton = QtWidgets.QPushButton(self.centralwidget)
        self.ekleButton.setGeometry(QtCore.QRect(110, 160, 75, 23))
        self.ekleButton.setObjectName("ekleButton")
        self.ekleButton.clicked.connect(self.nesneButton)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(190, 0, 20, 831))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(200, 740, 991, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 340, 201, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 0, 991, 751))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.graphicsView = QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 991, 751))
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)

        self.kapiIsmi = QtWidgets.QLineEdit(self.centralwidget)
        self.kapiIsmi.setGeometry(QtCore.QRect(10, 430, 113, 20))
        self.kapiIsmi.setObjectName("kapiIsmi")

        self.baglanacakKapiIsmi = QtWidgets.QLineEdit(self.centralwidget)
        self.baglanacakKapiIsmi.setGeometry(QtCore.QRect(10, 490, 113, 20))
        self.baglanacakKapiIsmi.setObjectName("baglanacakKapiIsmi")

        self.baglaButton = QtWidgets.QPushButton(self.centralwidget)
        self.baglaButton.setGeometry(QtCore.QRect(10, 530, 75, 23))
        self.baglaButton.setObjectName("baglaButton")
        self.baglaButton.clicked.connect(self.cizgiCiz)

        self.baglantilar1 = QtWidgets.QLabel(self.centralwidget)
        self.baglantilar1.setGeometry(QtCore.QRect(10,600,300,35))
        self.baglantilar1.setObjectName("baglanti1")

        self.baglantilar = QtWidgets.QLabel(self.centralwidget)
        self.baglantilar.setGeometry(QtCore.QRect(10,650,300,35))
        self.baglantilar.setObjectName("baglanti")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 400, 111, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 460, 111, 20))
        self.label_2.setObjectName("label_2")

        self.dugumRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.dugumRadio.setGeometry(QtCore.QRect(100, 10, 82, 17))
        self.dugumRadio.setObjectName("radioButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.allItems = []
        self.baglantilarr = {}
        self.objectID = 1
        self.cikisLabels = []

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LAB-2 PROJE-3"))
        self.notkapiRadio.setText(_translate("MainWindow", "NOT kapi"))
        self.bufferRadio.setText(_translate("MainWindow", "BUFFER kapi"))
        self.andkapiRadio.setText(_translate("MainWindow", "AND kapi"))
        self.orkapiRadio.setText(_translate("MainWindow", "OR kapi"))
        self.nandkapiRadio.setText(_translate("MainWindow", "NAND kapi"))
        self.norRadio.setText(_translate("MainWindow", "NOR kapi"))
        self.xorRadio.setText(_translate("MainWindow", "XOR kapi"))
        self.xnorRadio.setText(_translate("MainWindow", "XNOR kapi"))
        self.girisKutusuRadio.setText(_translate("MainWindow", "Giris Kutusu"))
        self.cikisKapisiRadio.setText(_translate("MainWindow", "Cikis Kapisi"))
        self.ledRadio.setText(_translate("MainWindow", "LED"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.ekleButton.setText(_translate("MainWindow", "Ekle"))
        self.baglaButton.setText(_translate("MainWindow", "Bağla"))
        self.label.setText(_translate("MainWindow", "Kapı ID"))
        self.label_2.setText(_translate("MainWindow", "Bağlanacak Kapı ID"))
        self.dugumRadio.setText(_translate("MainWindow", "Dugum"))
        self.baglantilar.setText(_translate("MainWindow","BAGLANTI YOK"))
        self.baglantilar1.setText(_translate("MainWindow","BAGLANTILAR"))

    def nesneButton(self):
        if self.notkapiRadio.isChecked():
            item = notGate('resimler/notGate.png', 0, 0, 55, 55)
        elif self.bufferRadio.isChecked():
            item = buffer('resimler/buffer.png', 0, 0, 55, 55)
        elif self.andkapiRadio.isChecked():
            item = andGate('resimler/andGate.png', 0, 0, 55, 55)
        elif self.orkapiRadio.isChecked():
            item = orGate('resimler/orGate.png', 0, 0, 55, 55)
        elif self.nandkapiRadio.isChecked():
            item = nandGate('resimler/nandGate.png', 0, 0, 55, 55)
        elif self.norRadio.isChecked():
            item = nor('resimler/nor.png', 0, 0, 55, 55)
        elif self.xorRadio.isChecked():
            item = xor('resimler/xor.png', 0, 0, 55, 55)
        elif self.xnorRadio.isChecked():
            item = xnor('resimler/xnor.png', 0, 0, 55, 55)
        elif self.girisKutusuRadio.isChecked():
            item = girisKutu('resimler/girisKutu.png', 0, 0, 55, 55)
        elif self.cikisKapisiRadio.isChecked():
            item = cikisKutu('resimler/cikisKutu.png', 0, 0, 55, 55)
            cikisLabel = QLabel(item)
            cikisLabel.setGeometry(0, 110, 55, 20)
            item.kapsamaAlan.addWidget(cikisLabel)
            self.cikisLabels.append(cikisLabel)
        elif self.ledRadio.isChecked():
            item = led('resimler/pasifled.png', 0, 0, 55, 55)

        elif self.dugumRadio.isChecked():
            item = dugum("resimler/dugum.png",0,0,55,55)

        
        item.setID(self.objectID)
        self.objectID += 1
        self.allItems.append(item)
        self.graphicsView.scene().addWidget(item)

    def cizgiCiz(self):
        kapiID = int(self.kapiIsmi.text())
        baglanacakKapıID = int(self.baglanacakKapiIsmi.text())

        kapi = next((item for item in self.allItems if item.id == kapiID), None)
        baglanacak_kapi = next((item for item in self.allItems if item.id == baglanacakKapıID), None)

        if kapi and baglanacak_kapi:
            if baglanacakKapıID not in self.baglantilarr:
                self.baglantilarr[baglanacakKapıID] = []
            self.baglantilarr[baglanacakKapıID].append(kapiID)

            line = QGraphicsLineItem()
            line.setPen(QPen(QColor("black"), 1))
            self.scene.addItem(line)
            line.setLine(kapi.x() + 25, kapi.y() + 25, baglanacak_kapi.x() + 25, baglanacak_kapi.y() + 25)

        self.baglantilar.setText("{}".format(self.baglantilarr))

    def start_simulation(self):
        def evaluate_kapi(kapi):
            inputs = []
            if kapi.id in self.baglantilarr:
                for input_id in self.baglantilarr[kapi.id]:
                    inputKapi = next((item for item in self.allItems if item.id == input_id), None)
                    if inputKapi:
                        inputs.append(evaluate_kapi(inputKapi))
            if isinstance(kapi, girisKutu):
                return kapi.get_value()
            return kapi.evaluate(inputs)
        
        for item in self.allItems:
            if isinstance(item, cikisKutu):
                result = evaluate_kapi(item)
                cikisLabel = next((label for label in self.cikisLabels if label.parent() == item), None)
                if cikisLabel:
                    cikisLabel.setText(f"Output: {result}")
        
        for item in self.allItems:
            if isinstance(item, led):
                result = evaluate_kapi(item)
                cikisLabel = next((label for label in self.cikisLabels if label.parent() == item), None)
                if cikisLabel:
                    cikisLabel.setText(f"Output: {result}")

        self.baglantilar.setText("{}".format(self.baglantilarr))


    def stopButonu(self):
        def evaluate_kapi(kapi):
            inputs = []
            if kapi.id in self.baglantilarr:
                for input_id in self.baglantilarr[kapi.id]:
                    inputKapi = next((item for item in self.allItems if item.id == input_id), None)
                    if inputKapi:
                        inputs.append(evaluate_kapi(inputKapi))

            if isinstance(kapi, girisKutu):
                return kapi.get_value()
            return kapi.evaluate(inputs)

        for item in self.allItems:
            if isinstance(item,led):
                item.evaluate([0])
                    
            elif isinstance(item, cikisKutu):
                cikisLabel = next((label for label in self.cikisLabels if label.parent() == item), None)
                if cikisLabel:
                    cikisLabel.setText(f"Output: {0}")

        

    def reset_simulation(self):
        self.graphicsView.scene().clear()
        self.allItems = []
        self.baglantilarr = {}
        self.objectID = 1
        self.cikisLabels = []
        self.baglantilar.setText("BAGLANTI YOK")

        


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
