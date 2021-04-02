from ioUtils import getFile
from listUtils import getFlatList
from artistIgnores import getArtistIgnores

class rateYourMusicSongCharts:
    def __init__(self):
        self.c_Best_singles_of_1945                                                        = ['Best_singles_of_1945']
        self.c_Best_singles_of_1946                                                        = ['Best_singles_of_1946']
        self.c_Best_singles_of_1947                                                        = ['Best_singles_of_1947']
        self.c_Best_singles_of_1948                                                        = ['Best_singles_of_1948']
        self.c_Best_singles_of_1949                                                        = ['Best_singles_of_1949']
        self.c_Best_singles_of_1950                                                        = ['Best_singles_of_1950']
        self.c_Best_singles_of_1951                                                        = ['Best_singles_of_1951']
        self.c_Best_singles_of_1952                                                        = ['Best_singles_of_1952']
        self.c_Best_singles_of_1953                                                        = ['Best_singles_of_1953']
        self.c_Best_singles_of_1954                                                        = ['Best_singles_of_1954']
        self.c_Best_singles_of_1955                                                        = ['Best_singles_of_1955']
        self.c_Best_singles_of_1956                                                        = ['Best_singles_of_1956']
        self.c_Best_singles_of_1957                                                        = ['Best_singles_of_1957']
        self.c_Best_singles_of_1958                                                        = ['Best_singles_of_1958']
        self.c_Best_singles_of_1959                                                        = ['Best_singles_of_1959']
        self.c_Best_singles_of_1960                                                        = ['Best_singles_of_1960']
        self.c_Best_singles_of_1961                                                        = ['Best_singles_of_1961']
        self.c_Best_singles_of_1962                                                        = ['Best_singles_of_1962']
        self.c_Best_singles_of_1963                                                        = ['Best_singles_of_1963']
        self.c_Best_singles_of_1964                                                        = ['Best_singles_of_1964']
        self.c_Best_singles_of_1965                                                        = ['Best_singles_of_1965']
        self.c_Best_singles_of_1966                                                        = ['Best_singles_of_1966']
        self.c_Best_singles_of_1967                                                        = ['Best_singles_of_1967']
        self.c_Best_singles_of_1968                                                        = ['Best_singles_of_1968']
        self.c_Best_singles_of_1969                                                        = ['Best_singles_of_1969']
        self.c_Best_singles_of_1970                                                        = ['Best_singles_of_1970']
        self.c_Best_singles_of_1971                                                        = ['Best_singles_of_1971']
        self.c_Best_singles_of_1972                                                        = ['Best_singles_of_1972']
        self.c_Best_singles_of_1973                                                        = ['Best_singles_of_1973']
        self.c_Best_singles_of_1974                                                        = ['Best_singles_of_1974']
        self.c_Best_singles_of_1975                                                        = ['Best_singles_of_1975']
        self.c_Best_singles_of_1976                                                        = ['Best_singles_of_1976']
        self.c_Best_singles_of_1977                                                        = ['Best_singles_of_1977']
        self.c_Best_singles_of_1978                                                        = ['Best_singles_of_1978']
        self.c_Best_singles_of_1979                                                        = ['Best_singles_of_1979']
        self.c_Best_singles_of_1980                                                        = ['Best_singles_of_1980']
        self.c_Best_singles_of_1981                                                        = ['Best_singles_of_1981']
        self.c_Best_singles_of_1982                                                        = ['Best_singles_of_1982']
        self.c_Best_singles_of_1983                                                        = ['Best_singles_of_1983']
        self.c_Best_singles_of_1984                                                        = ['Best_singles_of_1984']
        self.c_Best_singles_of_1985                                                        = ['Best_singles_of_1985']
        self.c_Best_singles_of_1986                                                        = ['Best_singles_of_1986']
        self.c_Best_singles_of_1987                                                        = ['Best_singles_of_1987']
        self.c_Best_singles_of_1988                                                        = ['Best_singles_of_1988']
        self.c_Best_singles_of_1989                                                        = ['Best_singles_of_1989']
        self.c_Best_singles_of_1990                                                        = ['Best_singles_of_1990']
        self.c_Best_singles_of_1991                                                        = ['Best_singles_of_1991']
        self.c_Best_singles_of_1992                                                        = ['Best_singles_of_1992']
        self.c_Best_singles_of_1993                                                        = ['Best_singles_of_1993']
        self.c_Best_singles_of_1994                                                        = ['Best_singles_of_1994']
        self.c_Best_singles_of_1995                                                        = ['Best_singles_of_1995']
        self.c_Best_singles_of_1996                                                        = ['Best_singles_of_1996']
        self.c_Best_singles_of_1997                                                        = ['Best_singles_of_1997']
        self.c_Best_singles_of_1998                                                        = ['Best_singles_of_1998']
        self.c_Best_singles_of_1999                                                        = ['Best_singles_of_1999']
        self.c_Best_singles_of_2000                                                        = ['Best_singles_of_2000']
        self.c_Best_singles_of_2001                                                        = ['Best_singles_of_2001']
        self.c_Best_singles_of_2002                                                        = ['Best_singles_of_2002']
        self.c_Best_singles_of_2003                                                        = ['Best_singles_of_2003']
        self.c_Best_singles_of_2004                                                        = ['Best_singles_of_2004']
        self.c_Best_singles_of_2005                                                        = ['Best_singles_of_2005']
        self.c_Best_singles_of_2006                                                        = ['Best_singles_of_2006']
        self.c_Best_singles_of_2007                                                        = ['Best_singles_of_2007']
        self.c_Best_singles_of_2008                                                        = ['Best_singles_of_2008']
        self.c_Best_singles_of_2009                                                        = ['Best_singles_of_2009']
        self.c_Best_singles_of_2010                                                        = ['Best_singles_of_2010']
        self.c_Best_singles_of_2011                                                        = ['Best_singles_of_2011']
        self.c_Best_singles_of_2012                                                        = ['Best_singles_of_2012']
        self.c_Best_singles_of_2013                                                        = ['Best_singles_of_2013']
        self.c_Best_singles_of_2014                                                        = ['Best_singles_of_2014']
        self.c_Best_singles_of_2015                                                        = ['Best_singles_of_2015']
        self.c_Best_singles_of_2016                                                        = ['Best_singles_of_2016']
        self.c_Best_singles_of_2017                                                        = ['Best_singles_of_2017']
        self.c_Best_singles_of_2018                                                        = ['Best_singles_of_2018']
        self.c_Best_singles_of_2019                                                        = ['Best_singles_of_2019']
        self.c_Best_singles_of_2020                                                        = ['Best_singles_of_2020']
        self.c_Best_singles_of_the_1890s                                                   = ['Best_singles_of_the_1890s']
        self.c_Best_singles_of_the_1900s                                                   = ['Best_singles_of_the_1900s']
        self.c_Best_singles_of_the_1910s                                                   = ['Best_singles_of_the_1910s']
        self.c_Best_singles_of_the_1920s                                                   = ['Best_singles_of_the_1920s']
        self.c_Best_singles_of_the_1930s                                                   = ['Best_singles_of_the_1930s']
        self.c_Best_singles_of_the_1940s                                                   = ['Best_singles_of_the_1940s']
        self.c_Best_singles_of_the_1950s                                                   = ['Best_singles_of_the_1950s']
        self.c_Best_singles_of_the_1960s                                                   = ['Best_singles_of_the_1960s']
        self.c_Best_singles_of_the_1970s                                                   = ['Best_singles_of_the_1970s']
        self.c_Best_singles_of_the_1980s                                                   = ['Best_singles_of_the_1980s']
        self.c_Best_singles_of_the_1990s                                                   = ['Best_singles_of_the_1990s']
        self.c_Best_singles_of_the_2000s                                                   = ['Best_singles_of_the_2000s']
        self.c_Best_singles_of_the_2010s                                                   = ['Best_singles_of_the_2010s']
        self.c_Worst_singles_of_1950                                                       = ['Worst_singles_of_1950']
        self.c_Worst_singles_of_1951                                                       = ['Worst_singles_of_1951']
        self.c_Worst_singles_of_1952                                                       = ['Worst_singles_of_1952']
        self.c_Worst_singles_of_1953                                                       = ['Worst_singles_of_1953']
        self.c_Worst_singles_of_1954                                                       = ['Worst_singles_of_1954']
        self.c_Worst_singles_of_1955                                                       = ['Worst_singles_of_1955']
        self.c_Worst_singles_of_1956                                                       = ['Worst_singles_of_1956']
        self.c_Worst_singles_of_1957                                                       = ['Worst_singles_of_1957']
        self.c_Worst_singles_of_1958                                                       = ['Worst_singles_of_1958']
        self.c_Worst_singles_of_1959                                                       = ['Worst_singles_of_1959']
        self.c_Worst_singles_of_1960                                                       = ['Worst_singles_of_1960']
        self.c_Worst_singles_of_1961                                                       = ['Worst_singles_of_1961']
        self.c_Worst_singles_of_1962                                                       = ['Worst_singles_of_1962']
        self.c_Worst_singles_of_1963                                                       = ['Worst_singles_of_1963']
        self.c_Worst_singles_of_1964                                                       = ['Worst_singles_of_1964']
        self.c_Worst_singles_of_1965                                                       = ['Worst_singles_of_1965']
        self.c_Worst_singles_of_1966                                                       = ['Worst_singles_of_1966']
        self.c_Worst_singles_of_1967                                                       = ['Worst_singles_of_1967']
        self.c_Worst_singles_of_1968                                                       = ['Worst_singles_of_1968']
        self.c_Worst_singles_of_1969                                                       = ['Worst_singles_of_1969']
        self.c_Worst_singles_of_1970                                                       = ['Worst_singles_of_1970']
        self.c_Worst_singles_of_1971                                                       = ['Worst_singles_of_1971']
        self.c_Worst_singles_of_1972                                                       = ['Worst_singles_of_1972']
        self.c_Worst_singles_of_1973                                                       = ['Worst_singles_of_1973']
        self.c_Worst_singles_of_1974                                                       = ['Worst_singles_of_1974']
        self.c_Worst_singles_of_1975                                                       = ['Worst_singles_of_1975']
        self.c_Worst_singles_of_1976                                                       = ['Worst_singles_of_1976']
        self.c_Worst_singles_of_1977                                                       = ['Worst_singles_of_1977']
        self.c_Worst_singles_of_1978                                                       = ['Worst_singles_of_1978']
        self.c_Worst_singles_of_1979                                                       = ['Worst_singles_of_1979']
        self.c_Worst_singles_of_1980                                                       = ['Worst_singles_of_1980']
        self.c_Worst_singles_of_1981                                                       = ['Worst_singles_of_1981']
        self.c_Worst_singles_of_1982                                                       = ['Worst_singles_of_1982']
        self.c_Worst_singles_of_1983                                                       = ['Worst_singles_of_1983']
        self.c_Worst_singles_of_1984                                                       = ['Worst_singles_of_1984']
        self.c_Worst_singles_of_1985                                                       = ['Worst_singles_of_1985']
        self.c_Worst_singles_of_1986                                                       = ['Worst_singles_of_1986']
        self.c_Worst_singles_of_1987                                                       = ['Worst_singles_of_1987']
        self.c_Worst_singles_of_1988                                                       = ['Worst_singles_of_1988']
        self.c_Worst_singles_of_1989                                                       = ['Worst_singles_of_1989']
        self.c_Worst_singles_of_1990                                                       = ['Worst_singles_of_1990']
        self.c_Worst_singles_of_1991                                                       = ['Worst_singles_of_1991']
        self.c_Worst_singles_of_1992                                                       = ['Worst_singles_of_1992']
        self.c_Worst_singles_of_1993                                                       = ['Worst_singles_of_1993']
        self.c_Worst_singles_of_1994                                                       = ['Worst_singles_of_1994']
        self.c_Worst_singles_of_1995                                                       = ['Worst_singles_of_1995']
        self.c_Worst_singles_of_1996                                                       = ['Worst_singles_of_1996']
        self.c_Worst_singles_of_1997                                                       = ['Worst_singles_of_1997']
        self.c_Worst_singles_of_1998                                                       = ['Worst_singles_of_1998']
        self.c_Worst_singles_of_1999                                                       = ['Worst_singles_of_1999']
        self.c_Worst_singles_of_2000                                                       = ['Worst_singles_of_2000']
        self.c_Worst_singles_of_2001                                                       = ['Worst_singles_of_2001']
        self.c_Worst_singles_of_2002                                                       = ['Worst_singles_of_2002']
        self.c_Worst_singles_of_2003                                                       = ['Worst_singles_of_2003']
        self.c_Worst_singles_of_2004                                                       = ['Worst_singles_of_2004']
        self.c_Worst_singles_of_2005                                                       = ['Worst_singles_of_2005']
        self.c_Worst_singles_of_2006                                                       = ['Worst_singles_of_2006']
        self.c_Worst_singles_of_2007                                                       = ['Worst_singles_of_2007']
        self.c_Worst_singles_of_2008                                                       = ['Worst_singles_of_2008']
        self.c_Worst_singles_of_2009                                                       = ['Worst_singles_of_2009']
        self.c_Worst_singles_of_2010                                                       = ['Worst_singles_of_2010']
        self.c_Worst_singles_of_2011                                                       = ['Worst_singles_of_2011']
        self.c_Worst_singles_of_2012                                                       = ['Worst_singles_of_2012']
        self.c_Worst_singles_of_2013                                                       = ['Worst_singles_of_2013']
        self.c_Worst_singles_of_2014                                                       = ['Worst_singles_of_2014']
        self.c_Worst_singles_of_2015                                                       = ['Worst_singles_of_2015']
        self.c_Worst_singles_of_2016                                                       = ['Worst_singles_of_2016']
        self.c_Worst_singles_of_2017                                                       = ['Worst_singles_of_2017']
        self.c_Worst_singles_of_2018                                                       = ['Worst_singles_of_2018']
        self.c_Worst_singles_of_2019                                                       = ['Worst_singles_of_2019']
        self.c_Worst_singles_of_2020                                                       = ['Worst_singles_of_2020']
        self.c_Worst_singles_of_the_1890s                                                  = ['Worst_singles_of_the_1890s']
        self.c_Worst_singles_of_the_1900s                                                  = ['Worst_singles_of_the_1900s']
        self.c_Worst_singles_of_the_1910s                                                  = ['Worst_singles_of_the_1910s']
        self.c_Worst_singles_of_the_1920s                                                  = ['Worst_singles_of_the_1920s']
        self.c_Worst_singles_of_the_1930s                                                  = ['Worst_singles_of_the_1930s']
        self.c_Worst_singles_of_the_1940s                                                  = ['Worst_singles_of_the_1940s']
        self.c_Worst_singles_of_the_1950s                                                  = ['Worst_singles_of_the_1950s']
        self.c_Worst_singles_of_the_1960s                                                  = ['Worst_singles_of_the_1960s']
        self.c_Worst_singles_of_the_1970s                                                  = ['Worst_singles_of_the_1970s']
        self.c_Worst_singles_of_the_1980s                                                  = ['Worst_singles_of_the_1980s']
        self.c_Worst_singles_of_the_1990s                                                  = ['Worst_singles_of_the_1990s']
        self.c_Worst_singles_of_the_2000s                                                  = ['Worst_singles_of_the_2000s']
        self.c_Worst_singles_of_the_2010s                                                  = ['Worst_singles_of_the_2010s']


        self.chartNames = self.__dict__.keys()


        self.chartRanks = {}
        ######### Singles - Best #########
        self.chartRanks[0] = ['c_Best_singles_of_the_1890s', 'c_Best_singles_of_the_1900s', 'c_Best_singles_of_the_1910s']
        self.chartRanks[1] = ['c_Best_singles_of_the_1920s', 'c_Best_singles_of_the_1930s', 'c_Best_singles_of_the_1940s']
        self.chartRanks[2] = ['c_Best_singles_of_the_1950s', 'c_Best_singles_of_the_1960s', 'c_Best_singles_of_the_1970s']
        self.chartRanks[3] = ['c_Best_singles_of_the_1980s', 'c_Best_singles_of_the_1990s', 'c_Best_singles_of_the_2000s']
        self.chartRanks[4] = ['c_Best_singles_of_the_2010s']
        ######### Singles - Worst #########
        self.chartRanks[5] = ['c_Worst_singles_of_the_1890s', 'c_Worst_singles_of_the_1900s', 'c_Worst_singles_of_the_1910s']
        self.chartRanks[6] = ['c_Worst_singles_of_the_1920s', 'c_Worst_singles_of_the_1930s', 'c_Worst_singles_of_the_1940s']
        self.chartRanks[7] = ['c_Worst_singles_of_the_1950s', 'c_Worst_singles_of_the_1960s', 'c_Worst_singles_of_the_1970s']
        self.chartRanks[8] = ['c_Worst_singles_of_the_1980s', 'c_Worst_singles_of_the_1990s', 'c_Worst_singles_of_the_2000s']
        self.chartRanks[9] = ['c_Worst_singles_of_the_2010s']
        ######### Albums - Best #########
        ######### Albums - Diverse #########
        ######### Albums - Esoteric #########
        ######### Albums - Worst #########
        ######### Mixes - Best #########
        ######### Mixes - Worst #########
        ######### Albums - Yearly #########
        ######### Singles - BestYearly #########
        self.chartRanks[10] = ['c_Best_singles_of_1945', 'c_Best_singles_of_1946', 'c_Best_singles_of_1947', 'c_Best_singles_of_1948', 'c_Best_singles_of_1949']
        self.chartRanks[11] = ['c_Best_singles_of_1950', 'c_Best_singles_of_1951', 'c_Best_singles_of_1952', 'c_Best_singles_of_1953', 'c_Best_singles_of_1954']
        self.chartRanks[12] = ['c_Best_singles_of_1955', 'c_Best_singles_of_1956', 'c_Best_singles_of_1957', 'c_Best_singles_of_1958', 'c_Best_singles_of_1959']
        self.chartRanks[13] = ['c_Best_singles_of_1960', 'c_Best_singles_of_1961', 'c_Best_singles_of_1962', 'c_Best_singles_of_1963', 'c_Best_singles_of_1964']
        self.chartRanks[14] = ['c_Best_singles_of_1965', 'c_Best_singles_of_1966', 'c_Best_singles_of_1967', 'c_Best_singles_of_1968', 'c_Best_singles_of_1969']
        self.chartRanks[15] = ['c_Best_singles_of_1970', 'c_Best_singles_of_1971', 'c_Best_singles_of_1972', 'c_Best_singles_of_1973', 'c_Best_singles_of_1974']
        self.chartRanks[16] = ['c_Best_singles_of_1975', 'c_Best_singles_of_1976', 'c_Best_singles_of_1977', 'c_Best_singles_of_1978', 'c_Best_singles_of_1979']
        self.chartRanks[17] = ['c_Best_singles_of_1980', 'c_Best_singles_of_1981', 'c_Best_singles_of_1982', 'c_Best_singles_of_1983', 'c_Best_singles_of_1984']
        self.chartRanks[18] = ['c_Best_singles_of_1985', 'c_Best_singles_of_1986', 'c_Best_singles_of_1987', 'c_Best_singles_of_1988', 'c_Best_singles_of_1989']
        self.chartRanks[19] = ['c_Best_singles_of_1990', 'c_Best_singles_of_1991', 'c_Best_singles_of_1992', 'c_Best_singles_of_1993', 'c_Best_singles_of_1994']
        self.chartRanks[20] = ['c_Best_singles_of_1995', 'c_Best_singles_of_1996', 'c_Best_singles_of_1997', 'c_Best_singles_of_1998', 'c_Best_singles_of_1999']
        self.chartRanks[21] = ['c_Best_singles_of_2000', 'c_Best_singles_of_2001', 'c_Best_singles_of_2002', 'c_Best_singles_of_2003', 'c_Best_singles_of_2004']
        self.chartRanks[22] = ['c_Best_singles_of_2005', 'c_Best_singles_of_2006', 'c_Best_singles_of_2007', 'c_Best_singles_of_2008', 'c_Best_singles_of_2009']
        self.chartRanks[23] = ['c_Best_singles_of_2010', 'c_Best_singles_of_2011', 'c_Best_singles_of_2012', 'c_Best_singles_of_2013', 'c_Best_singles_of_2014']
        self.chartRanks[24] = ['c_Best_singles_of_2015', 'c_Best_singles_of_2016', 'c_Best_singles_of_2017', 'c_Best_singles_of_2018', 'c_Best_singles_of_2019']
        self.chartRanks[25] = ['c_Best_singles_of_2020']
        ######### Singles - WorstYearly #########
        self.chartRanks[26] = ['c_Worst_singles_of_1950', 'c_Worst_singles_of_1951', 'c_Worst_singles_of_1952', 'c_Worst_singles_of_1953', 'c_Worst_singles_of_1954']
        self.chartRanks[27] = ['c_Worst_singles_of_1955', 'c_Worst_singles_of_1956', 'c_Worst_singles_of_1957', 'c_Worst_singles_of_1958', 'c_Worst_singles_of_1959']
        self.chartRanks[28] = ['c_Worst_singles_of_1960', 'c_Worst_singles_of_1961', 'c_Worst_singles_of_1962', 'c_Worst_singles_of_1963', 'c_Worst_singles_of_1964']
        self.chartRanks[29] = ['c_Worst_singles_of_1965', 'c_Worst_singles_of_1966', 'c_Worst_singles_of_1967', 'c_Worst_singles_of_1968', 'c_Worst_singles_of_1969']
        self.chartRanks[30] = ['c_Worst_singles_of_1970', 'c_Worst_singles_of_1971', 'c_Worst_singles_of_1972', 'c_Worst_singles_of_1973', 'c_Worst_singles_of_1974']
        self.chartRanks[31] = ['c_Worst_singles_of_1975', 'c_Worst_singles_of_1976', 'c_Worst_singles_of_1977', 'c_Worst_singles_of_1978', 'c_Worst_singles_of_1979']
        self.chartRanks[32] = ['c_Worst_singles_of_1980', 'c_Worst_singles_of_1981', 'c_Worst_singles_of_1982', 'c_Worst_singles_of_1983', 'c_Worst_singles_of_1984']
        self.chartRanks[33] = ['c_Worst_singles_of_1985', 'c_Worst_singles_of_1986', 'c_Worst_singles_of_1987', 'c_Worst_singles_of_1988', 'c_Worst_singles_of_1989']
        self.chartRanks[34] = ['c_Worst_singles_of_1990', 'c_Worst_singles_of_1991', 'c_Worst_singles_of_1992', 'c_Worst_singles_of_1993', 'c_Worst_singles_of_1994']
        self.chartRanks[35] = ['c_Worst_singles_of_1995', 'c_Worst_singles_of_1996', 'c_Worst_singles_of_1997', 'c_Worst_singles_of_1998', 'c_Worst_singles_of_1999']
        self.chartRanks[36] = ['c_Worst_singles_of_2000', 'c_Worst_singles_of_2001', 'c_Worst_singles_of_2002', 'c_Worst_singles_of_2003', 'c_Worst_singles_of_2004']
        self.chartRanks[37] = ['c_Worst_singles_of_2005', 'c_Worst_singles_of_2006', 'c_Worst_singles_of_2007', 'c_Worst_singles_of_2008', 'c_Worst_singles_of_2009']
        self.chartRanks[38] = ['c_Worst_singles_of_2010', 'c_Worst_singles_of_2011', 'c_Worst_singles_of_2012', 'c_Worst_singles_of_2013', 'c_Worst_singles_of_2014']
        self.chartRanks[39] = ['c_Worst_singles_of_2015', 'c_Worst_singles_of_2016', 'c_Worst_singles_of_2017', 'c_Worst_singles_of_2018', 'c_Worst_singles_of_2019']
        self.chartRanks[40] = ['c_Worst_singles_of_2020']
        ######### Titles #########
        ######### Artists #########
        ######### Script #########
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
