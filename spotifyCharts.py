from ioUtils import getFile
from listUtils import getFlatList
from artistIgnores import getArtistIgnores

class spotifyCharts:
    def __init__(self):

        self.saudiarabia         = ['regional-sa-weekly']
        self.ireland             = ['regional-ie-weekly']
        self.argentina           = ['regional-ar-weekly']
        self.norway              = ['regional-no-weekly']
        self.india               = ['regional-in-weekly']
        self.morocco             = ['regional-ma-weekly']
        self.chile               = ['regional-cl-weekly']
        self.hungary             = ['regional-hu-weekly']
        self.switzerland         = ['regional-ch-weekly']
        self.russia              = ['regional-ru-weekly']
        self.luxembourg          = ['regional-lu-weekly']
        self.portugal            = ['regional-pt-weekly']
        self.bulgaria            = ['regional-bg-weekly']
        self.japan               = ['regional-jp-weekly']
        self.honduras            = ['regional-hn-weekly']
        self.sweden              = ['regional-se-weekly']
        self.vietnam             = ['regional-vn-weekly']
        self.romania             = ['regional-ro-weekly']
        self.hongkong            = ['regional-hk-weekly']
        self.ecuador             = ['regional-ec-weekly']
        self.costarica           = ['regional-cr-weekly']
        self.newzealand          = ['regional-nz-weekly']
        self.indonesia           = ['regional-id-weekly']
        self.unitedkingdom       = ['regional-gb-weekly']
        self.france              = ['regional-fr-weekly']
        self.slovakia            = ['regional-sk-weekly']
        self.peru                = ['regional-pe-weekly']
        self.panama              = ['regional-pa-weekly']
        self.lithuania           = ['regional-lt-weekly']
        self.brazil              = ['regional-br-weekly']
        self.ukraine             = ['regional-ua-weekly']
        self.greece              = ['regional-gr-weekly']
        self.italy               = ['regional-it-weekly']
        self.spain               = ['regional-es-weekly']
        self.finland             = ['regional-fi-weekly']
        self.egypt               = ['regional-eg-weekly']
        self.czechrepublic       = ['regional-cz-weekly']
        self.uraguay             = ['regional-uy-weekly']
        self.isreal              = ['regional-il-weekly']
        self.paraguay            = ['regional-py-weekly']
        self.dominicanrepublic   = ['regional-do-weekly']
        self.iceland             = ['regional-is-weekly']
        self.austria             = ['regional-at-weekly']
        self.denmark             = ['regional-dk-weekly']
        self.singapore           = ['regional-sg-weekly']
        self.nicaragua           = ['regional-ni-weekly']
        self.canada              = ['regional-ca-weekly']
        self.belgium             = ['regional-be-weekly']
        self.mexico              = ['regional-mx-weekly']
        self.turkey              = ['regional-tr-weekly']
        self.germany             = ['regional-de-weekly']
        self.colombia            = ['regional-co-weekly']
        self.taiwan              = ['regional-tw-weekly']
        self.unitedstates        = ['regional-us-weekly']
        self.unitedarabemirates  = ['regional-ae-weekly']
        self.guatemala           = ['regional-gt-weekly']
        self.poland              = ['regional-pl-weekly']
        self.elsalvador          = ['regional-sv-weekly']
        self.thailand            = ['regional-th-weekly']
        self.netherlands         = ['regional-nl-weekly']
        self.estonia             = ['regional-ee-weekly']
        self.philippines         = ['regional-ph-weekly']
        self.bolivia             = ['regional-bo-weekly']
        self.australia           = ['regional-au-weekly']
        self.malaysia            = ['regional-my-weekly']
        self.southafrica         = ['regional-za-weekly']
        self.latvia              = ['regional-lv-weekly']
        self.world               = ['regional-global-weekly']
        
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