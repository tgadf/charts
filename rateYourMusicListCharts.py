from ioUtils import getFile
from listUtils import getFlatList
from artistIgnores import getArtistIgnores

class rateYourMusicListCharts:
    def __init__(self):
        self.c_1000_Great_Albums                                                           = ['1000_Great_Albums']
        self.c_1001_Albums_You_Must_Hear                                                   = ['1001_Albums_You_Must_Hear']
        self.c_1001_Albums_You_Must_Hear_Before_You_Die                                    = ['1001_Albums_You_Must_Hear_Before_You_Die']
        self.c_1001_discos_que_debes_escuchar_antes_de_forear                              = ['1001_discos_que_debes_escuchar_antes_de_forear']
        self.c_100_Best_Swedish_Albums                                                     = ['100_Best_Swedish_Albums']
        self.c_100_most_mind_bending_life_changing_brain_expanding_records_of_all_time     = ['100_most_mind_bending_life_changing_brain_expanding_records_of_all_time']
        self.c_200_Russian_Albums                                                          = ['200_Russian_Albums']
        self.c_2010_2019                                                                   = ['2010_2019']
        self.c_3_Favorite_Albums_of_each_year                                              = ['3_Favorite_Albums_of_each_year']
        self.c_500_All_Psychedelic_Albums_Game                                             = ['500_All_Psychedelic_Albums_Game']
        self.c_500_Death_Metal_Recordings_You_Must_Hear_Before_You_Die                     = ['500_Death_Metal_Recordings_You_Must_Hear_Before_You_Die']
        self.c_500_Most_Depressing_Songs_I_Ever_Heard                                      = ['500_Most_Depressing_Songs_I_Ever_Heard']
        self.c_70s_80s_Jamaican_Dub                                                        = ['70s_80s_Jamaican_Dub']
        self.c_953_of_My_Favorite_Albums_A_Z                                               = ['953_of_My_Favorite_Albums_A_Z']
        self.c_Africa_Albums                                                               = ['Africa_Albums']
        self.c_Albums_from_Benelux                                                         = ['Albums_from_Benelux']
        self.c_Albums_from_Canada                                                          = ['Albums_from_Canada']
        self.c_Albums_from_Eastern_Europe                                                  = ['Albums_from_Eastern_Europe']
        self.c_Albums_from_France                                                          = ['Albums_from_France']
        self.c_Albums_from_Germany                                                         = ['Albums_from_Germany']
        self.c_Albums_from_Ireland                                                         = ['Albums_from_Ireland']
        self.c_Albums_from_Italy                                                           = ['Albums_from_Italy']
        self.c_Albums_from_Landlocked_Europe                                               = ['Albums_from_Landlocked_Europe']
        self.c_Albums_from_Oceania                                                         = ['Albums_from_Oceania']
        self.c_Albums_from_Quebec                                                          = ['Albums_from_Quebec']
        self.c_Albums_from_Scandinavia                                                     = ['Albums_from_Scandinavia']
        self.c_Albums_from_Scotland                                                        = ['Albums_from_Scotland']
        self.c_Albums_from_Wales                                                           = ['Albums_from_Wales']
        self.c_Albums_from_the_Caribbean                                                   = ['Albums_from_the_Caribbean']
        self.c_Albums_from_the_Far_East                                                    = ['Albums_from_the_Far_East']
        self.c_Albums_from_the_Iberian_Peninsula                                           = ['Albums_from_the_Iberian_Peninsula']
        self.c_Albums_from_the_Spanish_Americas                                            = ['Albums_from_the_Spanish_Americas']
        self.c_Amazingly_Awful_Album_Art                                                   = ['Amazingly_Awful_Album_Art']
        self.c_An_Artist_from_Every_Region                                                 = ['An_Artist_from_Every_Region']
        self.c_An_Ode_to_the_Death_of_the_80s                                              = ['An_Ode_to_the_Death_of_the_80s']
        self.c_An_Outsider_Guitde_to_Russian_Dance_Music                                   = ['An_Outsider_Guitde_to_Russian_Dance_Music']
        self.c_Awful_Ass_Album_Covers                                                      = ['Awful_Ass_Album_Covers']
        self.c_Canada_in_the_1980s                                                         = ['Canada_in_the_1980s']
        self.c_Country_Rock_Colossus                                                       = ['Country_Rock_Colossus']
        self.c_DJ_Mixes                                                                    = ['DJ_Mixes']
        self.c_Danish_Artists                                                              = ['Danish_Artists']
        self.c_Dark_Ambient_Essentials                                                     = ['Dark_Ambient_Essentials']
        self.c_EMI_Nigeria_45s                                                             = ['EMI_Nigeria_45s']
        self.c_Emo_Rap                                                                     = ['Emo_Rap']
        self.c_Ethereal_Voices_in_Metal                                                    = ['Ethereal_Voices_in_Metal']
        self.c_Every_Charting_Single_in_the_UK                                             = ['Every_Charting_Single_in_the_UK']
        self.c_Favorite_Albums_2010_2019                                                   = ['Favorite_Albums_2010_2019']
        self.c_Favorite_Anthologies_Albums                                                 = ['Favorite_Anthologies_Albums']
        self.c_Favorite_Chinese_Albums                                                     = ['Favorite_Chinese_Albums']
        self.c_Favorite_Danish_Albums                                                      = ['Favorite_Danish_Albums']
        self.c_Favorite_Pop_Albums                                                         = ['Favorite_Pop_Albums']
        self.c_Favorite_Russian_Albums                                                     = ['Favorite_Russian_Albums']
        self.c_Foreign_Language_Albums_in_the_RYM_all_time                                 = ['Foreign_Language_Albums_in_the_RYM_all_time']
        self.c_Forever_Young_2500_Best_Songs                                               = ['Forever_Young_2500_Best_Songs']
        self.c_Funk_Albums_from_the_United_States_and_England                              = ['Funk_Albums_from_the_United_States_and_England']
        self.c_Futuristic_music                                                            = ['Futuristic_music']
        self.c_Gentle_Dads                                                                 = ['Gentle_Dads']
        self.c_Good_Ass_Album_Covers                                                       = ['Good_Ass_Album_Covers']
        self.c_Grammy_Album_of_the_Year                                                    = ['Grammy_Album_of_the_Year']
        self.c_Great_Albums_Made_by_Artists_over_60_years_old                              = ['Great_Albums_Made_by_Artists_over_60_years_old']
        self.c_Great_Albums_Made_by_Artists_under_20_years_old                             = ['Great_Albums_Made_by_Artists_under_20_years_old']
        self.c_Great_Belgian_Artists                                                       = ['Great_Belgian_Artists']
        self.c_Great_obscure_lesser_known_albums                                           = ['Great_obscure_lesser_known_albums']
        self.c_Greek_Artists                                                               = ['Greek_Artists']
        self.c_J_Pop_and_K_Pop_Party                                                       = ['J_Pop_and_K_Pop_Party']
        self.c_Jazz_Core_Collection                                                        = ['Jazz_Core_Collection']
        self.c_Jazz_and_other_Jazz_styles_from_Africa                                      = ['Jazz_and_other_Jazz_styles_from_Africa']
        self.c_Jazzcore_Punk_Jazz_Brutal_Jazz_etc_                                         = ['Jazzcore_Punk_Jazz_Brutal_Jazz_etc_']
        self.c_Lets_listen_to_Canadian_progressive_music                                   = ['Lets_listen_to_Canadian_progressive_music']
        self.c_Nightwalking_Music                                                          = ['Nightwalking_Music']
        self.c_Obscurities                                                                 = ['Obscurities']
        self.c_Personal_250_Korean_Albums                                                  = ['Personal_250_Korean_Albums']
        self.c_Post_club_deconstructed_club_Albums_EPs_and_compilations                    = ['Post_club_deconstructed_club_Albums_EPs_and_compilations']
        self.c_Prolific_Outsiders_and_Weirdos                                              = ['Prolific_Outsiders_and_Weirdos']
        self.c_Psychedelic_60s                                                             = ['Psychedelic_60s']
        self.c_Ranking_Albums_of_2016                                                      = ['Ranking_Albums_of_2016']
        self.c_Recommended_Dance_Singles_EP                                                = ['Recommended_Dance_Singles_EP']
        self.c_Scandinavian_Rock                                                           = ['Scandinavian_Rock']
        self.c_Song_of_the_day                                                             = ['Song_of_the_day']
        self.c_Strongest_Chinese_Albums_in_History                                         = ['Strongest_Chinese_Albums_in_History']
        self.c_Summer_song_playlist                                                        = ['Summer_song_playlist']
        self.c_UK_Singles_Chart_Every_artist_that_reached_1                                = ['UK_Singles_Chart_Every_artist_that_reached_1']
        self.c_Ultimate_NonPop                                                             = ['Ultimate_NonPop']
        self.c_Ultimate_Songs_of_1990                                                      = ['Ultimate_Songs_of_1990']
        self.c_Upbeat_2000s_Pop                                                            = ['Upbeat_2000s_Pop']
        self.c_Upbeat_2020s_Pop                                                            = ['Upbeat_2020s_Pop']
        self.c_Upbeat_70s_Pop                                                              = ['Upbeat_70s_Pop']
        self.c_Upbeat_80s_Pop                                                              = ['Upbeat_80s_Pop']
        self.c_Upbeat_90s_Pop                                                              = ['Upbeat_90s_Pop']
        self.c_Voice_is_an_instrument_Extended_vocal_vocabulary                            = ['Voice_is_an_instrument_Extended_vocal_vocabulary']
        self.c_all_the_k_Pop                                                               = ['all_the_k_Pop']
        self.c_contemporary_r_b_that_goes_against_the_grain                                = ['contemporary_r_b_that_goes_against_the_grain']
        self.c_r_b_for_the_sleepless_deep_r_b_                                             = ['r_b_for_the_sleepless_deep_r_b_']
        self.c_s_a_d                                                                       = ['s_a_d']
        self.c_songs_that_youtube_are_manipulating_me_into_listening_to                    = ['songs_that_youtube_are_manipulating_me_into_listening_to']
        self.c_terrorize_the_jam_like_troops_in_Pakistan                                   = ['terrorize_the_jam_like_troops_in_Pakistan']
        self.c_thats_the_way_love_is_200_deep_house_selection                              = ['thats_the_way_love_is_200_deep_house_selection']
        self.c_top_500_songs                                                               = ['top_500_songs']
        self.c_underground_new_wave_from_USA                                               = ['underground_new_wave_from_USA']


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
        self.chartRanks[0] = ['c_1000_Great_Albums', 'c_1001_Albums_You_Must_Hear', 'c_1001_Albums_You_Must_Hear_Before_You_Die', 'c_100_Best_Swedish_Albums', 'c_200_Russian_Albums', 'c_3_Favorite_Albums_of_each_year']
        self.chartRanks[1] = ['c_500_All_Psychedelic_Albums_Game', 'c_500_Most_Depressing_Songs_I_Ever_Heard', 'c_953_of_My_Favorite_Albums_A_Z', 'c_Africa_Albums', 'c_Albums_from_Benelux', 'c_Albums_from_Canada']
        self.chartRanks[2] = ['c_Albums_from_Eastern_Europe', 'c_Albums_from_France', 'c_Albums_from_Germany', 'c_Albums_from_Ireland', 'c_Albums_from_Italy', 'c_Albums_from_Landlocked_Europe']
        self.chartRanks[3] = ['c_Albums_from_Oceania', 'c_Albums_from_Quebec', 'c_Albums_from_Scandinavia', 'c_Albums_from_Scotland', 'c_Albums_from_Wales', 'c_Albums_from_the_Caribbean']
        self.chartRanks[4] = ['c_Albums_from_the_Far_East', 'c_Albums_from_the_Iberian_Peninsula', 'c_Albums_from_the_Spanish_Americas', 'c_Amazingly_Awful_Album_Art', 'c_Awful_Ass_Album_Covers', 'c_Favorite_Albums_2010_2019']
        self.chartRanks[5] = ['c_Favorite_Anthologies_Albums', 'c_Favorite_Chinese_Albums', 'c_Favorite_Danish_Albums', 'c_Favorite_Pop_Albums', 'c_Favorite_Russian_Albums', 'c_Foreign_Language_Albums_in_the_RYM_all_time']
        self.chartRanks[6] = ['c_Forever_Young_2500_Best_Songs', 'c_Funk_Albums_from_the_United_States_and_England', 'c_Good_Ass_Album_Covers', 'c_Grammy_Album_of_the_Year', 'c_Great_Albums_Made_by_Artists_over_60_years_old', 'c_Great_Albums_Made_by_Artists_under_20_years_old']
        self.chartRanks[7] = ['c_Personal_250_Korean_Albums', 'c_Post_club_deconstructed_club_Albums_EPs_and_compilations', 'c_Ranking_Albums_of_2016', 'c_Song_of_the_day', 'c_Strongest_Chinese_Albums_in_History', 'c_Ultimate_Songs_of_1990']
        ######### Artists #########
        self.chartRanks[8] = ['c_An_Artist_from_Every_Region', 'c_Danish_Artists', 'c_Great_Belgian_Artists', 'c_Greek_Artists']
        ######### Script #########
        ######### Other #########
        self.chartRanks[9] = ['c_1001_discos_que_debes_escuchar_antes_de_forear', 'c_100_most_mind_bending_life_changing_brain_expanding_records_of_all_time', 'c_2010_2019', 'c_500_Death_Metal_Recordings_You_Must_Hear_Before_You_Die', 'c_70s_80s_Jamaican_Dub', 'c_An_Ode_to_the_Death_of_the_80s']
        self.chartRanks[10] = ['c_An_Outsider_Guitde_to_Russian_Dance_Music', 'c_Canada_in_the_1980s', 'c_Country_Rock_Colossus', 'c_DJ_Mixes', 'c_Dark_Ambient_Essentials', 'c_EMI_Nigeria_45s']
        self.chartRanks[11] = ['c_Emo_Rap', 'c_Ethereal_Voices_in_Metal', 'c_Every_Charting_Single_in_the_UK', 'c_Futuristic_music', 'c_Gentle_Dads', 'c_Great_obscure_lesser_known_albums']
        self.chartRanks[12] = ['c_J_Pop_and_K_Pop_Party', 'c_Jazz_Core_Collection', 'c_Jazz_and_other_Jazz_styles_from_Africa', 'c_Jazzcore_Punk_Jazz_Brutal_Jazz_etc_', 'c_Lets_listen_to_Canadian_progressive_music', 'c_Nightwalking_Music']
        self.chartRanks[13] = ['c_Obscurities', 'c_Prolific_Outsiders_and_Weirdos', 'c_Psychedelic_60s', 'c_Recommended_Dance_Singles_EP', 'c_Scandinavian_Rock', 'c_Summer_song_playlist']
        self.chartRanks[14] = ['c_UK_Singles_Chart_Every_artist_that_reached_1', 'c_Ultimate_NonPop', 'c_Upbeat_2000s_Pop', 'c_Upbeat_2020s_Pop', 'c_Upbeat_70s_Pop', 'c_Upbeat_80s_Pop']
        self.chartRanks[15] = ['c_Upbeat_90s_Pop', 'c_Voice_is_an_instrument_Extended_vocal_vocabulary', 'c_all_the_k_Pop', 'c_contemporary_r_b_that_goes_against_the_grain', 'c_r_b_for_the_sleepless_deep_r_b_', 'c_s_a_d']
        self.chartRanks[16] = ['c_songs_that_youtube_are_manipulating_me_into_listening_to', 'c_terrorize_the_jam_like_troops_in_Pakistan', 'c_thats_the_way_love_is_200_deep_house_selection', 'c_top_500_songs', 'c_underground_new_wave_from_USA']
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
