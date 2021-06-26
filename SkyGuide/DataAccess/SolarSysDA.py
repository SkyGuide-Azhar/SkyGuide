from SkyGuide_DB.db import SkyGuideDBMember

class SolarSys(SkyGuideDBMember):
    
    def _init_(self):
        pass
        
#___________________________________________________________________________________
    
    def checkName(self,name):
        isNameCorrect = False
        
        self._cr.execute("select exists(select name from solar_sys where name = '{0}')".format(name))
        result = self._cr.fetchone()        
        
        if(result[0] == 1):
            isNameCorrect = True
        
        return isNameCorrect
    
#___________________________________________________________________________________
    
    def getByName(self,name):
        solarSysObjDict = {}
        
        self._cr.execute("select * from solar_sys where name = '{0}'".format(name))
        solarSysObjList = self._cr.fetchone()
        
        solarSysObjDict["Name"]                        = solarSysObjList[0]
        solarSysObjDict["Right ascension in time"]     = solarSysObjList[1]
        solarSysObjDict["Right ascension in degree"]   = solarSysObjList[2]
        solarSysObjDict["Declination"]                 = solarSysObjList[3]
        solarSysObjDict["Constellation"]               = solarSysObjList[4]
        solarSysObjDict["Magnitude"]                   = solarSysObjList[5]
        solarSysObjDict["Distance"]                    = solarSysObjList[6]
        solarSysObjDict["Diameter"]                    = solarSysObjList[7]
        solarSysObjDict["Mass"]                        = solarSysObjList[8]
        solarSysObjDict["Density"]                     = solarSysObjList[9]
        solarSysObjDict["Escape velocity"]             = solarSysObjList[10]
        solarSysObjDict["Sideral rotation"]            = solarSysObjList[11]
        
        return solarSysObjDict
    
