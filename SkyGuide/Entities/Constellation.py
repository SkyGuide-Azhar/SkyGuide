class Constellation():

    __name                        = None
    __IAU_Abbreviation            = None
    __rightAscensionStartInTime   = None
    __rightAscensionStartInDegree = None
    __rightAscensionEndInTime     = None
    __rightAscensionEndInDegree   = None
    __declinationStart            = None
    __declinationEnd              = None
    __genitive                    = None
    __meaning                     = None
    __brightestStar               = None
    
    def __init__(self):
        pass
    
    #-------------------------------------------------------------
    
    def SetName(self, name):
        self.__name = name
        
    def GetName(self):
        return self.__name
    
    #-------------------------------------------------------------
    
    def SetIAU(self, IAU):
        self.__IAU_Abbreviation = IAU
        
    def GetIAU(self):
        return self.__IAU_Abbreviation
        
    #-------------------------------------------------------------
    
    def SetRAStartTime(self, raStartTime):
        self.__rightAscensionStartInTime = raStartTime
        
    def GetRAStartTime(self):
        return self.__rightAscensionStartInTime
        
    #-------------------------------------------------------------
    
    def SetRAEndTime(self, raEndTime):
        self.__rightAscensionEndInTime = raEndTime
        
    def GetRAEndTime(self):
        return self.__rightAscensionEndInTime
    
    #-------------------------------------------------------------
    
    def SetRAStartDeg(self, raStartDeg):
        self.__rightAscensionStartInDegree = raStartDeg 
        
    def GetRAStartDeg(self):
        return self.__rightAscensionStartInDegree
    
    #-------------------------------------------------------------
    
    def SetRAEndDeg(self, raEndDeg):
        self.__rightAscensionEndInDegree = raEndDeg 
        
    def GetRAEndDeg(self):
        return self.__rightAscensionEndInDegree
        
    #-------------------------------------------------------------
    
    def SetDeclinationStart(self, decStart):
        self.__declinationStart = decStart
        
    def GetDeclinationStart(self):
        return self.__declinationStart
        
    #-------------------------------------------------------------
    
    def SetDeclinationEnd(self, decEnd):
        self.__declinationEnd = decEnd
        
    def GetDeclinationEnd(self):
        return self.__declinationEnd
    
    #-------------------------------------------------------------
    
    def SetGenitive(self, gen):
        self.__genitive = gen
        
    def GetGenitive(self):
        return self.__genitive
        
    #-------------------------------------------------------------
    
    def SetMeaning(self, meaning):
        self.__meaning = meaning
        
    def GetMeaning(self):
        return self.__meaning
        
    #-------------------------------------------------------------
    
    def SetBrightestStar(self, brStar):
        self.__brightestStar = brStar
        
    def GetBrightestStar(self):
        return self.__brightestStar
        
    