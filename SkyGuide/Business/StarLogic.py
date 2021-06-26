from DataAccess.StarsDA import StarsDA
from Entities.Star      import Star

class StarLogic():

    def __init__(self):
        pass
    
    def GetByName(self, name):
        star, con = StarsDA().getByName(name)
        returnStr = "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9} ".format(star.GetName(),
                         star.GetRATime(),
                         star.GetRADeg(),
                         star.GetDeclination(),
                         star.GetDistance(),
                         star.GetMagnitude(),
                         star.GetSpectrum(),
                         star.GetColorIdx(),
                         star.GetBayerName(),
                         star.GetConstellation())

        returnStr += "\n{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10} ".format(con.GetName(),
                          con.GetIAU(),
                          con.GetRAStartTime(),
                          con.GetRAStartDeg(),
                          con.GetRAEndTime(),
                          con.GetRAEndDeg(),
                          con.GetDeclinationStart(),
                          con.GetDeclinationEnd(),
                          con.GetGenitive(),
                          con.GetMeaning(),
                          con.GetBrightestStar())
        
        return returnStr
        
StarsDAobj = StarsDA()

StarsDAobj.SGDB_Connect()

print(StarLogic().GetByName("sirius"))

StarsDAobj.SGDB_Disconnect()