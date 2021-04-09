from searchUtils import findExt, findPatternExt, findDirs, findDirsPattern
from webUtils import getHTML
from timeUtils import getDateTime
from fileUtils import getBaseFilename, getDirBasics
from fsUtils import setDir, setFile, isFile, isDir
from ioUtils import getFile, saveFile
from listUtils import getFlatList
from collections import Counter
from os.path import join
from pandas import read_csv
from io import StringIO
import re
from rateYourMusicScriptCharts import rateYourMusicScriptCharts
from langdetect import detect




class rateYourMusicScriptData:
    def __init__(self, debug=False, minYear=1, maxYear=9999):
        
        self.basedir  = "/Volumes/Piggy/Charts/"
        self.basename  = "RateYourMusicScript"
        #self.baseDir  = "/Volumes/Piggy/Charts/{0}".format(self.
        self.files     = {}
        self.chartData = None
        self.sc        = rateYourMusicScriptCharts()

                
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
        

    def findFiles(self, pattern=None):
        savedir = join(self.basedir, "data", "rymscript", "categories")
        if not isDir(savedir):
            raise ValueError("Could not find directory: {0}".format(savedir))
        print(savedir)
        if pattern is None:
            dirs    = findDirs(savedir)
        else:
            dirs    = findDirsPattern(savedir, pattern=pattern)            
        fDict   = {}
        for dirVal in dirs:
            key = getDirBasics(dirVal)[-1]
            files = sorted(findExt(dirVal, ".htm") + findExt(dirVal, ".html"))
            fDict[key] = files
        self.files = fDict
        
        print("Found {0} key files.".format(len(self.files)))


    def getRYMChartData(self, bsdata, debug=False):
        tableData = []
        for item in bsdata.findAll("div", {"class": "chart_item_release"}):
            listArtists = item.findAll("a", {"class": "artist"})
            listAlbums  = item.findAll("a", {"class": "release"})

            ############################################
            ################## Artist ##################
            ############################################
            artistData = []
            for artistRef in listArtists:
                if artistRef is not None:
                    artistName  = artistRef.text
                    res = re.findall(r'\[.*?\]', artistName)
                    if len(res) == 1:
                        artistName = res[0][1:-1]
                    artistURL   = artistRef.attrs['href']
                    artistTitle = artistRef.attrs['title']
                else:
                    artistName  = None
                    artistURL   = None
                    artistTitle = None
                value = {"Name": artistName, "URL": artistURL, "Title": artistTitle}
                artistData.append(value)


            ###########################################
            ################## Album ##################
            ###########################################
            albumData = []
            for albumRef in listAlbums:
                if albumRef is not None:
                    albumName  = albumRef.text
                    albumURL   = albumRef.attrs['href']
                    albumTitle = albumRef.attrs['title']
                else:
                    albumName  = None
                    albumURL   = None
                    albumTitle = None
                value = {"Name": albumName, "URL": albumURL, "Title": albumTitle}
                albumData.append(value)

            if len(artistData) == 0 and len(albumData) == 0:
                continue
            if debug:
                print("Found {0: <14}: {1}".format("Artist", artistData))
                print("    Found {0: <10}: {1}".format("Album", albumData))
            tableData.append({"Artist": artistData, "Album": albumData, "Title": []})
        return tableData
        
        
    def getRYMListData(self, bsdata, debug=False):
        tableData = []
        for item in bsdata.findAll("div", {"class": "chart_item_release"}):
            listArtists = item.findAll("a", {"class": "artist"})
            listAlbums  = item.findAll("a", {"class": "release"})
            
        trs = table.findAll("tr")
        for itr,tr in enumerate(trs):
            listArtists = tr.findAll("a", {"class": "list_artist"})
            listAlbums  = tr.findAll("a", {"class": "list_album"})
            listTitles  = tr.findAll("span", {"class": "rendered_text"})


            ###########################################
            ################## Title ##################
            ###########################################
            titleData = []
            for titleText in listTitles:            
                if titleText is not None:
                    titleName = titleText.text
                else:
                    titleName = None
                value = {"Name": titleName}
                titleData.append(value)
                

            ############################################
            ################## Artist ##################
            ############################################
            artistData = []
            for artistRef in listArtists:
                if artistRef is not None:
                    artistName  = artistRef.text
                    res = re.findall(r'\[.*?\]', artistName)
                    if len(res) == 1:
                        artistName = res[0][1:-1]
                    artistURL   = artistRef.attrs['href']
                    artistTitle = artistRef.attrs['title']
                else:
                    artistName  = None
                    artistURL   = None
                    artistTitle = None
                value = {"Name": artistName, "URL": artistURL, "Title": artistTitle}
                artistData.append(value)


            ###########################################
            ################## Album ##################
            ###########################################
            albumData = []
            for albumRef in listAlbums:
                if albumRef is not None:
                    albumName  = albumRef.text
                    albumURL   = albumRef.attrs['href']
                    albumTitle = albumRef.attrs['title']
                else:
                    albumName  = None
                    albumURL   = None
                    albumTitle = None
                value = {"Name": albumName, "URL": albumURL, "Title": albumTitle}
                albumData.append(value)

            if len(artistData) == 0 and len(albumData) == 0:
                continue
            if debug:
                print("Found {0: <14}: {1}".format("Artist", artistData))
                print("   Found {0: <10}: {1}".format("Album", albumData))
                print("   Found {0: <10}: {1}".format("Album", titleData))
            tableData.append({"Artist": artistData, "Album": albumData, "Title": titleData})
        return tableData
    
        
    def getRYMArtistAlbumData(self, bsdata, debug=False):
        table = bsdata.find("table", {"id": "user_list"})
        if table is None:
            print("Could not find user_list table!")            
            1/0
            return []

        tableData = []
        trs = table.findAll("tr")
        for itr,tr in enumerate(trs):
            listArtists = tr.findAll("a", {"class": "list_artist"})
            listAlbums  = tr.findAll("a", {"class": "list_album"})
            listTitles  = tr.findAll("span", {"class": "rendered_text"})


            ###########################################
            ################## Title ##################
            ###########################################
            titleData = []
            for titleText in listTitles:            
                if titleText is not None:
                    titleName = titleText.text
                else:
                    titleName = None
                value = {"Name": titleName}
                titleData.append(value)
                

            ############################################
            ################## Artist ##################
            ############################################
            artistData = []
            for artistRef in listArtists:
                if artistRef is not None:
                    artistName  = artistRef.text
                    res = re.findall(r'\[.*?\]', artistName)
                    if len(res) == 1:
                        tmp  = artistName.split("[")[0].strip()
                        try:
                            lang = detect(tmp)
                        except:
                            lang = "UNK"
                        if lang not in ["en", "cy"]:
                            artistName = res[0][1:-1]
                        else:
                            artistName = tmp
                    artistURL   = artistRef.attrs['href']
                    artistTitle = artistRef.attrs['title']
                else:
                    artistName  = None
                    artistURL   = None
                    artistTitle = None
                value = {"Name": artistName, "URL": artistURL, "Title": artistTitle}
                artistData.append(value)


            ###########################################
            ################## Album ##################
            ###########################################
            albumData = []
            for albumRef in listAlbums:
                if albumRef is not None:
                    albumName  = albumRef.text
                    albumURL   = albumRef.attrs['href']
                    albumTitle = albumRef.attrs['title']
                else:
                    albumName  = None
                    albumURL   = None
                    albumTitle = None
                value = {"Name": albumName, "URL": albumURL, "Title": albumTitle}
                albumData.append(value)

            if len(artistData) == 0 and len(albumData) == 0:
                continue
                
                
            artistData, albumData, titleData = self.cleanListData(artistData, albumData, titleData)
            if debug:
                print("{0}/{1}".format(itr,len(trs)))
                print("Found {0: <14}: {1}".format("Artist", artistData))
                print("    Found {0: <10}: {1}".format("Album", albumData))
                print("    Found {0: <10}: {1}".format("Title", titleData))
                                
            tableData.append({"Artist": artistData, "Album": albumData, "Title": titleData})
        return tableData
    
    
    def cleanListData(self, artistData, albumData, titleData):
        goodArtists = sum([1 if x["Name"] is not None else 0 for x in artistData])
        goodAlbums  = sum([1 if x["Name"] is not None else 0 for x in albumData])
        goodTitles  = sum([1 if x["Name"] is not None else 0 for x in titleData])
        
        if goodAlbums > 0:
            titleData = [{"Name": None}]
            
        return artistData, albumData, titleData

        
    
    
    def parse(self, force=False, debug=False):
        self.findFiles(pattern=None)
        for key,files in self.files.items():
            savename = self.getSaveChartFilename(key)
            if isFile(savename):
                if force is False:
                    continue
                    
            data = []
            print("==> {0} ({1})".format(key, len(files)))            
            for i,ifile in enumerate(files):
                bsdata = getHTML(ifile)
                
                ## Releases, singles, albums
                if " releases of " in ifile or " singles of " in ifile or " albums of " in ifile:
                    retval = self.getRYMChartData(bsdata, debug=debug)
                elif " mixtapes and DJ mixes of the " in ifile:
                    retval = self.getRYMChartData(bsdata, debug=debug)                    
                else:
                    retval = self.getRYMArtistAlbumData(bsdata, debug=debug)
                data.append(retval)
            data = getFlatList(data)
            print("\tFound {0} entries".format(len(data)))
            goodArtists = sum([1 if sum([1 if y["Name"] is not None else 0 for y in x["Artist"]]) > 0 else 0 for x in data])
            goodAlbums  = sum([1 if sum([1 if y["Name"] is not None else 0 for y in x["Album"]]) > 0 else 0 for x in data])
            goodTitles  = sum([1 if sum([1 if y["Name"] is not None else 0 for y in x["Title"]]) > 0 else 0 for x in data])
            print("\t    Found {0} artist entries".format(goodArtists))
            print("\t    Found {0} album entries".format(goodAlbums))
            print("\t    Found {0} title entries".format(goodAlbums))
            self.saveChartData(key, data)
        
        
        
    def setArtistAlbumData(self):
        self.artistAlbumData = {artist: list(artistData["Songs"].keys()) + list(artistData["Albums"].keys()) for artist,artistData in self.fullChartData.items()}
        
        
    def getSaveChartName(self, categoryName):
        categoryName = categoryName.replace(" ", "_")
        categoryName = categoryName.replace("&", "_")
        categoryName = categoryName.replace("/", "_")
        categoryName = categoryName.replace("\\", "_")
        categoryName = categoryName.replace(",", "_")
        categoryName = categoryName.replace("'", "")
        categoryName = categoryName.replace("-", "_")
        categoryName = categoryName.replace("+", "_")
        categoryName = categoryName.replace("(", "_")
        categoryName = categoryName.replace(")", "_")
        categoryName = categoryName.replace("!", "")
        categoryName = categoryName.replace("♀", "_")
        categoryName = categoryName.replace("[", "")
        categoryName = categoryName.replace("]", "")
        categoryName = categoryName.replace(".", "_")
        categoryName = categoryName.replace("#", "")
        categoryName = categoryName.replace("____", "_")
        categoryName = categoryName.replace("___", "_")
        categoryName = categoryName.replace("__", "_")
        return categoryName
    
    def getSaveChartFilename(self, categoryName):
        savedir = join(self.basedir, "data", "rymscript", "results")
        if not isDir(savedir):
            raise ValueError("Could not find directory: {0}".format(savedir))
        saveName = setFile(savedir, "{0}.p".format(self.getSaveChartName(categoryName)))
        return saveName
        

    def saveChartData(self, category, categoryData):
        saveName = self.getSaveChartFilename(category)
        saveFile(idata=categoryData, ifile=saveName, debug=True)        
                        
        
    def getSummaryFiles(self):
        saveDir = join(self.basedir, "data", "rymscript", "results")
        if not isDir(saveDir):
            raise ValueError("Could not find directory: {0}".format(saveDir))
        files    = findExt(saveDir, ".p")
        print("Found {0} summary files".format(len(files)))
        return files
    
    
    def findCharts(self):
        files = [getBaseFilename(x) for x in self.getSummaryFiles()]
        ranks = {}
        ranks["Singles"]  = {"Best": [], "Worst": [], "BestYearly": [], "WorstYearly": []}
        ranks["Albums"]   = {"Best": [], "Worst": [], "Esoteric": [], "Diverse": [], "Yearly": []}
        ranks["Releases"] = {"Best": [], "Worst": []}
        ranks["Mixes"]    = {"Best": [], "Worst": []}
        ranks["Titles"]   = []
        ranks["Artists"]  = []
        ranks["Script"]   = []
        ranks["Other"]    = []
        for ifile in sorted(files):
            print("        self.c_{0: <75} = ['{1}']".format(ifile, ifile))
            if "_singles_of_the_" in ifile:
                if "Best_" in ifile:
                    ranks["Singles"]["Best"].append(ifile)
                elif "Worst_" in ifile:
                    ranks["Singles"]["Worst"].append(ifile)
                else:
                    ranks["Other"].append(ifile)
            elif "_albums_of_the_" in ifile:
                if "Best_" in ifile:
                    ranks["Albums"]["Best"].append(ifile)
                elif "Worst_" in ifile:
                    ranks["Albums"]["Worst"].append(ifile)
                elif "Diverse_" in ifile:
                    ranks["Albums"]["Diverse"].append(ifile)
                elif "Esoteric_" in ifile:
                    ranks["Albums"]["Esoteric"].append(ifile)
                else:
                    ranks["Other"].append(ifile)
            elif "_albums_of_" in ifile:
                    ranks["Albums"]["Yearly"].append(ifile)
            elif "_singles_of_" in ifile:
                if "Best_" in ifile:
                    ranks["Singles"]["BestYearly"].append(ifile)
                elif "Worst_" in ifile:
                    ranks["Singles"]["WorstYearly"].append(ifile)
                else:
                    ranks["Other"].append(ifile)
            elif "_Releases_" in ifile:
                if "Top" in ifile:
                    ranks["Releases"]["Best"].append(ifile)
                elif "Bottom" in ifile:
                    ranks["Releases"]["Worst"].append(ifile)
                elif "Artists_Releases_" in ifile and "script" in ifile:
                    ranks["Script"].append(ifile)
                else:
                    ranks["Other"].append(ifile)
            elif "_Mixes_" in ifile:
                if "Top_" in ifile or "Best_" in ifile:
                    ranks["Mixes"]["Best"].append(ifile)
                elif "Bottom" in ifile or "Worst_" in ifile:
                    ranks["Mixes"]["Worst"].append(ifile)
                else:
                    ranks["Other"].append(ifile)
            elif "Album" in ifile or "Song" in ifile:
                ranks["Titles"].append(ifile)
            elif "Artist" in ifile:
                if "Artists_with_" in ifile and "script" in ifile:
                    ranks["Script"].append(ifile)
                else:
                    ranks["Artists"].append(ifile)
            else:
                if "Artists_Releases_" in ifile and "script" in ifile:
                    ranks["Script"].append(ifile)
                elif "Releases_with_" in ifile and "script" in ifile:
                    ranks["Script"].append(ifile)
                else:
                    ranks["Other"].append(ifile)
                     
        print("\n")        
        print("        self.chartNames = self.__dict__.keys()")
        print("\n")
        print("        self.chartRanks = {}")
        rank = 0
        from numpy import ceil

        modVal=3
        print("        ######### Singles - Best #########")
        for ir in range(int(ceil(len(ranks["Singles"]["Best"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Singles"]["Best"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1

        modVal=3
        print("        ######### Singles - Worst #########")
        for ir in range(int(ceil(len(ranks["Singles"]["Worst"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Singles"]["Worst"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1
            
        modVal=3
        print("        ######### Albums - Best #########")
        for ir in range(int(ceil(len(ranks["Albums"]["Best"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Albums"]["Best"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1

        modVal=3
        print("        ######### Albums - Diverse #########")
        for ir in range(int(ceil(len(ranks["Albums"]["Diverse"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Albums"]["Diverse"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1

        modVal=3
        print("        ######### Albums - Esoteric #########")
        for ir in range(int(ceil(len(ranks["Albums"]["Esoteric"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Albums"]["Esoteric"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1

        modVal=3
        print("        ######### Albums - Worst #########")
        for ir in range(int(ceil(len(ranks["Albums"]["Worst"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Albums"]["Worst"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1

        modVal=7
        print("        ######### Mixes - Best #########")
        for ir in range(int(ceil(len(ranks["Albums"]["Best"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Mixes"]["Best"][start:end]
            if len(charts) > 0:
                print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
                rank += 1

        modVal=7
        print("        ######### Mixes - Worst #########")
        for ir in range(int(ceil(len(ranks["Albums"]["Worst"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Mixes"]["Worst"][start:end]
            if len(charts) > 0:
                print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
                rank += 1

        modVal=5
        print("        ######### Albums - Yearly #########")
        for ir in range(int(ceil(len(ranks["Albums"]["Yearly"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Albums"]["Yearly"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1

        modVal=5
        print("        ######### Singles - BestYearly #########")
        for ir in range(int(ceil(len(ranks["Singles"]["BestYearly"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Singles"]["BestYearly"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1

        modVal=5
        print("        ######### Singles - WorstYearly #########")
        for ir in range(int(ceil(len(ranks["Singles"]["WorstYearly"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Singles"]["WorstYearly"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1
            
        modVal=6
        print("        ######### Titles #########")
        for ir in range(int(ceil(len(ranks["Titles"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Titles"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1
            
        modVal=6
        print("        ######### Artists #########")
        for ir in range(int(ceil(len(ranks["Artists"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Artists"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1
            
        modVal=2
        print("        ######### Script #########")
        for ir in range(int(ceil(len(ranks["Script"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Script"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1
            
        modVal=6
        print("        ######### Other #########")
        for ir in range(int(ceil(len(ranks["Other"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Other"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1

        modVal=6
        print("        ######### Releases - Best #########")
        for ir in range(int(ceil(len(ranks["Releases"]["Best"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Releases"]["Best"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1

        modVal=6
        print("        ######### Releases - Worst #########")
        for ir in range(int(ceil(len(ranks["Releases"]["Worst"])/modVal))):
            start  = ir*modVal
            end    = (ir+1)*modVal
            charts = ranks["Releases"]["Worst"][start:end]
            print("        self.chartRanks[{0}] = {1}".format(rank, ['c_{0}'.format(x) for x in charts]))
            rank += 1
            
        #print("        self.chartRanks[0] = {0}".format(['c_{0}'.format(x) for x in ranks["Albums"]]))
        #print("        self.chartRanks[1] = {0}".format(['c_{0}'.format(x) for x in ranks["Songs"]]))
        #print("        self.chartRanks[2] = {0}".format(['c_{0}'.format(x) for x in ranks["Other"]]))
        #return ranks

    
        
    def setFullChartData(self):
        files = self.getSummaryFiles()
        for ifile in files:
            category = getBaseFilename(ifile)
            if category not in self.charts:
                continue
            print("  Using {0}".format(category))
            categoryData = getFile(ifile)
            for chartData in categoryData:
                artistData = chartData["Artist"]
                albumData  = chartData["Album"]
                titleData  = chartData["Title"]
                
                for artist in artistData:
                    artistName = self.renameArtist(artist["Name"])
                    artistURL  = artist["URL"]
                    if self.fullChartData.get(artistName) is None:
                        self.fullChartData[artistName] = {"Songs": {}, "Albums": {}}                    
                    
                    date = "X"
                    for album in albumData:
                        albumName = album["Name"]
                        if albumName is None:
                            continue
                        if len(albumName) == 0:
                            continue
                        albumURL  = album["URL"]
                        key = "Albums"

                        if self.fullChartData[artistName][key].get(albumName) is None:
                            self.fullChartData[artistName][key][albumName] = {}
                        if self.fullChartData[artistName][key][albumName].get(category) is None:
                            self.fullChartData[artistName][key][albumName][category] = {}
                        self.fullChartData[artistName][key][albumName][category][date] = 0               
                        
                    for title in titleData:
                        titleName = title["Name"]
                        if titleName is None:
                            continue
                        if len(titleName) == 0:
                            continue
                        key = "Songs"

                        if self.fullChartData[artistName][key].get(titleName) is None:
                            self.fullChartData[artistName][key][titleName] = {}
                        if self.fullChartData[artistName][key][titleName].get(category) is None:
                            self.fullChartData[artistName][key][titleName][category] = {}
                        self.fullChartData[artistName][key][titleName][category][date] = 0
                #print("{0: <40}{1}".format("{0}-{1}".format(chartName,stryear),len(self.fullChartData)))

        self.renameSummary()