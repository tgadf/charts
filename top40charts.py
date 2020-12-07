from ioUtils import getFile
from artistIgnores import getArtistIgnores

class top40Charts:
    def __init__(self):

        self.usa = ['USA Singles Top 40', 'USA Albums']
        self.usa = [x.replace("/", " ") for x in self.usa]
        
        self.uk = ['UK Singles Top 40', 'UK Top 20 Albums', 'Canada Top 20']
        self.uk = [x.replace("/", " ") for x in self.uk]
        
        self.world = ['Top40-Charts.com Web Top 100', 'China Top 20', 'German Top 40', 'Japan Top 20', 'Australia Top 20', 'Brazil Top 20',
                      'Greece Top 20', 'New Zealand Top 20', 'Bulgaria Top 20', 'Portugal Top 20', 'Airplay World Official Top 100', 
                      'Argentina Top 20', 'Austria Top 20', 'Belgium Top 20', 'Chile Top 20', 'Denmark Top 20',
                      'Digital Sales Top 100', 'Europe Official Top 100', 'Finland Top 20', 'France Top 20', 'HeatSeekers Radio Tracks',
                      'Hispanic America Top 40', 'India Top 20', 'Ireland Top 20', 'Italy Top 20', 'Muchmusic Top 30', 'Netherlands Top 20',
                      'Norway Top 20', 'Russia Top 20', 'Spain Top 20', 'Sweden Top 20', 'Switzerland Top 20', 'Taiwan Top 10',
                      'Ukraine Top 20', 'World Adult Top 20 Singles', 'World Country Top 20 Singles', 'World Dance / Trance Top 30 Singles',
                      'World Jazz Top 20 Singles', 'World Latin Top 30 Singles', 'World Modern Rock Top 30 Singles', 'World RnB Top 30 Singles',
                      'World Singles Official Top 100', 'World Soundtracks / OST Top 20 Singles'] 
        self.world = [x.replace("/", " ") for x in self.world]
        
        self.chartNames = self.__dict__.keys()

        
        self.chartRanks = {}
        self.chartRanks[0] = ['usa']
        self.chartRanks[1] = ['uk']
        self.chartRanks[2] = ['world']
        
        
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