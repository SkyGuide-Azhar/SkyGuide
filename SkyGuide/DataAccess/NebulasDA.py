from DataAccess.DB_Affiliate import DB_Affiliate
from Entities.Nebula         import Nebula
from Entities.Constellation  import Constellation

class NebulasDA(DB_Affiliate):

    def _init_(self):
        pass
        
#___________________________________________________________________________________
    
    def CheckName(self, name):
        isNameCorrect = False
        try:
            self._connection.cr.execute(f"select exists(select name from nebulas where name = '{name}')")
            result = self._connection.cr.fetchone()  
    
            if(result[0] == 1):
                isNameCorrect = True
        except:
            pass
        
        return isNameCorrect
    
#___________________________________________________________________________________
    
    def GetByName(self, name):
        nebula = Nebula()
        con    = Constellation() 
        
        try:
            queryStr = f"SELECT * FROM nebulas INNER JOIN constellations on constellations.IAU_abbr = nebulas.con WHERE nebulas.name = '{name}'"
            
            self._connection.cr.execute(queryStr)
            nebulaList =  self._connection.cr.fetchone()
            
            #---------------------- Nebula ----------------------------------
            
            nebula.SetName(nebulaList[0])
            nebula.SetRATime(nebulaList[1])
            nebula.SetRADeg(nebulaList[2])
            nebula.SetDeclination(nebulaList[3])
            nebula.SetDistance(nebulaList[4])
            nebula.SetDimensions(nebulaList[5])
            nebula.SetRadius(nebulaList[6])
            nebula.SetConstellation(nebulaList[7])
    
            #---------------------- Constellation ----------------------------
            
            con.SetName(nebulaList[8])
            con.SetIAU(nebulaList[9])
            con.SetRAStartTime(nebulaList[10])
            con.SetRAStartDeg(nebulaList[11])
            con.SetRAEndTime(nebulaList[12])
            con.SetRAEndDeg(nebulaList[13])
            con.SetDeclinationStart(nebulaList[14])
            con.SetDeclinationEnd(nebulaList[15])
            con.SetGenitive(nebulaList[16])
            con.SetMeaning(nebulaList[17])
            con.SetBrightestStar(nebulaList[18])
        
        except:
            pass
        
        return nebula, con
    
#___________________________________________________________________________________
    
    def AddNew(self, nebula):
        nebulaAlreadyExists = self.checkName(nebula.GetName())
        
        if(nebulaAlreadyExists):
            return "The provided nebula already exits."
        
        try:
            queryStr = "insert into nebulas values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"
            
            self._connection.cr.execute(queryStr.format(nebula.GetName(),
                                                        nebula.GetRATime(),
                                                        nebula.GetRADeg(),
                                                        nebula.GetDeclination(),
                                                        nebula.GetDistance(),
                                                        nebula.GetDimensions(),
                                                        nebula.GetRadius(),
                                                        nebula.GetConstellation()))
            self._connection.db.commit()
            
            return "Nebula is added successfully."
       
        except:
            return "The provided nebula failed to be added, kindly check the passed info and try again."




