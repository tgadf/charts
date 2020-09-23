from top40charts import top40chart
from timeUtils import getDateTime, isDate
from listUtils import isIn
from collections import Counter

class fullCharts:
    def __init__(self, t40charts, ctype=None, country=None, minYear=None, maxYear=None, debug=False):
        self.t40charts = t40charts
        self.debug     = False
        
        if country is None:
            self.country   = None
        elif isinstance(country, str):
            self.country   = [country]
        elif isinstance(country, list):
            self.country   = country
        else:
            raise ValueError("No idea about country value {0}".format(country))
            
        self.ctype = ctype
        if self.ctype is not None:
            if self.ctype not in ["Albums", "Singles"]:
                raise ValueError("Ctype must be Albums or Singles")                
            
        self.minYear   = minYear
        self.maxYear   = maxYear
        
        self.artistRenames   = {}

        self.fullChartData   = {}
        self.artistAlbumData = {}
        
    def setRenames(self, artistRenames):
        self.artistRenames = artistRenames
        
        
    def getArtistAlbumData(self):
        return self.artistAlbumData
    
    def getFullChartData(self):
        return self.fullChartData
        
        
    def setArtistAlbumData(self):
        self.artistAlbumData = {artist: list(artistData["Songs"].keys()) + list(artistData["Albums"].keys()) for artist,artistData in self.fullChartData.items()}
        
        
        
    def setFullChartData(self):
        fullChartData = {}
        renameStats   = Counter()
        for chartName, chartData in self.t40charts.items():
            
            if self.country is not None:
                if not isIn(self.country, chartName):
                    continue
            if self.ctype is not None:
                if self.ctype == "Albums":
                    if not chartName.endswith("Albums"):
                        continue
                elif self.ctype == "Singles":
                    if chartName.endswith("Albums"):
                        continue
            
            print("==> {0: <40}".format(chartName), end="\t")
            chartURL = chartData["URL"]
            chartID  = chartData["ID"]
            t40chart = top40chart(chartID, chartName, chartURL)
            chartResults = t40chart.getFullChartData()

            for date, values in chartResults.items():
                if self.minYear is not None:
                    if getDateTime(date).year < int(self.minYear):
                        continue
                if self.maxYear is not None:
                    if getDateTime(date).year > int(self.maxYear):
                        continue

                        
                for i,item in enumerate(values):
                    artist = item["Artist"]
                    renamedArtist = artist
                    for testArtist in self.artistRenames.keys():
                        if artist.find(testArtist) != -1:
                            tmp = renamedArtist
                            renamedArtist = renamedArtist.replace(testArtist, self.artistRenames.get(testArtist))
                            #print("{0}  <---- From ---- {1}".format(renamedArtist, tmp))
                            renameStats[renamedArtist] += 1
                            artist = renamedArtist
                    

                    artist = artist.replace("\r", "")                    
                    
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
        
        if self.artistRenames is not None:
            print("Renamed {0} artists".format(len(renameStats)))
            print("Most Common Artists:")
            for item in renameStats.most_common(5):
                print(item)