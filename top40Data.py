from timeUtils import getDateTime, isDate
from fileUtils import getBaseFilename
from listUtils import isIn
from collections import Counter
from os.path import join
from ioUtils import getFile, saveFile
from searchUtils import findExt

from artistIgnores import getArtistIgnores
from top40Charts import top40Charts
from top40 import top40chart


class top40Data:
    def __init__(self, minYear=None, maxYear=None, debug=False):
        self.debug  = False
        
        self.basedir  = "/Volumes/Piggy/Charts/"
        self.basename = "Top40"
                
        self.tc     = top40Charts()
        self.charts = []
        
        self.minYear   = minYear
        self.maxYear   = maxYear
        
        self.dbRenames       = None
        self.multirenameDB   = None

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
        
    def getArtists(self):
        return list(self.artistAlbumData.keys())
        
        
        
    def setRenames(self, artistRenames):
        self.artistRenames = artistRenames
        
    def setDBRenames(self, dbRenames):
        self.dbRenames = dbRenames
        
    def setMultiDBRenames(self, multirenameDB):
        self.multirenameDB = multirenameDB
        
        
    def setArtistAlbumData(self):
        self.artistAlbumData = {artist: list(artistData["Songs"].keys()) + list(artistData["Albums"].keys()) for artist,artistData in self.fullChartData.items()}
        
        
    
    def setChartUsage(self, name=None, rank=None):
        if rank is not None:
            if isinstance(rank, list):
                for item in rank:
                    self.charts += self.tc.getChartsByRank(item)
            elif isinstance(rank, int):
                self.charts += self.tc.getChartsByRank(rank)
        elif name is not None:
            self.charts += self.tc.getCharts(name)
        else:
            self.charts = self.tc.getCharts(None)
        if name is None:
            name = "None"
        print("  Using Charts ({0}): {1}".format(name, self.charts))
        
        
    def findFiles(self):
        savedir = join(self.basedir, "data", "top40")
        self.files   = findExt(savedir, ext='.p')         
        print("Found {0} files.".format(len(self.files)))
        
        
        
    def setFullChartData(self):   
        dbRenameStats     = 0    
        multiRenameStats  = 0

        fullChartData = {}

        
        self.findFiles()
        if len(self.files) == 0:
            raise ValueError("There are no files. Something is wrong...")
        self.files = {getBaseFilename(x).replace("/", " "): x for x in self.files}
        
        for chartName, ifile in self.files.items():
            if chartName not in self.charts:
                continue
            print("==> {0: <40}".format(chartName), end="\t")
            #t40chart = top40chart(chartID, chartName, chartURL)
            chartResults = getFile(ifile)

            for date, values in chartResults.items():
                if self.minYear is not None:
                    if getDateTime(date).year < int(self.minYear):
                        continue
                if self.maxYear is not None:
                    if getDateTime(date).year > int(self.maxYear):
                        continue

                        
                for i,item in enumerate(values):
                    artistName = item["Artist"]
                    

                    ## Test for rename
                    renamedArtistName = artistName
                    if self.dbRenames is not None:
                        tmpName = self.dbRenames.renamed(renamedArtistName)
                        if tmpName != renamedArtistName:
                            dbRenameStats += 1
                        renamedArtistName = tmpName

                    ## Test for multi rename
                    #renamedArtistName = artistName
                    if self.multirenameDB is not None:
                        tmpName = self.multirenameDB.renamed(renamedArtistName)
                        if tmpName != renamedArtistName:
                            multiRenameStats += 1
                        renamedArtistName = tmpName

                    artist = renamedArtistName

                    renamedArtistName = artist
                    renamedArtistName = renamedArtistName.replace("\r", "").strip()
                    if renamedArtistName != artist:
                        dbRenameStats += 1
                    artist = renamedArtistName

                    ignoreStatus = getArtistIgnores(artist)
                    if ignoreStatus is False:
                        continue
                        
                                            
                    album  = item["Album"]
                    if album in ["Soundtrack"]:
                        continue

                    if fullChartData.get(artist) is None:
                        fullChartData[artist] = {"Songs": {}, "Albums": {}}
                    if chartName.endswith("Albums"):
                        key = "Albums"
                    else:
                        key = "Songs"
                    if fullChartData[artist][key].get(album) is None:
                        fullChartData[artist][key][album] = {}
                    if fullChartData[artist][key][album].get(chartName) is None:
                        fullChartData[artist][key][album][chartName] = {}
                    fullChartData[artist][key][album][chartName][date] = i
            print(len(fullChartData))
        self.fullChartData = fullChartData
                
        print("Renamed {0} single artists".format(dbRenameStats))
        print("Renamed {0} multi artists".format(multiRenameStats))