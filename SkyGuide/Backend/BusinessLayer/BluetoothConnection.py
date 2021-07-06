from serial import Serial
import serial.tools.list_ports as PortsList
from time import sleep

class BluetoothConnection():
    def __init__(self, baudRate):
        self.__port = ""
        self.__isBTConnected = False
        self.__BT = None
        self.__baudRate = baudRate

#------------------------------------------------------

    def __checkForBluetooth(self):
        ports = list(PortsList.comports())
        for p in ports:
            if (not "Bluetooth" in p.description):
                ports.remove(p)
        if (len(ports)):
            if (len(ports) > 1):
                self.__port = ports[1].name
            else:
                self.__port = ports[0].name
        else:
            self.__isBTConnected = False

#------------------------------------------------------

    def ConnectBT(self):
        self.__checkForBluetooth()
        if(not self.__isBTConnected):
            self.__BT = Serial(port=self.__port, baudrate=self.__baudRate, timeout=.1)
            self.__isBTConnected = True

# ------------------------------------------------------

    def Send(self, msg):
        if (self.__isBTConnected):
            self.__BT.write(bytes(msg, 'utf-8'))

# ------------------------------------------------------

    def Recieve(self):
        data = ""
        if (self.__isBTConnected):
            while (not len(data)):
                data = self.__BT.readline()
        return data.decode('utf-8')

# ------------------------------------------------------

    def DisconnectBT(self):
        if(self.__isBTConnected):
            self.__BT.close()