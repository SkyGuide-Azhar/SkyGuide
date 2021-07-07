from Backend.BusinessLayer.SG_Utilities   import SG_Utilities
from Backend.DataAccessLayer.DB_Affiliate import DB_Affiliate

class SGDB_Interface(DB_Affiliate):
    
    def __init__(self):
        pass

#-----------------------------------------------------------------

    def GetByName(self, tableName, objName):
        DA_Obj = SG_Utilities().FindObj(tableName)
        RA = DEC = ""
        objFound = False

        if(DA_Obj.CheckName(objName)):
            table1_Obj, table2_Obj = DA_Obj.GetByName(objName)
            objFound = True
        
        if(not objFound and tableName == "constellations"):
            if(DA_Obj.CheckIAU(objName)):
                table1_Obj, table2_Obj = DA_Obj.GetByIAU(objName)
                objFound = True

        if(not objFound):
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
        utilitiesObj = SG_Utilities()
        ra  = tableObj.GetRATime().strip()
        dec = tableObj.GetDeclination().strip()
        
        correctInput, ra, dec = utilitiesObj.RA_DEC_Check(ra, dec)
        if(not correctInput):
            return "The entered right assension or declination was incorrect."
            
        if(tableName != "supernova_remnants"):
            isConExist, IAU = utilitiesObj.IAUCheck(tableObj.GetConstellation())
            if(isConExist):
                tableObj.SetConstellation(IAU)
            else:
                return "The Constellation doesn't exist."
        tableObj.SetRADeg(ra)
        
        return utilitiesObj.FindObj(tableName).AddNew(tableObj)
        
#__________________________________________________________________________________
    
    def SGDB_Connect(self):
        self.Connect()
        
#__________________________________________________________________________________

    def SGDB_Disconnect(self):
        self.Disconnect()









