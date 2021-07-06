# This Python file uses the following encoding: utf-8
import sys
import os

from threading   import Thread, Event
from time        import sleep
from static_vars import static_vars

from Backend.ApplicationLayer.AddObject       import AddObject
from Backend.ApplicationLayer.SearchObject    import SearchObject
from Backend.BusinessLayer.InternetConnection import InternetConnection
from Backend.BusinessLayer.MountCommunication import MountCommunication
from Backend.BusinessLayer.SGDB_Interface     import SGDB_Interface

from PySide2.QtGui  import QGuiApplication
from PySide2.QtQml  import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal

class SkyGuideApp (QObject):

    def __init__(self):
        QObject.__init__(self)

        self.AddObject     = AddObject()
        self.SearchObject = SearchObject()
        self.SGDB_Interface = SGDB_Interface()
        self.ExitEvent = Event()
        self.netConnection = InternetConnection()
        self.mountCommunication = MountCommunication()
        self.NewConnectionState = False
        self.UserRA  = 0
        self.UserDEC = 90

    #_______________________ Net Connection ____________________________

    internetConnected = Signal(bool)
    def InternetCheck(self):
        while(True):
            self.netConnection.Check()

            if(self.netConnection.IsInternetOn):
                if(not self.NewConnectionState):
                    self.SGDB_Interface.SGDB_Connect()
                    self.NewConnectionState = True
            else:
                self.NewConnectionState = False

            self.internetConnected.emit(self.netConnection.IsInternetOn)
            sleep(0.1)

            if self.ExitEvent.is_set():
                break

    #__________________________ Add star _______________________________

    starAddResult = Signal(str)

    @Slot(str, str, str, str, str, str, str, str, str)
    def addUserStar(self, name, ra_time, dec_deg, dist, mag, spect, color_idx, bayer, con):
        outMsgStr = AddObject().AddUserStar(name, ra_time, dec_deg, dist, mag, spect, color_idx, bayer, con)
        self.starAddResult.emit(outMsgStr)

    #__________________________ Add nebula _______________________________

    nebulaAddResult = Signal(str)

    @Slot(str, str, str, str, str, str, str)
    def addUserNebula(self, name, ra_time, dec_deg, dist, dimensions, radius, con):
        outMsgStr = AddObject().AddUserNebula(name, ra_time, dec_deg, dist, dimensions, radius, con)
        self.nebulaAddResult.emit(outMsgStr)

    #__________________________ Add supernova_remnant _______________________________

    supernovaRemnantAddResult = Signal(str)

    @Slot(str, str, str, str, str, str)
    def addUserSupernovaRemnant(self, name, ra_time, dec_deg, dist, fvfe, remnant):
        outMsgStr = AddObject().AddUserSupernovaRemnant(name, ra_time, dec_deg, dist, fvfe, remnant)
        self.supernovaRemnantAddResult.emit(outMsgStr)

    #__________________________ Search for object _______________________________

    searchResult = Signal(str)
    searchStatus = Signal(bool)

    @Slot(str, str)
    def getSearchResult(self, objType, objName):
        searchResult, searchStatus, self.UserRA, self.UserDEC = self.SearchObject.GetSearchResult(objType, objName)
        self.searchStatus.emit(searchStatus)
        self.searchResult.emit(searchResult)


#----------------------------------- Main ----------------------
if __name__ == "__main__":

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.load(os.path.join(os.path.dirname(__file__), "Frontend\qml\main.qml"))

    main = SkyGuideApp()

    Thread(target = main.InternetCheck).start()
    Thread(target = main.mountCommunication.SendToMount).start()

    engine.rootContext().setContextProperty("backend", main)

    if not engine.rootObjects():
        sys.exit(-1)

    isAppExecEnded = app.exec_()

    if(not isAppExecEnded):

        # put any thing you want to do after the app is closed
        main.SGDB_Interface.SGDB_Disconnect()
        main.ExitEvent.set()
        main.mountCommunication.ExitEvent.set()

    sys.exit(isAppExecEnded)



























    """
            QObject.__init__(self)
            self.__SGDB_Interface = SkyGuideDB_Interface()
            self.__searchObj = SG_Search(self.__SGDB_Interface)
            self.__addObj = SG_Add(self.__SGDB_Interface)








"""
