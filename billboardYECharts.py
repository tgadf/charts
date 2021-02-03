from ioUtils import getFile
from artistIgnores import getArtistIgnores

class billboardYECharts:
    def __init__(self):
        
        self.countryMusic = ['country-digital-songs', 'country-artists-duo-group', 'hot-country-songs-artists', 'top-country-albums',
                             'country-streaming-songs-artists', 'country-airplay-artists', 'country-digital-songs-artists',
                             'country-streaming-songs', 'top-country-artists', 'country-artists-male', 'hot-country-songs',
                             'country-artists-female', 'top-country-albums-artists', 'new-country-artists', 'country-airplay-songs']

        self.gospel = ['hot-gospel-songs', 'gospel-albums', 'hot-gospel-songs-artists', 'gospel-albums-artists',
                       'gospel-digital-songs', 'gospel-digital-songs-artists', 'gospel-streaming-songs',
                       'gospel-airplay-songs', 'top-gospel-new-artists', 'top-gospel-artists-female', 'gospel-airplay-artists',
                       'top-gospel-artists-duo-group', 'gospel-streaming-songs-artists', 'top-gospel-artists', 'top-gospel-artists-male']

        self.adult = ['adult-contemporary-artists', 'adult-pop-songs-artists', 'adult-pop-songs', 'adult-contemporary-songs']

        self.cast = ['cast-albums']

        self.rhythmic = ['rhythmic-songs', 'rhythmic-artists']

        self.soundtracks = ['top-soundtracks-albums']

        self.blues = ['blues-albums-artists', 'blues-albums']

        self.jazz = ['jazz-albums-artists', 'contemporary-jazz-albums', 'smooth-jazz-songs-artists', 'smooth-jazz-songs',
                     'contemporary-jazz-artists', 'jazz-albums', 'traditional-jazz-albums-artists']

        self.new_age = ['new-age-albums', 'new-age-albums-artists']

        self.pop = ['pop-songs', 'pop-songs-artists']

        self.streaming_songs = ['on-demand-songs', 'streaming-songs-artists', 'on-demand-songs-artists', 'streaming-songs']

        self.reggae = ['reggae-albums-artists', 'reggae-albums']

        self.world = ['world-albums', 'world-albums-artists']

        self.independent = ['independent-artists', 'independent-albums']

        self.social = ['social-50-artists']

        self.comedy = ['comedy-albums', 'comedy-albums-artists']

        self.hot_100 = ['hot-100-songs', 'hot-100-artists-male', 'hot-100-artists',
                        'hot-100-artists-female', 'hot-100-artists-duo-group']
        self.hot = self.hot_100

        self.christian = ['top-christian-new-artists', 'hot-christian-songs-artists', 'christian-digital-songs',
                          'christian-digital-songs-artists', 'hot-christian-songs', 'christian-streaming-songs-artists',
                          'hot-christian-adult-contemporary', 'top-christian-artists-male', 'christian-albums',
                          'top-christian-artists', 'christian-airplay-artists', 'top-christian-artists-female',
                          'top-christian-artists-duo-group', 'christian-streaming-songs', 'christian-airplay-songs',
                          'christian-albums-artists', 'hot-christian-adult-contemporary-artists']
        self.christian += self.gospel

        self.americana__folk = ['folk-albums', 'folk-artists']
        self.folkblue = self.americana__folk

        self.songwriters__publishers = ['dance-electronic-songwriters', 'hot-christian-songswriters',
                                        'hot-country-songwriters', 'hot-latin-songswriters', 'hot-100-songwriters',
                                        'hot-r-and-and-b-hip-hop-songwriters', 'hot-rock-songwriters', 'rap-songwriters',
                                        'r-and-b-songwriters', 'hot-christian-adult-contemporary-songwriters']

        self.rap = ['rap-digital-songs-artists', 'rap-airplay-artists', 'hot-rap-songs-artists', 'rap-airplay-songs',
                    'hot-rap-songs', 'rap-streaming-songs', 'rap-digital-songs',
                    'rap-streaming-songs-artists', 'rap-albums', 'rap-albums-artists']
        self.rnb = self.rap

        self.international = ['top-canadian-albums', 'canadian-hot-100', 'candaian-hot-100-artists', 'hot-canadian-digital-songs']
        self.canadian = self.international

        self.latin = ['latin-streaming-songs-artists', 'latin-digital-songs-artists', 'hot-latin-songs-artists',
                      'latin-rhythm-albums-artists', 'regional-mexican-airplay-songs', 'top-new-latin-artists',
                      'latin-pop-airplay-artists', 'top-latin-albums-artists', 'latin-pop-albums-artists',
                      'regional-mexican-airplay-artists', 'regional-mexican-albums-artists', 'top-latin-artists-female',
                      'latin-pop-albums', 'tropical-airplay-songs', 'latin-digital-songs', 'regional-mexican-albums',
                      'hot-latin-songs', 'tropical-albums', 'latin-rhythm-albums-', 'top-latin-albums', 'latin-airplay-artists',
                      'top-latin-artists-male', 'latin-airplay-songs', 'top-latin-artists-duo-group', 'latin-rhythm-airplay-artists',
                      'latin-pop-airplay-songs', 'tropical-airplay-artists', 'tropical-albums-artists', 'latin-rhythm-airplay-songs',
                      'latin-streaming-songs', 'top-latin-artists']

        self.rb = ['hot-mainstream-r-and-and-b-hip-hop-songs', 'hot-r-and-and-b-songs', 'adult-r-and-b-artists',
                   'r-and-b-digital-songs-artists', 'r-and-b-albums-artists', 'hot-r-and-and-b-songs-artists',
                   'r-and-b-streaming-songs-artists', 'r-and-b-digital-songs', 'r-and-b-albums', 'r-and-b-streaming-songs',
                   'adult-r-and-b-songs', 'hot-mainstream-r-and-and-b-hip-hop-artists']
        self.rnb += self.rb

        self.digital_song_sales = ['digital-songs', 'digital-songs-artists']
        self.digital = self.digital_song_sales

        self.other_albums = ['current-albums', 'tastemakers-albums', 'compilation-albums', 'vinyl-albums',
                             'top-album-title-sales', 'top-album-sales-artists']

        self.kid = ['kid-albums', 'kid-albums-artists']

        self.rock = ['mainstream-rock-artists', 'rock-digital-songs', 'mainstream-rock-songs-artists', 'top-rock-albums',
                     'top-new-rock-artists', 'hard-rock-digital-song-sales-yearend', 'hard-rock-albums-artists', 
                     'hot-rock-songs', 'rock-streaming-songs', 'hard-rock-albums', 'rock-digital-songs-artists',
                     'top-rock-artists','rock-airplay-artists', 'hot-rock-songs-artists', 'top-rock-albums-artists', 
                     'rock-airplay-songs', 'rock-streaming-songs-artists']
        self.alternative = ['adult-alternative-songs', 'alternative-digital-song-sales-yearend',
                            'alternative-songs', 'alternative-songs-artists', 'adult-alternative-songs-artists',
                            'top-alternative-album-artists','top-alternative-albums']

        self.classical = ['classical-albums-artists', 'classical-crossover-albums', 'traditional-classical-albums-artists',
                          'classical-crossover-albums-artists', 'traditional-classical-albums', 'classical-albums']

        self.billboard_200 = ['the-billboard-200-artists-male', 'top-billboard-200-artists', 'the-billboard-200-artists-female',
                              'top-billboard-200-albums', 'the-billboard-200-artists-duo-group']
        self.top = self.billboard_200

        self.bluegrass = ['bluegrass-artists', 'bluegrass-albums']
        self.folkblue += self.bluegrass

        self.overall = ['top-artists-female', 'top-artists-duo-group', 'top-artists', 'top-new-artists', 'top-artists-male']
        self.top = self.overall

        self.dance__electronic = ['top-dance-electronic-artists', 'dance-electronic-digital-songs-artists',
                                  'dance-electronic-digital-songs', 'dance-mix-show-airplay-songs', 'dance-electronic-albums',
                                  'dance-mix-show-airplay-artists', 'top-dance-electronic-new-artists', 'hot-dance-electronic-songs',
                                  'dance-electronic-streaming-songs-artists', 'hot-dance-electronic-songs-artists',
                                  'dance-electronic-streaming-songs', 'top-new-dance-eletronic-artists']
        self.electronic = self.dance__electronic

        self.rb__hip_hop = ['r-and-and-b-hip-hop-artists-female', 'top-r-and-b-hip-hop-albums', 'r-and-b-hip-hop-digital-songs',
                            'new-r-and-and-b-hip-hop-artists', 'top-r-and-b-hip-hop-albums-artists', 'r-and-and-b-hip-hop-artists-duo-group',
                            'r-and-and-b-hip-hop-artists-male', 'hot-r-and-and-b-hip-hop-songs', 'r-and-b-hip-hop-digital-songs-artists',
                            'hot-r-and-b-hip-hop-songs-artists', 'r-and-b-hip-hop-airplay-songs', 'top-r-and-b-hip-hop-artists',
                            'r-and-b-hip-hop-streaming-songs-artists', 'r-and-b-hip-hop-streaming-songs', 'r-and-b-hip-hop-airplay-artists']
        self.rnb += self.rb__hip_hop

        self.catalog = ['catalog-artists', 'catalog-albums']

        self.radio_songs = ['radio-songs-artists', 'radio-songs']
        self.radio = self.radio_songs
        
        
        
        
        self.chartNames = self.__dict__.keys()

        self.ignoreSong = {}
        
        self.chartRanks = {}
        
        self.chartRanks[0]  = ['hot']
        self.ignoreSong[0]  = False
        
        self.chartRanks[1]  = ['adult']
        self.ignoreSong[1]  = False
        
        self.chartRanks[2]  = ['alternative', 'countryMusic', 'rock', 'rnb']
        self.ignoreSong[2]  = True
        
        self.chartRanks[3]  = self.chartRanks[2]
        self.ignoreSong[3]  = False
        
        self.chartRanks[4]  = ['christian', 'canadian', 'comedy', 'radio']
        self.ignoreSong[4]  = True
        
        self.chartRanks[5]  = self.chartRanks[4]
        self.ignoreSong[5]  = False
        
        self.chartRanks[6]  = ['folkblue', 'electronic', 'latin', 'world', 'classical', 'digital', 'social', 'jazz', 'new_age',   'kid', 'cast', 'soundtracks', 'blues', 'rhythmic', 'streaming_songs', 'independent', 'other_albums', 'catalog', 'reggae']
        self.ignoreSong[6]  = True
        
        self.chartRanks[7]  = self.chartRanks[6]
        self.ignoreSong[7]  = False


        notfound = {}
        for chartName in self.chartNames:            
            found=False
            for key,vals in self.chartRanks.items():
                if chartName in vals:
                    found=True
            if found:
                continue
            notfound[chartName] = True
            
        
        
    def getChartsByRank(self, rank):
        categories = self.chartRanks[rank]
        charts = []
        for chart in categories:
            rankCharts = self.getCharts(chart)
            if self.ignoreSong[rank] is True:
                rankCharts = [x for x in rankCharts if not x.endswith("songs")]
            charts += rankCharts
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