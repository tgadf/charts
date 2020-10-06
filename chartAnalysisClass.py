from ioUtils import getFile, saveFile
from multiArtist import multiartist
from myMusicDBMap import myMusicDBMap
from matchChartMusic import matchChartMusic
from artistIgnores import getArtistIgnores
from pandas import DataFrame

from multiprocessing import Pool    
from time import sleep
from copy import deepcopy


class matchedChartArtistsClass:
    def __init__(self, chartType, debug=False):
        self.chartType = chartType
        self.debug = debug
        
        self.savename = "matched{0}ChartArtists.p".format(self.chartType)
        self.matchedChartResults = getFile(ifile=self.savename, debug=True)
        
    
    def saveMatchedChartArtists(self, matchedChartResults=None):
        if matchedChartResults is None:
            matchedChartResults = self.matchedChartResults
        print("Saving {0} artists to {1}".format(len(matchedChartResults), self.savename))
        saveFile(idata=matchedChartResults, ifile=self.savename, debug=True)


    def getMatchedChartArtists(self, init=False):
        if init is True:
            return {}
        self.matchedChartResults = getFile(ifile=self.savename, debug=True)
        return self.matchedChartResults
    

class artistAlbumDataClass:
    def __init__(self, chartType, debug=False):
        self.chartType = chartType
        self.debug = debug
        
        self.savename = "current{0}ArtistAlbumData.p".format(self.chartType)
        self.artistAlbumData = getFile(ifile=self.savename, debug=True)
        
    
    def saveArtistAlbumData(self):
        print("Saving {0} artists to {1}".format(len(self.artistAlbumData), self.savename))
        saveFile(idata=self.artistAlbumData, ifile=self.savename, debug=True)


    def getArtistAlbumData(self, init=False):
        if init is True:
            return {}
        self.artistAlbumData = getFile(ifile=self.savename, debug=True)
        return self.artistAlbumData
    

class fullChartArtistAlbumDataClass:
    def __init__(self, chartType, debug=False):
        self.chartType = chartType
        self.debug = debug
        
        self.savename = "current{0}FullChartArtistAlbumData.p".format(self.chartType)
        self.fullChartData = getFile(ifile=self.savename, debug=True)
        
    
    def saveFullChartData(self):
        print("Saving {0} artists to {1}".format(len(self.fullChartData), self.savename))
        saveFile(idata=self.fullChartData, ifile=self.savename, debug=True)


    def getFullChartData(self, init=False):
        if init is True:
            return {}
        self.fullChartData = getFile(ifile=self.savename, debug=True)
        return self.fullChartData


class masterRenameClass:
    def __init__(self, debug=False):
        self.debug = False
        self.savename = "masterRename.yaml"
        self.artistRenames = getFile(self.savename, debug=True)

    def getArtistRenames(self):
        return self.artistRenames

    def saveArtistRenames(self):
        saveFile(idata=self.artistRenames, ifile=self.savename, debug=True)

class chartAnalysisClass:
    def __init__(self, full=False, debug=False):
        self.debug = debug
        
        self.mdb     = None
        self.mularts = None
        self.mcm     = None
        
        self.chartType = None
        self.fullDB    = False
        
        
        self.setMA()
        self.setMDB(full=full)
        self.setMCM(full=False, mdb=self.mdb)
        
        self.aad = None
        self.fcd = None
        self.mca = None
        self.mr  = masterRenameClass()
        self.artistRenames = self.mr.getArtistRenames()
        
        self.init = False

        self.allArtists       = None
        self.singleArtists    = None
        self.manyArtists      = None
        self.manyArtistAlbums = None

        self.unMatchedSingleArtists     = None
        self.singleArtistAlbums         = None
        self.unMatchedSingleManyArtists = None
        self.manySingleArtistAlbums     = None
        
        self.matchedSingleArtists       = []
        self.unMatchedSingleArtists     = []
        self.manySingleArtists          = []
        self.matchedSingleManyArtists   = []
        self.unMatchedSingleManyArtists = []
        
        
    def setChartType(self, chartType):
        print("="*50,"setChartType(chartType={0})".format(chartType),"="*50)
        self.chartType = chartType
        if self.aad is None:
            self.aad = artistAlbumDataClass(self.chartType)
        if self.fcd is None:
            self.fcd = fullChartArtistAlbumDataClass(self.chartType)
        if self.mca is None:
            self.mca = matchedChartArtistsClass(self.chartType)

            
    def isFullDB(self):
        return self.fullDB
    
    def loadFull(self):        
        self.setMA()
        self.setMDB(full=True)
        self.setMCM(full=True, mdb=self.mdb)
        self.fullDB = True
        

    def setMDB(self, full=False):
        self.mdb = myMusicDBMap(debug=False)
        if full:
            self.mdb.getFullDBData()
            self.fullDB = True

    def setMA(self):
        multiDelimArtists=open("../multiartist/multiDelimArtists.dat").readlines()
        multiDelimArtists = [x.replace("\n", "") for x in multiDelimArtists]
        multiDelimArtists[:3]

        self.mularts  = multiartist(cutoff=0.9, discdata=None, exact=False)
        self.mularts.setKnownMultiDelimArtists(multiDelimArtists)

    def setMCM(self, full=False, mdb=None):
        if mdb is None:
            self.mdb = self.getMDB(full=full)
        self.mcm = matchChartMusic(mdb)
    
    
    
    
    
    def loadChartData(self):
        print("="*50,"loadChartData()","="*50)
        if self.aad is None:
            self.aad = artistAlbumData(self.chartType)
        artistAlbumData = self.aad.getArtistAlbumData()

        if self.fcd is None:
            self.fcd = fullChartArtistAlbumData(self.chartType)
        fullChartData = self.fcd.getFullChartData()

        
        allArtists      = list(artistAlbumData.keys())
        print("There are {0} artist album entries".format(len(allArtists)))

        manyArtists   = [artist for artist in list(artistAlbumData.keys()) if len(self.mularts.getArtistNames(artist)) > 1]
        manyArtistAlbums = {artist: {"Artists": self.mularts.getArtistNames(artist)} for artist in manyArtists}
        print("There are {0} many artist entries".format(len(manyArtists)))

        singleArtists   = [artist for artist in list(artistAlbumData.keys()) if len(self.mularts.getArtistNames(artist)) == 1]
        print("There are {0} single artist entries".format(len(singleArtists)))

        self.artistAlbumData  = artistAlbumData
        self.fullChartData    = fullChartData
        self.allArtists       = allArtists        
        self.singleArtists    = singleArtists
        self.manyArtists      = manyArtists
        self.manyArtistAlbums = manyArtistAlbums



    def loadMatchedChartData(self, init=False):
        print("="*50,"loadMatchedChartData(init={0})".format(init),"="*50)
        self.init = init
        if self.mca is None:
            self.mca = matchedChartArtists(self.chartType)
        self.matchedChartResults = self.mca.getMatchedChartArtists(init=init)
        
        self.loadSingleArtistsMatchedChartData()
        self.loadManyArtistsMatchedChartData()
        
            
    def loadSingleArtistsMatchedChartData(self):
        print("="*50,"loadSingleArtistsMatchedChartData()","="*50)
        print("There are {0} matched chart artists".format(len(self.matchedChartResults)))
        print("There are {0} single artists (to be matched)".format(len(self.singleArtists)))

        singleArtistStatus     = {singleArtist: self.matchedChartResults.get(singleArtist) is not None for singleArtist in self.singleArtists}
        singleArtistAlbums     = {}
        for singleArtist in self.singleArtists:
            singleArtistAlbums[singleArtist] = self.artistAlbumData[singleArtist]
        matchedSingleArtists   = [singleArtist for singleArtist,isMatched in singleArtistStatus.items() if isMatched is True]
        unMatchedSingleArtists = [singleArtist for singleArtist,isMatched in singleArtistStatus.items() if isMatched is False]
                
        self.singleArtistAlbums     = singleArtistAlbums
        self.matchedSingleArtists   = matchedSingleArtists
        self.unMatchedSingleArtists = unMatchedSingleArtists
        self.summarySingleArtists(full=False)


        
    def loadManyArtistsMatchedChartData(self):
        print("="*50,"loadManyArtistsMatchedChartData()","="*50)
        print("There are {0} matched chart artists".format(len(self.matchedChartResults)))
        print("There are {0} many artists (to be matched)".format(len(self.manyArtists)))

        manySingleArtists      = {manyArtist: list(self.mularts.getArtistNames(manyArtist).keys()) for manyArtist in self.manyArtists}
        manySingleArtistStatus = {}
        manySingleArtistAlbums = {}
        for manyArtist, manySingleArtistValues in manySingleArtists.items():
            for manySingleArtist in manySingleArtistValues:
                if len(manySingleArtist) == 0:
                    continue
                renamedManySingleArtist = self.artistRenames.get(manySingleArtist)
                if renamedManySingleArtist is not None:
                    print("\t{0}  <---- From ---- {1}".format(renamedManySingleArtist, manySingleArtist))
                    manySingleArtist = renamedManySingleArtist

                if self.singleArtistAlbums.get(manySingleArtist) is not None:
                    self.singleArtistAlbums[manySingleArtist] += self.artistAlbumData[manyArtist]
                else:
                    if manySingleArtistStatus.get(manySingleArtist) is None:
                        manySingleArtistStatus[manySingleArtist] = self.matchedChartResults.get(manySingleArtist) is not None
                        manySingleArtistAlbums[manySingleArtist] = []
                    manySingleArtistAlbums[manySingleArtist] += self.artistAlbumData[manyArtist]

        matchedSingleManyArtists   = [singleArtist for singleArtist,isMatched in manySingleArtistStatus.items() if isMatched is True]
        unMatchedSingleManyArtists = [singleArtist for singleArtist,isMatched in manySingleArtistStatus.items() if isMatched is False]

        self.manySingleArtists          = manySingleArtists
        self.manySingleArtistStatus     = manySingleArtistStatus
        self.manySingleArtistAlbums     = manySingleArtistAlbums
        self.matchedSingleManyArtists   = matchedSingleManyArtists
        self.unMatchedSingleManyArtists = unMatchedSingleManyArtists
        self.summaryManySingleArtists(full=False)
        
        

    def updateMatchChartResults(self, latestResults):
        print("="*50,"updateMatchChartResults(latestResults)","="*50)
        if self.mca is None:
            self.mca = matchedChartArtists(self.chartType)
        matchedChartResults = self.mca.getMatchedChartArtists(init=self.init)
        
        nAdded=0
        for latestArtist,latestArtistResults in DataFrame(latestResults).to_dict().items():
            matches = sum([True for x in latestArtistResults.values() if x is not None])
            if matches == 0:
                continue
            if matchedChartResults.get(latestArtist) is None:
                pass
                update = True
                nAdded += 1
                #print("   Adding artist {0}".format(latestArtist))
                matchedChartResults[latestArtist] = latestArtistResults
            else:
                for db,dbID in latestArtistResults.items():
                    if dbID is not None:
                        if matchedChartResults[latestArtist].get(db) is None:
                            pass
                            update = True
                            print(latestArtist)
                            print("      Setting {0} ID to {1}".format(db,dbID))
                            matchedChartResults[latestArtist][db] = str(dbID)
                        else:
                            if str(matchedChartResults[latestArtist][db]) != str(dbID):
                                raise ValueError("Error with db {0} for artist {1}, possibles [{2},{3}]".format(db, latestArtist, dbID, dbID, matchedChartResults[latestArtist][db]))

        print("Added {0} new artists to the chart results".format(nAdded))
        self.mca.saveMatchedChartArtists(matchedChartResults)
        self.loadMatchedChartData(init=False)
        
        
    def summary(self, full=False):
        print("="*50,"Summary()","="*50)
        self.summarySingleArtists(full)
        print("-"*100)
        self.summaryManySingleArtists(full)
        print("="*100)
        print("\n")



        
    def summarySingleArtists(self, full=False):
        print("="*30,"Single Artists")
        print("\tThere are {0} single Artists".format(len(self.singleArtists)))
        print("\tThere are {0} single Artist Albums".format(len(self.singleArtistAlbums)))
        print("\tThere are {0} matched Artists".format(len(self.matchedSingleArtists)))
        print("\tThere are {0} unMatched Artists".format(len(self.unMatchedSingleArtists)))
        if full is True:
            for i,artist in enumerate(self.unMatchedSingleArtists):
                print(i,'\t',artist)
                print("\t---> ",self.singleArtistAlbums[artist])
            print("="*150)

    def summaryManySingleArtists(self, full=False):
        print("="*30,"Many Single Artists")
        print("\tThere are {0} many Artists".format(len(self.manyArtists)))
        print("\tThere are {0} many single Artists".format(len(self.manySingleArtistStatus)))
        print("\tThere are {0} matched many single Artists".format(len(self.matchedSingleManyArtists)))
        print("\tThere are {0} unMatched many single Artists".format(len(self.unMatchedSingleManyArtists)))
        if full is True:
            for i,artist in enumerate(self.unMatchedSingleManyArtists):
                print(i,'\t',artist)
                print("\t",self.manySingleArtistAlbums[artist])
            print("="*150)
        
        
    def showMatched(self):
        self.summary(full=True)