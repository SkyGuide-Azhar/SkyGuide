from SkyGuide_DB.db import SkyGuideDBMember

class Nebulas(SkyGuideDBMember):

    def _init_(self):
        pass
        
#___________________________________________________________________________________
    
    def checkName(self,name):
        isNameCorrect = False
        
        result = self._db.execute("select exists(select name from nebulas where name like '{0}')".format(name)).fetchone()  

        if(result[0] == 1):
            isNameCorrect = True
        
        return isNameCorrect
    
#___________________________________________________________________________________
    
    def getByName(self, name):
        nebulaDict = {}
        queryStr = "SELECT * FROM nebulas INNER JOIN constellations on constellations.IAU_abbr = nebulas.con WHERE nebulas.name = '{0}'"
        
        nebulaList = self._db.execute(queryStr.format(name)).fetchone()

        nebulaDict["Name"]                          = nebulaList[0]
        nebulaDict["Right ascension in time"]       = nebulaList[1]
        nebulaDict["Right ascension in degree"]     = nebulaList[2]
        nebulaDict["Declination"]                   = nebulaList[3]
        nebulaDict["Distance"]                      = nebulaList[4]
        nebulaDict["Dimensions"]                    = nebulaList[5]
        nebulaDict["Radius"]                        = nebulaList[6]
        nebulaDict["Constellation"]                 = nebulaList[7]
        
        nebulaDict["--------- Constellation Info"]      = " ---------" # To seperate output for the user
        
        nebulaDict["Constellation name"]                = nebulaList[8]
        nebulaDict["IAU Abbreviation"]                  = nebulaList[9]
        nebulaDict["Right ascension start in time"]     = nebulaList[10]
        nebulaDict["Right ascension start in degree"]   = nebulaList[11]
        nebulaDict["Right ascension end in time"]       = nebulaList[12]
        nebulaDict["Right ascension end in degree"]     = nebulaList[13]
        nebulaDict["Declination start"]                 = nebulaList[14]
        nebulaDict["Declination end"]                   = nebulaList[15]
        nebulaDict["Genitive"]                          = nebulaList[16]
        nebulaDict["Meaning"]                           = nebulaList[17]
        nebulaDict["Brightest star"]                    = nebulaList[18]
    
        return nebulaDict
    
#___________________________________________________________________________________
    
    def addNew(self, nebulaDict):
        nebulaAlreadyExists = self.checkName(nebulaDict["name"])
        
        if(nebulaAlreadyExists):
            return "The provided nebula already exits."

        queryStr = "insert into nebulas values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
        
        self._db.execute(queryStr.format(nebulaDict["name"],
                                         nebulaDict["ra_time"],
                                         nebulaDict["ra_deg"],
                                         nebulaDict["dec_deg"],
                                         nebulaDict["dist"],
                                         nebulaDict["dimensions"],
                                         nebulaDict["radius"],
                                         nebulaDict["con"]))
        self._db.commit()
        return "Nebula is added successfully."
        
    
    
    
    
    
    
