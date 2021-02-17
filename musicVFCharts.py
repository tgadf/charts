from ioUtils import getFile
from listUtils import getFlatList
from artistIgnores import getArtistIgnores

class musicVFCharts:
    def __init__(self):
        
        self.artists = ["Artists"]
        self.country = ["Country"]
        self.rnb     = ["RnB"]
        self.adult   = ["Adult"]
        self.dance   = ["Dance"]
        self.rock    = ["Rock"]
        self.singles = ["Singles"]
        
        self.chartNames = self.__dict__.keys()

        self.chartRanks = {}
        self.chartRanks[0] = ['artists']
        self.chartRanks[1] = ['singles']
        self.chartRanks[2] = ['adult']        
        self.chartRanks[3] = ['rock']        
        self.chartRanks[4] = ['country']
        self.chartRanks[5] = ['rnb']
        self.chartRanks[6] = ['dance']
        
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
        if len(charts) == 0:
            raise ValueError("Could not find any charts: {0}".format(self.__dict__.keys()))
        print("  Using {0} Charts".format(len(charts)))
        return charts