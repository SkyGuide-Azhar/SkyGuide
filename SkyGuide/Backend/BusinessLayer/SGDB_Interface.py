import re

from Backend.BusinessLayer.SG_Utilities   import SG_Utilities
from Backend.DataAccessLayer.DB_Affiliate import DB_Affiliate

class SGDB_Interface(DB_Affiliate):
    
    def __init__(self):
        pass

#-----------------------------------------------------------------

    def GetByName(self, tableName, objName):
        DA_Obj = SG_Utilities().FindObj(tableName)
        RA = DEC = ""
        
        if(DA_Obj.CheckName(objName)):
            table1_Obj, table2_Obj = DA_Obj.GetByName(objName)
        
        elif(tableName == "constellations"):
            if(DA_Obj.CheckIAU(objName)):
                table1_Obj, table2_Obj = DA_Obj.GetByIAU(objName)
        
        else:
            return "\n\nThe provided object name is incorrect.", None, None
        
        if(tableName == "constellations"):
            RA  = table1_Obj.GetRAStartDeg()
            DEC = table1_Obj.GetDeclinationStart()
        else:
            RA  = table1_Obj.GetRADeg()
            DEC = table1_Obj.GetDeclination()
        
        returnStr = str(table1_Obj)
        
        if(table2_Obj != None):
            returnStr += str(table2_Obj)
        
        return returnStr, RA, DEC

#-----------------------------------------------------------------

    def AddNew(self, tableName, tableObj):
        ra  = tableObj.GetRATime().strip()
        dec = tableObj.GetDeclination().strip()
        
        raRegex  = "^((\d)|([0-1]\d)|([2][0-3]))(.\d+)?h\s+((\d)|([0-5]\d))(.\d+)?m\s+((\d)|([0-5]\d))(.\d+)?s$"
        decRegex = "^-?(([0-8]?\d)(.\d+)?)|(90)$"
        
        if(not (re.search(raRegex, ra) and re.search(decRegex, dec) )):
            return "The entered right assension or declination was incorrect."
            
        if(tableName != "supernova_remnants"):
            isConExist, IAU = SG_Utilities().IAUCheck(tableObj.GetConstellation())
            if(isConExist):
                tableObj.SetConstellation(IAU)
            else:
                return "The Constellation doesn't exist."
        tableObj.SetRADeg(SG_Utilities().RATimeToDeg(ra))
        
        return SG_Utilities().FindObj(tableName).AddNew(tableObj)
        
#__________________________________________________________________________________
    
    def SGDB_Connect(self):
        self.Connect()
        
#__________________________________________________________________________________

    def SGDB_Disconnect(self):
        self.Disconnect()









