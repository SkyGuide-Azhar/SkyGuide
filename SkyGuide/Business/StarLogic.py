from SGDB_Interface import SGDB_Interface

from threading   import Thread
from static_vars import static_vars

from InternetConnection import NetCheck
from MountCommunication import MountCommunication

UserRA  = 0
UserDec = 90

#-------------------------------------------------------------------------- 

class StarLogic():

    def __init__(self):
        pass
 
    def GetByName(self, name):
        
        return SGDB_Interface().GetByName("stars", name)
        

#-------------------------------------------------------------------------- 
@static_vars(NewState = False)
def IsDBConnectionOn():

    if(NetCheck.IsInternetOn):   
        if(not IsDBConnectionOn.NewState):
            SGDB_Interface().SGDB_Connect()
            IsDBConnectionOn.NewState = True
    else:
        IsDBConnectionOn.NewState = False
    
    return IsDBConnectionOn.NewState

#-------------------------------------------------------------------------- 
def PrintByName(name):
    global UserRA, UserDec

    if(IsDBConnectionOn()):
        printStr, RA, DEC = StarLogic().GetByName(name)
        if(RA != None):
            UserRA  = RA
            UserDec = DEC
        print(printStr)
    else:
        print("Net is down")

#--------------------------------------------------------------------------     
if __name__ == "__main__":
    
    NetCheck = NetCheck()
    
    MountCommunication = MountCommunication()
    
    Thread(target = NetCheck.Check).start()
    Thread(target = MountCommunication.SendToMount).start()
    
    while(True):
        
        x = input("Enter the stars name: ")
        
        if(x == "d"):
            break
        elif(x == "send"):
            MountCommunication.RA  = UserRA
            MountCommunication.DEC = UserDec
        else:
            PrintByName(x)
    
    if(IsDBConnectionOn()):    
        SGDB_Interface().SGDB_Disconnect()
    
    NetCheck.ExitEvent.set()
    MountCommunication.ExitEvent.set()