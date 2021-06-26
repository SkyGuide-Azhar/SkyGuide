from DataAccess.DB_Connection import SkyGuideDBConnection

class SkyGuideDBAffiliate:

    _connection = SkyGuideDBConnection()

    def __init__(self):
          pass


    def SGDB_Disconnect(self):
        self._connection.SGDB_Disconnect()
       
    
    def SGDB_Connect(self):
        self._connection.SGDB_Connect()