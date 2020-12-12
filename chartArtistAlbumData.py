from ioUtils import getFile
from masterArtistNameDB import masterArtistNameDB
from billboardData import billboardData
from top40Data import top40Data

class chartArtistAlbumData:    
    def __init__(self, chartType):
        self.chartType = chartType
        self.dclass = {"Billboard": billboardData(), "Top40": top40Data()}
        if self.chartType not in self.dclass.keys():
            raise ValueError("ChartType {0} is not allowed".format(self.chartType))

        self.setRenameDB("main")
        
        self.artistAlbumData = None
        self.setArtistAlbumData()
        
        self.singleArtistAlbumData = None
        self.manyArtistAlbumData   = None
        
        
    def getArtistAlbumData(self):
        return self.singleArtistAlbumData, self.manyArtistAlbumData
        
        
    def setRenameDB(self, renameName):
        try:
            self.renameDB = masterArtistNameDB(renameName, init=False)
        except:
            self.renameDB = None


            
    ################################################################################################
    ## Create Artist Data
    ################################################################################################    
    def setArtistAlbumData(self):
        rawArtistAlbumData    = getFile(self.dclass[self.chartType].getArtistAlbumDataFilename())
        nRenamed = 0
        fixedArtistAlbumData = {}
        print("There are {0} unique artists in artist albums data".format(len(rawArtistAlbumData)))
        for artistName,artistAlbums in rawArtistAlbumData.items():
            renamedArtistName = artistName
            if self.renameDB is not None:
                tmpName = self.renameDB.renamed(renamedArtistName)
                if tmpName != renamedArtistName:
                    nRenamed += 1
                renamedArtistName = tmpName
            if fixedArtistAlbumData.get(renamedArtistName) is None:
                fixedArtistAlbumData[renamedArtistName] = []
            fixedArtistAlbumData[renamedArtistName] += artistAlbums
        print("There are {0} newly unique artists in artist albums data".format(len(fixedArtistAlbumData)))
        print("Renamed {0} artists".format(nRenamed))
        self.artistAlbumData = fixedArtistAlbumData
        
        
    ################################################################################################
    ## Create Indiv Artist Data
    ################################################################################################    
    def createIndivArtistAlbumData(self):
        if self.artistAlbumData is None:
            raise ValueError("Artist Album Data is not set!")

        
        from multiArtist import multiartist
        multiDelimArtists=open("../multiartist/multiDelimArtists.dat").readlines()
        multiDelimArtists = [x.replace("\n", "") for x in multiDelimArtists]
        multiDelimArtists[:3]

        mularts  = multiartist(cutoff=0.9, discdata=None, exact=False)
        #mularts.setKnownMultiDelimArtists(multiDelimArtists)    

        print("There are {0: <6} unique artist entries in the artist albums data".format(len(self.artistAlbumData)))
        singleArtistAlbumData     = {artistName: artistAlbums for artistName,artistAlbums in self.artistAlbumData.items() if len(mularts.getArtistNames(artistName)) >= 1}
        manyArtistAlbumData       = {}

        print("There are {0: <6} single artist entries in the artist albums data".format(len(singleArtistAlbumData)))


        manyArtists       = {artist: mularts.getArtistNames(artist) for artist in self.artistAlbumData.keys() if singleArtistAlbumData.get(artist) is None}

        print("There are {0: <6} multi artist entries in the artist albums data".format(len(manyArtists)))

        for manyartist,artists in manyArtists.items():
            manyArtistAlbums = artistAlbumData[manyartist]
            for artistName in artists:            
                if singleArtistAlbumData.get(artistName) is not None:
                    singleArtistAlbumData[artistName] += manyArtistAlbums
                else:
                    if manyArtistAlbumData.get(artistName) is not None:
                        manyArtistAlbumData[artistName] += manyArtistAlbums
                    else:
                        manyArtistAlbumData[artistName] = manyArtistAlbums

        print("There are {0: <6} solo artist entries in the artist albums data".format(len(singleArtistAlbumData)))
        print("There are {0: <6} many artist entries in the artist albums data".format(len(manyArtistAlbumData)))
        
        self.singleArtistAlbumData = singleArtistAlbumData
        self.manyArtistAlbumData   = manyArtistAlbumData