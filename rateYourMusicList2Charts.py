from ioUtils import getFile
from listUtils import getFlatList
from artistIgnores import getArtistIgnores

class rateYourMusicList2Charts:
    def __init__(self):
        self.c_100_Favourite_Songs_of_All_Time                                             = ['100_Favourite_Songs_of_All_Time']
        self.c_1500_Songs_From_Under_The_Floorboards                                       = ['1500_Songs_From_Under_The_Floorboards']
        self.c_200_Greatest_Rock_Artists_of_All_Time                                       = ['200_Greatest_Rock_Artists_of_All_Time']
        self.c_3500_Albums_You_Gotta_Listen_To                                             = ['3500_Albums_You_Gotta_Listen_To']
        self.c_50_Greatest_Hawaii_Albums_of_All_Time                                       = ['50_Greatest_Hawaii_Albums_of_All_Time']
        self.c_ALL_JAPAN_The_Greatest_JPN_Albums                                           = ['ALL_JAPAN_The_Greatest_JPN_Albums']
        self.c_Around_the_World_of_Traditional_Music_in_80_Records                         = ['Around_the_World_of_Traditional_Music_in_80_Records']
        self.c_Best_360_R_B_Albums                                                         = ['Best_360_R_B_Albums']
        self.c_Best_Albums_Of_All_Time                                                     = ['Best_Albums_Of_All_Time']
        self.c_Best_Albums_of_Reggaeton_of_All_Time                                        = ['Best_Albums_of_Reggaeton_of_All_Time']
        self.c_Best_Female_Voices                                                          = ['Best_Female_Voices']
        self.c_Best_of_Jazz_Improv_1970s_2010s_                                            = ['Best_of_Jazz_Improv_1970s_2010s_']
        self.c_Best_of_the_1970s                                                           = ['Best_of_the_1970s']
        self.c_Best_of_the_1980s                                                           = ['Best_of_the_1980s']
        self.c_Billboard_charts_1990s                                                      = ['Billboard_charts_1990s']
        self.c_Black_White                                                                 = ['Black_White']
        self.c_Blood_Pumps_1500_Favorite_Albums                                            = ['Blood_Pumps_1500_Favorite_Albums']
        self.c_Blow_Up_Magazines_600_essential_albums                                      = ['Blow_Up_Magazines_600_essential_albums']
        self.c_Brazil                                                                      = ['Brazil']
        self.c_CITY_LIFE_ESCAPE                                                            = ['CITY_LIFE_ESCAPE']
        self.c_COUNTRY_STRONG                                                              = ['COUNTRY_STRONG']
        self.c_Eastern_Europe_DIY_Tapes_1978_89                                            = ['Eastern_Europe_DIY_Tapes_1978_89']
        self.c_Greatest_Rappers_of_All_Time                                                = ['Greatest_Rappers_of_All_Time']
        self.c_Guide_To_Indie_Twee_Pop                                                     = ['Guide_To_Indie_Twee_Pop']
        self.c_Hazy_Memory_Nocturnal_Version                                               = ['Hazy_Memory_Nocturnal_Version']
        self.c_Helio_Reviews_the_Singles                                                   = ['Helio_Reviews_the_Singles']
        self.c_Hip_Hop_Artists_for_Me_to_Check_Out                                         = ['Hip_Hop_Artists_for_Me_to_Check_Out']
        self.c_Hip_Hop_Greatest_Albums_of_All_Time                                         = ['Hip_Hop_Greatest_Albums_of_All_Time']
        self.c_Hip_Hop_in_the_2010s_An_Essential_Chronology                                = ['Hip_Hop_in_the_2010s_An_Essential_Chronology']
        self.c_Japanese_Albums_That_I_Like                                                 = ['Japanese_Albums_That_I_Like']
        self.c_Most_commented_on_comment_boxes                                             = ['Most_commented_on_comment_boxes']
        self.c_Music_to_commit_suicide_to                                                  = ['Music_to_commit_suicide_to']
        self.c_My_100_Favourite_Singles_of_the_1990s                                       = ['My_100_Favourite_Singles_of_the_1990s']
        self.c_My_300_Favourite_Albums_Ranked                                              = ['My_300_Favourite_Albums_Ranked']
        self.c_My_300_favorite_Albums                                                      = ['My_300_favorite_Albums']
        self.c_My_75_Favourite_Singles_of_the_2000s                                        = ['My_75_Favourite_Singles_of_the_2000s']
        self.c_My_Best_Hip_Hop_Producers_Of_All_Time                                       = ['My_Best_Hip_Hop_Producers_Of_All_Time']
        self.c_My_Top_1000_Favorite_Hip_Hop_Albums                                         = ['My_Top_1000_Favorite_Hip_Hop_Albums']
        self.c_My_Top_100_Swedish_Albums                                                   = ['My_Top_100_Swedish_Albums']
        self.c_My_Top_2500_Bands_of_all_time                                               = ['My_Top_2500_Bands_of_all_time']
        self.c_My_Top_500_Songs_of_All_Time                                                = ['My_Top_500_Songs_of_All_Time']
        self.c_My_favorite_Album_Covers_of_SIX_different_types                             = ['My_favorite_Album_Covers_of_SIX_different_types']
        self.c_My_number_1_hits                                                            = ['My_number_1_hits']
        self.c_My_top_50_Britpop_songs_                                                    = ['My_top_50_Britpop_songs_']
        self.c_POPTIMISM_Boy_Bands_Girl_Groups_Pop_Rock_Electropop_90s_onward_Dance_Pop_Latin_Pop_K_Pop_J_Pop_Teen_Pop = ['POPTIMISM_Boy_Bands_Girl_Groups_Pop_Rock_Electropop_90s_onward_Dance_Pop_Latin_Pop_K_Pop_J_Pop_Teen_Pop']
        self.c_Rolling_Stone_Japans_100_Greatest_Japanese_Rock_Albums_of_All_Time          = ['Rolling_Stone_Japans_100_Greatest_Japanese_Rock_Albums_of_All_Time']
        self.c_Serpentine_Gallery_50_Of_The_Very_Best_Post_Punk_Albums                     = ['Serpentine_Gallery_50_Of_The_Very_Best_Post_Punk_Albums']
        self.c_Short_Dogs_In_The_House_The_Shortest_Albums_Ever                            = ['Short_Dogs_In_The_House_The_Shortest_Albums_Ever']
        self.c_TOP_100_SONGWRITERS                                                         = ['TOP_100_SONGWRITERS']
        self.c_Tapeaholics_Anonymous                                                       = ['Tapeaholics_Anonymous']
        self.c_Thailand_Luk_Thung_Molam                                                    = ['Thailand_Luk_Thung_Molam']
        self.c_The_Best_500_Albums_Of_The_20th_Century                                     = ['The_Best_500_Albums_Of_The_20th_Century']
        self.c_The_Best_Album_in_Every_Genre_Ive_Heard                                     = ['The_Best_Album_in_Every_Genre_Ive_Heard']
        self.c_The_Top_100_Albums_of_1980s                                                 = ['The_Top_100_Albums_of_1980s']
        self.c_The_Top_125_Singles_of_1997                                                 = ['The_Top_125_Singles_of_1997']
        self.c_The_Wires_150_Sonic_Essentials_and_Aural_Obscurities                        = ['The_Wires_150_Sonic_Essentials_and_Aural_Obscurities']
        self.c_The_best_songs_by_all_female_rock_bands                                     = ['The_best_songs_by_all_female_rock_bands']
        self.c_The_most_melancholic_albums_ever                                            = ['The_most_melancholic_albums_ever']
        self.c_These_1_840_K_Pop_Albums_Are_the_Best_Maybe                                 = ['These_1_840_K_Pop_Albums_Are_the_Best_Maybe']
        self.c_Top_1000_tracks_of_all_time                                                 = ['Top_1000_tracks_of_all_time']
        self.c_Top_100_Alt_Country_Albums_of_All_Time                                      = ['Top_100_Alt_Country_Albums_of_All_Time']
        self.c_Top_100_Favorite_Hip_Hop_Albums_of_All_Time                                 = ['Top_100_Favorite_Hip_Hop_Albums_of_All_Time']
        self.c_Top_100_Japanese_Albums                                                     = ['Top_100_Japanese_Albums']
        self.c_Top_1200_Singles_of_the_90s                                                 = ['Top_1200_Singles_of_the_90s']
        self.c_Top_200_Worst_Artists_v2                                                    = ['Top_200_Worst_Artists_v2']
        self.c_Top_250_Reggae_Albums_According_to_RYMs_Heavy_Reggae_Heads_                 = ['Top_250_Reggae_Albums_According_to_RYMs_Heavy_Reggae_Heads_']
        self.c_Top_500_Best_Albums_Ever_Made                                               = ['Top_500_Best_Albums_Ever_Made']
        self.c_Top_501_Favorite_Albums                                                     = ['Top_501_Favorite_Albums']
        self.c_Top_50_albums_by_nordic_scandinavian_artists                                = ['Top_50_albums_by_nordic_scandinavian_artists']
        self.c_Top_Artists_Chart                                                           = ['Top_Artists_Chart']
        self.c_Trap_releases_I_like                                                        = ['Trap_releases_I_like']
        self.c_WOEBOTs_The_100_Greatest_Records_Ever                                       = ['WOEBOTs_The_100_Greatest_Records_Ever']
        self.c_Who_ruled_the_80s_The_200_biggest_artists_of_the_decade_in_the_USA_         = ['Who_ruled_the_80s_The_200_biggest_artists_of_the_decade_in_the_USA_']
        self.c_XPNs_2014_88_Worst_Songs_Of_All_Time                                        = ['XPNs_2014_88_Worst_Songs_Of_All_Time']
        self.c_You_Make_Me_Feel_Like_A_Tyrannosaurus_Rex_Dinosaur_Cover_Art                = ['You_Make_Me_Feel_Like_A_Tyrannosaurus_Rex_Dinosaur_Cover_Art']


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
        self.chartRanks[0] = ['c_100_Favourite_Songs_of_All_Time', 'c_1500_Songs_From_Under_The_Floorboards', 'c_3500_Albums_You_Gotta_Listen_To', 'c_50_Greatest_Hawaii_Albums_of_All_Time', 'c_ALL_JAPAN_The_Greatest_JPN_Albums', 'c_Best_360_R_B_Albums']
        self.chartRanks[1] = ['c_Best_Albums_Of_All_Time', 'c_Best_Albums_of_Reggaeton_of_All_Time', 'c_Blood_Pumps_1500_Favorite_Albums', 'c_Hip_Hop_Greatest_Albums_of_All_Time', 'c_Japanese_Albums_That_I_Like', 'c_My_300_Favourite_Albums_Ranked']
        self.chartRanks[2] = ['c_My_300_favorite_Albums', 'c_My_Top_1000_Favorite_Hip_Hop_Albums', 'c_My_Top_100_Swedish_Albums', 'c_My_Top_500_Songs_of_All_Time', 'c_My_favorite_Album_Covers_of_SIX_different_types', 'c_Rolling_Stone_Japans_100_Greatest_Japanese_Rock_Albums_of_All_Time']
        self.chartRanks[3] = ['c_Serpentine_Gallery_50_Of_The_Very_Best_Post_Punk_Albums', 'c_Short_Dogs_In_The_House_The_Shortest_Albums_Ever', 'c_The_Best_500_Albums_Of_The_20th_Century', 'c_The_Best_Album_in_Every_Genre_Ive_Heard', 'c_The_Top_100_Albums_of_1980s', 'c_These_1_840_K_Pop_Albums_Are_the_Best_Maybe']
        self.chartRanks[4] = ['c_Top_100_Alt_Country_Albums_of_All_Time', 'c_Top_100_Favorite_Hip_Hop_Albums_of_All_Time', 'c_Top_100_Japanese_Albums', 'c_Top_250_Reggae_Albums_According_to_RYMs_Heavy_Reggae_Heads_', 'c_Top_500_Best_Albums_Ever_Made', 'c_Top_501_Favorite_Albums']
        self.chartRanks[5] = ['c_XPNs_2014_88_Worst_Songs_Of_All_Time']
        ######### Artists #########
        self.chartRanks[6] = ['c_200_Greatest_Rock_Artists_of_All_Time', 'c_Hip_Hop_Artists_for_Me_to_Check_Out', 'c_Top_200_Worst_Artists_v2', 'c_Top_Artists_Chart']
        ######### Script #########
        ######### Other #########
        self.chartRanks[7] = ['c_Around_the_World_of_Traditional_Music_in_80_Records', 'c_Best_Female_Voices', 'c_Best_of_Jazz_Improv_1970s_2010s_', 'c_Best_of_the_1970s', 'c_Best_of_the_1980s', 'c_Billboard_charts_1990s']
        self.chartRanks[8] = ['c_Black_White', 'c_Blow_Up_Magazines_600_essential_albums', 'c_Brazil', 'c_CITY_LIFE_ESCAPE', 'c_COUNTRY_STRONG', 'c_Eastern_Europe_DIY_Tapes_1978_89']
        self.chartRanks[9] = ['c_Greatest_Rappers_of_All_Time', 'c_Guide_To_Indie_Twee_Pop', 'c_Hazy_Memory_Nocturnal_Version', 'c_Helio_Reviews_the_Singles', 'c_Hip_Hop_in_the_2010s_An_Essential_Chronology', 'c_Most_commented_on_comment_boxes']
        self.chartRanks[10] = ['c_Music_to_commit_suicide_to', 'c_My_100_Favourite_Singles_of_the_1990s', 'c_My_75_Favourite_Singles_of_the_2000s', 'c_My_Best_Hip_Hop_Producers_Of_All_Time', 'c_My_Top_2500_Bands_of_all_time', 'c_My_number_1_hits']
        self.chartRanks[11] = ['c_My_top_50_Britpop_songs_', 'c_POPTIMISM_Boy_Bands_Girl_Groups_Pop_Rock_Electropop_90s_onward_Dance_Pop_Latin_Pop_K_Pop_J_Pop_Teen_Pop', 'c_TOP_100_SONGWRITERS', 'c_Tapeaholics_Anonymous', 'c_Thailand_Luk_Thung_Molam', 'c_The_Top_125_Singles_of_1997']
        self.chartRanks[12] = ['c_The_Wires_150_Sonic_Essentials_and_Aural_Obscurities', 'c_The_best_songs_by_all_female_rock_bands', 'c_The_most_melancholic_albums_ever', 'c_Top_1000_tracks_of_all_time', 'c_Top_1200_Singles_of_the_90s', 'c_Top_50_albums_by_nordic_scandinavian_artists']
        self.chartRanks[13] = ['c_Trap_releases_I_like', 'c_WOEBOTs_The_100_Greatest_Records_Ever', 'c_Who_ruled_the_80s_The_200_biggest_artists_of_the_decade_in_the_USA_', 'c_You_Make_Me_Feel_Like_A_Tyrannosaurus_Rex_Dinosaur_Cover_Art']
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
