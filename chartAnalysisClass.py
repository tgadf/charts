from ioUtils import getFile, saveFile
from fsUtils import isFile
from multiArtist import multiartist
from myMusicDBMap import myMusicDBMap
from matchChartMusic import matchChartMusic
from artistIgnores import getArtistIgnores
from pandas import DataFrame, Series

from multiprocessing import Pool    
from time import sleep
from copy import deepcopy


class matchedChartArtistsClass:
    def __init__(self, chartType, debug=False):
        self.chartType = chartType
        self.debug = debug
        
        self.savename = "matched{0}ChartArtists.p".format(self.chartType)
        self.matchedChartResults = self.getMatchedChartArtists(init=False, force=True)
        
    
    def saveMatchedChartArtists(self, matchedChartResults=None):
        if matchedChartResults is None:
            matchedChartResults = self.matchedChartResults
        print("\tSaving {0} artists to {1}".format(len(matchedChartResults), self.savename))
        saveFile(idata=matchedChartResults, ifile=self.savename, debug=True)


    def getMatchedChartArtists(self, init=False, force=False):
        if init is True:
            return {}
        if force is False:
            return self.matchedChartResults
        
        if isFile(self.savename):
            print("\tLoading Previously Matched Artists From {0}".format(self.savename))
            self.matchedChartResults = getFile(ifile=self.savename, debug=True)
        else:
            print("\tReturning Empty Matched Artists")
            self.matchedChartResults = {}
        return self.matchedChartResults
    

class artistAlbumDataClass:
    def __init__(self, chartType, debug=False):
        self.chartType = chartType
        self.debug = debug
        
        self.savename = "current{0}ArtistAlbumData.p".format(self.chartType)
        self.artistAlbumData = self.getArtistAlbumData(init=False, force=True)
        
    
    def saveArtistAlbumData(self):
        print("\tSaving {0} artists to {1}".format(len(self.artistAlbumData), self.savename))
        saveFile(idata=self.artistAlbumData, ifile=self.savename, debug=True)


    def getArtistAlbumData(self, init=False, force=False):
        if init is True:
            return {}
        if force is False:
            return self.artistAlbumData
        
        print("\tLoading Artist Albums Data From {0}".format(self.savename))
        self.artistAlbumData = getFile(ifile=self.savename, debug=True)
        return self.artistAlbumData
    

class fullChartArtistAlbumDataClass:
    def __init__(self, chartType, debug=False):
        self.chartType = chartType
        self.debug = debug
        
        self.savename = "current{0}FullChartArtistAlbumData.p".format(self.chartType)
        self.fullChartData = self.getFullChartData(init=False, force=True)
        
    
    def saveFullChartData(self):
        print("\tSaving {0} artists to {1}".format(len(self.fullChartData), self.savename))
        saveFile(idata=self.fullChartData, ifile=self.savename, debug=True)


    def getFullChartData(self, init=False, force=False):
        if init is True:
            return {}
        if force is False:
            return self.fullChartData
        
        print("\tLoading Full Artist Chart Data From {0}".format(self.savename))
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
    def __init__(self, chartType, init=False, full=False, debug=False):
        self.debug = debug
        
        self.mdb     = None
        self.mularts = None
        self.mcm     = None
        
        self.chartType = chartType
        self.fullDB    = False
        
        if full is False:
            self.setMA()
            self.setMDB(full=full)
            self.setMCM(full=False, mdb=self.mdb)
        
        self.mr  = masterRenameClass()
        self.artistRenames = self.mr.getArtistRenames()
        
        self.init = False

        self.allArtists       = None
        self.singleArtists    = None
        self.manyArtists      = None

        self.unMatchedSingleArtists     = None
        self.singleArtistAlbums         = None
        self.unMatchedSingleManyArtists = None
        self.manySingleArtistAlbums     = None
        
        self.matchedSingleArtists       = []
        self.unMatchedSingleArtists     = []
        self.matchedSingleManyArtists   = []
        self.unMatchedSingleManyArtists = []
        
        
        ### Artist Album Data     
        print("-"*50,"Getting Artist Album Data","-"*50)
        self.aad             = artistAlbumDataClass(self.chartType)
        self.artistAlbumData = self.aad.getArtistAlbumData()
        print("-"*125)
        print("\n"*2)

        ### Full Chart Data
        print("-"*50,"Getting Full Chart Artist Album Data","-"*50)
        self.fcd           = fullChartArtistAlbumDataClass(self.chartType)
        self.fullChartData = self.fcd.getFullChartData()
        print("-"*125)
        print("\n"*2)
        
        ### Matched Chart Data
        print("-"*50,"Getting Matched Chart Artist Album Data","-"*50)
        self.mca                 = matchedChartArtistsClass(self.chartType)
        self.matchedChartResults = self.mca.getMatchedChartArtists(init=init)
        print("-"*125)
        print("\n"*2)
        
        
    def loadPreviouslyMatchedChartArtists(self, init=False, split=True):
        if self.mca is not None:
            print("-"*50,"Loading Previously Matched Chart Artists","-"*50)
            self.matchedChartResults = self.mca.getMatchedChartArtists(init=init)
            self.setChartArtists(split=split)
            self.findArtistsMatchedStatus()
            print("-"*125)
            print("\n"*2)

        

    def getArtistAlbumSearchPairs(self, atype, maxCounts=None):
        if atype.upper() == "ALL":
            return dict(zip([self.allArtists, None]))
        elif atype.upper() == "SINGLE":
            #return dict(zip([self.unMatchedSingleArtists, self.singleArtistAlbums]))
            if maxCounts is None:
                return [self.unMatchedSingleArtists, self.singleArtistAlbums]
            else:
                unMatchedSingleArtists      = self.unMatchedSingleArtists[:maxCounts]
                unMatchedSingleArtistAlbums = {k: v for k,v in self.singleArtistAlbums.items() if k in unMatchedSingleArtists}
                return [unMatchedSingleArtists, unMatchedSingleArtistAlbums]
        elif atype.upper() == "MANY":
            if maxCounts is None:
                return [self.unMatchedSingleManyArtists, self.manySingleArtistAlbums]
            return [self.unMatchedSingleManyArtists, self.manySingleArtistAlbums]
            #return dict(zip([self.unMatchedSingleManyArtists, self.manySingleArtistAlbums]))
        else:
            raise ValueError("Atype must be [All, Single, Many")
        return dict(zip([None,None]))
        
        

            
    def isFullDB(self):
        return self.fullDB
    
    def setFull(self, mdb, mcm):        
        print("-"*50,"setFull()","-"*50)
        self.mdb = mdb
        self.mcm = mcm
        self.setMA()
        print("-"*125)
        print("")
        
    
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
    
    
    
    
    ################################################################################################
    # Split Single/Many Artist Data
    ################################################################################################
    def splitSingleManyArtistsData(self, artists, split=True):
        if not isinstance(artists, list):
            raise ValueError("Artists must be a list!")
        
        if split is True:
            manySingleArtists = [artist for artist in artists if len(self.mularts.getArtistNames(artist)) > 1]
            manyArtists       = {artist: self.mularts.getArtistNames(artist) for artist in manySingleArtists}
            singleArtists     = [artist for artist in artists if len(self.mularts.getArtistNames(artist)) == 1]
        else:
            manyArtists       = {}
            singleArtists     = artists
            
        return {"Single": singleArtists, "Many": manyArtists}
        
    
    ################################################################################################
    # Load Chart Data
    ################################################################################################
    def setChartArtists(self, split=True):
        print("-"*50,"setChartArtists()","-"*50)
        allArtists      = list(self.artistAlbumData.keys())
        print("   There are {0: <6} artist entries".format(len(allArtists)))
        
        retval = self.splitSingleManyArtistsData(allArtists, split)
        singleArtists = retval["Single"]
        print("   There are {0: <6} single artist entries".format(len(singleArtists)))
        manyArtists   = retval["Many"]
        print("   There are {0: <6} many artist entries".format(len(manyArtists)))

        self.allArtists       = allArtists        
        self.singleArtists    = singleArtists
        self.manyArtists      = manyArtists
        
        print("-"*125)
        print("\n"*2)
        
    
    ################################################################################################
    # Load Matched Data
    ################################################################################################
    def findArtistsMatchedStatus(self, init=False):
        print("  ","="*50,"findArtistsMatchedStatus(init={0})".format(init),"="*50)
        self.findSingleArtistsMatchedStatus()
        self.findManyArtistsMatchedStatus()
        
        print("-"*125)
        print("\n"*2)
        
        
    def isMatchedArtist(self, artistName):
        matchVal = self.matchedChartResults.get(artistName)
        if matchVal is None:
            return False
        else:
            if isinstance(matchVal, dict):
                #print("isMatchedArtist:",artistName,matchVal)
                try:
                    result = Series(matchVal).nunique() > 0
                except:
                    result = False
                return result
            else:
                raise ValueError("Dictionary match value for artistName {0} is a {1}".format(artistName, type(matchVal)))
            
        
            
    def findSingleArtistsMatchedStatus(self, singleArtists=None):
        print("\t","="*50,"findSingleArtistsMatchedStatus()","="*50)
        print("\t\tThere are {0: <6} single artists (to be matched)".format(len(self.singleArtists)))

        singleArtistStatus     = {singleArtist: self.isMatchedArtist(singleArtist) for singleArtist in self.singleArtists}
        singleArtistAlbums     = {singleArtist: self.artistAlbumData[singleArtist] for singleArtist in self.singleArtists}        
        
        matchedSingleArtists   = [singleArtist for singleArtist,isMatched in singleArtistStatus.items() if isMatched is True]
        unMatchedSingleArtists = [singleArtist for singleArtist,isMatched in singleArtistStatus.items() if isMatched is False]
                
        self.singleArtistAlbums     = singleArtistAlbums
        self.matchedSingleArtists   = matchedSingleArtists
        self.unMatchedSingleArtists = unMatchedSingleArtists
        self.summarySingleArtists(full=False)


        
    def findManyArtistsMatchedStatus(self, manyArtists=None):
        print("\t","="*50,"findManyArtistsMatchedStatus()","="*50)
        if manyArtists is None:
            manyArtists = self.manyArtists
        print("\t\tThere are {0: <6} many artists (to be matched)".format(len(manyArtists)))
        if self.artistAlbumData is None:
            raise ValueError("Need Artist Album Data To Determine Matched Status")

        manySingleArtistStatus   = {}
        manySingleArtistAlbums   = {}
        reverseManySingleArtists = {}
        for manyArtist, manySingleArtistValues in manyArtists.items():
            for manySingleArtist in manySingleArtistValues:
                if len(manySingleArtist) == 0:
                    continue
                renamedManySingleArtist = self.artistRenames.get(manySingleArtist)
                if renamedManySingleArtist is not None:
                    #print("\t{0}  <---- From ---- {1}".format(renamedManySingleArtist, manySingleArtist))
                    manySingleArtist = renamedManySingleArtist

                    
                if reverseManySingleArtists.get(manySingleArtist) is None:
                    reverseManySingleArtists[manySingleArtist] = []
                reverseManySingleArtists[manySingleArtist].append(manyArtist)
                
                if self.singleArtistAlbums.get(manySingleArtist) is not None:
                    self.singleArtistAlbums[manySingleArtist] += self.artistAlbumData[manyArtist]
                else:
                    if manySingleArtistStatus.get(manySingleArtist) is None:
                        manySingleArtistStatus[manySingleArtist] = self.isMatchedArtist(manySingleArtist)
                        manySingleArtistAlbums[manySingleArtist] = []
                    manySingleArtistAlbums[manySingleArtist] += self.artistAlbumData[manyArtist]

        matchedSingleManyArtists   = [singleArtist for singleArtist,isMatched in manySingleArtistStatus.items() if isMatched is True]
        unMatchedSingleManyArtists = [singleArtist for singleArtist,isMatched in manySingleArtistStatus.items() if isMatched is False]

        self.manySingleArtistStatus     = manySingleArtistStatus
        self.manySingleArtistAlbums     = manySingleArtistAlbums
        self.reverseManySingleArtists   = reverseManySingleArtists
        self.matchedSingleManyArtists   = matchedSingleManyArtists
        self.unMatchedSingleManyArtists = unMatchedSingleManyArtists
        self.summaryManySingleArtists(full=False)
        
        


        
    #########################################################################################################
    ## Update After Matching
    #########################################################################################################
    def setMatchedChartArtists(self, matchedChartResults=None):
        if matchedChartResults is None:
            self.matchedChartResults = self.mca.getMatchedChartArtists()
        else:
            self.matchedChartResults = matchedChartResults
        print("\tsetMatchedChartArtists -> {0}".format(len(self.matchedChartResults)))
        
    
    def saveMatchedChartArtists(self):
        self.mca.saveMatchedChartArtists(self.matchedChartResults)
        
    
    def updateMatchChartResults(self, latestResults, force=False, debug=False):
        print("="*50,"updateMatchChartResults(latestResults)","="*50)
        
        nAdded=0
        for latestArtist,latestArtistResults in DataFrame(latestResults).to_dict().items():
            matches = sum([True for x in latestArtistResults.values() if x is not None])
            if matches == 0:
                if force is False:
                    continue
            if self.matchedChartResults.get(latestArtist) is None:
                pass
                update = True
                nAdded += 1
                #print("   Adding artist {0}".format(latestArtist))
                self.matchedChartResults[latestArtist] = latestArtistResults
            else:
                for db,dbID in latestArtistResults.items():
                    if dbID is not None:
                        if self.matchedChartResults[latestArtist].get(db) is None:
                            pass
                            update = True
                            print(latestArtist)
                            print("      Setting {0} ID to {1}".format(db,dbID))
                            self.matchedChartResults[latestArtist][db] = str(dbID)
                        else:
                            if str(self.matchedChartResults[latestArtist][db]) != str(dbID):
                                raise ValueError("Error with db {0} for artist {1}, possibles [{2},{3}]".format(db, latestArtist, dbID, self.matchedChartResults[latestArtist][db]))

        print("Added {0} new artists to the chart results".format(nAdded))
        #self.mca.saveMatchedChartArtists(self.matchedChartResults)
        self.findArtistsMatchedStatus()
        
        
        
        
        
    #########################################################################################################
    ## Summary
    #########################################################################################################
    def summary(self, full=False):
        print("="*50,"Summary()","="*50)
        self.summarySingleArtists(full)
        print("-"*100)
        self.summaryManySingleArtists(full)
        print("="*100)
        print("\n")

        
    #########################################################################################################
    ## Summary (Single Artists)
    #########################################################################################################
    def summarySingleArtists(self, full=False):
        print("\t","="*30,"Single Artists")
        print("\t\tThere are {0: <6} single Artists".format(len(self.singleArtists)))
        print("\t\tThere are {0: <6} single Artist Albums".format(len(self.singleArtistAlbums)))
        print("\t\tThere are {0: <6} matched Artists".format(len(self.matchedSingleArtists)))
        print("\t\tThere are {0: <6} unMatched Artists".format(len(self.unMatchedSingleArtists)))
        if full is True:
            for i,artist in enumerate(self.unMatchedSingleArtists):
                print(i,'\t',artist)
                print("\t---> ",self.singleArtistAlbums[artist])
            print("="*150)

        
    #########################################################################################################
    ## Summary (Many Artists)
    #########################################################################################################
    def summaryManySingleArtists(self, full=False):
        print("\t","="*30,"Many Single Artists")
        print("\t\tThere are {0: <6} many Artists".format(len(self.manyArtists)))
        print("\t\tThere are {0: <6} many single Artists".format(len(self.manySingleArtistStatus)))
        print("\t\tThere are {0: <6} matched many single Artists".format(len(self.matchedSingleManyArtists)))
        print("\t\tThere are {0: <6} unMatched many single Artists".format(len(self.unMatchedSingleManyArtists)))
        if full is True:
            for i,artist in enumerate(self.unMatchedSingleManyArtists):
                print(i,'\t',artist)
                print("\t",self.manySingleArtistAlbums[artist])
            print("="*150)
        
        
    def showMatched(self):
        self.summary(full=True)