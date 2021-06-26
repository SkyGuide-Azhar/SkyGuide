class Star():

    __name                   = None
    __rightAscensionInTime   = None
    __rightAscensionInDegree = None
    __declination            = None
    __distance               = None
    __magnitude              = None
    __spectrum               = None
    __colorIndex             = None
    __bayerName              = None
    __constellation          = None
    
    def __init__(self):
        pass
    
    #-------------------------------------------------------------
    
    def SetName(self, name):
        self.__name = name
        
    def GetName(self):
        return self.__name
        
    #-------------------------------------------------------------
    
    def SetRATime(self, raTime):
        self.__rightAscensionInTime = raTime
        
    def GetRATime(self):
        return self.__rightAscensionInTime
        
    #-------------------------------------------------------------
    
    def SetRADeg(self, raDeg):
        self.__rightAscensionInDegree = raDeg 
        
    def GetRADeg(self):
        return self.__rightAscensionInDegree
        
    #-------------------------------------------------------------
    
    def SetDeclination(self, dec):
        self.__declination = dec
        
    def GetDeclination(self):
        return self.__declination
        
    #-------------------------------------------------------------
    
    def SetDistance(self, dis):
        self.__distance = dis
        
    def GetDistance(self):
        return self.__distance
        
    #-------------------------------------------------------------
    
    def SetMagnitude(self, mag):
        self.__magnitude = mag
        
    def GetMagnitude(self):
        return self.__magnitude
        
    #-------------------------------------------------------------
    
    def SetSpectrum(self, spec):
        self.__spectrum = spec
        
    def GetSpectrum(self):
        return self.__spectrum
        
    #-------------------------------------------------------------
    
    def SetColorIdx(self, cIdx):
        self.__colorIndex = cIdx
        
    def GetColorIdx(self):
        return self.__colorIndex
        
    #-------------------------------------------------------------
    
    def SetBayerName(self, bayerName):
        self.__bayerName = bayerName
        
    def GetBayerName(self):
        return self.__bayerName
        
    #-------------------------------------------------------------
    
    def SetConstellation(self, con):
        self.__constellation = con
        
    def GetConstellation(self):
        return self.__constellation
    
    
    