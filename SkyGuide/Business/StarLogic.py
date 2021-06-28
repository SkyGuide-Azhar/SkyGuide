from DataAccess.StarsDA import StarsDA

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
        star, con = StarsDA().getByName(name)
        returnStr = "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n-------------------------------------".format(star.GetName(),
                         star.GetRATime(),
                         star.GetRADeg(),
                         star.GetDeclination(),
                         star.GetDistance(),
                         star.GetMagnitude(),
                         star.GetSpectrum(),
                         star.GetColorIdx(),
                         star.GetBayerName(),
                         star.GetConstellation())

        returnStr += "\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}\n///////////////END-STAR//////////////////////////////////".format(con.GetName(),
                          con.GetIAU(),
                          con.GetRAStartTime(),
                          con.GetRAStartDeg(),
                          con.GetRAEndTime(),
                          con.GetRAEndDeg(),
                          con.GetDeclinationStart(),
                          con.GetDeclinationEnd(),
                          con.GetGenitive(),
                          con.GetMeaning(),
                          con.GetBrightestStar())
        
        return returnStr
        
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
            StarsDA().SGDB_Connect()
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
        StarsDA().SGDB_Disconnect()
    
    ExitEvent.set()