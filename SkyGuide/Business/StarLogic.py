from SGDB_Interface import SGDB_Interface

from threading   import Thread
from static_vars import static_vars

from NetCheck import NetCheck
from MountCommunication import MountCommunication

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

    if(IsDBConnectionOn()):
        printStr, RA, DEC = StarLogic().GetByName(name)
        if(RA != None):
            MountCommunication.RA  = RA
            MountCommunication.DEC = DEC
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
        PrintByName(x)
    
    if(IsDBConnectionOn()):    
        SGDB_Interface().SGDB_Disconnect()
    
    NetCheck.ExitEvent.set()
    MountCommunication.ExitEvent.set()