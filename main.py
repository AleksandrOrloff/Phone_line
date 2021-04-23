import serial
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        port='/dev/ttyACM1'
        self.dev = serial.Serial(
                 # Здесь указывается устройство, с которым будет производится работа
                 # /dev/ttyUSBx - для Linux
                 # /dev/tty.SLAB_USBtoUART - для MacOS
                 port, 
                 # Скорость передачи
                 baudrate=9600,
                 # Использование бита четности
                 parity=serial.PARITY_NONE,
                 # Длина стоп-бита
                 stopbits=serial.STOPBITS_ONE,
                 # Длина пакета
                 bytesize=serial.EIGHTBITS,
                 # Максимальное время ожидания устройства
                 timeout=3.0
        )
        if (self.dev.isOpen()):
            print ("RNG: Re-open serial port %s" % port)
            self.dev.close()
            self.dev.open()
        else:
            print ("RNG: Open serial port %s" % port)
            self.dev.open()
        self._State_options = (0, 1, )
        self._Band_options = (0, 1, 2, )
        self._Attenuation_options = (0, 1, 2, 3, 4, 5, 6, 7, 8, )
        self.buttonGroup.buttonClicked[int].connect(
        	lambda i: self.set_State(self._State_options[i+1]))
        self.comboBox.currentIndexChanged.connect(
        	lambda i: self.set_Band(self._Band_options[i]))
        self.comboBox_2.currentIndexChanged.connect(
        	lambda i: self.set_Attenuation(self._Attenuation_options[i]))


    def set_State(self, state):
        cmd = "0%x".encode() % state
        self.dev.write(cmd)
        print(cmd)

    def set_Band(self, band):
        cmd = "2%x".encode() % band
        self.dev.write(cmd)
        print(cmd)

    def set_Attenuation(self, attenuation):
        cmd = "1%x".encode() % attenuation
        self.dev.write(cmd)
        print(cmd)

    def closeEvent(self, e):
        self.dev.write("0%x".encode() % 0)
        self.dev.write("2%x".encode() % 0)
        self.dev.write("1%x".encode() % 0)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
