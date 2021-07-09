# This Python file uses the following encoding: utf-8
import sys
import os

from threading   import Thread

from Backend.ApplicationLayer.SkyGuideApp import SkyGuideApp

from PySide2.QtGui  import QGuiApplication
from PySide2.QtQml  import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal


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
        if(main.netConnection.IsInternetOn):
            main.SGDB_Interface.SGDB_Disconnect()
        main.ExitEvent.set()
        main.mountCommunication.ExitEvent.set()

    sys.exit(isAppExecEnded)
