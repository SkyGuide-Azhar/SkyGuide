class Star():
    
    def __init__(self):
        pass


    def __str__(self):
        returnStr = f"""
Name : {self.GetName()}\n
Right ascension in time : {self.GetRATime()}\n
Rght ascension in degree : {self.GetRADeg()}\n
Declination : {self.GetDeclination()}\n
Distance : {self.GetDistance()}\n
Magnitude : {self.GetMagnitude()}\n
Spectrum : {self.GetSpectrum()}\n
Color index : {self.GetColorIdx()}\n
Bayer name : {self.GetBayerName()}\n
Constellation : {self.GetConstellation()}\n\n
--------------------------- Constellation Info --------------------------\n
        """
        return returnStr
#-------------------------------------------------------------
    
    __name = None
    def SetName(self, name):
        self.__name = name
    def GetName(self):
        return self.__name
        
#-------------------------------------------------------------
    
    __rightAscensionInTime = None
    def SetRATime(self, raTime):
        self.__rightAscensionInTime = raTime
    def GetRATime(self):
        return self.__rightAscensionInTime
        
#-------------------------------------------------------------
    
    __rightAscensionInDegree = None
    def SetRADeg(self, raDeg):
        self.__rightAscensionInDegree = raDeg 
    def GetRADeg(self):
        return self.__rightAscensionInDegree
        
#-------------------------------------------------------------
    
    __declination = None
    def SetDeclination(self, dec):
        self.__declination = dec
    def GetDeclination(self):
        return self.__declination
        
#-------------------------------------------------------------
    
    __distance = None
    def SetDistance(self, dis):
        self.__distance = dis
    def GetDistance(self):
        return self.__distance
        
#-------------------------------------------------------------
    
    __magnitude = None
    def SetMagnitude(self, mag):
        self.__magnitude = mag
    def GetMagnitude(self):
        return self.__magnitude
        
#-------------------------------------------------------------
    
    __spectrum = None
    def SetSpectrum(self, spec):
        self.__spectrum = spec
    def GetSpectrum(self):
        return self.__spectrum
        
#-------------------------------------------------------------
    
    __colorIndex = None
    def SetColorIdx(self, cIdx):
        self.__colorIndex = cIdx
    def GetColorIdx(self):
        return self.__colorIndex
        
#-------------------------------------------------------------
    
    __bayerName = None
    def SetBayerName(self, bayerName):
        self.__bayerName = bayerName
    def GetBayerName(self):
        return self.__bayerName
        
#-------------------------------------------------------------
    
    __constellation = None
    def SetConstellation(self, con):
        self.__constellation = con
    def GetConstellation(self):
        return self.__constellation
    
