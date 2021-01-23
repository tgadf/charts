from searchUtils import findExt
from webUtils import getHTML
from fileUtils import getBaseFilename
from fsUtils import setDir, setFile, isFile, isDir
from ioUtils import getFile, saveFile
from collections import Counter
from os.path import join
from billboardYECharts import billboardYECharts

class billboardYE:
    def __init__(self, debug=False, minYear=1, maxYear=9999):
        
        self.basedir  = "/Volumes/Piggy/Charts/"
        self.basename  = "BillboardYE"
        #self.baseDir  = "/Volumes/Piggy/Charts/{0}".format(self.
        self.files     = []
        self.chartData = None
        
        self.bYEc = billboardYECharts()
        
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
                    self.charts += self.bYEc.getChartsByRank(item)
            elif isinstance(rank, int):
                self.charts += self.bYEc.getChartsByRank(rank)
        elif name is not None:
            self.charts += self.bYEc.getCharts(name)
        else:
            self.charts = self.bYEc.getCharts(None)
        if name is None:
            name = "None"
        print("  Using Charts ({0}): {1}".format(name, self.charts))
        
        
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
        
        

    def parseArtistTitle(self, bsdata, titleType=None):
        chartList = bsdata.find("div", {"class": "chart-details__item-list"})
        if chartList is None:
            raise ValueError("Could not find chart details!")
        articles = chartList.findAll("article", {"class": "ye-chart-item"})
        retval = []
        for rank,article in enumerate(articles):
            item  = article.find("div", {"class": "ye-chart-item__title"})
            title = item.text
            name  = None
            if titleType is None:
                name = title.strip()
            item = article.find("div", {"class": "ye-chart-item__artist"})
            href = item.find("a")
            url  = None
            if titleType is not None:
                name = item.text
            if href is not None:
                url  = href.attrs['href'].strip()
            if titleType is None:
                retval.append({"Artist": name, "URL": url, "Rank": rank+1})
            else:
                retval.append({"Artist": name, titleType: title, "URL": url, "Rank": rank+1})

        #print("\tFound {0} entries".format(len(retval)))
        return retval


    def findFiles(self):
        savedir = join(self.basedir, "data", "billboardYE", "categories")
        if not isDir(savedir):
            raise ValueError("Could not find directory: {0}".format(savedir))
        self.files   = findExt(savedir, ext='.p')
        print("Found {0} files.".format(len(self.files)))
        
    
    def parse(self):
        self.findFiles()

        data = {}
        for ifile in self.files:
            bsdata = getHTML(ifile)
            category,chart,chartType,year,chartName = getBaseFilename(ifile).split("__")

            if sum([chartName.endswith(x) for x in ["artists", "artists-female", "artists-male", "songwriters", "group", "songswriters"]]):
                retval = self.parseArtistTitle(bsdata)
            elif sum([chartName.endswith(x) for x in ["songs", "song-sales-yearend"]]):
                retval = self.parseArtistTitle(bsdata, "Song")
            elif sum([chartName.endswith(x) for x in ["adult-contemporary", "hot-100"]]):
                retval = self.parseArtistTitle(bsdata, "Song")
            elif sum([chartName.endswith(x) for x in ["albums", "albums-", "top-album-title-sales"]]):
                retval = self.parseArtistTitle(bsdata, "Album")
            elif sum([chartName.endswith(x) for x in ["distributors", "corporations", "labels", "publishers", "producers", "music-video-sales"]]):
                continue
            else:
                raise ValueError("Not sure what to do with {0}".format(ifile))

            if data.get(category) is None:
                data[category] = {}
            if data[category].get(year) is None:
                data[category][year] = {}
            data[category][year][chartName] = retval
            
        self.chartData = data
        
        
        
    def setArtistAlbumData(self):
        self.artistAlbumData = {artist: list(artistData["Songs"].keys()) + list(artistData["Albums"].keys()) for artist,artistData in self.fullChartData.items()}
        
        
        
    def saveChartData(self):
        for category,categoryData in self.chartData.items():
            savedir = join(self.basedir, "data", "billboardYE", "results")
            if not isDir(savedir):
                raise ValueError("Could not find directory: {0}".format(savedir))
            saveName = setFile(saveDir, "{0}.p".format(category))
            saveFile(idata=categoryData, ifile=saveName, debug=True)
                
        
    def getSummaryFiles(self):
        saveDir = join(self.basedir, "data", "billboardYE", "results")
        if not isDir(saveDir):
            raise ValueError("Could not find directory: {0}".format(saveDir))
        files    = findExt(saveDir, ".p")
        print("Found {0} summary files".format(len(files)))
        return files
    
        
    def setFullChartData(self):
        files = self.getSummaryFiles()
        for ifile in files:
            category = getBaseFilename(ifile)
            categoryData = getFile(ifile)
            for year,yearData in categoryData.items():
                for chartName,chartData in yearData.items():

                    if chartName not in self.charts:
                        continue
                        
                    if True:
                        if int(year) < int(self.minYear):
                            continue
                        if int(year) > int(self.maxYear):
                            continue
                        
                    for item in chartData:
                        artistName = item["Artist"]
                        if artistName is None:
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