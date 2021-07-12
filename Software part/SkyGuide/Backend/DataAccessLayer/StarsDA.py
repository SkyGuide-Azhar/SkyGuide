from Backend.DataAccessLayer.DB_Affiliate import DB_Affiliate
from Backend.Entities.Star                import Star
from Backend.Entities.Constellation       import Constellation


class StarsDA(DB_Affiliate): 
    
    def __init__(self):
        pass
        
#___________________________________________________________________________________
    
    def CheckName(self,name):
        isNameCorrect = False
        try: 
            self._connection.cr.execute(f"select exists(select name from stars where name = '{name}')")
            result = self._connection.cr.fetchone()        
            
            if(result[0] == 1):
                isNameCorrect = True
        except:
            pass
        
        return isNameCorrect
    
#___________________________________________________________________________________
    
    def GetByName(self, name):
        star = Star()
        con  = Constellation() 
        
        try:    
            queryStr = f"SELECT * FROM stars INNER JOIN constellations on constellations.IAU_abbr = stars.con WHERE stars.name = '{name}'"
            
            self._connection.cr.execute(queryStr)
            starList =  self._connection.cr.fetchone()
            
            #---------------------- Star ----------------------------------
            
            star.SetName(starList[0])
            star.SetRATime(starList[1])
            star.SetRADeg(starList[2])
            star.SetDeclination(starList[3])
            star.SetDistance(starList[4])
            star.SetMagnitude(starList[5])
            star.SetSpectrum(starList[6])
            star.SetColorIdx(starList[7])
            star.SetBayerName(starList[8])
            star.SetConstellation(starList[9])
            
            #---------------------- Constellation ----------------------------
            
            con.SetName(starList[10])
            con.SetIAU(starList[11])
            con.SetRAStartTime(starList[12])
            con.SetRAStartDeg(starList[13])
            con.SetRAEndTime(starList[14])
            con.SetRAEndDeg(starList[15])
            con.SetDeclinationStart(starList[16])
            con.SetDeclinationEnd(starList[17])
            con.SetGenitive(starList[18])
            con.SetMeaning(starList[19])
            con.SetBrightestStar(starList[20])
        
        except:
            pass
        
        return star, con
    
#___________________________________________________________________________________
    
    def AddNew(self, star):
        starAlreadyExists = self.CheckName(star.GetName())
        
        if(starAlreadyExists):
            return "The provided star already exits."
        
        try:
            queryStr = "insert into stars values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')"
            
            self._connection.cr.execute(queryStr.format(star.GetName(),
                                                        star.GetRATime(),
                                                        star.GetRADeg(),
                                                        star.GetDeclination(),
                                                        star.GetDistance(),
                                                        star.GetMagnitude(),
                                                        star.GetSpectrum(),
                                                        star.GetColorIdx(),
                                                        star.GetBayerName(),
                                                        star.GetConstellation()))
            self._connection.db.commit()
            
            return "Star is added successfully."    
        
        except:
             return "The provided star failed to be added, kindly check the passed info and try again."
    
    
    
    
