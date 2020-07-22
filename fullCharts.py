from top40charts import top40chart
from timeUtils import getDateTime, isDate
from collections import Counter

class fullCharts:
    def __init__(self, t40charts, country=None, minYear=None, debug=False):
        self.t40charts = t40charts
        self.debug     = False
        
        self.country   = country
        self.minYear   = minYear
        
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
                if not self.country in chartName:
                    continue
                if "Albums" in chartName:
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
                        
                for i,item in enumerate(values):
                    artist = item["Artist"]
                    renamedArtist = self.artistRenames.get(artist)
                    if renamedArtist is not None:
                        print("{0}  <---- From ---- {1}".format(renamedArtist, artist))
                        renameStats[renamedArtist] += 1
                        artist = renamedArtist
                    
                    album  = item["Album"]
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