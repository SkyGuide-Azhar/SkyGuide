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
from Backend.BusinessLayer.SG_Utilities       import SG_Utilities

from PySide2.QtGui  import QGuiApplication
from PySide2.QtQml  import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal

class SkyGuideApp (QObject):

    def __init__(self):
        QObject.__init__(self)

        self.AddObject     = AddObject()
        self.SearchObject  = SearchObject()
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
            sleep(0.5)

            if self.ExitEvent.is_set():
                break

    #__________________________ Add star _______________________________

    starAddResult = Signal(str)

    @Slot(str, str, str, str, str, str, str, str, str)
    def addUserStar(self, name, ra_time, dec_deg, dist, mag, spect, color_idx, bayer, con):
        outMsgStr = "Your internet connection is down!"
        if(self.netConnection.IsInternetOn):
            outMsgStr = AddObject().AddUserStar(name, ra_time, dec_deg, dist, mag, spect, color_idx, bayer, con)
        self.starAddResult.emit(outMsgStr)

    #__________________________ Add nebula _______________________________

    nebulaAddResult = Signal(str)

    @Slot(str, str, str, str, str, str, str)
    def addUserNebula(self, name, ra_time, dec_deg, dist, dimensions, radius, con):
        outMsgStr = "Your internet connection is down!"
        if(self.netConnection.IsInternetOn):
            outMsgStr = AddObject().AddUserNebula(name, ra_time, dec_deg, dist, dimensions, radius, con)
        self.nebulaAddResult.emit(outMsgStr)

    #__________________________ Add supernova_remnant _______________________________

    supernovaRemnantAddResult = Signal(str)

    @Slot(str, str, str, str, str, str)
    def addUserSupernovaRemnant(self, name, ra_time, dec_deg, dist, fvfe, remnant):
        outMsgStr = "Your internet connection is down!"
        if(self.netConnection.IsInternetOn):
            outMsgStr = AddObject().AddUserSupernovaRemnant(name, ra_time, dec_deg, dist, fvfe, remnant)
        self.supernovaRemnantAddResult.emit(outMsgStr)

    #__________________________ Search for object _______________________________

    searchResult = Signal(str)
    searchStatus = Signal(bool)

    @Slot(str, str)
    def getSearchResult(self, objType, objName):
        searchResult, searchStatus, self.UserRA, self.UserDEC = "Net is down", False, self.UserRA, self.UserDEC

        if(self.netConnection.IsInternetOn):
            searchResult, searchStatus, RA, DEC = self.SearchObject.GetSearchResult(objType, objName)
            if(RA != None):
                self.UserRA  = RA
                self.UserDEC = DEC

        self.searchStatus.emit(searchStatus)
        self.searchResult.emit(searchResult)

    #__________________________ SendToMount for searchpage _________________________

    @Slot()
    def sendToMount_Search(self):
        self.mountCommunication.RA  = self.UserRA
        self.mountCommunication.DEC = self.UserDEC

    #__________________________ Explore object _______________________________

    expolreResult = Signal(str)

    @Slot(str, str)
    def expolreObject(self, RA, DEC):

        checkResult, RA, DEC = SG_Utilities().RA_DEC_Check(RA, DEC)

        if(checkResult):
            returnStr = "The inputs are sent to mount"
            self.mountCommunication.RA  = RA
            self.mountCommunication.DEC = DEC
        else:
            returnStr = "The provided inputs are incorrect.\n\n Kindly check them and try again."

        self.expolreResult.emit(returnStr)


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
        if(main.netConnection.IsInternetOn):
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
