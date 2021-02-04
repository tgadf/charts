from ioUtils import getFile
from listUtils import getFlatList
from artistIgnores import getArtistIgnores

class spotifyCharts:
    def __init__(self):

        self.us          = ['regional-us-weekly']
        self.denmark     = ['regional-dk-weekly']
        self.england     = ['regional-gb-weekly']
        self.world       = ['regional-global-weekly']
        self.india       = ['regional-in-weekly']
        self.japan       = ['regional-jp-weekly']
        self.mexico      = ['regional-mx-weekly']
        self.brazil      = ['regional-br-weekly']
        self.southafrica = ['regional-za-weekly']
        self.russia      = ['regional-ru-weekly']
        self.isreal      = ['regional-il-weekly']
        self.italy       = ['regional-it-weekly']
        
        self.chartNames = self.__dict__.keys()
        
        self.chartRanks = {}
        self.chartRanks[0] = ['us']
        self.chartRanks[1] = ['england']
        self.chartRanks[2] = ['world']
        self.chartRanks[3] = ['denmark', 'southafrica']
        self.chartRanks[4] = ['italy', 'isreal']
        self.chartRanks[5] = ['india', 'russia']
        self.chartRanks[6] = ['japan']
        self.chartRanks[7] = ['mexico']
        self.chartRanks[8] = ['brazil']
        
        
    def getChartsByRank(self, rank):
        categories = self.chartRanks[rank]
        charts = []
        for chart in categories:
            charts += self.getCharts(chart)
        print("  Using {0} Charts".format(len(charts)))
        return charts
        
    def getCharts(self, name=None):        
        charts = []
        if name is None:
            print("  Getting All Charts")
            for chart in self.chartNames:
                charts += self.__dict__[chart]
        else:
            print("  Getting Chart For {0}".format(name))
            name = name.replace("-", "_")
            print("name = {0}".format(name))
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