from SkyGuide_DB.db import SkyGuideDBMember

class Constellations(SkyGuideDBMember):
    
    def _init_(self):
        pass
        
#___________________________________________________________________________________
    
    def checkName(self,name):
        isNameCorrect = False
        
        result = self._db.execute("select exists(select name from constellations where name = '{0}')".format(name)).fetchone()

        if(result[0] == 1):
            isNameCorrect = True
        
        return isNameCorrect
    
#___________________________________________________________________________________
    
    def checkIAU(self,IAU_abbr):
        isIAU_abbrCorrect = False
        
        result = self._db.execute("select exists(select name from constellations where IAU_abbr = '{0}')".format(IAU_abbr)).fetchone()
                
        
        if(result[0] == 1):
            isIAU_abbrCorrect = True
        
        return isIAU_abbrCorrect
    
#___________________________________________________________________________________
    
    def getByName(self,name):
        conDict = {}
        
        conList = self._db.execute("select * from constellations where name = '{0}'".format(name)).fetchone()
        
        conDict["Name"]                              = conList[0]
        conDict["IAU Abbreviation"]                  = conList[1]
        conDict["Right ascension start in time"]     = conList[2]
        conDict["Right ascension start in degree"]   = conList[3]
        conDict["Right ascension end in time"]       = conList[4]
        conDict["Right ascension end in degree"]     = conList[5]
        conDict["Declination start"]                 = conList[6]
        conDict["Declination end"]                   = conList[7]
        conDict["Genitive"]                          = conList[8]
        conDict["Meaning"]                           = conList[9]
        conDict["Brightest star"]                    = conList[10]
    
        return conDict
    
#___________________________________________________________________________________
    
    def getByIAU(self,IAU_abbr):
        conDict = {}
        
        conList = self._db.execute("select * from constellations where IAU_abbr = '{0}'".format(IAU_abbr)).fetchone()
    
        conDict["Name"]                              = conList[0]
        conDict["IAU Abbreviation"]                  = conList[1]
        conDict["Right ascension start in time"]     = conList[2]
        conDict["Right ascension start in degree"]   = conList[3]
        conDict["Right ascension end in time"]       = conList[4]
        conDict["Right ascension end in degree"]     = conList[5]
        conDict["Declination start"]                 = conList[6]
        conDict["Declination end"]                   = conList[7]
        conDict["Genitive"]                          = conList[8]
        conDict["Meaning"]                           = conList[9]
        conDict["Brightest star"]                    = conList[10]
    
        return conDict
    
    
