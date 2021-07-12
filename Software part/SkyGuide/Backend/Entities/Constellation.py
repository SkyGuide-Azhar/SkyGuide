class Constellation():
    
    def __init__(self):
        pass


    def __str__(self):
        returnStr = f"""
Name : {self.GetName()}\n
IAU Abbriviation : {self.GetIAU()}\n
Right ascension start in time : {self.GetRAStartTime()}\n
Right ascension end in time : {self.GetRAEndTime()}\n
Right ascension start in degree : {self.GetRAStartDeg()}\n
Right ascension end in degree : {self.GetRAEndDeg()}\n
Declination start : {self.GetDeclinationStart()}\n
Declination end : {self.GetDeclinationEnd()}\n
Genitive : {self.GetGenitive()}\n
Meaning : {self.GetMeaning()}\n
Brightest Star : {self.GetBrightestStar()}\n
        """
        return returnStr

    #-------------------------------------------------------------
    
    __name = None
    def SetName(self, name):
        self.__name = name
    def GetName(self):
        return self.__name
    
    #-------------------------------------------------------------
    
    __IAU_Abbreviation = None
    def SetIAU(self, IAU):
        self.__IAU_Abbreviation = IAU     
    def GetIAU(self):
        return self.__IAU_Abbreviation
        
    #-------------------------------------------------------------
    
    __rightAscensionStartInTime = None
    def SetRAStartTime(self, raStartTime):
        self.__rightAscensionStartInTime = raStartTime    
    def GetRAStartTime(self):
        return self.__rightAscensionStartInTime
        
    #-------------------------------------------------------------
    
    __rightAscensionEndInTime = None
    def SetRAEndTime(self, raEndTime):
        self.__rightAscensionEndInTime = raEndTime   
    def GetRAEndTime(self):
        return self.__rightAscensionEndInTime
    
    #-------------------------------------------------------------
    
    __rightAscensionStartInDegree = None
    def SetRAStartDeg(self, raStartDeg):
        self.__rightAscensionStartInDegree = raStartDeg         
    def GetRAStartDeg(self):
        return self.__rightAscensionStartInDegree
    
    #-------------------------------------------------------------
    
    __rightAscensionEndInDegree = None
    def SetRAEndDeg(self, raEndDeg):
        self.__rightAscensionEndInDegree = raEndDeg        
    def GetRAEndDeg(self):
        return self.__rightAscensionEndInDegree
        
    #-------------------------------------------------------------
    
    __declinationStart = None
    def SetDeclinationStart(self, decStart):
        self.__declinationStart = decStart        
    def GetDeclinationStart(self):
        return self.__declinationStart
        
    #-------------------------------------------------------------
    
    __declinationEnd = None
    def SetDeclinationEnd(self, decEnd):
        self.__declinationEnd = decEnd        
    def GetDeclinationEnd(self):
        return self.__declinationEnd
    
    #-------------------------------------------------------------
    
    __genitive = None
    def SetGenitive(self, gen):
        self.__genitive = gen        
    def GetGenitive(self):
        return self.__genitive
        
    #-------------------------------------------------------------
    
    __meaning = None
    def SetMeaning(self, meaning):
        self.__meaning = meaning        
    def GetMeaning(self):
        return self.__meaning
        
    #-------------------------------------------------------------
    
    __brightestStar = None
    def SetBrightestStar(self, brStar):
        self.__brightestStar = brStar      
    def GetBrightestStar(self):
        return self.__brightestStar
        
    
