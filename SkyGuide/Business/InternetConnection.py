import requests

from time import sleep
from threading   import Event



class InternetConnection():
    
    def __init__(self):
        self.ExitEvent = Event()
        self.IsInternetOn = False       
        
#-----------------------------------------

    def Check(self):
        while(True):
            try:
               _ = requests.get("http://www.google.com", timeout = 2)
               self.IsInternetOn =  True
               
            except (requests.ConnectionError, requests.Timeout):
               self.IsInternetOn =  False  
               
            finally:
                sleep(0.1)
                if self.ExitEvent.is_set():
                    break
                
#-----------------------------------------