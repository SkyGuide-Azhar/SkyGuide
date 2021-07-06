from Backend.DataAccessLayer.DB_Affiliate  import DB_Affiliate
from Backend.Entities.SupernovaRemnant     import SupernovaRemnant

class SupernovaRemnantsDA(DB_Affiliate):

    def _init_(self):
        pass
        
#___________________________________________________________________________________
    
    def CheckName(self,name):
        isNameCorrect = False      
        try:
            
            self._connection.cr.execute(f"select exists(select name from supernova_remnants where name like '{name}')")
            result = self._connection.cr.fetchone()  
    
            if(result[0] == 1):
                isNameCorrect = True
        except:
            pass
        
        return isNameCorrect
    
#___________________________________________________________________________________
    
    def GetByName(self, name):
        supernovaRemnant = SupernovaRemnant()
        
        try:
            queryStr = f"select * from supernova_remnants where name like '{name}'"
            
            self._connection.cr.execute(queryStr)
            srList =  self._connection.cr.fetchone()
            
            
            supernovaRemnant.SetName(srList[0])
            supernovaRemnant.SetRATime(srList[1])
            supernovaRemnant.SetRADeg(srList[2])
            supernovaRemnant.SetDeclination(srList[3])
            supernovaRemnant.SetFVFE(srList[4])
            supernovaRemnant.SetDistance(srList[5])
            supernovaRemnant.SetRemnant(srList[6])
        
        except:
            pass

        return supernovaRemnant, None
    
#___________________________________________________________________________________
    
    def AddNew(self, supernovaRemnant):   
        srAlreadyExists = self.CheckName(supernovaRemnant.GetName())
        
        if(srAlreadyExists):
            return "The provided supernova remnant already exits."
        
        try:
            queryStr = "insert into supernova_remnants values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')"
            
            self._connection.cr.execute(queryStr.format(supernovaRemnant.GetName(),
                                                        supernovaRemnant.GetRATime(),
                                                        supernovaRemnant.GetRADeg(),
                                                        supernovaRemnant.GetDeclination(),
                                                        supernovaRemnant.GetFVFE(),
                                                        supernovaRemnant.GetDistance(),
                                                        supernovaRemnant.GetRemnant()))
            
            self._connection.db.commit()
        
            return "The supernova remnant is added successfully."
        
        except:
            return "The provided supernova remnant failed to be added, kindly check the passed info and try again."
    

    
    
