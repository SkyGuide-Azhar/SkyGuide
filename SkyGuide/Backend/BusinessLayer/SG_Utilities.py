from Backend.DataAccessLayer.StarsDA             import StarsDA
from Backend.DataAccessLayer.SolarSysDA          import SolarSysDA
from Backend.DataAccessLayer.NebulasDA           import NebulasDA
from Backend.DataAccessLayer.SupernovaRemnantsDA import SupernovaRemnantsDA
from Backend.DataAccessLayer.ConstellationsDA    import ConstellationsDA

from Backend.Entities.Constellation         import Constellation
from Backend.Entities.Star                  import Star
from Backend.Entities.Nebula                import Nebula
from Backend.Entities.SolarSysObj           import SolarSysObj
from Backend.Entities.SupernovaRemnant      import SupernovaRemnant

class SG_Utilities():
    
    def __init__(self):
        pass
    
#-----------------------------------------------------------------
    
    def FindObj(self, tableName):
        returnObj = None
        
        if(tableName == "stars"):
            returnObj = StarsDA()
        
        elif(tableName == "constellations"):
            returnObj = ConstellationsDA()
        
        elif(tableName == "nebulas"):
            returnObj = NebulasDA()
        
        elif(tableName == "solar_sys"):
            returnObj = SolarSysDA()
        
        elif(tableName == "supernova_remnants"):
            returnObj = SupernovaRemnantsDA()
            
        else:
            raise Exception("SkyGuideDB_Interface, the passed table name is incorrect!")
        
        return returnObj

#-----------------------------------------------------------------
       
    def IAUCheck(self, con):
        constellation = ConstellationsDA()
        returnStr        = "The Constellation doesn't exist." 
        returnBool       = False
        
        if(constellation.CheckName(con)):
            returnStr = constellation.GetByName(con)[0].GetIAU()
            returnBool = True
        elif(constellation.CheckIAU(con)):
            returnStr = con
            returnBool = True
        
        return (returnBool, returnStr)       
    
#__________________________________________________________________________________
    
    
    def RATimeToDeg(self, raTime):
        hours = float(raTime[:raTime.index("h")])
        mins  = float(raTime[raTime.index("h")+1:raTime.index("m")].strip())
        secs  = float(raTime[raTime.index("m")+1:raTime.index("s")].strip())
        
        degStr = str(hours*15 + mins*(1/4) + secs*(1/240))
        return degStr[:degStr.index(".")+5]




