from ioUtils import getFile
from listUtils import getFlatList
from artistIgnores import getArtistIgnores

class rateYourMusicScriptCharts:
    def __init__(self):
        self.c_Artists_Releases_with_Gujarati_script                                       = ['Artists_Releases_with_Gujarati_script']
        self.c_Artists_Releases_with_Gurmukhi_script                                       = ['Artists_Releases_with_Gurmukhi_script']
        self.c_Artists_Releases_with_Kannada_script                                        = ['Artists_Releases_with_Kannada_script']
        self.c_Artists_Releases_with_Khmer_script                                          = ['Artists_Releases_with_Khmer_script']
        self.c_Artists_Releases_with_Lao_script                                            = ['Artists_Releases_with_Lao_script']
        self.c_Artists_Releases_with_Malayalam_script                                      = ['Artists_Releases_with_Malayalam_script']
        self.c_Artists_Releases_with_NKo_script                                            = ['Artists_Releases_with_NKo_script']
        self.c_Artists_Releases_with_Oriya_script                                          = ['Artists_Releases_with_Oriya_script']
        self.c_Artists_Releases_with_Syriac_script                                         = ['Artists_Releases_with_Syriac_script']
        self.c_Artists_Releases_with_Telugu_script                                         = ['Artists_Releases_with_Telugu_script']
        self.c_Artists_Releases_with_Tibetan_script                                        = ['Artists_Releases_with_Tibetan_script']
        self.c_Artists_Releases_with_Tifinagh_script                                       = ['Artists_Releases_with_Tifinagh_script']
        self.c_Artists_with_Arabic_script                                                  = ['Artists_with_Arabic_script']
        self.c_Artists_with_Armenian_script                                                = ['Artists_with_Armenian_script']
        self.c_Artists_with_Bengali_script                                                 = ['Artists_with_Bengali_script']
        self.c_Artists_with_Burmese_script                                                 = ['Artists_with_Burmese_script']
        self.c_Artists_with_Devanagari_script                                              = ['Artists_with_Devanagari_script']
        self.c_Artists_with_Geez_script                                                    = ['Artists_with_Geez_script']
        self.c_Artists_with_Greek_script                                                   = ['Artists_with_Greek_script']
        self.c_Artists_with_Hangul_script                                                  = ['Artists_with_Hangul_script']
        self.c_Artists_with_Hebrew_script                                                  = ['Artists_with_Hebrew_script']
        self.c_Artists_with_Sinhala_script                                                 = ['Artists_with_Sinhala_script']
        self.c_Artists_with_Tamil_script                                                   = ['Artists_with_Tamil_script']
        self.c_Artists_with_Thai_script                                                    = ['Artists_with_Thai_script']
        self.c_Releases_with_Armenian_script                                               = ['Releases_with_Armenian_script']
        self.c_Releases_with_Devanagari_script                                             = ['Releases_with_Devanagari_script']
        self.c_Releases_with_Hangul_script                                                 = ['Releases_with_Hangul_script']


        self.chartNames = self.__dict__.keys()


        self.chartRanks = {}
        ######### Singles - Best #########
        ######### Singles - Worst #########
        ######### Albums - Best #########
        ######### Albums - Diverse #########
        ######### Albums - Esoteric #########
        ######### Albums - Worst #########
        ######### Mixes - Best #########
        ######### Mixes - Worst #########
        ######### Albums - Yearly #########
        ######### Singles - BestYearly #########
        ######### Singles - WorstYearly #########
        ######### Titles #########
        ######### Artists #########
        ######### Script #########
        self.chartRanks[0] = ['c_Artists_Releases_with_Gujarati_script', 'c_Artists_Releases_with_Gurmukhi_script']
        self.chartRanks[1] = ['c_Artists_Releases_with_Kannada_script', 'c_Artists_Releases_with_Khmer_script']
        self.chartRanks[2] = ['c_Artists_Releases_with_Lao_script', 'c_Artists_Releases_with_Malayalam_script']
        self.chartRanks[3] = ['c_Artists_Releases_with_NKo_script', 'c_Artists_Releases_with_Oriya_script']
        self.chartRanks[4] = ['c_Artists_Releases_with_Syriac_script', 'c_Artists_Releases_with_Telugu_script']
        self.chartRanks[5] = ['c_Artists_Releases_with_Tibetan_script', 'c_Artists_Releases_with_Tifinagh_script']
        self.chartRanks[6] = ['c_Artists_with_Arabic_script', 'c_Artists_with_Armenian_script']
        self.chartRanks[7] = ['c_Artists_with_Bengali_script', 'c_Artists_with_Burmese_script']
        self.chartRanks[8] = ['c_Artists_with_Devanagari_script', 'c_Artists_with_Geez_script']
        self.chartRanks[9] = ['c_Artists_with_Greek_script', 'c_Artists_with_Hangul_script']
        self.chartRanks[10] = ['c_Artists_with_Hebrew_script', 'c_Artists_with_Sinhala_script']
        self.chartRanks[11] = ['c_Artists_with_Tamil_script', 'c_Artists_with_Thai_script']
        self.chartRanks[12] = ['c_Releases_with_Armenian_script', 'c_Releases_with_Devanagari_script']
        self.chartRanks[13] = ['c_Releases_with_Hangul_script']
        ######### Other #########
        ######### Releases - Best #########
        ######### Releases - Worst #########   
        
        
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
