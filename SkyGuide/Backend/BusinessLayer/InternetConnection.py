import requests

class InternetConnection():
    
    def __init__(self):
        self.IsInternetOn = False       
        
#-----------------------------------------

    def Check(self):
        try:
            _ = requests.get("http://www.google.com", timeout = 2)
            self.IsInternetOn =  True
               
        except (requests.ConnectionError, requests.Timeout):
            self.IsInternetOn =  False

                
#-----------------------------------------
