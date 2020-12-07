from billboardCharts import billboardCharts
from fileUtils import getBasename, getDirname, getBaseFilename
from timeUtils import clock, elapsed
from webUtils import getHTML, getWebData
from timeUtils import getDateTime, isDate
from listUtils import getFlatList
from ioUtils import saveJoblib, loadJoblib, saveFile, getFile
from os.path import join
from searchUtils import findExt
import urllib
from time import sleep
from collections import Counter
from artistIgnores import getArtistIgnores


class billboardData:
    def __init__(self, minYear=None, maxYear=None, country=None, debug=False):
        debug=False    
        
        self.basedir  = "/Volumes/Piggy/Charts/"
        self.basename = "Billboard"
        
        self.bc = billboardCharts()
        self.charts = []
        self.files = []
        self.findFiles()
            
        self.minYear   = minYear
        self.maxYear   = maxYear
        
        self.artistRenames   = {}
        self.dbRenames       = {}

        self.chartData       = {}
        self.fullChartData   = {}
        self.artistAlbumData = {}
        
        
    def getFullChartDataFilename(self):
        ifile="current{0}FullChartArtistAlbumData.p".format(self.basename)
        return ifile

    def getFullChartData(self):
        return getFile(self.getFullChartDataFilename())
        
    def saveFullChartData(self):
        print("Saving {0} Full Artist Data".format(len(self.fullChartData)))
        saveFile(idata=self.fullChartData, ifile=self.getFullChartDataFilename(), debug=True)        
        
        
    def getArtistAlbumDataFilename(self):
        ifile="current{0}ArtistAlbumData.p".format(self.basename)
        return ifile
    
    def getArtistAlbumData(self):
        return getFile(self.getArtistAlbumDataFilename())
        
    def saveArtistAlbumData(self):
        print("Saving {0} Artist Album Data to {1}".format(len(self.artistAlbumData), self.getArtistAlbumDataFilename()))
        saveFile(idata=self.artistAlbumData, ifile=self.getArtistAlbumDataFilename(), debug=True)

        
        
    def setRenames(self, artistRenames):
        self.artistRenames = artistRenames  
        
    def setDBRenames(self, dbRenames):
        self.dbRenames = dbRenames 
        
    def getArtistAlbumData(self):
        return self.artistAlbumData
    
    def getFullChartData(self):
        return self.fullChartData
    
    def setChartUsage(self, name=None, rank=None):
        #charts = ['adult', 'alternative', 'folkblue', 'christian', 'countryMusic', 'electronic', 'hot', 'top', 'rnb', 'rock',
        #          'canadian', 'latin', 'mexican', 'world', 'holiday', 'classical', 'jazz', 'comedy', 'newage', 'general',
        #          'kids', 'twitter', 'vinyl', 'rare', 'soundtrack']
        
        if rank is not None:
            if isinstance(rank, list):
                for item in rank:
                    self.charts += self.bc.getChartsByRank(item)
            elif isinstance(rank, int):
                self.charts += self.bc.getChartsByRank(rank)
        elif name is not None:
            self.charts += self.bc.getCharts(name)
        else:
            self.charts = self.bc.getCharts(None)
        if name is None:
            name = "None"
        print("  Using Charts ({0}): {1}".format(name, self.charts))
        
    
                
    def setArtistAlbumData(self):
        self.artistAlbumData = {artist: list(artistData["Songs"].keys()) + list(artistData["Albums"].keys()) for artist,artistData in self.fullChartData.items()}
        
    def findFiles(self):
        savedir = join(self.basedir, "data", "billboard", "results")
        self.files   = findExt(savedir, ext='.p')         
        print("Found {0} files.".format(len(self.files)))

    
    def setFullChartData(self):        
        renameStats  = Counter()
        chartCounter = Counter()
        
        if len(self.files) == 0:
            raise ValueError("There are no files. Something is wrong...")
        
        for ifile in self.files:
            fdata = getFile(ifile)
            for chartName, cnameResults in fdata.items():
                if chartName not in self.charts:
                    continue
                
                for date, dResults in cnameResults.items():
                    if self.minYear is not None:
                        if getDateTime(date).year < int(self.minYear):
                            continue
                    if self.maxYear is not None:
                        if getDateTime(date).year > int(self.maxYear):
                            continue
                    stryear = getDateTime(date).year

                    artist = dResults["Artist"]

                    renamedArtist = artist
                    for testArtist in self.artistRenames.keys():
                        if artist.find(testArtist) != -1:
                            tmp = renamedArtist
                            renamedArtist = renamedArtist.replace(testArtist, self.artistRenames.get(testArtist))
                            #print("{0}  <---- From ---- {1}".format(renamedArtist, tmp))
                            renameStats[renamedArtist] += 1
                            artist = renamedArtist 
                    
                    if self.dbRenames.get(artist) is not None:
                        renamedArtist = self.dbRenames[artist]
                        renameStats[renamedArtist] += 1
                        artist = renamedArtist  

                    ignoreStatus = getArtistIgnores(artist)
                    if ignoreStatus is False:
                        continue


                    chartCounter[chartName] += 1

                    album  = dResults["Name"]

                    if self.chartData.get(artist) is None:
                        self.chartData[artist] = Counter()
                    self.chartData[artist][album] += 1
                    
                    if self.fullChartData.get(artist) is None:
                        self.fullChartData[artist] = {"Songs": {}, "Albums": {}}
                    if chartName.endswith("Albums"):
                        key = "Albums"
                    else:
                        key = "Songs"
                    if self.fullChartData[artist][key].get(album) is None:
                        self.fullChartData[artist][key][album] = {}
                    if self.fullChartData[artist][key][album].get(chartName) is None:
                        self.fullChartData[artist][key][album][chartName] = {}
                    self.fullChartData[artist][key][album][chartName][date] = 0
                #print("{0: <40}{1}".format("{0}-{1}".format(chartName,stryear),len(self.fullChartData)))