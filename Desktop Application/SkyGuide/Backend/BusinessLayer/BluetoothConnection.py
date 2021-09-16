from serial import Serial
from time import sleep

class BluetoothConnection():
    def __init__(self, baudRate, comPort):
        self.__port = comPort
        self.__isBTConnected = False
        self.__BT = None
        self.__baudRate = baudRate

#------------------------------------------------------

    def ConnectBT(self):
        self.__BT = Serial(port=self.__port, baudrate=self.__baudRate, timeout=.1)
        self.__isBTConnected = True

# ------------------------------------------------------

    def Send(self, msg):
        if (self.__isBTConnected):
            self.__BT.write(bytes(msg, 'utf-8'))

# ------------------------------------------------------

    def Recieve(self):
        data = ""
        i = 0
        if (self.__isBTConnected):
            while ((not len(data)) and (i < 3)):
                data = self.__BT.readline()
                i += 1
                sleep(1)
        return data.decode('utf-8')

# ------------------------------------------------------

    def DisconnectBT(self):
        if(self.__isBTConnected):
            self.__BT.close()
