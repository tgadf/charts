from ioUtils import getFile
from listUtils import getFlatList
from artistIgnores import getArtistIgnores

class rateYourMusicCharts:
    def __init__(self):
        self.c_Best_albums_of_1950                                                         = ['Best_albums_of_1950']
        self.c_Best_albums_of_1951                                                         = ['Best_albums_of_1951']
        self.c_Best_albums_of_1952                                                         = ['Best_albums_of_1952']
        self.c_Best_albums_of_1953                                                         = ['Best_albums_of_1953']
        self.c_Best_albums_of_1954                                                         = ['Best_albums_of_1954']
        self.c_Best_albums_of_1955                                                         = ['Best_albums_of_1955']
        self.c_Best_albums_of_1956                                                         = ['Best_albums_of_1956']
        self.c_Best_albums_of_1957                                                         = ['Best_albums_of_1957']
        self.c_Best_albums_of_1958                                                         = ['Best_albums_of_1958']
        self.c_Best_albums_of_1959                                                         = ['Best_albums_of_1959']
        self.c_Best_albums_of_1960                                                         = ['Best_albums_of_1960']
        self.c_Best_albums_of_1961                                                         = ['Best_albums_of_1961']
        self.c_Best_albums_of_1962                                                         = ['Best_albums_of_1962']
        self.c_Best_albums_of_1963                                                         = ['Best_albums_of_1963']
        self.c_Best_albums_of_1964                                                         = ['Best_albums_of_1964']
        self.c_Best_albums_of_1965                                                         = ['Best_albums_of_1965']
        self.c_Best_albums_of_1966                                                         = ['Best_albums_of_1966']
        self.c_Best_albums_of_1967                                                         = ['Best_albums_of_1967']
        self.c_Best_albums_of_1968                                                         = ['Best_albums_of_1968']
        self.c_Best_albums_of_1969                                                         = ['Best_albums_of_1969']
        self.c_Best_albums_of_1970                                                         = ['Best_albums_of_1970']
        self.c_Best_albums_of_1971                                                         = ['Best_albums_of_1971']
        self.c_Best_albums_of_1972                                                         = ['Best_albums_of_1972']
        self.c_Best_albums_of_1973                                                         = ['Best_albums_of_1973']
        self.c_Best_albums_of_1974                                                         = ['Best_albums_of_1974']
        self.c_Best_albums_of_1975                                                         = ['Best_albums_of_1975']
        self.c_Best_albums_of_1976                                                         = ['Best_albums_of_1976']
        self.c_Best_albums_of_1977                                                         = ['Best_albums_of_1977']
        self.c_Best_albums_of_1978                                                         = ['Best_albums_of_1978']
        self.c_Best_albums_of_1979                                                         = ['Best_albums_of_1979']
        self.c_Best_albums_of_1980                                                         = ['Best_albums_of_1980']
        self.c_Best_albums_of_1981                                                         = ['Best_albums_of_1981']
        self.c_Best_albums_of_1982                                                         = ['Best_albums_of_1982']
        self.c_Best_albums_of_1983                                                         = ['Best_albums_of_1983']
        self.c_Best_albums_of_1984                                                         = ['Best_albums_of_1984']
        self.c_Best_albums_of_1985                                                         = ['Best_albums_of_1985']
        self.c_Best_albums_of_1986                                                         = ['Best_albums_of_1986']
        self.c_Best_albums_of_1987                                                         = ['Best_albums_of_1987']
        self.c_Best_albums_of_1988                                                         = ['Best_albums_of_1988']
        self.c_Best_albums_of_1989                                                         = ['Best_albums_of_1989']
        self.c_Best_albums_of_1990                                                         = ['Best_albums_of_1990']
        self.c_Best_albums_of_1991                                                         = ['Best_albums_of_1991']
        self.c_Best_albums_of_1992                                                         = ['Best_albums_of_1992']
        self.c_Best_albums_of_1993                                                         = ['Best_albums_of_1993']
        self.c_Best_albums_of_1994                                                         = ['Best_albums_of_1994']
        self.c_Best_albums_of_1995                                                         = ['Best_albums_of_1995']
        self.c_Best_albums_of_1996                                                         = ['Best_albums_of_1996']
        self.c_Best_albums_of_1997                                                         = ['Best_albums_of_1997']
        self.c_Best_albums_of_1998                                                         = ['Best_albums_of_1998']
        self.c_Best_albums_of_1999                                                         = ['Best_albums_of_1999']
        self.c_Best_albums_of_2000                                                         = ['Best_albums_of_2000']
        self.c_Best_albums_of_2001                                                         = ['Best_albums_of_2001']
        self.c_Best_albums_of_2002                                                         = ['Best_albums_of_2002']
        self.c_Best_albums_of_2003                                                         = ['Best_albums_of_2003']
        self.c_Best_albums_of_2004                                                         = ['Best_albums_of_2004']
        self.c_Best_albums_of_2005                                                         = ['Best_albums_of_2005']
        self.c_Best_albums_of_2006                                                         = ['Best_albums_of_2006']
        self.c_Best_albums_of_2007                                                         = ['Best_albums_of_2007']
        self.c_Best_albums_of_2008                                                         = ['Best_albums_of_2008']
        self.c_Best_albums_of_2009                                                         = ['Best_albums_of_2009']
        self.c_Best_albums_of_2010                                                         = ['Best_albums_of_2010']
        self.c_Best_albums_of_2011                                                         = ['Best_albums_of_2011']
        self.c_Best_albums_of_2012                                                         = ['Best_albums_of_2012']
        self.c_Best_albums_of_2013                                                         = ['Best_albums_of_2013']
        self.c_Best_albums_of_2014                                                         = ['Best_albums_of_2014']
        self.c_Best_albums_of_2015                                                         = ['Best_albums_of_2015']
        self.c_Best_albums_of_2016                                                         = ['Best_albums_of_2016']
        self.c_Best_albums_of_2017                                                         = ['Best_albums_of_2017']
        self.c_Best_albums_of_2018                                                         = ['Best_albums_of_2018']
        self.c_Best_albums_of_2019                                                         = ['Best_albums_of_2019']
        self.c_Best_albums_of_2020                                                         = ['Best_albums_of_2020']
        self.c_Best_albums_of_the_1900s                                                    = ['Best_albums_of_the_1900s']
        self.c_Best_albums_of_the_1910s                                                    = ['Best_albums_of_the_1910s']
        self.c_Best_albums_of_the_1920s                                                    = ['Best_albums_of_the_1920s']
        self.c_Best_albums_of_the_1930s                                                    = ['Best_albums_of_the_1930s']
        self.c_Best_albums_of_the_1940s                                                    = ['Best_albums_of_the_1940s']
        self.c_Best_albums_of_the_1950s                                                    = ['Best_albums_of_the_1950s']
        self.c_Best_albums_of_the_1960s                                                    = ['Best_albums_of_the_1960s']
        self.c_Best_albums_of_the_1970s                                                    = ['Best_albums_of_the_1970s']
        self.c_Best_albums_of_the_1980s                                                    = ['Best_albums_of_the_1980s']
        self.c_Best_albums_of_the_1990s                                                    = ['Best_albums_of_the_1990s']
        self.c_Best_albums_of_the_2000s                                                    = ['Best_albums_of_the_2000s']
        self.c_Best_albums_of_the_2010s                                                    = ['Best_albums_of_the_2010s']
        self.c_Bottom_Mixes_of_the_1980s                                                   = ['Bottom_Mixes_of_the_1980s']
        self.c_Bottom_Mixes_of_the_1990s                                                   = ['Bottom_Mixes_of_the_1990s']
        self.c_Bottom_Mixes_of_the_2000s                                                   = ['Bottom_Mixes_of_the_2000s']
        self.c_Bottom_Mixes_of_the_2010s                                                   = ['Bottom_Mixes_of_the_2010s']
        self.c_Bottom_Releases_of_the_1950s                                                = ['Bottom_Releases_of_the_1950s']
        self.c_Bottom_Releases_of_the_1960s                                                = ['Bottom_Releases_of_the_1960s']
        self.c_Bottom_Releases_of_the_1970s                                                = ['Bottom_Releases_of_the_1970s']
        self.c_Bottom_Releases_of_the_1980s                                                = ['Bottom_Releases_of_the_1980s']
        self.c_Bottom_Releases_of_the_1990s                                                = ['Bottom_Releases_of_the_1990s']
        self.c_Bottom_Releases_of_the_2000s                                                = ['Bottom_Releases_of_the_2000s']
        self.c_Bottom_Releases_of_the_2010s                                                = ['Bottom_Releases_of_the_2010s']
        self.c_Diverse_albums_of_the_1950s                                                 = ['Diverse_albums_of_the_1950s']
        self.c_Diverse_albums_of_the_1960s                                                 = ['Diverse_albums_of_the_1960s']
        self.c_Diverse_albums_of_the_1970s                                                 = ['Diverse_albums_of_the_1970s']
        self.c_Diverse_albums_of_the_1980s                                                 = ['Diverse_albums_of_the_1980s']
        self.c_Diverse_albums_of_the_1990s                                                 = ['Diverse_albums_of_the_1990s']
        self.c_Diverse_albums_of_the_2000s                                                 = ['Diverse_albums_of_the_2000s']
        self.c_Diverse_albums_of_the_2010s                                                 = ['Diverse_albums_of_the_2010s']
        self.c_Esoteric_albums_of_the_1950s                                                = ['Esoteric_albums_of_the_1950s']
        self.c_Esoteric_albums_of_the_1960s                                                = ['Esoteric_albums_of_the_1960s']
        self.c_Esoteric_albums_of_the_1970s                                                = ['Esoteric_albums_of_the_1970s']
        self.c_Esoteric_albums_of_the_1980s                                                = ['Esoteric_albums_of_the_1980s']
        self.c_Esoteric_albums_of_the_1990s                                                = ['Esoteric_albums_of_the_1990s']
        self.c_Esoteric_albums_of_the_2000s                                                = ['Esoteric_albums_of_the_2000s']
        self.c_Esoteric_albums_of_the_2010s                                                = ['Esoteric_albums_of_the_2010s']
        self.c_Top_Mixes_of_the_1980s                                                      = ['Top_Mixes_of_the_1980s']
        self.c_Top_Mixes_of_the_1990s                                                      = ['Top_Mixes_of_the_1990s']
        self.c_Top_Mixes_of_the_2000s                                                      = ['Top_Mixes_of_the_2000s']
        self.c_Top_Mixes_of_the_2010s                                                      = ['Top_Mixes_of_the_2010s']
        self.c_Top_Releases_of_the_1950s                                                   = ['Top_Releases_of_the_1950s']
        self.c_Top_Releases_of_the_1960s                                                   = ['Top_Releases_of_the_1960s']
        self.c_Top_Releases_of_the_1970s                                                   = ['Top_Releases_of_the_1970s']
        self.c_Top_Releases_of_the_1980s                                                   = ['Top_Releases_of_the_1980s']
        self.c_Top_Releases_of_the_1990s                                                   = ['Top_Releases_of_the_1990s']
        self.c_Top_Releases_of_the_2000s                                                   = ['Top_Releases_of_the_2000s']
        self.c_Top_Releases_of_the_2010s                                                   = ['Top_Releases_of_the_2010s']
        self.c_Worst_albums_of_the_1900s                                                   = ['Worst_albums_of_the_1900s']
        self.c_Worst_albums_of_the_1910s                                                   = ['Worst_albums_of_the_1910s']
        self.c_Worst_albums_of_the_1920s                                                   = ['Worst_albums_of_the_1920s']
        self.c_Worst_albums_of_the_1930s                                                   = ['Worst_albums_of_the_1930s']
        self.c_Worst_albums_of_the_1940s                                                   = ['Worst_albums_of_the_1940s']
        self.c_Worst_albums_of_the_1950s                                                   = ['Worst_albums_of_the_1950s']
        self.c_Worst_albums_of_the_1960s                                                   = ['Worst_albums_of_the_1960s']
        self.c_Worst_albums_of_the_1970s                                                   = ['Worst_albums_of_the_1970s']
        self.c_Worst_albums_of_the_1980s                                                   = ['Worst_albums_of_the_1980s']
        self.c_Worst_albums_of_the_1990s                                                   = ['Worst_albums_of_the_1990s']
        self.c_Worst_albums_of_the_2000s                                                   = ['Worst_albums_of_the_2000s']
        self.c_Worst_albums_of_the_2010s                                                   = ['Worst_albums_of_the_2010s']


        self.chartNames = self.__dict__.keys()


        self.chartRanks = {}
        ######### Singles - Best #########
        ######### Singles - Worst #########
        ######### Albums - Best #########
        self.chartRanks[0] = ['c_Best_albums_of_the_1900s', 'c_Best_albums_of_the_1910s', 'c_Best_albums_of_the_1920s']
        self.chartRanks[1] = ['c_Best_albums_of_the_1930s', 'c_Best_albums_of_the_1940s', 'c_Best_albums_of_the_1950s']
        self.chartRanks[2] = ['c_Best_albums_of_the_1960s', 'c_Best_albums_of_the_1970s', 'c_Best_albums_of_the_1980s']
        self.chartRanks[3] = ['c_Best_albums_of_the_1990s', 'c_Best_albums_of_the_2000s', 'c_Best_albums_of_the_2010s']
        ######### Albums - Diverse #########
        self.chartRanks[4] = ['c_Diverse_albums_of_the_1950s', 'c_Diverse_albums_of_the_1960s', 'c_Diverse_albums_of_the_1970s']
        self.chartRanks[5] = ['c_Diverse_albums_of_the_1980s', 'c_Diverse_albums_of_the_1990s', 'c_Diverse_albums_of_the_2000s']
        self.chartRanks[6] = ['c_Diverse_albums_of_the_2010s']
        ######### Albums - Esoteric #########
        self.chartRanks[7] = ['c_Esoteric_albums_of_the_1950s', 'c_Esoteric_albums_of_the_1960s', 'c_Esoteric_albums_of_the_1970s']
        self.chartRanks[8] = ['c_Esoteric_albums_of_the_1980s', 'c_Esoteric_albums_of_the_1990s', 'c_Esoteric_albums_of_the_2000s']
        self.chartRanks[9] = ['c_Esoteric_albums_of_the_2010s']
        ######### Albums - Worst #########
        self.chartRanks[10] = ['c_Worst_albums_of_the_1900s', 'c_Worst_albums_of_the_1910s', 'c_Worst_albums_of_the_1920s']
        self.chartRanks[11] = ['c_Worst_albums_of_the_1930s', 'c_Worst_albums_of_the_1940s', 'c_Worst_albums_of_the_1950s']
        self.chartRanks[12] = ['c_Worst_albums_of_the_1960s', 'c_Worst_albums_of_the_1970s', 'c_Worst_albums_of_the_1980s']
        self.chartRanks[13] = ['c_Worst_albums_of_the_1990s', 'c_Worst_albums_of_the_2000s', 'c_Worst_albums_of_the_2010s']
        ######### Mixes - Best #########
        self.chartRanks[14] = ['c_Top_Mixes_of_the_1980s', 'c_Top_Mixes_of_the_1990s', 'c_Top_Mixes_of_the_2000s', 'c_Top_Mixes_of_the_2010s']
        ######### Mixes - Worst #########
        self.chartRanks[15] = ['c_Bottom_Mixes_of_the_1980s', 'c_Bottom_Mixes_of_the_1990s', 'c_Bottom_Mixes_of_the_2000s', 'c_Bottom_Mixes_of_the_2010s']
        ######### Albums - Yearly #########
        self.chartRanks[16] = ['c_Best_albums_of_1950', 'c_Best_albums_of_1951', 'c_Best_albums_of_1952', 'c_Best_albums_of_1953', 'c_Best_albums_of_1954']
        self.chartRanks[17] = ['c_Best_albums_of_1955', 'c_Best_albums_of_1956', 'c_Best_albums_of_1957', 'c_Best_albums_of_1958', 'c_Best_albums_of_1959']
        self.chartRanks[18] = ['c_Best_albums_of_1960', 'c_Best_albums_of_1961', 'c_Best_albums_of_1962', 'c_Best_albums_of_1963', 'c_Best_albums_of_1964']
        self.chartRanks[19] = ['c_Best_albums_of_1965', 'c_Best_albums_of_1966', 'c_Best_albums_of_1967', 'c_Best_albums_of_1968', 'c_Best_albums_of_1969']
        self.chartRanks[20] = ['c_Best_albums_of_1970', 'c_Best_albums_of_1971', 'c_Best_albums_of_1972', 'c_Best_albums_of_1973', 'c_Best_albums_of_1974']
        self.chartRanks[21] = ['c_Best_albums_of_1975', 'c_Best_albums_of_1976', 'c_Best_albums_of_1977', 'c_Best_albums_of_1978', 'c_Best_albums_of_1979']
        self.chartRanks[22] = ['c_Best_albums_of_1980', 'c_Best_albums_of_1981', 'c_Best_albums_of_1982', 'c_Best_albums_of_1983', 'c_Best_albums_of_1984']
        self.chartRanks[23] = ['c_Best_albums_of_1985', 'c_Best_albums_of_1986', 'c_Best_albums_of_1987', 'c_Best_albums_of_1988', 'c_Best_albums_of_1989']
        self.chartRanks[24] = ['c_Best_albums_of_1990', 'c_Best_albums_of_1991', 'c_Best_albums_of_1992', 'c_Best_albums_of_1993', 'c_Best_albums_of_1994']
        self.chartRanks[25] = ['c_Best_albums_of_1995', 'c_Best_albums_of_1996', 'c_Best_albums_of_1997', 'c_Best_albums_of_1998', 'c_Best_albums_of_1999']
        self.chartRanks[26] = ['c_Best_albums_of_2000', 'c_Best_albums_of_2001', 'c_Best_albums_of_2002', 'c_Best_albums_of_2003', 'c_Best_albums_of_2004']
        self.chartRanks[27] = ['c_Best_albums_of_2005', 'c_Best_albums_of_2006', 'c_Best_albums_of_2007', 'c_Best_albums_of_2008', 'c_Best_albums_of_2009']
        self.chartRanks[28] = ['c_Best_albums_of_2010', 'c_Best_albums_of_2011', 'c_Best_albums_of_2012', 'c_Best_albums_of_2013', 'c_Best_albums_of_2014']
        self.chartRanks[29] = ['c_Best_albums_of_2015', 'c_Best_albums_of_2016', 'c_Best_albums_of_2017', 'c_Best_albums_of_2018', 'c_Best_albums_of_2019']
        self.chartRanks[30] = ['c_Best_albums_of_2020']
        ######### Singles - BestYearly #########
        ######### Singles - WorstYearly #########
        ######### Titles #########
        ######### Artists #########
        ######### Script #########
        ######### Other #########
        ######### Releases - Best #########
        self.chartRanks[31] = ['c_Top_Releases_of_the_1950s', 'c_Top_Releases_of_the_1960s', 'c_Top_Releases_of_the_1970s', 'c_Top_Releases_of_the_1980s', 'c_Top_Releases_of_the_1990s', 'c_Top_Releases_of_the_2000s']
        self.chartRanks[32] = ['c_Top_Releases_of_the_2010s']
        ######### Releases - Worst #########
        self.chartRanks[33] = ['c_Bottom_Releases_of_the_1950s', 'c_Bottom_Releases_of_the_1960s', 'c_Bottom_Releases_of_the_1970s', 'c_Bottom_Releases_of_the_1980s', 'c_Bottom_Releases_of_the_1990s', 'c_Bottom_Releases_of_the_2000s']
        self.chartRanks[34] = ['c_Bottom_Releases_of_the_2010s'] 
        
        
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
