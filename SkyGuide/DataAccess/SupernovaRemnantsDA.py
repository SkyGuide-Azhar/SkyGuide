from SkyGuide_DB.db import SkyGuideDBMember

class SupernovaRemnants(SkyGuideDBMember):

    def _init_(self):
        pass
        
#___________________________________________________________________________________
    
    def checkName(self,name):
        isNameCorrect = False
        
        result = self._db.execute("select exists(select name from supernova_remnants where name like '{0}')".format(name)).fetchone()

        if(result[0] == 1):
            isNameCorrect = True
        
        return isNameCorrect

#___________________________________________________________________________________
    
    def getByName(self, name):
        srDict = {}
        queryStr = "select * from supernova_remnants where name like '{0}'"
        srList = self._db.execute(queryStr.format(name)).fetchone()
        
        srDict["Name"]                          = srList[0]
        srDict["Right ascension in time"]       = srList[1]
        srDict["Right ascension in degree"]     = srList[2]
        srDict["Declination"]                   = srList[3]
        srDict["First visible from earth"]      = srList[4]
        srDict["Distance"]                      = srList[5]
        srDict["Remnant"]                       = srList[6]

        return srDict
    
#___________________________________________________________________________________
    
    def addNew(self, srDict):
        srAlreadyExists = self.checkName(srDict["name"])
        
        if(srAlreadyExists):
            return "The provided supernova remnant already exits."

        queryStr = "insert into supernova_remnants values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')"
        
        self._db.execute(queryStr.format(srDict["name"],
                                         srDict["ra_time"],
                                         srDict["ra_deg"],
                                         srDict["dec_deg"],
                                         srDict["fvfe"],
                                         srDict["dist"],
                                         srDict["remnant"]))
        self._db.commit()
        
        return "The supernova remnant is added successfully."
    
    
    
    
    
    
