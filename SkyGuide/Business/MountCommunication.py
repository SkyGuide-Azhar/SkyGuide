
import serial

from time import sleep
from datetime import datetime
from requests import get
from threading   import Event


class MountCommunication():
    
    def __init__(self):
        self.longitude = 0
        self.RA        = 0
        self.DEC       = 90
        self.LST       = 0
        self.ExitEvent = Event()
    
#-----------------------------------------

    def __getLongitude(self):        
        response  = get("https://ipinfo.io/")
        longitude = response.json()["loc"].split(",")[1]
       
        self.longitude = float(longitude)

#-----------------------------------------

    def __updateLST(self):
           
        todayDT = datetime.today()
        
        year  = todayDT.year
        month = todayDT.month
        day   = todayDT.day
        
        hours = todayDT.hour
        minutes = todayDT.minute
        
        if(not self.longitude):    
            self.__getLongitude()
        
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

    def SendToMount(self):
        while(True): 
            self.__updateLST()
            print(f"{self.RA},{self.DEC},{self.LST}")
            
            sleep(5)
            
            if self.ExitEvent.is_set():
                break
            
    
#-----------------------------------------