class Nebula():

    def __init__(self):
        pass


    def __str__(self):
        returnStr = f"""
Name : {self.GetName()}\n
Right ascension in time : {self.GetRATime()}\n
Right ascension in degree : {self.GetRADeg()}\n
Declination : {self.GetDeclination()}\n
Distance : {self.GetDistance()}\n
Dimensions : {self.GetDimensions()}\n
Radius : {self.GetRadius()}\n\n
Constellation : {self.GetConstellation()}\n\n
--------------------------- Constellation Info --------------------------\n
        """
        return returnStr

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
    
    __distance = None
    def SetDistance(self, distance):
            self.__distance = distance
    def GetDistance(self):
            return self.__distance
    
    #------------------------------------------
    
    __dimensions = None
    def SetDimensions(self, dimensions):
            self.__dimensions = dimensions
    def GetDimensions(self):
            return self.__dimensions
    
    #------------------------------------------
    
    __radius = None
    def SetRadius(self, radius):
            self.__radius = radius
    def GetRadius(self):
            return self.__radius
    
    #------------------------------------------
    
    __constellation = None
    def SetConstellation(self, constellation):
            self.__constellation = constellation
    def GetConstellation(self):
            return self.__constellation
