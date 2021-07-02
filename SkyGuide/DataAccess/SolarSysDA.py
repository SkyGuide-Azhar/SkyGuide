from DataAccess.DB_Affiliate    import SkyGuideDBAffiliate
from Entities.SolarSysObj       import SolarSysObj

class SolarSys(SkyGuideDBAffiliate):
    
    def _init_(self):
        pass
        
#___________________________________________________________________________________
    
    def checkName(self,name):
        isNameCorrect = False
        try:
            self._connection.cr.execute(f"select exists(select name from solar_sys where name = '{name}')")
            result = self._connection.cr.fetchone()        
            
            if(result[0] == 1):
                isNameCorrect = True
        except:
            pass
        
        return isNameCorrect
    
#___________________________________________________________________________________
    
    def getByName(self,name):
        solarSysObj = SolarSysObj()
        
        try:
            queryStr = f"select * from solar_sys where name = '{name}'"
            
            self._connection.cr.execute(queryStr)
            solarSysObjList =  self._connection.cr.fetchone()
            
            solarSysObj.SetName(solarSysObjList[0])
            solarSysObj.SetRATime(solarSysObjList[1])
            solarSysObj.SetRADeg(solarSysObjList[2])
            solarSysObj.SetDeclination(solarSysObjList[3])
            solarSysObj.SetConstellation(solarSysObjList[4])
            solarSysObj.SetMagnitude(solarSysObjList[5])
            solarSysObj.SetDistance(solarSysObjList[6])
            solarSysObj.SetDiameter(solarSysObjList[7])
            solarSysObj.SetMass(solarSysObjList[8])
            solarSysObj.SetDensity(solarSysObjList[9])
            solarSysObj.SetEscapeVelocity(solarSysObjList[10])
            solarSysObj.SetSideralRotation(solarSysObjList[11])
        
        except:
            pass
        
        return solarSysObj
        