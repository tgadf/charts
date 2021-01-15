from ioUtils import getFile
from artistIgnores import getArtistIgnores

class billboardCharts:
    def __init__(self):

        self.adult =  ['adult-contemporary','adult-pop-songs']
        self.adult += ["ASI", "ATF"]

        self.alternative =  ['alternative-albums', 'alternative-songs']
        self.alternative += ["MRT", "ALT"]

        self.folkblue = ['americana-folk-albums', 'bluegrass-albums', 'blues-albums']
        self.folkblue = ["BLU", "BGR", "FLK"]

        self.christian  = ['christian-airplay', 'hot-christian-songs', 'christian-albums', 'christian-digital-song-sales', 'christian-songs', 'christian-streaming-songs']
        self.christian += ['gospel-airplay', 'gospel-albums', 'gospel-digital-song-sales', 'gospel-songs', 'gospel-streaming-songs']
        self.christian += ["CRI", "CRT", "ICO", "ILL", "SLL", "GOS", "GSI", "GSS", "CHS", "GDT"]

        self.countryMusic  = ['country-airplay', 'country-albums', 'country-digital-song-sales', 'country-songs', 'country-streaming-songs']
        self.countryMusic += ["CSA", "CSI", "CST", "CLP", "CDT"]

        self.electronic  = ['dance-club-play-songs', 'dance-electronic-albums', 'dance-electronic-digital-song-sales', 'dance-electronic-songs', 'dance-electronic-streaming-songs']
        self.electronic += ["DAN", "DAS", "DDT", "BSI", "BST", "DSI", "ELP"]
        
        self.hot  = ['hot-100', 'pop-songs', 'radio-songs']
        self.hot += ['streaming-songs', 'rhythmic-40', 'heatseekers-albums']    
        self.top  = ['billboard-200', 'artist-100', 'top-album-sales']
        self.hot += self.top
        self.hot += ["TLN", "HSB", "HSI", "TLP", "TSL", "TFM", "ATS"]

        self.rnb  = ['r-and-b-albums', 'r-and-b-hip-hop-digital-song-sales', 'r-and-b-hip-hop-streaming-songs', 'r-and-b-songs', 'r-b-hip-hop-albums', 'r-b-hip-hop-songs']
        self.rnb += ['rap-albums','rap-song', 'hot-r-and-b-hip-hop-airplay']
        self.rnb += ["RLP", "RAP", "RBL", "RBM", "RBS", "RBT", "BLP"]

        self.rock  = ['rock-airplay','hot-mainstream-rock-tracks', 'rock-albums','rock-digital-song-sales','rock-songs','rock-streaming-songs', 'hard-rock-albums']
        self.rock += ["RCK", "RKA", "RKT", "ROS", "RTT", "MTL", "ARK"]

        self.canadian = ['canadian-albums','canadian-hot-100']
        self.canadian += ["CAN", "CNA"]
        self.latin    = ['latin-airplay','latin-albums','latin-digital-song-sales','latin-pop-albums','latin-pop-songs','latin-songs','latin-streaming-songs']
        self.latin   += ["HTA", "HTL", "LSS", "LDT", "LPO", "LPP", "LCM"]
        self.mexican  = ['regional-mexican-albums','regional-mexican-songs']
        self.mexican += ["LRM", "LMX"]
        self.world    = ['china-v-chart', 'japan-hot-100','tropical-albums', 'tropical-songs','world-albums', 'reggae-albums']
        self.world   += ["LSA", "LTS", "JPN", "WLP", "JAH", "ARG"]

        self.holiday  = ['holiday-albums','holiday-season-digital-song-sales','holiday-songs','holiday-streaming-songs']
        self.holiday += ['XSS', "XML", "XDT", "ASX"]

        self.classical  = ['classical-albums']
        self.classical += ['COA']

        self.jazz  = ['jazz-albums', 'jazz-songs']
        self.jazz += ['JLS', 'JSI']

        self.comedy  = ['comedy-albums']
        self.comedy += ['GIG']

        self.newage  = ['new-age-albums']
        self.newage += ['NLP']

        self.general = ['digital-albums','digital-song-sales']
        self.general = ['HDS', 'DLP']

        self.kids  = ['kids-albums']
        self.kids += ['KID']

        self.twitter  = ['twitter-emerging-artists', 'twitter-top-tracks', 'social-50']
        self.twitter += ['STM', 'SOC']

        self.vinyl  = ['vinyl-albums', "catalog-albums", 'tastemaker-albums']
        self.vinyl += ["TAS", "VNL", "TLC"]

        self.rare  = ['independent-albums']
        self.rare += ['IND']

        self.soundtrack  = ['soundtracks']
        self.soundtrack += ["STX"]
        
        self.chartNames = self.__dict__.keys()

        
        self.chartRanks = {}
        self.chartRanks[0] = ['top']
        self.chartRanks[1] = ['hot', 'adult']
        self.chartRanks[2] = ['alternative', 'countryMusic', 'rock', 'rnb']
        self.chartRanks[3] = ['christian', 'canadian', 'comedy', 'general', 'twitter']
        self.chartRanks[4] = ['folkblue', 'electronic', 'latin', 'mexican', 'world', 'classical', 'jazz', 'newage', 'kids', 'vinyl', 'rare', 'soundtrack', 'holiday']
        
        
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
            if name in self.__dict__.keys():
                charts += self.__dict__[name]
            if name == "country":
                charts += self.__dict__["countryMusic"]                
        if len(charts) == 0:
            raise ValueError("Could not find any charts: {0}".format(self.__dict__.keys()))
        print("  Using {0} Charts".format(len(charts)))
        return charts