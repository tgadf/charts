from ioUtils import getFile
from listUtils import getFlatList
from artistIgnores import getArtistIgnores

class billboardCharts:
    def __init__(self):

        self.adult_contemporary                       = ['adult-contemporary', 'ASI']
        self.adult_pop_songs                          = ['adult-pop-songs', 'ATF']
        self.adult                                    = [self.adult_contemporary, self.adult_pop_songs]

        self.alternative_albums                       = ['alternative-albums', 'ALT']
        self.alternative_songs                        = ['alternative-songs', 'MRT']
        self.alternative                              = [self.alternative_albums, self.alternative_songs]

        self.americana_folk_albums                    = ['americana-folk-albums', 'FLK']
        self.bluegrass_albums                         = ['bluegrass-albums', 'BGR']
        self.blues_albums                             = ['blues-albums', 'BLU']
        self.folkblue                                 = [self.americana_folk_albums, self.bluegrass_albums, self.blues_albums]

        self.christian_airplay                        = ['christian-airplay', 'CRI']
        self.hot_christian_songs                      = ['hot-christian-songs']
        self.christian_albums                         = ['christian-albums', 'ILL']
        self.christian_digital_song_sales             = ['christian-digital-song-sales', 'CRT']
        self.christian_songs                          = ['christian-songs', 'ICO']
        self.christian_streaming_songs                = ['christian-streaming-songs', 'CHS']
        self.gospel_airplay                           = ['gospel-airplay', 'GOS']
        self.gospel_albums                            = ['gospel-albums', 'SLL']
        self.gospel_digital_song_sales                = ['gospel-digital-song-sales', 'GDT']
        self.gospel_songs                             = ['gospel-songs', 'GSI']
        self.gospel_streaming_songs                   = ['gospel-streaming-songs', 'GSS']
        self.christian                                = [self.christian_airplay, self.hot_christian_songs, self.christian_albums, self.christian_digital_song_sales, self.christian_songs, self.christian_streaming_songs, self.gospel_airplay, self.gospel_albums, self.gospel_digital_song_sales, self.gospel_songs, self.gospel_streaming_songs]

        self.country_airplay                          = ['country-airplay', 'CSA']
        self.country_albums                           = ['country-albums', 'CLP']
        self.country_digital_song_sales               = ['country-digital-song-sales', 'CDT']
        self.country_songs                            = ['country-songs', 'CSI']
        self.country_streaming_songs                  = ['country-streaming-songs', 'CST']
        self.countryMusic                             = [self.country_airplay, self.country_albums, self.country_digital_song_sales, self.country_songs, self.country_streaming_songs]

        self.dance_club_play_songs                    = ['dance-club-play-songs', 'DSI']
        self.dance_electronic_albums                  = ['dance-electronic-albums', 'ELP']
        self.dance_electronic_digital_song_sales      = ['dance-electronic-digital-song-sales', 'DDT']
        self.dance_electronic_songs                   = ['dance-electronic-songs', 'DAN']
        self.dance_electronic_streaming_songs         = ['dance-electronic-streaming-songs', 'DAS']
        self.electronic                               = [self.dance_club_play_songs, self.dance_electronic_albums, self.dance_electronic_digital_song_sales, self.dance_electronic_songs, self.dance_electronic_streaming_songs]

        self.hot_100                                  = ['hot-100', 'HSI']
        self.pop_songs                                = ['pop-songs', 'TFM']
        self.radio_songs                              = ['radio-songs', 'HSB']
        self.streaming_songs                          = ['streaming-songs', 'STM']
        self.rhythmic_40                              = ['rhythmic-40', 'TFC']
        self.heatseekers_albums                       = ['heatseekers-albums', 'TLN']
        self.hot                                      = [self.hot_100, self.pop_songs, self.radio_songs, self.streaming_songs, self.rhythmic_40, self.heatseekers_albums]

        self.billboard_200                            = ['billboard-200', 'TLP']
        self.artist_100                               = ['artist-100', 'ATS']
        self.top_album_sales                          = ['top-album-sales', 'TSL']
        self.top                                      = [self.billboard_200, self.artist_100, self.top_album_sales]

        self.r_and_b_albums                           = ['r-and-b-albums', 'RBL']
        self.r_and_b_hip_hop_digital_song_sales       = ['r-and-b-hip-hop-digital-song-sales', 'RBT']
        self.r_and_b_hip_hop_streaming_songs          = ['r-and-b-hip-hop-streaming-songs', 'RBS']
        self.r_and_b_songs                            = ['r-and-b-songs', 'BST']
        self.r_b_hip_hop_albums                       = ['r-b-hip-hop-albums', 'BLP']
        self.r_b_hip_hop_songs                        = ['r-b-hip-hop-songs', 'BSI']
        self.rap_albums                               = ['rap-albums', 'RLP']
        self.rap_song                                 = ['rap-song', 'RAP']
        self.hot_r_and_b_hip_hop_airplay              = ['hot-r-and-b-hip-hop-airplay', 'RBM']
        self.rnb                                      = [self.r_and_b_albums, self.r_and_b_hip_hop_digital_song_sales, self.r_and_b_hip_hop_streaming_songs, self.r_and_b_songs, self.r_b_hip_hop_albums, self.r_b_hip_hop_songs, self.rap_albums, self.rap_song, self.hot_r_and_b_hip_hop_airplay]
        
        self.rock_airplay                             = ['rock-airplay', 'RKA']
        self.hot_mainstream_rock_tracks               = ['hot-mainstream-rock-tracks', 'RTT']
        self.rock_albums                              = ['rock-albums', 'RCK']
        self.rock_digital_song_sales                  = ['rock-digital-song-sales', 'RKT']
        self.rock_songs                               = ['rock-songs', 'ARK']
        self.rock_streaming_songs                     = ['rock-streaming-songs', 'ROS']
        self.hard_rock_albums                         = ['hard-rock-albums', 'MTL']
        self.rock                                     = [self.rock_airplay, self.hot_mainstream_rock_tracks, self.rock_albums, self.rock_digital_song_sales, self.rock_songs, self.rock_streaming_songs, self.hard_rock_albums]

        self.canadian_albums                          = ['canadian-albums', 'CNA']
        self.canadian_hot_100                         = ['canadian-hot-100', 'CAN']
        self.canadian                                 = [self.canadian_albums, self.canadian_hot_100]

        self.latin_airplay                            = ['latin-airplay', 'HTA']
        self.latin_albums                             = ['latin-albums', 'LCM']
        self.latin_digital_song_sales                 = ['latin-digital-song-sales', 'LDT']
        self.latin_pop_albums                         = ['latin-pop-albums', 'LPP']
        self.latin_pop_songs                          = ['latin-pop-songs', 'LPO']
        self.latin_songs                              = ['latin-songs', 'HTL']
        self.latin_streaming_songs                    = ['latin-streaming-songs', 'LSS']
        self.latin                                    = [self.latin_airplay, self.latin_albums, self.latin_digital_song_sales, self.latin_pop_albums, self.latin_pop_songs, self.latin_songs, self.latin_streaming_songs]

        self.regional_mexican_albums                  = ['regional-mexican-albums', 'LRM']
        self.regional_mexican_songs                   = ['regional-mexican-songs', 'LMX']
        self.mexican                                  = [self.regional_mexican_albums, self.regional_mexican_songs]

        self.china_v_chart                            = ['china-v-chart']
        self.japan_hot_100                            = ['japan-hot-100', 'JPN']
        self.tropical_albums                          = ['tropical-albums', 'LTS']
        self.tropical_songs                           = ['tropical-songs', 'LSA']
        self.world_albums                             = ['world-albums', 'WLP']
        self.reggae_albums                            = ['reggae-albums', 'JAH']
        self.world                                    = [self.china_v_chart, self.japan_hot_100, self.tropical_albums, self.tropical_songs, self.world_albums, self.reggae_albums]

        self.holiday_albums                           = ['holiday-albums', 'XML']
        self.holiday_season_digital_song_sales        = ['holiday-season-digital-song-sales', 'XDT']
        self.holiday_songs                            = ['holiday-songs', 'ASX']
        self.holiday_streaming_songs                  = ['holiday-streaming-songs', 'XSS']
        self.holiday                                  = [self.holiday_albums, self.holiday_season_digital_song_sales, self.holiday_songs, self.holiday_streaming_songs]

        self.classical_albums                         = ['classical-albums', 'COA']
        self.classical                                = [self.classical_albums]

        self.jazz_albums                              = ['jazz-albums', 'JLS']
        self.jazz_songs                               = ['jazz-songs', 'JSI']
        self.jazz                                     = [self.jazz_albums, self.jazz_songs]

        self.comedy_albums                            = ['comedy-albums', 'GIG']
        self.comedy                                   = [self.comedy_albums]

        self.new_age_albums                           = ['new-age-albums', 'NLP']
        self.newage                                   = [self.new_age_albums]

        self.digital_albums                           = ['digital-albums', 'DLP']
        self.digital_song_sales                       = ['digital-song-sales', 'HDS']
        self.general                                  = [self.digital_albums, self.digital_song_sales]

        self.kids_albums                              = ['kids-albums', 'KID']
        self.kids                                     = [self.kids_albums]

        self.twitter_emerging_artists                 = ['twitter-emerging-artists']
        self.twitter_top_tracks                       = ['twitter-top-tracks']
        self.social_50                                = ['social-50', 'SOC']
        self.twitter                                  = [self.twitter_emerging_artists, self.twitter_top_tracks, self.social_50]

        self.vinyl_albums                             = ['vinyl-albums', 'VNL']
        self.catalog_albums                           = ['catalog-albums', 'TLC']
        self.tastemaker_albums                        = ['tastemaker-albums', 'TAS']
        self.vinyl                                    = [self.vinyl_albums, self.catalog_albums, self.tastemaker_albums]

        self.independent_albums                       = ['independent-albums', 'IND']
        self.rare                                     = [self.independent_albums]

        self.soundtracks                              = ['soundtracks', 'STX']
        self.soundtrack                               = [self.soundtracks]


        
        self.chartNames = self.__dict__.keys()

        
        self.chartRanks = {}
        self.chartRanks[0] = ['top']
        self.chartRanks[1] = ['hot', 'adult']
        self.chartRanks[2] = ['alternative', 'countryMusic', 'rock']
        self.chartRanks[3] = ['christian', 'rnb']
        self.chartRanks[4] = ['canadian', 'comedy', 'general', 'twitter']
        self.chartRanks[5] = ['folkblue', 'classical', 'jazz']
        self.chartRanks[6] = ['electronic', 'newage', 'kids', 'vinyl', 'rare', 'soundtrack', 'holiday']
        self.chartRanks[7] = ['latin', 'mexican']        
        self.chartRanks[8] = ['world']
        
        
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