import mysql.connector

class SkyGuideDBConnection:
    
    def __init__(self):
        pass
    

    def SGDB_Disconnect(self):
        self.cr.close()
        
        self.db.disconnect()
        
        
    def SGDB_Connect(self):
        self.db = mysql.connector.connect(host     = "blsprj9kvpcmrjmnpalh-mysql.services.clever-cloud.com",
                                          user     = "ujssc4bzehkf9pu8",
                                          passwd   = "o9hGS7tBabkfZlgruG6Q",
                                          database = "blsprj9kvpcmrjmnpalh")
        self.cr = self.db.cursor()
