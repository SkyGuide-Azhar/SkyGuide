from Backend.DataAccessLayer.DB_Connection import DB_Connection

class DB_Affiliate:

    _connection = DB_Connection()

    def __init__(self):
          pass


    def Disconnect(self):
        self._connection.SGDB_Disconnect()
       
    
    def Connect(self):
        self._connection.SGDB_Connect()
