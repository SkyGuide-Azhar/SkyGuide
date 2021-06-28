class SupernovaRemnant():

    def __init__(self):
        pass
    
    #------------------------------------------
    
    __name = None
    def SetName(self, name):
            self.__name = name
    def GetName(self):
            return self.__name
    
    #------------------------------------------
    
    __rightAscensionInTime = None
    def SetRATime(self, rATime):
            self.__rightAscensionInTime = rATime
    def GetRATime(self):
            return self.__rightAscensionInTime
    
    #------------------------------------------
    
    __rightAscensionInDegree = None
    def SetRADeg(self, rADeg):
            self.__rightAscensionInDegree = rADeg
    def GetRADeg(self):
            return self.__rightAscensionInDegree
    
    #------------------------------------------
    
    __declination = None
    def SetDeclination(self, declination):
            self.__declination = declination
    def GetDeclination(self):
            return self.__declination
    
    #------------------------------------------
    
    __firstVisibleFromEarth = None
    def SetFVFE(self, fVFE):
            self.__firstVisibleFromEarth = fVFE
    def GetFVFE(self):
            return self.__firstVisibleFromEarth
    
    #------------------------------------------
    
    __distance = None
    def SetDistance(self, distance):
            self.__distance = distance
    def GetDistance(self):
            return self.__distance
    
    #------------------------------------------
    
    __remnant = None
    def SetRemnant(self, remnant):
            self.__remnant = remnant
    def GetRemnant(self):
            return self.__remnant
