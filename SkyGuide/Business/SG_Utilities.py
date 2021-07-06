from DataAccess.StarsDA             import StarsDA
from DataAccess.SolarSysDA          import SolarSysDA
from DataAccess.NebulasDA           import NebulasDA
from DataAccess.SupernovaRemnantsDA import SupernovaRemnantsDA
from DataAccess.ConstellationsDA    import ConstellationsDA

from Entities.Constellation         import Constellation
from Entities.Star                  import Star
from Entities.Nebula                import Nebula
from Entities.SolarSysObj           import SolarSysObj
from Entities.SupernovaRemnant      import SupernovaRemnant

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
        
        if(constellation.checkName(con)):
            returnStr = constellation.GetByName(con).GetIAU()
            returnBool = True
        elif(constellation.checkIAU(con)):
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




