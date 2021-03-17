from searchUtils import findExt, findPatternExt
from webUtils import getHTML
from timeUtils import getDateTime
from fileUtils import getBaseFilename
from fsUtils import setDir, setFile, isFile, isDir
from ioUtils import getFile, saveFile
from collections import Counter
from os.path import join
from pandas import read_csv, DataFrame
from io import StringIO


class russiaCharts:
    def __init__(self):
        self.russia = ['russia']

        self.chartNames = self.__dict__.keys()
        
        self.chartRanks = {}
        self.chartRanks[0] = ['russia']
        
        self.countries = ["russia"]
        
    def getChartsByRank(self, rank):
        print("Using Charts For Rank {0}".format(rank))
        categories = self.chartRanks[rank]
        print("    Categories: {0}".format(categories))
        charts = []
        for chart in categories:
            print("\tChart: {0}".format(chart))
            charts += self.getCharts(chart)
        print("Using {0} Charts For Rank {1}".format(len(charts), rank))
        return charts
        
    def getCharts(self, name=None):        
        charts = []
        if name is None:
            print("  Getting All Charts")
            for chart in self.chartNames:
                charts += self.__dict__[chart]
        else:
            #print("  Getting Chart For [{0}]".format(name))
            name = name.replace("-", "_")
            #print("name = {0}".format(name))
            if name in self.__dict__.keys():
                chartList = self.__dict__[name]
                if isinstance(chartList[0], list):
                    charts += getFlatList(chartList)
                else:
                    charts += chartList
            if name == "country":
                charts += getFlatList(self.__dict__["countryMusic"])
        if len(charts) == 0:
            raise ValueError("Could not find any charts: {0}".format(self.__dict__.keys()))
        print("  Using {0} Charts".format(len(charts)))
        return charts


class russiaData:
    def __init__(self, debug=False, minYear=1, maxYear=9999):
        
        self.basedir   = "/Volumes/Piggy/Charts/"
        self.basename  = "russia"
        #self.baseDir  = "/Volumes/Piggy/Charts/{0}".format(self.
        self.files     = []
        self.chartData = None
        self.udCharts  = russiaCharts()

                
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
                    self.charts += self.udCharts.getChartsByRank(item)
            elif isinstance(rank, int):
                self.charts += self.udCharts.getChartsByRank(rank)
        elif name is not None:
            self.charts += self.udCharts.getCharts(name)
        else:
            self.charts = self.udCharts.getCharts(None)
        #if name is None:
        #    name = "None"
        print("=== ChartUsage ===")
        if name is not None:
            print("  Using Charts (Name={0}): {1}".format(name, self.charts))
        if rank is not None:
            print("  Using Charts (Rank={0}): {1}".format(rank, self.charts))
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
        savedir = join(self.basedir, "data", "russia", "categories")
        if not isDir(savedir):
            raise ValueError("Could not find directory: {0}".format(savedir))
        self.files   = findExt(savedir, ext='.p')
        print("Found {0} files.".format(len(self.files)))
    
    
    def parse(self):
        data = {}
        self.findFiles()
        for ifile in self.files:
            category  = getBaseFilename(ifile).split('_')[0]
            chartName = "_".join(getBaseFilename(ifile).split('_')[1:])
            fdata = getFile(ifile)
            if data.get(category) is None:
                data[category] = {}
            data[category][chartName] = fdata
        self.chartData = data
        self.saveChartData()


        
    def setArtistAlbumData(self):
        self.artistAlbumData = {artist: list(artistData["Songs"].keys()) + list(artistData["Albums"].keys()) for artist,artistData in self.fullChartData.items()}
        
        
    def saveChartData(self):
        for category,categoryData in self.chartData.items():
            saveDir = join(self.basedir, "data", "russia", "results")
            if not isDir(saveDir):
                raise ValueError("Could not find directory: {0}".format(savedir))
            categoryName = category.replace(" ", "_")
            categoryName = categoryName.replace("&", "_")
            categoryName = categoryName.replace("/", "_")
            saveName = setFile(saveDir, "{0}.p".format(categoryName))
            saveFile(idata=categoryData, ifile=saveName, debug=True)
                
        
    def getSummaryFiles(self):
        saveDir = join(self.basedir, "data", "russia", "results")
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
                if not isinstance(chartData, DataFrame):
                    raise ValueError("{0} is not a DataFrame".format(chartName))
                    
                date = "X"
                columns = list(chartData.columns)
                if "Album" in columns:
                    for irow,row in chartData.iterrows():
                        artistName = row["Artist"]
                        albumName  = row["Album"]
                        artistName = self.renameArtist(artistName)

                        if self.fullChartData.get(artistName) is None:
                            self.fullChartData[artistName] = {"Songs": {}, "Albums": {}}
                        key = "Albums"
                        if self.fullChartData[artistName][key].get(albumName) is None:
                            self.fullChartData[artistName][key][albumName] = {}
                        if self.fullChartData[artistName][key][albumName].get(chartName) is None:
                            self.fullChartData[artistName][key][albumName][chartName] = {}
                        self.fullChartData[artistName][key][albumName][chartName][date] = 0
                elif "Single" in columns:
                    for irow,row in chartData.iterrows():
                        artistName = row["Artist"]
                        titleName  = row["Single"]
                        artistName = self.renameArtist(artistName)

                        if self.fullChartData.get(artistName) is None:
                            self.fullChartData[artistName] = {"Songs": {}, "Albums": {}}
                        key = "Songs"
                        if self.fullChartData[artistName][key].get(titleName) is None:
                            self.fullChartData[artistName][key][titleName] = {}
                        if self.fullChartData[artistName][key][titleName].get(chartName) is None:
                            self.fullChartData[artistName][key][titleName][chartName] = {}
                        self.fullChartData[artistName][key][titleName][chartName][date] = 0
                else:
                    for irow,row in chartData.iterrows():
                        artistName = row["Artists"]
                        artistName = self.renameArtist(artistName)

                        if self.fullChartData.get(artistName) is None:
                            self.fullChartData[artistName] = {"Songs": {}, "Albums": {}}
                            
        self.renameSummary()