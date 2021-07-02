from SGDB_Interface import SGDB_Interface

from threading   import Event, Thread
from time        import sleep
from static_vars import static_vars

import requests


ExitEvent = Event()
IsInternetOn = False

#-------------------------------------------------------------------------- 

class StarLogic():

    def __init__(self):
        pass
 
    def GetByName(self, name):
        
        return SGDB_Interface().GetByName("stars", name)
        
#-------------------------------------------------------------------------- 
def NetCheck():
    global IsInternetOn, ExitEvent
    
    while(True):
        try:
           _ = requests.get("http://www.google.com", timeout = 2)
           IsInternetOn =  True
           
        except (requests.ConnectionError, requests.Timeout):
           IsInternetOn =  False  
           
        finally:
            sleep(0.1)
            if ExitEvent.is_set():
                break

#-------------------------------------------------------------------------- 
@static_vars(NewState = False)
def IsDBConnectionOn():
    global IsInternetOn
    
    if(IsInternetOn):   
        if(not IsDBConnectionOn.NewState):
            SGDB_Interface().SGDB_Connect()
            IsDBConnectionOn.NewState = True
    else:
        IsDBConnectionOn.NewState = False
    
    return IsDBConnectionOn.NewState

#-------------------------------------------------------------------------- 
def PrintByName(name):

    if(IsDBConnectionOn()):
        print(StarLogic().GetByName(name))
    else:
        print("Net is down")

#--------------------------------------------------------------------------     
if __name__ == "__main__":
    
    t1 = Thread(target = NetCheck)
    t1.start()
    
    while(True):
        x = input("Enter the stars name: ")
        if(x == "d"):
            break
        PrintByName(x)
    
    if(IsDBConnectionOn()):    
        SGDB_Interface().SGDB_Disconnect()
    
    ExitEvent.set()