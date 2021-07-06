from Backend.BusinessLayer.SGDB_Interface import SGDB_Interface

from Backend.Entities.Nebula              import Nebula
from Backend.Entities.Star                import Star
from Backend.Entities.SupernovaRemnant    import SupernovaRemnant




class AddObject:

    def __init__(self):
        self.__SGDB_Interface = SGDB_Interface()

    #-----------Stars--------------------
    def AddUserStar(self, name, ra_time, dec_deg, dist, mag, spect, color_idx, bayer, con):

        star = Star()

        star.SetName(name)
        star.SetRATime(ra_time)
        star.SetDeclination(dec_deg)
        star.SetDistance(dist)
        star.SetMagnitude(mag)
        star.SetSpectrum(spect)
        star.SetColorIdx(color_idx)
        star.SetBayerName(bayer)
        star.SetConstellation(con)

        try:
            returnStr = self.__SGDB_Interface.AddNew("stars",star)
        except:
            returnStr = "An error accured while adding the provided star information"
        finally:
            return returnStr

    #-----------Nebulas--------------------
    def AddUserNebula(self, name, ra_time, dec_deg, dist, dimensions, radius, con):

        nebula = Nebula()

        nebula.SetName(name)
        nebula.SetRATime(ra_time)
        nebula.SetDeclination(dec_deg)
        nebula.SetDistance(dist)
        nebula.SetDimensions(dimensions)
        nebula.SetRadius(radius)
        nebula.SetConstellation(con)

        try:
            returnStr = self.__SGDB_Interface.AddNew("nebulas",nebula)
        except:
            returnStr = "An error accured while adding the provided nebula information"
        finally:
            return returnStr

    #-----------Supernova Remnants---------
    def AddUserSupernovaRemnant(self, name, ra_time, dec_deg, dist, fvfe, remnant):

        supernovaRemnant = SupernovaRemnant()

        supernovaRemnant.SetName(name)
        supernovaRemnant.SetRATime(ra_time)
        supernovaRemnant.SetDeclination(dec_deg)
        supernovaRemnant.SetFVFE(dist)
        supernovaRemnant.SetDistance(fvfe)
        supernovaRemnant.SetRemnant(remnant)

        try:
            returnStr = self.__SGDB_Interface.AddNew("supernova_remnants",supernovaRemnant)
        except:
            returnStr = "An error accured while adding the provided supernova remnant information"
        finally:
            return returnStr
