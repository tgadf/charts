from ioUtils import getFile
from masterArtistNameDB import masterArtistNameDB
from billboardData import billboardData
from billboardYE import billboardYE
from top40Data import top40Data
from spotifyData import spotifyData
from multiArtist import multiartist

class chartArtistAlbumData:    
    def __init__(self, chartType, ignoreMultiNames=False):
        self.chartType = chartType
        print("chartArtistAlbumData({0})".format(chartType))
        self.dclass = {"Billboard": billboardData(), "BillboardYE": billboardYE(), "Top40": top40Data(), "Spotify": spotifyData()}
        if self.chartType not in self.dclass.keys():
            raise ValueError("ChartType {0} is not allowed".format(self.chartType))
            

        self.ignoreMultiNames = ignoreMultiNames
        self.mularts  = multiartist(cutoff=0.9, discdata=None, exact=False)
        multinames = getFile("../multiartist/knownMultiArtists.yaml")  
        self.mularts.setKnownMultiDelimArtists(multinames)
        print("  Assigning {0} known multi-name artists".format(len(multinames)))
            

        self.setRenameDB("main")
        self.setMultiRenameDB("multi")
        
        self.artistAlbumData = None
        self.albumsData      = {}
        self.setArtistAlbumData()
        
        self.fullArtistAlbumData   = None
        self.singleArtistAlbumData = None
        self.manyArtistAlbumData   = None
        
        
    def getArtistAlbumData(self):
        return self.singleArtistAlbumData, self.manyArtistAlbumData

    def getSingleArtistAlbumData(self):
        return self.singleArtistAlbumData
    
    def getManyArtistAlbumData(self):
        return self.manyArtistAlbumData
    
    def getFullArtistAlbumData(self):
        return self.fullArtistAlbumData
    
    def getTypeArtistAlbumData(self, mType):
        retval = {"Single": self.getSingleArtistAlbumData(),
                  "Many":   self.getManyArtistAlbumData(),
                  "Full":   self.getFullArtistAlbumData()}
        return retval[mType]
    
    def getIndivArtistAlbumData(self, artistName, mType):
        try:
            return self.getTypeArtistAlbumData(mType)[artistName]
        except:
            raise ValueError("Could not return album data for artist {0}".format(artistName))
        
        
    def setRenameDB(self, renameName):
        try:
            self.renameDB = masterArtistNameDB(renameName, init=False)
        except:
            self.renameDB = None
        
        
    def setMultiRenameDB(self, renameName):
        try:
            self.multirenameDB = masterArtistNameDB(renameName, init=False)
        except:
            self.multirenameDB = None


            
    ################################################################################################
    ## Create Artist Data
    ################################################################################################    
    def setArtistAlbumData(self):
        rawArtistAlbumData    = getFile(self.dclass[self.chartType].getArtistAlbumDataFilename())
        nRenamed      = 0
        nRenamedMulti = 0
        fixedArtistAlbumData = {}
        print("There are {0} unique artists in artist albums data".format(len(rawArtistAlbumData)))
        for artistName,artistAlbums in rawArtistAlbumData.items():
            
            ## Test for rename
            renamedArtistName = artistName
            if self.renameDB is not None:
                tmpName = self.renameDB.renamed(renamedArtistName)
                if tmpName != renamedArtistName:
                    nRenamed += 1
                renamedArtistName = tmpName
            
            ## Test for multi rename
            #renamedArtistName = artistName
            if self.multirenameDB is not None:
                tmpName = self.multirenameDB.renamed(renamedArtistName)
                if tmpName != renamedArtistName:
                    nRenamedMulti += 1
                renamedArtistName = tmpName
                
            if fixedArtistAlbumData.get(renamedArtistName) is None:
                fixedArtistAlbumData[renamedArtistName] = []
            fixedArtistAlbumData[renamedArtistName] += artistAlbums
        print("There are {0} newly unique artists in artist albums data".format(len(fixedArtistAlbumData)))
        print("Renamed {0} artists".format(nRenamed))
        print("Renamed {0} artists (multi)".format(nRenamedMulti))
        self.artistAlbumData = fixedArtistAlbumData
                
    def getArtistData(self, artist):
        return self.artistAlbumData.get(artist)
        

        
    ################################################################################################
    ## Create Indiv Album Lookup Data
    ################################################################################################    
    def setAlbumsLookupData(self):
        self.albumsData = {}
        for artistName, artistAlbums in self.artistAlbumData.items():
            for artistAlbum in artistAlbums:
                if self.albumsData.get(artistAlbum) is None:
                    self.albumsData[artistAlbum] = []
                self.albumsData[artistAlbum].append(artistName)
                
    def getAlbumsData(self, album):
        return self.albumsData.get(album)
         
        
        
    ################################################################################################
    ## Create Indiv Artist Data
    ################################################################################################    
    def createIndivArtistAlbumData(self):
        if self.artistAlbumData is None:
            raise ValueError("Artist Album Data is not set!")

            
        self.setAlbumsLookupData()
        

        print("There are {0: <6} unique artist entries in the artist albums data".format(len(self.artistAlbumData)))
        if self.ignoreMultiNames is True:
            singleArtistAlbumData     = {artistName: artistAlbums for artistName,artistAlbums in self.artistAlbumData.items() if len(self.mularts.getArtistNames(artistName)) >= 1}
        else:
            singleArtistAlbumData     = {artistName: artistAlbums for artistName,artistAlbums in self.artistAlbumData.items() if len(self.mularts.getArtistNames(artistName)) == 1}
        self.singleArtists        = {artistName: True for artistName in singleArtistAlbumData.keys()}
        manyArtistAlbumData       = {}

        print("There are {0: <6} single artist entries in the artist albums data".format(len(singleArtistAlbumData)))


        manyArtists       = {artist: self.mularts.getArtistNames(artist) for artist in self.artistAlbumData.keys() if singleArtistAlbumData.get(artist) is None}
        self.manyArtists  = manyArtists

        print("There are {0: <6} multi artist entries in the artist albums data".format(len(manyArtists)))

        nRenamed = 0
        for manyartist,artists in manyArtists.items():
            manyArtistAlbums = self.artistAlbumData[manyartist]
            for artistName in artists:

                ## Test for rename
                renamedArtistName = artistName
                if self.renameDB is not None:
                    tmpName = self.renameDB.renamed(renamedArtistName)
                    if tmpName != renamedArtistName:
                        nRenamed += 1
                    renamedArtistName = tmpName
                artistName = renamedArtistName
                
                if singleArtistAlbumData.get(artistName) is not None:
                    singleArtistAlbumData[artistName] += manyArtistAlbums
                else:
                    if manyArtistAlbumData.get(artistName) is not None:
                        manyArtistAlbumData[artistName] += manyArtistAlbums
                    else:
                        manyArtistAlbumData[artistName] = manyArtistAlbums

        print("Renamed {0} multi artists".format(nRenamed))
        print("There are {0: <6} solo artist entries in the artist albums data".format(len(singleArtistAlbumData)))
        print("There are {0: <6} many artist entries in the artist albums data".format(len(manyArtistAlbumData)))
        
        self.singleArtistAlbumData = singleArtistAlbumData
        self.manyArtistAlbumData   = manyArtistAlbumData
        self.fullArtistAlbumData   = res = {**self.singleArtistAlbumData, **self.manyArtistAlbumData}
        print("There are {0: <6} full artist entries in the artist albums data".format(len(self.fullArtistAlbumData)))
        self.fullArtists = list(self.fullArtistAlbumData.keys())