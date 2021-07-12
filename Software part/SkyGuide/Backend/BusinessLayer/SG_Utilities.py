
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
        raDeg = ""

        try:
            hours = float(raTime[:raTime.index("h")])
            mins  = float(raTime[raTime.index("h")+1:raTime.index("m")].strip())
            secs  = float(raTime[raTime.index("m")+1:raTime.index("s")].strip())

            if((0 <= hours < 24) and (0 <= mins < 60) and (0 <= secs < 60)):
                degStr = str(hours*15 + mins*(1/4) + secs*(1/240))
                raDeg = float(degStr[:degStr.index(".")+5])
        except:
            pass
        finally:
            return raDeg

#__________________________________________________________________________________

    def __tryParseToFloat(self, num):
        try:
            float(num)
            return True
        except:
            return False

#__________________________________________________________________________________
    def RA_DEC_Check(self, RA, DEC):
        returnBool = False
        raDeg      = self.RATimeToDeg(RA)

        if(self.__tryParseToFloat(DEC) and (-90.0 <= float(DEC) <= 90.0)):
            DEC = float(DEC)

            if(self.__tryParseToFloat(RA) and (0.0 <= float(RA) < 360.0)):
                RA = float(RA)
                returnBool = True
            elif(raDeg != ""):
                RA = raDeg
                returnBool = True

        return returnBool, RA, DEC





