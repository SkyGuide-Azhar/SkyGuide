from Backend.BusinessLayer.SGDB_Interface import SGDB_Interface


class SearchObject():

    def __init__(self):
        self.__SGDB_Interface = SGDB_Interface()

    #---------------------------------------------------

    def GetSearchResult(self, objType, objName):

        searchResult, RA, DEC = self.__SGDB_Interface.GetByName(objType, objName)

        if(RA == None):
            searchStatus = False
        else:
            searchStatus = True

        return searchResult, searchStatus, RA, DEC


