from Backend.DataAccessLayer.DB_Affiliate import DB_Affiliate
from Backend.Entities.Constellation       import Constellation

class ConstellationsDA(DB_Affiliate):
    
    def _init_(self):
        pass
        
#___________________________________________________________________________________
    
    def CheckName(self, name):
        isNameCorrect = False
        try:
            self._connection.cr.execute(f"select exists(select name from constellations where name = '{name}')")
            result = self._connection.cr.fetchone()  
    
            if(result[0] == 1):
                isNameCorrect = True
        except:
            pass
        
        return isNameCorrect
    
#___________________________________________________________________________________
    
    def CheckIAU(self, IAU_abbr):
        isIAU_abbrCorrect = False
        try:
            self._connection.cr.execute(f"select exists(select name from constellations where IAU_abbr = '{IAU_abbr}')")
            result = self._connection.cr.fetchone()  
    
            if(result[0] == 1):
                isIAU_abbrCorrect = True
        except:
            pass
        
        return isIAU_abbrCorrect
    
#___________________________________________________________________________________
    
    def GetByName(self, name):
        con = Constellation()
        
        try:
            queryStr = f"select * from constellations where name = '{name}'"
            
            self._connection.cr.execute(queryStr)
            conList =  self._connection.cr.fetchone()
            
            con.SetName(conList[0])
            con.SetIAU(conList[1])
            con.SetRAStartTime(conList[2])
            con.SetRAStartDeg(conList[3])
            con.SetRAEndTime(conList[4])
            con.SetRAEndDeg(conList[5])
            con.SetDeclinationStart(conList[6])
            con.SetDeclinationEnd(conList[7])
            con.SetGenitive(conList[8])
            con.SetMeaning(conList[9])
            con.SetBrightestStar(conList[10])
        
        except:
            pass
        
        return con, None
    
#___________________________________________________________________________________
    
    def GetByIAU(self, IAU_abbr):
        con = Constellation()
        
        try:
            queryStr = f"select * from constellations where IAU_abbr = '{IAU_abbr}'"
            
            self._connection.cr.execute(queryStr)
            conList =  self._connection.cr.fetchone()
            
            con.SetName(conList[0])
            con.SetIAU(conList[1])
            con.SetRAStartTime(conList[2])
            con.SetRAStartDeg(conList[3])
            con.SetRAEndTime(conList[4])
            con.SetRAEndDeg(conList[5])
            con.SetDeclinationStart(conList[6])
            con.SetDeclinationEnd(conList[7])
            con.SetGenitive(conList[8])
            con.SetMeaning(conList[9])
            con.SetBrightestStar(conList[10])
        
        except:
            pass
        
        return con, None
    
    
