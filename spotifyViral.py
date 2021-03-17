from searchUtils import findExt, findPatternExt
from webUtils import getHTML
from timeUtils import getDateTime
from fileUtils import getBaseFilename
from fsUtils import setDir, setFile, isFile, isDir
from ioUtils import getFile, saveFile
from collections import Counter
from os.path import join
from pandas import read_csv
from io import StringIO


from ioUtils import getFile
from listUtils import getFlatList
from artistIgnores import getArtistIgnores

class spotifyViralCharts:
    def __init__(self):

        self.saudiarabia         = ['viral-sa-weekly']
        self.ireland             = ['viral-ie-weekly']
        self.argentina           = ['viral-ar-weekly']
        self.norway              = ['viral-no-weekly']
        self.india               = ['viral-in-weekly']
        self.morocco             = ['viral-ma-weekly']
        self.chile               = ['viral-cl-weekly']
        self.hungary             = ['viral-hu-weekly']
        self.switzerland         = ['viral-ch-weekly']
        self.russia              = ['viral-ru-weekly']
        self.luxembourg          = ['viral-lu-weekly']
        self.portugal            = ['viral-pt-weekly']
        self.bulgaria            = ['viral-bg-weekly']
        self.japan               = ['viral-jp-weekly']
        self.honduras            = ['viral-hn-weekly']
        self.sweden              = ['viral-se-weekly']
        self.vietnam             = ['viral-vn-weekly']
        self.romania             = ['viral-ro-weekly']
        self.hongkong            = ['viral-hk-weekly']
        self.ecuador             = ['viral-ec-weekly']
        self.costarica           = ['viral-cr-weekly']
        self.newzealand          = ['viral-nz-weekly']
        self.indonesia           = ['viral-id-weekly']
        self.unitedkingdom       = ['viral-gb-weekly']
        self.france              = ['viral-fr-weekly']
        self.slovakia            = ['viral-sk-weekly']
        self.peru                = ['viral-pe-weekly']
        self.panama              = ['viral-pa-weekly']
        self.lithuania           = ['viral-lt-weekly']
        self.brazil              = ['viral-br-weekly']
        self.ukraine             = ['viral-ua-weekly']
        self.greece              = ['viral-gr-weekly']
        self.italy               = ['viral-it-weekly']
        self.spain               = ['viral-es-weekly']
        self.finland             = ['viral-fi-weekly']
        self.egypt               = ['viral-eg-weekly']
        self.czechrepublic       = ['viral-cz-weekly']
        self.uraguay             = ['viral-uy-weekly']
        self.isreal              = ['viral-il-weekly']
        self.paraguay            = ['viral-py-weekly']
        self.dominicanrepublic   = ['viral-do-weekly']
        self.iceland             = ['viral-is-weekly']
        self.austria             = ['viral-at-weekly']
        self.denmark             = ['viral-dk-weekly']
        self.singapore           = ['viral-sg-weekly']
        self.nicaragua           = ['viral-ni-weekly']
        self.canada              = ['viral-ca-weekly']
        self.belgium             = ['viral-be-weekly']
        self.mexico              = ['viral-mx-weekly']
        self.turkey              = ['viral-tr-weekly']
        self.germany             = ['viral-de-weekly']
        self.colombia            = ['viral-co-weekly']
        self.taiwan              = ['viral-tw-weekly']
        self.unitedstates        = ['viral-us-weekly']
        self.unitedarabemirates  = ['viral-ae-weekly']
        self.guatemala           = ['viral-gt-weekly']
        self.poland              = ['viral-pl-weekly']
        self.elsalvador          = ['viral-sv-weekly']
        self.thailand            = ['viral-th-weekly']
        self.netherlands         = ['viral-nl-weekly']
        self.estonia             = ['viral-ee-weekly']
        self.philippines         = ['viral-ph-weekly']
        self.bolivia             = ['viral-bo-weekly']
        self.australia           = ['viral-au-weekly']
        self.malaysia            = ['viral-my-weekly']
        self.southafrica         = ['viral-za-weekly']
        self.latvia              = ['viral-lv-weekly']
        self.world               = ['viral-global-weekly']
        
        self.chartNames = self.__dict__.keys()
        
        self.chartRanks = {}
        self.chartRanks[0] = ['unitedstates', 'canada']
        self.chartRanks[1] = ['unitedkingdom', 'australia', 'ireland', 'newzealand']
        self.chartRanks[2] = ['germany', 'austria', 'switzerland']
        self.chartRanks[3] = ['italy', 'france', 'spain', 'netherlands', 'luxembourg']
        self.chartRanks[4] = ['finland', 'iceland', 'belgium', 'czechrepublic', 'hungary']
        self.chartRanks[5] = ['denmark', 'sweden', 'norway']
        self.chartRanks[6] = ['isreal', 'turkey', 'saudiarabia', 'unitedarabemirates', 'egypt', 'morocco']
        self.chartRanks[7] = ['russia', 'ukraine', 'bulgaria', 'latvia', 'estonia', 'lithuania', 'slovakia', 'romania', 'poland']
        self.chartRanks[8] = ['mexico', 'costarica', 'panama', 'dominicanrepublic', 'guatemala', 'nicaragua', 'honduras', 'elsalvador']        
        self.chartRanks[9] = ['colombia', 'argentina', 'peru', 'paraguay', 'uraguay', 'chile', 'bolivia', 'ecuador']
        self.chartRanks[10] = ['japan', 'hongkong', 'vietnam', 'taiwan', 'thailand', 'malaysia', 'singapore']
        self.chartRanks[11] = ['philippines', 'greece', 'indonesia', 'india', 'southafrica']
        self.chartRanks[12] = ['brazil', 'portugal']
        self.chartRanks[13] = ['world']
        
        
        self.countries = {'sa': 'Saudi Arabia', 'ie': 'Ireland', 'ar': 'Argentina', 'no': 'Norway', 'ma': 'India', 'in': 'Morocco', 'cl': 'Chile', 'hu': 'Hungary', 'ch': 'Switzerland', 'ru': 'Russia', 'lu': 'Luxembourg', 'pt': 'Portugal', 'bg': 'Bulgaria', 'jp': 'Japan', 'hn': 'Honduras', 'se': 'Sweden', 'vn': 'Vietnam', 'ro': 'Romania', 'hk': 'Hong Kong', 'ec': 'Ecuador', 'cr': 'Costa Rica', 'nz': 'New Zealand', 'id': 'Indonesia', 'gb': 'United Kingdom', 'fr': 'France', 'sk': 'Slovakia', 'pe': 'Peru', 'pa': 'Panama', 'lt': 'Lithuania', 'br': 'Brazil', 'ua': 'Ukraine', 'gr': 'Greece', 'it': 'Italy', 'es': 'Spain', 'fi': 'Finland', 'eg': 'Egypt', 'cz': 'Czech Republic', 'uy': 'Uraguay', 'il': 'Isreal', 'py': 'Paraguay', 'do': 'Dominican Republic', 'is': 'Iceland', 'at': 'Austria', 'dk': 'Denmark', 'sg': 'Singapore', 'ni': 'Nicaragua', 'ca': 'Canada', 'be': 'Belgium', 'mx': 'Mexico', 'tr': 'Turkey', 'de': 'Germany', 'co': 'Colombia', 'tw': 'Taiwan', 'us': 'United States', 'ae': 'United Arab Emirates', 'gt': 'Guatemala', 'pl': 'Poland', 'sv': 'El Salvador', 'th': 'Thailand', 'nl': 'Netherlands', 'ee': 'Estonia', 'ph': 'Philippines', 'bo': 'Bolivia', 'au': 'Australia', 'my': 'Malaysia', 'za': 'South Africa', 'lv': 'Latvia'}
        
        
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


class spotifyViralData:
    def __init__(self, debug=False, minYear=1, maxYear=9999):
        
        self.basedir  = "/Volumes/Piggy/Charts/"
        self.basename  = "SpotifyViral"
        #self.baseDir  = "/Volumes/Piggy/Charts/{0}".format(self.
        self.files     = []
        self.chartData = None
        self.sc        = spotifyViralCharts()

                
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
        

    def findFiles(self, abbr=None):
        savedir = join(self.basedir, "data", "spotifyviral", "categories")
        print(savedir)
        if not isDir(savedir):
            raise ValueError("Could not find directory: {0}".format(savedir))
        if abbr is not None:
            self.files   = findPatternExt(savedir, pattern="-{0}-".format(abbr), ext='.p')
        else:
            self.files   = findExt(savedir, ext='.p')
        print("Found {0} files.".format(len(self.files)))
        
    
    def parse(self):
        for abbr in self.sc.countries.keys():
            print("==> {0}".format(abbr))
            self.findFiles(abbr)
            data = {}

            for i,ifile in enumerate(self.files):
                #if i % 100 == 0:
                #    print("Processesing {0}/{1}".format(i,len(self.files)))
                bsdataH = getHTML(ifile)
                if bsdataH.find("div", {"class": "chart-error"}) is not None:
                    continue
                try:
                    bsdata = read_csv(StringIO(bsdataH.find("p").text), skiprows=1)
                except:
                    continue
                #bsdata = read_csv(ifile, skiprows=1)

                category  = "-".join(getBaseFilename(ifile).split("-")[:3])
                date      = getBaseFilename(ifile).split("--")[1:][0]

                bsdata.columns = ["Position", "Track Name", "Artist", "URL"]
                chartData = {}
                for irow,row in bsdata.iterrows():
                    artist = row["Artist"]
                    song   = row["Track Name"]
                    rank   = row["Position"]
                    url    = row["URL"]

                    chartName = "Viral50"
                    if chartData.get(chartName) is None:
                        chartData[chartName] = []
                    chartData[chartName].append({"Artist": artist, "Song": song, "URL": url, "Rank": rank})

                if data.get(category) is None:
                    data[category] = {}
                for chartName,chartInfo in chartData.items():
                    if data[category].get(chartName) is None:
                        data[category][chartName] = {}
                    data[category][chartName][date] = chartInfo

            if len(data) > 0:
                self.saveChartData(category, data[category])
            #self.chartData = data
        
        
        
    def setArtistAlbumData(self):
        self.artistAlbumData = {artist: list(artistData["Songs"].keys()) + list(artistData["Albums"].keys()) for artist,artistData in self.fullChartData.items()}
        
        
        
    def saveChartData(self, category, categoryData):
        savedir = join(self.basedir, "data", "spotifyviral", "results")
        if not isDir(savedir):
            raise ValueError("Could not find directory: {0}".format(savedir))
        saveName = setFile(savedir, "{0}.p".format(category))
        saveFile(idata=categoryData, ifile=saveName, debug=True)
                
        
    def getSummaryFiles(self):
        saveDir = join(self.basedir, "data", "spotifyviral", "results")
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
                            try:
                                str(song)
                            except:
                                continue
                            title = str(song).replace("\n", "").strip()
                        elif album is not None:
                            key = "Albums"
                            try:
                                str(album)
                            except:
                                continue
                            title = str(album).replace("\n", "").strip()
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