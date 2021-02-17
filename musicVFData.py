from musicVFCharts import musicVFCharts
from searchUtils import findExt, findPatternExt
from webUtils import getHTML
from timeUtils import getDateTime
from fileUtils import getBaseFilename, getDirBasics, getDirname
from fsUtils import setDir, setFile, isFile, isDir
from ioUtils import getFile, saveFile
from collections import Counter
from os.path import join
from pandas import read_csv
from io import StringIO


class musicVFData:
    def __init__(self, debug=False, minYear=1, maxYear=9999):
        
        self.basedir  = "/Volumes/Piggy/Charts/"
        self.basename  = "musicvf"
        #self.baseDir  = "/Volumes/Piggy/Charts/{0}".format(self.
        self.files     = []
        self.chartData = None
        self.sc        = musicVFCharts()

                
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
        

    def findFiles(self):
        savedir = join(self.basedir, "data", "musicvf", "categories")
        if not isDir(savedir):
            raise ValueError("Could not find directory: {0}".format(savedir))        
        years = range(1900, 2020+1)
        files = []
        for year in years:
            yfile = setFile(savedir, "{0}.p".format(year))
            if isFile(yfile):
                files.append(yfile)
            files += findExt(setDir(savedir, str(year)), ext=".p")
        self.files = files
        print("Found {0} files.".format(len(self.files)))
        


    def getSongData(self, bsdata):
        songYearData = []

        divLetters = ["bloc-{0}".format(x) for x in ["A", "B", "C", "D", "E", "F", "H"]]
        headers    = [bsdata.find("div", {"class": "{0}".format(x)}) for x in divLetters]
        headers    = [x.text.replace("\xa0", "").strip() for x in headers]
        data = {}
        retval = {}
        for i,divLetter in enumerate(divLetters):
            if headers[i] == "USpeak":
                continue
            entries = bsdata.findAll("div", {"class": "{0}".format(divLetter)})[1:]
            data[headers[i]] = entries

        #data["Year"]  = [x.find('a').text for x in data["Date"]]
        retval = []
        for j,val in enumerate(data["TitleAlbum"]):
            #print(j,'\t',len(val.findAll("a")))
            taHeaders = ["Song", "Artist", "Album", "Image"]
            taRefs    = val.findAll('a')
            taData    = dict(zip(taHeaders, taRefs))
            #print(taData)

            try:
                titleName = taData["Song"].attrs['title']
                titleName = titleName.replace("[article]", "").strip()
                titleName = titleName.replace("[video]", "").strip()
                titleURL  = taData["Song"].attrs['href']
            except:
                titleName = None
                titleURL  = None
            titleData = {"Name": titleName, "URL": titleURL}
            #print('\t',titleData)

            try:
                artistName = taData["Artist"].text
                artistURL  = taData["Artist"].attrs['href']
            except:
                artistName = None
                artistURL  = None
            artistData = {"Name": artistName, "URL": artistURL}
            #print('\t',artistData)

            try:
                albumName  = taData["Album"].attrs['title']
                albumURL   = taData["Album"].attrs['href']
            except:
                albumName  = None
                albumURL   = None
            albumData  = {"Name": albumName, "URL": albumURL}
            #print('\t',albumData)

            songData = {"Title": titleData, "Artist": artistData, "Album": albumData} #, "Year": data['Year'][j]}
            #print(j,'\t',songData)
            songYearData.append(songData)   

        return songYearData


    def getArtistData(self, bsdata):
        artistYearData = {}
        for it,table in enumerate(bsdata.findAll("table")):
            if len(table.findAll("th")) == 0:
                continue

            trs = table.findAll("tr")
            if len(trs) == 0:
                continue

            if len(trs[0].findAll("th")) == 0:
                continue

            ths = [th.text.replace("\ax0", "").strip() for th in table.findAll("th")]
            if ths[0] == "":
                ths[0] = "Pos"
            #print(ths)

            start = None
            for itr,tr in enumerate(trs[1:]):
                if len(tr.findAll("th")) > 0:
                    start = itr+2
                    break

            if start is None:
                break
                raise ValueError("Could not understand this table...")            
            for itr,tr in enumerate(trs[start:]):
                #print(itr,'\t',tr)
                rowdata = dict(zip(ths, tr.findAll("td")))
                #print(rowdata)
                #print(itr,'\t',rowdata["Pos"])

                try:
                    pos = int(rowdata["Pos"].text.replace(".", ""))
                except:
                    raise ValueError("Unsure how to parse pos [{0}]".format(rowdata["Pos"]))

                try:
                    artistRef  = rowdata["Artist"].find("a")
                    artistName = artistRef.text
                    artistURL  = artistRef.attrs['href']
                except:
                    artistName = None
                    artistURL  = None
                artistData = {"Name": artistName, "URL": artistURL}


                titlesData = []
                songs = rowdata["Songs"].findAll("a")
                for song in songs:
                    try:
                        attrs = song.attrs
                        if attrs['href'].startswith("top_songs_of"):
                            continue
                    except:
                        continue

                    try:
                        titleName = song.text
                        titleName = titleName.replace("[article]", "").strip()
                        titleName = titleName.replace("[video]", "").strip()
                        titleURL  = attrs['href']
                    except:
                        titleName = None
                        titleURL  = None
                    titleData = {"Name": titleName, "URL": titleURL}
                    titlesData.append(titleData)

                if artistYearData.get(pos) is not None:
                    break
                if pos == 1:
                    pass
                artistYearData[pos] = {"Artist": artistData, "Titles": titlesData}

        return artistYearData


    
    def parse(self):
        self.findFiles()
        data = {}

        for i,ifile in enumerate(self.files):
            category = getBaseFilename(ifile)
            try:
                year = int(category)
                category = "Singles"
                print("\t",year)
            except:
                try:
                    year = int(getDirBasics(getDirname(ifile))[-1])
                except:
                    raise ValueError("Can't find a year for {0}".format(ifile))
                    
            if category == "Artists":
                bsdata = getHTML(ifile)
                retval = self.getArtistData(bsdata)
            else:
                bsdata = getHTML(ifile)
                retval = self.getSongData(bsdata)
            if data.get(category) is None:
                data[category] = {}
            data[category][year] = retval

        self.chartData = data

        
        
    def setArtistAlbumData(self):
        self.artistAlbumData = {artist: list(artistData["Songs"].keys()) + list(artistData["Albums"].keys()) for artist,artistData in self.fullChartData.items()}
        
        
    def saveChartData(self):
        for category,categoryData in self.chartData.items():
            saveDir = join(self.basedir, "data", "musicvf", "results")
            if not isDir(saveDir):
                raise ValueError("Could not find directory: {0}".format(savedir))
            saveName = setFile(saveDir, "{0}.p".format(category))
            saveFile(idata=categoryData, ifile=saveName, debug=True)
                
        
    def getSummaryFiles(self):
        saveDir = join(self.basedir, "data", "musicvf", "results")
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
            for year,yearData in categoryData.items():
                if True:
                    if int(year) < int(self.minYear):
                        continue
                    if int(year) > int(self.maxYear):
                        continue
                        
                if category == "Artists":
                    chartName = category
                    for pos,posData in yearData.items():
                        artistData = posData["Artist"]
                        titlesData = posData["Titles"]
                        
                        artistName = artistData["Name"]
                        artistURL  = artistData["URL"]
                        if artistName is None:
                            continue
                            
                        if self.fullChartData.get(artistName) is None:
                            self.fullChartData[artistName] = {"Songs": {}, "Albums": {}}

                        key = "Songs"
                        for titleData in titlesData:
                            titleName = titleData["Name"]
                            titleURL  = titleData["URL"]

                            if self.fullChartData[artistName].get(key) is None:
                                self.fullChartData[artistName][key] = {}
                            if self.fullChartData[artistName][key].get(titleName) is None:
                                self.fullChartData[artistName][key][titleName] = {}
                            if self.fullChartData[artistName][key][titleName].get(chartName) is None:
                                self.fullChartData[artistName][key][titleName][chartName] = {}
                            self.fullChartData[artistName][key][titleName][chartName][year] = 0                            
                else:
                    chartName = category
                    for songData in yearData:
                        artistData = songData["Artist"]
                        titleData  = songData["Title"]
                        albumData  = songData["Artist"]
                        
                        artistName = artistData["Name"]
                        artistURL  = artistData["URL"]
                        if artistName is None:
                            continue
                            
                        if self.fullChartData.get(artistName) is None:
                            self.fullChartData[artistName] = {"Songs": {}, "Albums": {}}
                            
                        titleName = titleData["Name"]
                        titleURL  = titleData["URL"]
                        
                        albumName = albumData["Name"]
                        albumURL  = albumData["URL"]
                        
                        for key,name in {"Song": titleName, "Albums": albumName}.items():
                            if name is not None:
                                if self.fullChartData[artistName].get(key) is None:
                                    self.fullChartData[artistName][key] = {}
                                if self.fullChartData[artistName][key].get(name) is None:
                                    self.fullChartData[artistName][key][name] = {}
                                if self.fullChartData[artistName][key][name].get(chartName) is None:
                                    self.fullChartData[artistName][key][name][chartName] = {}
                                self.fullChartData[artistName][key][name][chartName][year] = 0              
                                
                #print(year,'\t',len(self.fullChartData))

        self.renameSummary()