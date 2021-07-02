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

    def GetObjAsStr(self, tableObj):
        returnStr = ""
        
        if(type(tableObj) == Star):
            returnStr = f"""
Name : {tableObj.GetName()}\n\n
Right ascension in time : {tableObj.GetRATime()}\n\n
Rght ascension in degree : {tableObj.GetRADeg()}\n\n
Declination : {tableObj.GetDeclination()}\n\n
Distance : {tableObj.GetDistance()}\n\n
Magnitude : {tableObj.GetMagnitude()}\n\n
Spectrum : {tableObj.GetSpectrum()}\n\n
Color index : {tableObj.GetColorIdx()}\n\n
Bayer name : {tableObj.GetBayerName()}\n\n
Constellation : {tableObj.GetConstellation()}\n\n
            """
        
        elif(type(tableObj) == Constellation):
            returnStr = f"""
Name : {tableObj.GetName()}\n\n
IAU Abbriviation : {tableObj.GetIAU()}\n\n
Right ascension start in time : {tableObj.GetRAStartTime()}\n\n
Right ascension end in time : {tableObj.GetRAEndTime()}\n\n
Right ascension start in degree : {tableObj.GetRAStartDeg()}\n\n
Right ascension end in degree : {tableObj.GetRAEndDeg()}\n\n
Declination start : {tableObj.GetDeclinationStart()}\n\n
Declination end : {tableObj.GetDeclinationEnd()}\n\n
Genitive : {tableObj.GetGenitive()}\n\n
Meaning : {tableObj.GetMeaning()}\n\n
Brightest Star : {tableObj.GetBrightestStar()}\n\n
            """
            
        elif(type(tableObj) == Nebula):
            returnStr = f"""
Name : {tableObj.GetName()}\n\n
Right ascension in time : {tableObj.GetRATime()}\n\n
Right ascension in degree : {tableObj.GetRADeg()}\n\n
Declination : {tableObj.GetDeclination()}\n\n
Distance : {tableObj.GetDistance()}\n\n
Dimensions : {tableObj.GetDimensions()}\n\n
Radius : {tableObj.GetRadius()}\n\n
Constellation : {tableObj.GetConstellation()}\n\n
            """
            
        elif(type(tableObj) == SolarSysObj):
            returnStr = f"""
Name : {tableObj.GetName()}\n\n
Right ascension in time : {tableObj.GetRATime()}\n\n
Right ascension in degree : {tableObj.GetRADeg()}\n\n
Declination : {tableObj.GetDeclination()}\n\n
Distance : {tableObj.GetDistance()}\n\n
Magnitude : {tableObj.GetMagnitude()}\n\n
Mass : {tableObj.GetMass()}\n\n
Density : {tableObj.GetDensity()}\n\n
Escape Velocity : {tableObj.GetEscapeVelocity()}\n\n
Diameter : {tableObj.GetDiameter()}\n\n
Sideral Rotation : {tableObj.GetSideralRotation()}\n\n
Constellation : {tableObj.GetConstellation()}\n\n
            """
        
        elif(type(tableObj) == SupernovaRemnant):
            returnStr = f"""
Name : {tableObj.GetName()}\n\n
Right ascension in time : {tableObj.GetRATime()}\n\n
Right ascension in degree : {tableObj.GetRADeg()}\n\n
Declination : {tableObj.GetDeclination()}\n\n
Distance : {tableObj.GetDistance()}\n\n
First Visible From Earth : {tableObj.GetFVFE()}\n\n
Remnant : {tableObj.GetRemnant()}\n\n
            """
        
        else:
            raise Exception("SkyGuideDB_Interface, the passed table name is incorrect!")
            
        return returnStr
        
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




