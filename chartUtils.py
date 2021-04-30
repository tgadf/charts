from tqdm import tqdm
from multiprocessing import Pool
from functools import partial
from ioUtils import getFile, saveFile
from fsUtils import setFile
import time
from matchDBArtist import matchDBArtist
from difflib import SequenceMatcher



def getThresholds(minAlbums=None):
    thresholds = {}
    thresholds[1000] = {'numArtistName': 1, 'artistNameCutoff': 0.95, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': int(200/8), 'score': 10.0}
    thresholds[500]  = {'numArtistName': 1, 'artistNameCutoff': 0.95, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': int(200/8), 'score': 5.0}
    thresholds[200]  = {'numArtistName': 1, 'artistNameCutoff': 0.95, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': int(200/8), 'score': 2.5}
    thresholds[100]  = {'numArtistName': 1, 'artistNameCutoff': 0.95, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': int(100/8), 'score': 1.5}
    thresholds[50]   = {'numArtistName': 2, 'artistNameCutoff': 0.95, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': int(50/8), 'score': 1.5}
    thresholds[20]   = {'numArtistName': 2, 'artistNameCutoff': 0.95, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': 3, 'score': 1.5}
    thresholds[10]   = {'numArtistName': 5, 'artistNameCutoff': 0.90, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': 2, 'score': 1.5}
    thresholds[5]    = {'numArtistName': 5, 'artistNameCutoff': 0.90, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': 2, 'score': 1.5}
    thresholds[3]    = {'numArtistName': 5, 'artistNameCutoff': 0.90, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': 2, 'score': 1.5}
    thresholds[2]    = {'numArtistName': 5, 'artistNameCutoff': 0.90, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': 1, 'score': 2.0}
    thresholds[1]    = {'numArtistName': 5, 'artistNameCutoff': 0.90, 'artistAlbumCutoff': 0.9, 'numArtistAlbums': 1, 'score': 0.9}

    if minAlbums is None:
        return thresholds
    return thresholds[minAlbums]


def getIterItems():
    iterItems = {50: {"Max": 10000, "Vals": 50}}
    iterItems.update({20: {"Max": 50, "Vals": 100}})
    iterItems.update({10: {"Max": 20, "Vals": 200}})
    iterItems.update({5: {"Max": 10, "Vals": 250}})
    iterItems.update({3: {"Max": 5, "Vals": 500}})
    iterItems.update({2: {"Max": 3, "Vals": 750}})
    iterItems.update({1: {"Max": 2, "Vals": 1000}})
    return iterItems


def getLooseThresholds(numArtists=50, artistCutoff=0.75, albumCutoff=0.75):
    if albumCutoff is not None:
        return {'numArtistName': numArtists, 'artistNameCutoff': artistCutoff, 
                'artistAlbumCutoff': albumCutoff, 'numArtistAlbums': 1, 'score': albumCutoff}
    else:
        return {'numArtistName': numArtists, 'artistNameCutoff': artistCutoff, 
                'artistAlbumCutoff': None, 'numArtistAlbums': None, 'score': None}

    
def getThresholdsWithoutAlbums(cutoff=0.9):
    return {'numArtistName': 5, 'artistNameCutoff': cutoff, 'artistAlbumCutoff': None, 'numArtistAlbums': None, 'score': None}
    
def getAllThresholds():
    return {'numArtistName': 1, 'artistNameCutoff': 0.0, 'artistAlbumCutoff': None, 'numArtistAlbums': None, 'score': None}
    
    
def findMissingArtists(mdbmap, maindb):
    toget = {}
    ###################################################################################################
    # Diagnostics
    ###################################################################################################
    for primaryKey,artistData in mdbmap.items():
        for db,dbID in artistData.getDict().items():
            if dbID is not None:
                secondaryArtistName = maindb.getArtistDBNameFromID(db, dbID)
                if secondaryArtistName is None:
                    if toget.get(db) is None:
                        toget[db] = []
                    toget[db].append(primaryArtistName)
                    continue    
                    
                    
def addDiscogs(mdbmaps, chartType, amID, dbID):
    mdbmaps[chartType].addArtistDataByKey(amID, "Discogs", dbID)

def addAllMusic(mdbmaps, chartType, amID, dbID):
    if dbID is not None:
        dbID = dbID[2:]
    mdbmaps[chartType].addArtistDataByKey(amID, "AllMusic", dbID)

def addDeezer(mdbmaps, chartType, amID, dbID):
    mdbmaps[chartType].addArtistDataByKey(amID, "Deezer", dbID)

def addLastFM(mdbmaps, chartType, amID, dbID):
    mdbmaps[chartType].addArtistDataByKey(amID, "LastFM", dbID)

def addAlbumOfTheYear(mdbmaps, chartType, amID, dbID):
    mdbmaps[chartType].addArtistDataByKey(amID, "AlbumOfTheYear", dbID)

def addKWorbSpotify(mdbmaps, chartType, amID, dbID):
    mdbmaps[chartType].addArtistDataByKey(amID, "KWorbSpotify", dbID)

def addKWorbiTunes(mdbmaps, chartType, amID, dbID):
    mdbmaps[chartType].addArtistDataByKey(amID, "KWorbiTunes", dbID)

def addKWorbYouTube(mdbmaps, chartType, amID, dbID):
    mdbmaps[chartType].addArtistDataByKey(amID, "KWorbYouTube", dbID)

def addRateYourMusic(mdbmaps, chartType, amID, dbID):
    if dbID is not None:
        if dbID.startswith("Artist"):
            dbID = dbID[6:]
        if dbID.startswith("[Artist") and dbID.endswith("]"):
            dbID = dbID[7:-1]
    mdbmaps[chartType].addArtistDataByKey(amID, "RateYourMusic", dbID)

def addMusicBrainz(mdbmaps, chartType, amID, url, maindb=None):
    try:
        int(url)
        dbID = url
    except:
        if maindb is None:
            dbID = None
        else:
            dbID = maindb.getArtistDBIDFromUtil("MusicBrainz", url)
    mdbmaps[chartType].addArtistDataByKey(amID, "MusicBrainz", dbID)
    
    
def createIgnoreList():
    ignoresList = ["chartIgnores.yaml"]
    ignoresList = []

    ignoresList = []
    ignoresList.append("Artists Stand Up To Cancer")
    ignoresList.append("Cast Of Rent")
    ignoresList.append("2006 Broadway Cast Recording")
    ignoresList.append("Original Broadway Cast Of Dear Evan Hansen")
    ignoresList.append("Various")
    ignoresList.append("Various Artists")
    ignoresList.append("Various artists")
    ignoresList.append("various artists")
    ignoresList.append("Read-Along")
    ignoresList.append("unknown artist")
    ignoresList.append("Varios Artistas")
    ignoresList.append("Artists Against Bullying")
    ignoresList.append("Varios")
    ignoresList.append("Sleep Music Lullabies")
    ignoresList.append("Yoga Meditation Tribe")
    ignoresList.append("The Cast Of Stomp")
    ignoresList.append("Quincy Jones Feat. The Cast Of Stomp/The Yes/No Productions")
    ignoresList.append("Walt Disney Read-Along")
    ignoresList.append("Classical Lullabies For Babies Academy")
    ignoresList.append("Diverse")
    ignoresList.append("Blandade Artister")
    saveFile(idata=ignoresList, ifile="chartIgnoreArtists.yaml")

    unknownList = []
    unknownList.append("Amil-lion")
    unknownList.append("Yung Lito")
    unknownList.append("Idols")
    unknownList.append("X Factor Finalists")
    unknownList.append("R")
    unknownList.append("Malena")
    unknownList.append("Neales")
    unknownList.append("Incognito")
    unknownList.append('"Patches" Stewart')
    unknownList.append("X Factor NZ Top 12")
    unknownList.append("X Factor Finalists 2009")
    unknownList.append("X Factor Finalists 2008")
    unknownList.append("Factor Finalists 2011")
    saveFile(idata=unknownList, ifile="chartUnknownArtists.yaml")

    
    
    internationalList = []
    internationalList.append("3robiu")
    internationalList.append("Multi-interpretes")
    internationalList.append("Mormon Tabernacle Choir/Orch. At Temple Square/Yoncheva/Mumford/Villazon/Terfel (Wilberg)")
    internationalList.append("Villazon")
    internationalList.append("Mumford")
    internationalList.append("Vienna Philharmonic (Dudamel)")
    internationalList.append("Louisville Orchestra (Abrams)")
    internationalList += ['Eight Ranger', 'Yi Yang Qian Xi', "ONE N' ONLY", "MoLa", "Sus Invitados"]
    internationalList += ['Juanma Y Su Tuna Para Todo El Ano', 'NYC', 'Nogizaka 48', 'Sho Kiryuin from Golden Bomber']
    internationalList += ['The MONSTERS', 'ZERO-G', 'Huang Lige', 'Renzo', 'Bodan Shonen Dan', 'ST RISH', 'King Cream Soda']
    internationalList += ['Good Morning America', 'Hotta Ke BAND', 'Feng Jianyu', 'Stanley Most']
    internationalList += ['Cardiff City Fc', 'Leeds United Team', 'Monkey Hangerz']
    internationalList += ['Good Child Foundation', 'Neon Brotherhood', 'Rogue Souljahz']
    internationalList += ['GMC', 'Krossfade', 'Dave Howley', 'Toko', 'Y-not', 'Afro Music']
    internationalList += ['Husvenne', 'Maca Boy', 'Skyndeep', 'TwitterXmassingle', 'Julieanne Dineen', 'Julie-Anne Dineen', 'Anybodies']
    internationalList += ["Miro"] # Bulgaria
    internationalList += ["Lama", 'Vintaj', 'D-flow', 'U. Dumanska', 'Leonard', 'MARY', 'Naomi', 'IKE', 'FIESTA!', 'Francisco Loría']
    internationalList += ['SANARI', 'KIRA', 'Deep Ng', 'BOYZ', 'SEUNGRI', 'TLDK', 'Della', 'Dadado Huang', 'WONFU', 'DEN', 'PORTRAIT', '2T FLOW', 'GULF', 'VANGOE', 'DA 阿達']
    internationalList += ['Renan Almendarez Coello', 'Alfredo Ramirez Corral']
    internationalList += ['K-One', 'K.One', 'Miss Murphy', 'Bandits', 'Pop', 'Industry', 'Bigg Face', 'Atlas', 'Chico', 'Pictures', 'Jay-Jay Harvey']
    internationalList += ['Paw Justice', 'Jay-Jay Feeney', 'Guy Williams & Scribe', 'Dominic Harvey & Scribe']
    internationalList += ['Ole']
    saveFile(idata=internationalList, ifile="chartInternationalArtists.yaml")

    
    
    tonewUnknownList  = ['Lil Adrei', 'The 7 Dimensions', 'HIXTAPE', 'Porky Slim']
    tonewUnknownList += ['SL', 'Sidemen', 'Mastermind', 'HOSH', 'Frosty']
    saveFile(idata=tonewUnknownList, ifile="chartToNewArtists.yaml")

    
    
    soundtrackList = ['Jul På Vesterbro', 'Troy & Gabriella', 'High School Musical 2', "The Monstars"]
    saveFile(idata=soundtrackList, ifile="chartSoundtrackArtists.yaml")
    
    
    billboardList = ["Jazz Masters"]
    saveFile(idata=billboardList, ifile="chartBillboardArtists.yaml")

    
    
    applemusicList  = ['Dutch','Deno','DHT','Sadbh']
    applemusicList += ['DDG', 'Lean Trap', 'MOLO', 'Amina']
    applemusicList += ['Rocket Girls 101', "David Miles", "Cyril"]
    applemusicList += ["Camur"]
    saveFile(idata=applemusicList, ifile="chartAppleMusicArtists.yaml")

    
    
    spotifyList  = ['ROS', 'Mortal Frame', 'BENGELS', 'ILLSIGHT', 'KOI', 'VLS', 'EDGR', 'Kyle Edwards;DJ Smallz 732', 'Kyle Edwards;Chris Bevrly', 'La Vida Moderna', 'PJAY CZ', 'SK']
    spotifyList += ['KING', 'CHILI', 'İntizar', 'Archez', 'buller', "Moov'art"]
    spotifyList += ['Gunwest', 'NEEL', 'Cdeep', 'Fomins', 'Crime Sea']
    spotifyList += ['Alan 2', 'Adonis 66']
    spotifyList += ['DJ Yayo', 'Jason William']
    spotifyList += ['hachi', 'STEADY&CO.', 'Srene', 'Dsean', 'MASON', 'VA', 'IT’S', 'ONEONE',
                    'yui FLOWER FLOWER', 'ミゾベリョウ odol', 't', 'The GoGo Tuner Family']
    saveFile(idata=spotifyList, ifile="chartSpotifyArtists.yaml")

    
    
    musicvf  = ['The Georgia Minstrel Co.', "The Gilmore's Band", 'J. Aldrich Libbey', 'George Alexander', 'Lew Dockstader', 'Grace Nelson', 'The Columbia Comedy Trio', 'Frederic Rose', 'Ralph Herz', 'Joe Maxwell', 'A.D. Madeira']
    musicvf += ['The Lyric Quartet', "The Conway's Band", 'The Columbia Mixed Quartet', 'The Columbia Mixed Double Quartet', 'The Blue & White Marimba Band', 'The Imperial Quartet of Chicago', 'Louis Gravieure', "M.J. O'Connell", 'Harry Ellis', 'French Army Band', 'Eddy Brown', 'the Lyric Quartet', 'the Columbia Stellar Quartet']
    musicvf += ['The Broadway Quartet', 'Anthony Urato', 'The Club Royal Orchestra', 'The Virginians', 'The Broadway Dance Orchestra', 'Okeh Laughing Record', 'King Oliver & His Jazz Band', 'Lew Holtz & His Orchestra', 'Ace Brigode & His Virginians', 'Carolyn Thompson', 'The Radiolites', 'The Colonial Club Orchestra', 'Perry Askam',
                'Harold Grayson & His Orchestra', 'Lee Morse', 'Lou Gold', 'Adrian Schubert', 'Arnold Johnson']
    musicvf += ["Joe Morrison", "Emil Velasco", "Mark Fisher & His Orchestra", "His Salon Orchestra"]
    musicvf += ["George Hamilton", "Obregon's Orchestra", "Herbie Kay", "Frank Dailey", "Martha Stewart", "His Orchestra"]
    musicvf += ['September [Swedish dance singer]', 'Brian Keith', 'Coco', 'Chico [Chico Slimani]']
    musicvf += ['The Meters [1°]', 'Kenny', 'The Goodies', 'Cast', '2play', 'The Feeling', 'Matt Willis', 'His Swing Band', 'His Melody Makers']
    musicvf += ['The Spiders', 'Sonny Boy Williamson [2°]', 'The Heartbeats', 'Willows', 'The Falcons', 'Song Trust', 'Andy Gibson [singer]',
                'Desol', 'Dreamers', 'His All-Stars', 'the Soul Rockers', 'Earl', 'Sharon Paige and Harold Melvin', 'Victoria Shaw and Bryan White']
    saveFile(idata=musicvf, ifile="chartMusicVFArtists.yaml")

    
    
    rymList = ["deadman 死​人", "I Walk Down the Beaten Path, as the Clouds Continue Their Song... Crash... and the Rain Falls on But Victory Is in My Eye", "r/Kanye",
               "as the Clouds Continue Their Song... Crash... and the Rain Falls on But Victory Is in My Eye", "Rich & Famous", 'FRA',
               '80s', 'house', 'dance', 'The Union Gap', 'Miracle Records', 'Bc13',
               "12 Hundred Thousand Mysteries Were Released Into My Consciousness When All of a Sudden I Realised the Existence of a Sub-Realm That Led Me to the Ways of Non-Ecstatic Concentration",
               "Anagramma", "Tele-Visions"]
    rymList += ['Berliner Records', '周旋', 'Emerson Records', 'Edison', 'USA MI', 'Shakti', 'Co']
    rymList += ['ふーりがんだいなそー']
    saveFile(idata=rymList, ifile="chartRateYourMusicArtists.yaml")
    
    
    
    multimatch =['Dzharahov', 'Dzharakhov']
    multimatch+=['Gerald', 'Harvey', 'The Upsetters', 'The Upsetter', 'Lil B', "Lil 'B"]
    multimatch+=['Ritual', 'Rituaal', 'Band Aid 30', 'Band Aid 20']
    multimatch+=['Carmel', 'Caramel', 'Tomorrow', '4Tomorrow', 'G Herbo', "Lil' Herb"]
    multimatch+=['Super Junior-H']
    multimatch+=['Mark Wills', 'Mark Willis']
    multimatch+=["Night Shadows", "Night Shadow", "Yuan Yawei", "Tina Ray"]
    multimatch+=["Supercar", "60s", "Davenport", "DSBM"]
    saveFile(idata=multimatch, ifile="chartMultiMatchArtists.yaml")

    
    
    latinList = ["Miguel Pinero"]
    saveFile(idata=latinList, ifile="chartLatinAmericaArtists.yaml")


    ################################################################################
    # List of ignore files
    ################################################################################
    ignoresList = ["chartIgnoreArtists.yaml", "chartUnknownArtists.yaml", "chartInternationalArtists.yaml",
                   "chartSpotifyArtists.yaml", "chartToNewArtists.yaml", "chartAppleMusicArtists.yaml",
                   "chartSoundtrackArtists.yaml", "chartMusicVFArtists.yaml", "chartLatinAmericaArtists.yaml",
                   "chartRateYourMusicArtists.yaml", "chartBillboardArtists.yaml",
                   "chartMultiMatchArtists.yaml"]
    return ignoresList


def addSpotifyExtras(mdbmaps):
    print("=======> Adding Spotify Extras <=======")   
    addDiscogs(mdbmaps, "Spotify", "744a36c0d6f6a70d21492bacd787ed7c", "3284587")   ### [Son Miserables]
    addAllMusic(mdbmaps, "Spotify", "744a36c0d6f6a70d21492bacd787ed7c", "mn0003976615")   ### [Son Miserables]
    
    print("=======> Done Adding Spotify Extras <=======")   
    mdbmaps["Spotify"].save()

    
def addBillboardExtras(mdbmaps): 
    print("=======> Adding Billboard Extras <=======")   
    addDiscogs(mdbmaps, "Billboard", "ab57e7cccc317dd923eca645ea91f778", "383352")   ### [Joe Rene And Orchestra]
    addLastFM(mdbmaps, "Billboard", "27c0347cca29761886fef6f71b4e5343", None)   ### [The 5 Browns]
    addKWorbSpotify(mdbmaps, "Billboard", "f85c376f6e9d822bb0fd77d796c8d849", None)   ### [Los Cadillacs]
    
    print("=======> Done Adding Billboard Extras <=======")   
    mdbmaps["Billboard"].save()
    

def addBillboardYEExtras(mdbmaps):    
    addDiscogs(mdbmaps, "BillboardYE", "f19201e31420fee5b8b4b8d31afac756", "37737")   ### [Dave Brubeck]
    addRateYourMusic(mdbmaps, "BillboardYE", "f19201e31420fee5b8b4b8d31afac756", "Artist19093")   ### [Dave Brubeck]
    addAllMusic(mdbmaps, "BillboardYE", "f19201e31420fee5b8b4b8d31afac756", "0000958533")   ### [Dave Brubeck]
    addAllMusic(mdbmaps, "BillboardYE", "fbe56cc641e9d04e1b4fcdd924a9c8cc", "0001587860")   ### [Carlos y Alejandra]
    addKWorbSpotify(mdbmaps, "BillboardYE", "3a5c9959eac049a36959afef9cd6a50c", None)   ### [Los Cadillacs]

    mdbmaps["BillboardYE"].save()

    
def addMusicVFExtras(mdbmaps):    
    print("=======> Adding MusicVF Extras <=======")   
    addDiscogs(mdbmaps, "MusicVF", "1f7b5453ba1804f413bf127e230278ad", "4892300")   ### [The Castillian Troubadors]
    addDiscogs(mdbmaps, "MusicVF", "724e838678ee9e6c035146a1061a5d78", "8567655")   ### [The Wesson Brothers]
    addDiscogs(mdbmaps, "MusicVF", "f1610c7f9a40df7ed45a84483b92df86", "1775471")   ### [Maurice Burkhardt]
    addDiscogs(mdbmaps, "MusicVF", "f8d11da26d6696c67d821ef2208b88fc", "1140899")   ### [Les Paul And His Trio]
    addDiscogs(mdbmaps, "MusicVF", "dd725606a7b19cadd4fce4b32b3fd27a", "869936")    ### [Spade Cooley And His Orchestra]
    addDiscogs(mdbmaps, "MusicVF", "60eb2aca394160bae8544cc384c1a194", "283174")    ### [Bunny Berigan & His Orchestra]
    addDiscogs(mdbmaps, "MusicVF", "327e660219fe8294f8622cadd72892d5", "3766687")   ### [The Hotel Commodore Orchestra]
    addRateYourMusic(mdbmaps, "MusicVF", "4aa28ba2d125f2c83c2253daa5e58861", "Artist19093")   ### [Dave Brubeck]
    addDiscogs(mdbmaps, "MusicVF", "4aa28ba2d125f2c83c2253daa5e58861", "37737")   ### [Dave Brubeck]
    addAllMusic(mdbmaps, "MusicVF", "4aa28ba2d125f2c83c2253daa5e58861", "0000958533")   ### [Dave Brubeck]
    addAllMusic(mdbmaps, "MusicVF", "a4b9fb7275d480a00e15bf30c533c3cd", "0000407008")   ### [Nicole [German singer]]
    addDiscogs(mdbmaps, "MusicVF", "a4b9fb7275d480a00e15bf30c533c3cd", "409266")   ### [Nicole [German singer]]
    addDiscogs(mdbmaps, "MusicVF", "34578b29b07a064a2488b2b9aebdc119", "445147")   ### [Kiara]
    addDiscogs(mdbmaps, "MusicVF", "98e0dacca02ca21a790aeacd91106c3e", "307262")   ### [T-Bone Walker]

    addMusicBrainz(mdbmaps, "MusicVF", "48928634a6b700e3b2e349e3a8aad184", None)   ### [Jordan Hill]

    mdbmaps["MusicVF"].save()
    print("=======> Done Adding MusicVF Extras <=======")
    

def addRateYourMusicList2Extras(mdbmaps):   
    print("=======> Adding RYMList2 Extras <=======") 
    addRateYourMusic(mdbmaps, "RYMList2", "9e8065a28d13d1d8f6145db349c4601c", "Artist43129")   ### [Kyo]
    addRateYourMusic(mdbmaps, "RYMList2", "c1b596eeb3c08a7fc29faee03cc1d147", "Artist429150")   ### [Toshinori Kondo - Massimo Pupillo - Peter Brötzmann - Paal Nilssen-Love]
    addRateYourMusic(mdbmaps, "RYMList2", "5fc8411eed4d2ed37e7a0530f297a531", "Artist54994")   ### [Om]
    addRateYourMusic(mdbmaps, "RYMList2", "00b4bfa4c5363ef77a28adf013a0e636", "Artist224026")   ### [iTAL tEK]
    addRateYourMusic(mdbmaps, "RYMList2", "64851b4a679c792013267c8f2ce511ff", "Artist1054006")   ### [EP]
    
    addLastFM(mdbmaps, "RYMList2", "daa5e59581fdd686f080b09a9c34c898", None)   ### [Seven Codes]
    addLastFM(mdbmaps, "RYMList2", "21956c51a3d2155d642741f5562848cc", None)   ### [Bigot]
    addAlbumOfTheYear(mdbmaps, "RYMList2", "f36b4cf77fb2c87293beb3478c11a38e", None)   ### [Lil' B]
    addLastFM(mdbmaps, "RYMList2", "6aab6452f364430a730c00ef19493f47", None)   ### [Monophonia]
    addAllMusic(mdbmaps, "RYMList2", "d4086df35682f742512afd742738d565", None)   ### [The Beatnigs]
    addMusicBrainz(mdbmaps, "RYMList2", "d4086df35682f742512afd742738d565", None)   ### [The Beatnigs]

    mdbmaps["RYMList2"].save()
    print("=======> Done Adding RYMList2 Extras <=======")

    
def addRateYourMusicListExtras(mdbmaps):    
    print("=======> Adding RYMList Extras <=======")
    addRateYourMusic(mdbmaps, "RYMList", "a0941ae318d243562fd6e8f0047be68f", "Artist551368")   ### [rap]
    addRateYourMusic(mdbmaps, "RYMList", "66f4fd801ae17fbfa09db10051c97233", "Artist54494")   ### [Naranja Mecánica]
    addRateYourMusic(mdbmaps, "RYMList", "859f60d0c389ac6f41e234ebc13ca551", "Artist134194")   ### [Ion]
    
    addRateYourMusic(mdbmaps, "RYMList", "54d6f90de9c01bd5f97b0c5c935d6eb8", "Artist46147")   ### [Mirror]
    addRateYourMusic(mdbmaps, "RYMList", "58cb47daa671cb05cea372a8203f3889", "Artist72011")   ### [Tower]

    addAllMusic(mdbmaps, "RYMList", "fd136d5f4f65b8818ed836d0540eda89", None)   ### [Rocket]
    addAllMusic(mdbmaps, "RYMList", "3dcdf136b677a4edc4a6675c596c72b6", None)   ### [Waves]
    addAllMusic(mdbmaps, "RYMList", "0e0f1473ef1ff19290c73b10eb2bdde0", None)   ### [Aardvarks]
    addLastFM(mdbmaps, "RYMList", "5a8a3f660d458a8d13a1bcf248d83eb9", None)   ### [Magical Ring]    
    addLastFM(mdbmaps, "RYMList", "03136e1d681aa6f5bb67ee3411dc8a01", None)   ### [Low Tape]

    addMusicBrainz(mdbmaps, "RYMList", "185620464d79713e1ad7285065bcc493", None)   ### [Shivers]
    addDiscogs(mdbmaps, "RYMList", "6470207715f98801ea5f01b92b21984a", None)   ### [Coaxial]
    addMusicBrainz(mdbmaps, "RYMList", "b6ec90a4f91fa4b8ac079d8eb4dee97e", None)   ### [Mishka]
    addAllMusic(mdbmaps, "RYMList", "327ea2b427836d44dd7978bb7af16041", None)   ### [Balance and Composure]
    addDiscogs(mdbmaps, "RYMList", "57aad1e3cc25ed29fb1c89129480bac4", None)   ### [Population 1]
    addDiscogs(mdbmaps, "RYMList", "0405f666802c1615a9952210a2b53ae4", None)   ### [Sansa Trio]
    addDiscogs(mdbmaps, "RYMList", "d3fdfde1f38a3d208bef74073dd3dfff", None)   ### [Kiddog]
    addDiscogs(mdbmaps, "RYMList", "b85011581c61807fcb5b6eb7b3833c26", None)   ### [Andra]
    addDiscogs(mdbmaps, "RYMList", "4e38f40ee6f78bccbb598737c70e5a08", None)   ### [Radiana]
    addDiscogs(mdbmaps, "RYMList", "5781cac80925f8a24ddb4c2236969087", None)   ### [Ad Bourke]
    addDiscogs(mdbmaps, "RYMList", "0481ee6620e67e0728c89174dbb3cd58", None)   ### [Maestro Fresh‐Wes]
    addAllMusic(mdbmaps, "RYMList", "75d5d5dec840a474f21937840406085c", None)   ### [Talisma]
    addDiscogs(mdbmaps, "RYMList", "99937df9e12f1805c0600d3ed6b163be", None)   ### [Doo‐Dooettes]
    addLastFM(mdbmaps, "RYMList", "b5880e8f0311e1eb6d8ceb439d04dd4b", None)   ### [Model Citizens]
    addDiscogs(mdbmaps, "RYMList", "d6ddcc2f502bf5dca5d6ccfc7002a301", None)   ### [Special Affects]
    addRateYourMusic(mdbmaps, "RYMList", "dbd036ad4e5bab089be00e8b8262a788", "Artist35980")   ### [Sal Mineo]
    addRateYourMusic(mdbmaps, "RYMList", "1c15f053dec15c7c74977c131f0d0816", "Artist466083")   ### [Krew Kats]
    
    mdbmaps["RYMList"].save()
    print("=======> Done Adding RYMList Extras <=======")

    
def addRateYourMusicAlbumExtras(mdbmaps):
    print("=======> Adding RYMAlbum Extras <=======")
    addRateYourMusic(mdbmaps, "RYMAlbum", "2676354b20971358f99c018bb5166249", "Artist227989")   ### [Орк. Лен. Госфилармонии]
    addRateYourMusic(mdbmaps, "RYMAlbum", "5568c5cd1f375cfccebac78243f4226c", "Artist3704")   ### [Orchestre des Concerts Straram - Vlassoff Choir - Igor Stravinsky]
    addRateYourMusic(mdbmaps, "RYMAlbum", "3fb4f7b9b2ffd635c7825de270542e81", "Artist159869")   ### [L' orchestre symphonique Marius-François Gaillard]
    addRateYourMusic(mdbmaps, "RYMAlbum", "30c9590a4c918367a0c02f7eeca6bf92", "Artist3704")   ### [Philharmonic-Symphony Orchestra of New York - Igor Stravinsky]
    addRateYourMusic(mdbmaps, "RYMAlbum", "6e9cfbafc10856cd81a74d36d96989af", "Artist1388769")   ### [Ralph Ginsburgh]
    addRateYourMusic(mdbmaps, "RYMAlbum", "09a11e97c959023575e350a3e9b31476", "Artist574889")   ### [sic]
    addRateYourMusic(mdbmaps, "RYMAlbum", "fdfe0431ed10d22863c515b2a65b089a", "Artist1078036")   ### [Goo]
    addDiscogs(mdbmaps, "RYMAlbum", "130af77b0b47d5a301a2fe6990c8bf49", "452918")
    addDeezer(mdbmaps, "RYMAlbum", "e9fdb9535f5c977893ad49866e32d0a1", "94821")   ### [Vanity Fare]
    addDiscogs(mdbmaps, "RYMAlbum", "2da24bf0bdf2a9a61adbd2ac8a24087c", "904280")   ### [Liner]
    addAllMusic(mdbmaps, "RYMAlbum", "dc4fcb5ce6b42f19f21d4836c00e727a", None)   ### [Denis]
    addMusicBrainz(mdbmaps, "RYMAlbum", "b65aa7c8aa0dd0e421f49f0a4e6e44c2", None)   ### [Grimms]
    addMusicBrainz(mdbmaps, "RYMAlbum", "b788d97b37676ecbe3e8efffc9792bc0", None)   ### [Diamond Reo]
    addMusicBrainz(mdbmaps, "RYMAlbum", "a331af1b46d8d34d4de4d272981fc691", None)   ### [Pereza]
    addMusicBrainz(mdbmaps, "RYMAlbum", "8a9bc67d359b1708272ef9bd1a427578", None)   ### [Argent]
    addLastFM(mdbmaps, "RYMAlbum", "18ed6f753f8cd73d55dc349518afc6eb", None)   ### [Aragon]
    addAllMusic(mdbmaps, "RYMAlbum", "c537fdeaf8535fabf3d51fbc853cae18", None)   ### [Craaft]
    addAllMusic(mdbmaps, "RYMAlbum", "81186f9e1d816cc823060be6f7dd320c", None)   ### [Towers]
    addDiscogs(mdbmaps, "RYMAlbum", "6c97fba73dd6b1b947d03ffb83a51149", "2033528")   ### [Vlassoff Choir]
    
    addMusicBrainz(mdbmaps, "RYMAlbum", "0051c1befa7e3d119ee83afbdea7a69d", None)   ### [Montrose]
    addDiscogs(mdbmaps, "RYMAlbum", "46396fc41381788974c5228027ef2b18", None)   ### [Kestrel]
    addMusicBrainz(mdbmaps, "RYMAlbum", "e850b306e0389f39d67a67da495ad990", None)   ### [The Nuns]
    addRateYourMusic(mdbmaps, "RYMAlbum", "affa43e9bb02a864da11985179e46782", None)   ### [Millennium]
    addMusicBrainz(mdbmaps, "RYMAlbum", "c537fdeaf8535fabf3d51fbc853cae18", None)   ### [Craaft]
    
    mdbmaps["RYMAlbum"].save()
    print("=======> Done Adding RYMAlbum Extras <=======")


def addRateYourMusicSongExtras(mdbmaps):
    print("=======> Adding RYMSong Extras <=======")
    addRateYourMusic(mdbmaps, "RYMSong", "0aa91f1a30f8f2a42837000d86b0b077", "Artist730236")   ### [The Jewels]
    addRateYourMusic(mdbmaps, "RYMSong", "bbe2284440a5ca7e9cee0c894f4ffc6b", "Artist1456972")   ### [Audrey]
    addRateYourMusic(mdbmaps, "RYMSong", "0af9c0f46ea39e373954213be0af12dd", "Artist147012")   ### [Lone Star]
    addRateYourMusic(mdbmaps, "RYMSong", "929d91adaba88bb3bf0b1b252ac58708", "Artist420728")   ### [New Look]
    addRateYourMusic(mdbmaps, "RYMSong", "74eff37d9682574b063da121b162cb2d", "Artist286815")   ### [Harvey]
    addRateYourMusic(mdbmaps, "RYMSong", "7da006fc273092ffccdb3d84bcc378bc", "Artist5452")   ### [Gerald]

    addAllMusic(mdbmaps, "RYMSong", "4f42f062997510fb306f329531ca0a3e", None)   ### [Ffrancis]
    addAllMusic(mdbmaps, "RYMSong", "18290ea5e91975198dfa70f5c6770f0b", None)   ### [Choerry]
    addAllMusic(mdbmaps, "RYMSong", "bda28b3a4d25d6ace9d7dc0fbb0afd11", None)   ### [Virago]
    addMusicBrainz(mdbmaps, "RYMSong", "bda28b3a4d25d6ace9d7dc0fbb0afd11", None)   ### [Virago]
    addLastFM(mdbmaps, "RYMSong", "4f42f062997510fb306f329531ca0a3e", None)   ### [Ffrancis]
    
    mdbmaps["RYMSong"].save()
    print("=======> Done Adding RYMSong Extras <=======")