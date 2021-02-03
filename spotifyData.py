from spotifyCharts import spotifyCharts
from searchUtils import findExt
from webUtils import getHTML
from timeUtils import getDateTime
from fileUtils import getBaseFilename
from fsUtils import setDir, setFile, isFile, isDir
from ioUtils import getFile, saveFile
from collections import Counter
from os.path import join
from pandas import read_csv

class spotifyData:
    def __init__(self, debug=False, minYear=1, maxYear=9999):
        
        self.basedir  = "/Volumes/Piggy/Charts/"
        self.basename  = "Spotify"
        #self.baseDir  = "/Volumes/Piggy/Charts/{0}".format(self.
        self.files     = []
        self.chartData = None
        self.sc        = spotifyCharts()

                
        self.charts = []
        self.fullChartData   = {}
        self.artistAlbumData = {}
        
        self.dbRenames        = None
        self.dbRenameStats    = 0
        self.multirenameDB    = None
        self.multiRenameStats = 0
            
        self.minYear   = minYear
        self.maxYear   = maxYear
    
    def setChartUsage(self, name=None, rank=None):
        if rank is not None:
            if isinstance(rank, list):
                for item in rank:
                    self.charts += self.sc.getChartsByRank(item)
            elif isinstance(rank, int):
                self.charts += self.sc.getChartsByRank(rank)
        elif name is not None:
            self.charts += self.sc.getCharts(name)
        else:
            self.charts = self.sc.getCharts(None)
        if name is None:
            name = "None"
        print("  Using Charts ({0}): {1}".format(name, self.charts))
        return
        
        
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

        

        

    def renameArtist(self, artistName):
        ## Test for rename
        renamedArtistName = artistName
        if self.dbRenames is not None:
            tmpName = self.dbRenames.renamed(renamedArtistName)
            if tmpName != renamedArtistName:
                self.dbRenameStats += 1
            renamedArtistName = tmpName

        ## Test for multi rename
        #renamedArtistName = artistName
        if self.multirenameDB is not None:
            tmpName = self.multirenameDB.renamed(renamedArtistName)
            if tmpName != renamedArtistName:
                self.multiRenameStats += 1
            renamedArtistName = tmpName

        artist = renamedArtistName     
        return artist
    
        
    def renameSummary(self):
        if self.dbRenameStats is not None:
            print("Renamed {0} single artists".format(self.dbRenameStats))
        if self.multiRenameStats:
            print("Renamed {0} multi artists".format(self.multiRenameStats))
            
    def ignores(self, artistName):
        if artistName in ["Original Broadway Cast Recording", "Studio Cast Recording", "The 2011 Broadway Cast Recording",
                          "Original Cast Recording", "The 2010 Cast Album", "Original London Cast Recording",
                          "The Broadway Cast Recording", "Original Broadway Cast", "The 2015 Broadway Cast Recording", 
                          "The New Broadway Cast Recording", "Cast Recording", "The Original 1985 London Cast Recording",
                          "World Premiere Cast Recording", "New Broadway Cast Recording"]:
            return True
        if artistName in ["Various Artists"]:
            return True
        return False
            

    def setDBRenames(self, dbRenames):
        self.dbRenames = dbRenames
        
    def setMultiDBRenames(self, multirenameDB):
        self.multirenameDB = multirenameDB
        

    def findFiles(self):
        savedir = join(self.basedir, "data", "spotify", "categories")
        print(savedir)
        if not isDir(savedir):
            raise ValueError("Could not find directory: {0}".format(savedir))
        self.files   = findExt(savedir, ext='.csv')
        print("Found {0} files.".format(len(self.files)))
        
    
    def parse(self):
        self.findFiles()

        data = {}
        for ifile in self.files:
            bsdata = read_csv(ifile, skiprows=1)
            
            category  = "-".join(getBaseFilename(ifile).split("-")[:3])
            date      = getBaseFilename(ifile).split("--")[1:][0]
            
            chartData = {}
            for irow,row in bsdata.iterrows():
                artist = row["Artist"]
                song   = row["Track Name"]
                rank   = row["Position"]
                url    = row["URL"]
                
                chartName = "Top200"
                if chartData.get(chartName) is None:
                    chartData[chartName] = []
                chartData[chartName].append({"Artist": artist, "Song": song, "URL": url, "Rank": rank})

            if data.get(category) is None:
                data[category] = {}
            for chartName,chartInfo in chartData.items():
                if data[category].get(chartName) is None:
                    data[category][chartName] = {}
                data[category][chartName][date] = chartInfo
            
        self.chartData = data
        
        
        
    def setArtistAlbumData(self):
        self.artistAlbumData = {artist: list(artistData["Songs"].keys()) + list(artistData["Albums"].keys()) for artist,artistData in self.fullChartData.items()}
        
        
        
    def saveChartData(self):
        for category,categoryData in self.chartData.items():
            savedir = join(self.basedir, "data", "spotify", "results")
            if not isDir(savedir):
                raise ValueError("Could not find directory: {0}".format(savedir))
            saveName = setFile(savedir, "{0}.p".format(category))
            saveFile(idata=categoryData, ifile=saveName, debug=True)
                
        
    def getSummaryFiles(self):
        saveDir = join(self.basedir, "data", "spotify", "results")
        if not isDir(saveDir):
            raise ValueError("Could not find directory: {0}".format(saveDir))
        files    = findExt(saveDir, ".p")
        print("Found {0} summary files".format(len(files)))
        return files
    
        
    def setFullChartData(self):
        files = self.getSummaryFiles()
        for ifile in files:
            category = getBaseFilename(ifile)
            if category not in self.charts:
                continue
            print("  Using {0}".format(category))
            categoryData = getFile(ifile)            
            for chartName,chartData in categoryData.items():
                for date,dateData in chartData.items():
                    dt = getDateTime(date)
                    year = dt.year
                    if True:
                        if int(year) < int(self.minYear):
                            continue
                        if int(year) > int(self.maxYear):
                            continue
                        
                    for item in dateData:
                        artistName = item["Artist"]
                        if artistName is None:
                            continue        
                        if not isinstance(artistName,str):
                            continue
                        artistName = artistName.replace("\n", "").strip()
                        artistName = self.renameArtist(artistName)
                        
                        if self.ignores(artistName) is True:
                            continue
                        
                        artistURL  = item["URL"]

                        song       = item.get("Song")
                        album      = item.get("Album")
                        rank       = item.get("Rank")
                        
                        #print(artistName,'\t',chartName,'\t\t',item,'\t\t',song,album)


                        if song is not None:
                            key = "Songs"
                            title = song.replace("\n", "").strip()
                        elif album is not None:
                            key = "Albums"
                            title = album.replace("\n", "").strip()
                        else:
                            continue
                            #print(chartName)
                            #raise ValueError("Not a song or album")
                            
                            
                        if self.fullChartData.get(artistName) is None:
                            self.fullChartData[artistName] = {"Songs": {}, "Albums": {}}
                        date = year


                        if self.fullChartData[artistName].get(key) is None:
                            self.fullChartData[artistName][key] = {}
                        if self.fullChartData[artistName][key].get(title) is None:
                            self.fullChartData[artistName][key][title] = {}
                        if self.fullChartData[artistName][key][title].get(chartName) is None:
                            self.fullChartData[artistName][key][title][chartName] = {}
                        self.fullChartData[artistName][key][title][chartName][date] = 0
                    #print("{0: <40}{1}".format("{0}-{1}".format(chartName,stryear),len(self.fullChartData)))

        self.renameSummary()