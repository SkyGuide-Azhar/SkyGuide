from time import sleep
from datetime import datetime
from requests import get
from threading   import Event

from Backend.BusinessLayer.BluetoothConnection import BluetoothConnection


class MountCommunication():
    
    def __init__(self):
        self.longitude = 0#31.470
        self.latitude  = 0#30.03
        self.LST       = 0
        self.RA        = 0
        self.updatedRA = 0
        self.DEC       = 90
        self.ExitEvent = Event()
        
        self.BTConnection = BluetoothConnection(baudRate = 9600, comPort = "COM3")
    
#-----------------------------------------

    def __getLocation(self):
        response  = get("https://ipinfo.io/", timeout=1)
        longitude = response.json()["loc"].split(",")[1]
        latitude  = response.json()["loc"].split(",")[0]
       
        self.longitude = float(longitude)
        self.latitude  = float(latitude)

#-----------------------------------------

    def __updateLST(self):
           
        todayDT = datetime.today()
        
        year  = todayDT.year
        month = todayDT.month
        day   = todayDT.day
        
        hours = todayDT.hour
        minutes = todayDT.minute
        
        if(not self.longitude):    
            self.__getLocation()
        
        #------------------ Calculations ---------------------
        
        ut = (hours + minutes/60)/24
        
        day += ut
        
        A = int(year/100)
        B = 2 - A + int(A/4)
        
        JD = int(365.25*(year+4716)) + int(30.6001*(month+1)) + day + B - 1524.5
        
        #calculate the Greenwhich mean sidereal time:
        GMST = (18.697374558 + 24.06570982441908*(JD - 2451545))%24
        
        #Convert to the local sidereal time by adding the longitude (in hours) from the GMST.
        #(Hours = Degrees/15, Degrees = Hours*15)
        longitude = self.longitude / 15      #Convert longitude to hours
        
        LST = GMST + longitude - 2   #Fraction LST. If negative we want to add 24...
        
        if LST < 0:
            LST = LST +24
            
        self.LST = float(format(LST*15,".3f"))

    #-----------------------------------------

    def __updateRA(self):

        self.__updateLST()
        if(self.latitude > 0):
            if (self.LST>180):
                self.updatedRA = self.RA + (360.0 - self.LST)
            else:
                self.updatedRA = self.RA - self.LST
        else:
            if (self.LST>180):
                self.updatedRA = self.RA - (360 - self.LST)
            else:
                self.updatedRA = self.RA + self.LST

    #-----------------------------------------

    def SendToMount(self):
        while(True):
            try:
                if self.ExitEvent.is_set():
                    break

                self.__updateRA()
                self.BTConnection.ConnectBT()

                strRA , strDEC = format(self.updatedRA,".3f"), format(self.DEC,".3f")
                self.BTConnection.Send( f"{strRA},{strDEC}" )
                print( f"{strRA},{strDEC}" )
                if(len(self.BTConnection.Recieve())):
                    self.BTConnection.DisconnectBT()
                sleep(3)

            except:
                self.BTConnection.DisconnectBT()
                sleep(5)

        self.BTConnection.DisconnectBT()
    
#-----------------------------------------
