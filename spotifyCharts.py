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
        self.egypt       = ['regional-eg-weekly']
        self.australia   = ['regional-au-weekly']
        self.phillipines = ['regional-ph-weekly']
        self.hongkong    = ['regional-hk-weekly']
        self.vietnam     = ['regional-vn-weekly']
        self.colombia    = ['regional-co-weekly']
        self.argentina   = ['regional-ar-weekly']
        self.turkey      = ['regional-tr-weekly']
        self.taiwan      = ['regional-tw-weekly']
        self.austria     = ['regional-at-weekly']
        self.greece      = ['regional-gr-weekly']
        self.ukraine     = ['regional-ua-weekly']
        self.uae         = ['regional-ae-weekly']
        self.indonesia   = ['regional-id-weekly']
        self.ireland     = ['regional-ie-weekly']
        self.iceland     = ['regional-is-weekly']
        self.bulgaria    = ['regional-bg-weekly']
        self.thailand    = ['regional-th-weekly']
        self.domincan    = ['regional-do-weekly']
        self.france      = ['regional-fr-weekly']
        self.germany     = ['regional-de-weekly']
        self.saudiarabia = ['regional-sa-weekly']
        self.finland     = ['regional-fi-weekly']
        self.sweden      = ['regional-se-weekly']
        
        self.chartNames = self.__dict__.keys()
        
        self.chartRanks = {}
        self.chartRanks[0] = ['us']
        self.chartRanks[1] = ['england', 'australia', 'ireland']
        self.chartRanks[2] = ['germany', 'austria']
        self.chartRanks[3] = ['italy', 'france']
        self.chartRanks[4] = ['finland', 'iceland']
        self.chartRanks[5] = ['denmark', 'sweden']
        self.chartRanks[6] = ['isreal', 'turkey', 'saudiarabia', 'uae', 'egypt']
        self.chartRanks[7] = ['russia', 'ukraine', 'bulgaria']
        self.chartRanks[8] = ['mexico', 'colombia', 'argentina', 'domincan']
        self.chartRanks[9] = ['japan', 'hongkong', 'vietnam', 'taiwan', 'thailand']
        self.chartRanks[10] = ['phillipines', 'greece', 'indonesia', 'india', 'southafrica']
        self.chartRanks[11] = ['brazil']
        self.chartRanks[12] = ['world']
        
        
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