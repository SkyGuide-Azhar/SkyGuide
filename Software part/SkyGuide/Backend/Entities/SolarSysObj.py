class SolarSysObj():
    
    def __init__(self):
        pass


    def __str__(self):
        returnStr = f"""
Name : {self.GetName()}\n
Right ascension in time : {self.GetRATime()}\n
Right ascension in degree : {self.GetRADeg()}\n
Declination : {self.GetDeclination()}\n
Distance : {self.GetDistance()}\n
Magnitude : {self.GetMagnitude()}\n
Mass : {self.GetMass()}\n
Density : {self.GetDensity()}\n
Escape Velocity : {self.GetEscapeVelocity()}\n
Diameter : {self.GetDiameter()}\n
Sideral Rotation : {self.GetSideralRotation()}\n
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
    
    __constellation = None
    def SetConstellation(self, constellation):
            self.__constellation = constellation
    def GetConstellation(self):
            return self.__constellation
    
    #------------------------------------------
    
    __magnitude = None
    def SetMagnitude(self, magnitude):
            self.__magnitude = magnitude
    def GetMagnitude(self):
            return self.__magnitude
    
    #------------------------------------------
    
    __distance = None
    def SetDistance(self, distance):
            self.__distance = distance
    def GetDistance(self):
            return self.__distance
    
    #------------------------------------------
    
    __diameter = None
    def SetDiameter(self, diameter):
            self.__diameter = diameter
    def GetDiameter(self):
            return self.__diameter
    
    #------------------------------------------
    
    __mass = None
    def SetMass(self, mass):
            self.__mass = mass
    def GetMass(self):
            return self.__mass
    
    #------------------------------------------
    
    __density = None
    def SetDensity(self, density):
            self.__density = density
    def GetDensity(self):
            return self.__density
    
    #------------------------------------------
    
    __escapeVelocity = None
    def SetEscapeVelocity(self, escapeVelocity):
            self.__escapeVelocity = escapeVelocity
    def GetEscapeVelocity(self):
            return self.__escapeVelocity
    
    #------------------------------------------
    
    __sideralRotation = None
    def SetSideralRotation(self, sideralRotation):
            self.__sideralRotation = sideralRotation
    def GetSideralRotation(self):
            return self.__sideralRotation
