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
    if dbID is None:
        return
    mdbmaps[chartType].addArtistDataByKey(amID, "Discogs", dbID)

def addAllMusic(mdbmaps, chartType, amID, dbID):
    if dbID is None:
        return
    dbID = dbID[2:]
    mdbmaps[chartType].addArtistDataByKey(amID, "AllMusic", dbID)

def addDeezer(mdbmaps, chartType, amID, dbID):
    if dbID is None:
        return
    mdbmaps[chartType].addArtistDataByKey(amID, "Deezer", dbID)

def addRateYourMusic(mdbmaps, chartType, amID, dbID):
    if dbID is None:
        return
    if dbID.startswith("Artist"):
        dbID = dbID[6:]
    if dbID.startswith("[Artist") and dbID.endswith("]"):
        dbID = dbID[7:-1]
    mdbmaps[chartType].addArtistDataByKey(amID, "RateYourMusic", dbID)

def addMusicBrainz(mdbmaps, chartType, amID, url):
    try:
        int(url)
        dbID = url
    except:
        dbID = maindb.getArtistDBIDFromUtil("MusicBrainz", url)
    if dbID is None:
        return
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

    
    
    latinList = ["Miguel Pinero"]
    saveFile(idata=latinList, ifile="chartLatinAmericaArtists.yaml")


    ################################################################################
    # List of ignore files
    ################################################################################
    ignoresList = ["chartIgnoreArtists.yaml", "chartUnknownArtists.yaml", "chartInternationalArtists.yaml",
                   "chartSpotifyArtists.yaml", "chartToNewArtists.yaml", "chartAppleMusicArtists.yaml",
                   "chartSoundtrackArtists.yaml", "chartMusicVFArtists.yaml", "chartLatinAmericaArtists.yaml",
                   "chartRateYourMusicArtists.yaml", "chartBillboardArtists.yaml"]
    return ignoresList


def addBillboardExtras(mdbmaps):    
    addDiscogs(mdbmaps, "Billboard", "ab57e7cccc317dd923eca645ea91f778", "383352")   ### [Joe Rene And Orchestra]
    mdbmaps["Billboard"].save()
    

def addBillboardYEExtras(mdbmaps):    
    addDiscogs(mdbmaps, "BillboardYE", "f19201e31420fee5b8b4b8d31afac756", "37737")   ### [Dave Brubeck]
    addRateYourMusic(mdbmaps, "BillboardYE", "f19201e31420fee5b8b4b8d31afac756", "Artist19093")   ### [Dave Brubeck]
    addAllMusic(mdbmaps, "BillboardYE", "f19201e31420fee5b8b4b8d31afac756", "0000958533")   ### [Dave Brubeck]
    addAllMusic(mdbmaps, "BillboardYE", "fbe56cc641e9d04e1b4fcdd924a9c8cc", "0001587860")   ### [Carlos y Alejandra]
    mdbmaps["BillboardYE"].save()

    
def addMusicVFExtras(mdbmaps):    
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

    mdbmaps["MusicVF"].save()
    

def addRateYourMusicList2Extras(mdbmaps):    
    addRateYourMusic(mdbmaps, "RYMList2", "9e8065a28d13d1d8f6145db349c4601c", "Artist43129")   ### [Kyo]
    addRateYourMusic(mdbmaps, "RYMList2", "c1b596eeb3c08a7fc29faee03cc1d147", "Artist429150")   ### [Toshinori Kondo - Massimo Pupillo - Peter Brötzmann - Paal Nilssen-Love]
    addRateYourMusic(mdbmaps, "RYMList2", "5fc8411eed4d2ed37e7a0530f297a531", "Artist54994")   ### [Om]
    addRateYourMusic(mdbmaps, "RYMList2", "00b4bfa4c5363ef77a28adf013a0e636", "Artist224026")   ### [iTAL tEK]
    addRateYourMusic(mdbmaps, "RYMList2", "64851b4a679c792013267c8f2ce511ff", "Artist1054006")   ### [EP]
    
    mdbmaps["RYMList2"].save()

    
def addRateYourMusicListExtras(mdbmaps):    
    addRateYourMusic(mdbmaps, "RYMList", "a0941ae318d243562fd6e8f0047be68f", "Artist551368")   ### [rap]
    addRateYourMusic(mdbmaps, "RYMList", "66f4fd801ae17fbfa09db10051c97233", "Artist54494")   ### [Naranja Mecánica]
    addRateYourMusic(mdbmaps, "RYMList", "859f60d0c389ac6f41e234ebc13ca551", "Artist134194")   ### [Ion]
    mdbmaps["RYMList"].save()

def addRateYourMusicAlbumExtras(mdbmaps):
    addRateYourMusic(mdbmaps, "RYMAlbum", "2676354b20971358f99c018bb5166249", "Artist227989")   ### [Орк. Лен. Госфилармонии]
    addRateYourMusic(mdbmaps, "RYMAlbum", "5568c5cd1f375cfccebac78243f4226c", "Artist3704")   ### [Orchestre des Concerts Straram - Vlassoff Choir - Igor Stravinsky]
    addRateYourMusic(mdbmaps, "RYMAlbum", "3fb4f7b9b2ffd635c7825de270542e81", "Artist159869")   ### [L' orchestre symphonique Marius-François Gaillard]
    addRateYourMusic(mdbmaps, "RYMAlbum", "30c9590a4c918367a0c02f7eeca6bf92", "Artist3704")   ### [Philharmonic-Symphony Orchestra of New York - Igor Stravinsky]
    addRateYourMusic(mdbmaps, "RYMAlbum", "6e9cfbafc10856cd81a74d36d96989af", "Artist1388769")   ### [Ralph Ginsburgh]
    addRateYourMusic(mdbmaps, "RYMAlbum", "09a11e97c959023575e350a3e9b31476", "Artist574889")   ### [sic]
    addRateYourMusic(mdbmaps, "RYMAlbum", "fdfe0431ed10d22863c515b2a65b089a", "Artist1078036")   ### [Goo]

    mdbmaps["RYMAlbum"].save()

def addRateYourMusicSongExtras(mdbmaps):
    addRateYourMusic(mdbmaps, "RYMSong", "0aa91f1a30f8f2a42837000d86b0b077", "Artist730236")   ### [The Jewels]
    addRateYourMusic(mdbmaps, "RYMSong", "bbe2284440a5ca7e9cee0c894f4ffc6b", "Artist1456972")   ### [Audrey]
    addRateYourMusic(mdbmaps, "RYMSong", "0af9c0f46ea39e373954213be0af12dd", "Artist147012")   ### [Lone Star]
    addRateYourMusic(mdbmaps, "RYMSong", "929d91adaba88bb3bf0b1b252ac58708", "Artist420728")   ### [New Look]
    addRateYourMusic(mdbmaps, "RYMSong", "74eff37d9682574b063da121b162cb2d", "Artist286815")   ### [Harvey]
    addRateYourMusic(mdbmaps, "RYMSong", "7da006fc273092ffccdb3d84bcc378bc", "Artist5452")   ### [Gerald]
    mdbmaps["RYMSong"].save()

def addRateYourMusicExtras(mdbmaps):
    addDiscogs(mdbmaps, "RYM", "b412df01490b6da86145e6b0e890e59c", "288559")   ### [Nostromo]
    addDiscogs(mdbmaps, "RYM", "c2d4a776c42f2566cac00f2423891439", "215668")   ### [The Gathering]
    addDiscogs(mdbmaps, "RYM", "c6882555eceadb0c91b633a449077513", "955")   ### [Broadcast]
    addDiscogs(mdbmaps, "RYM", "6c7a6b3c6f8de01bba1f9d85c6ee8146", "999922")   ### [Pantheïst]
    addDiscogs(mdbmaps, "RYM", "400685efa3748c9536fcd068be0a3f11", "10995")   ### [e.badu]
    addDiscogs(mdbmaps, "RYM", "42437a44e2a2a2fc89779f979a4e3200", "3065668")   ### [Mi'Gauss]
    addDiscogs(mdbmaps, "RYM", "770f5e3fc15226b23ea5ffbc5ff084aa", "851948")   ### [Nebelnest]
    addDiscogs(mdbmaps, "RYM", "1c881264a592a9a3ea38373c0bd75663", "27341")   ### [Automator]
    
    addDiscogs(mdbmaps, "RYM", "2597f344f61ca6c416eb9a0cfb67dec4", "227036")   ### [The Impressions]
    addDiscogs(mdbmaps, "RYM", "da5d62968824257ba7cbf3b2f7f47ad1", "450658")   ### [The Playmates]
    addDiscogs(mdbmaps, "RYM", "ed0bfd1197e4073ad35673c61fecc9fb", "4294583")   ### [Neues Symphonie-Orchester]
    addDiscogs(mdbmaps, "RYM", "c1b893709cdd72f1588d33298ec26974", "5471330")   ### [Philharmonic-Symphony Orchestra of New York]
    addDiscogs(mdbmaps, "RYM", "d0f3d6e11b58fa9c56495b30772121c4", "2635291")   ### [Orchestre des Concerts Straram]
    addDiscogs(mdbmaps, "RYM", "dc04678008e9ee4c59c8e652a5591378", "980605")   ### [Palace Theatre Orchestra]
    addDiscogs(mdbmaps, "RYM", "d8fba95a5c8459942e6f2b67a734248c", "5355721")   ### [Berlin Cathedral Choir]
    addDiscogs(mdbmaps, "RYM", "b724641190d765cfdb64b61a197cf9ec", "1055642")   ### [Erika Stiedry-Wagner]
    addDiscogs(mdbmaps, "RYM", "6c4555fceb1524eb620cb8d7cd2177d4", "1055646")   ### [Kalman Bloch]
    addDiscogs(mdbmaps, "RYM", "7d2b99fe085718896f914ad195fccd23", "1178525")   ### [Joshua White and His Carolinians]
    addDiscogs(mdbmaps, "RYM", "218215868a1831f082ee2446fd0b234b", "5007882")   ### [Hulda Geischen]
    addDiscogs(mdbmaps, "RYM", "a836c30a9ca2c5df8195a76b038ba13c", "793224")   ### [Christine Charnstrom]
    addDiscogs(mdbmaps, "RYM", "1f9529765ea22099272759b2c94299b1", "793222")   ### [William Wendlandt]
    addDiscogs(mdbmaps, "RYM", "702a8c46e34e083340f586abf99815f3", "1055647")   ### [Leonard Posella]
    addDiscogs(mdbmaps, "RYM", "7d06e4a0884c421672a908c92d65a8ec", "355185")   ### [The Quintet of the Hot Club of France]    
    
    addDiscogs(mdbmaps, "RYM", "655b7353bc2671baab4c5326dfa14967", "3378978")   ### [Polk Miller and His Old South Quartette]
    addDiscogs(mdbmaps, "RYM", "afbcdcd7941e83bf90346956af6b1c45", "412679")   ### [Henry Thomas (Rag Time Texas)]
    addDiscogs(mdbmaps, "RYM", "f3390264106f051e68cfa67a6b58d1d6", "412679")   ### [Henry Thomas (Ragtime Texas)]
    addDiscogs(mdbmaps, "RYM", "faa06e387b42e380dd17c260f91296f2", "1353296")   ### [Dinwiddie Colored Quartet]
    addDiscogs(mdbmaps, "RYM", "8c24d342a16ffdc026e42381ca8c0fd9", "1411406")   ### [Issler's Orchestra]
    addDiscogs(mdbmaps, "RYM", "3281826c2d5b9adc0ad8e3d82b2dbdd7", "499047")   ### [Sousa's Grand Concert Band]
    addDiscogs(mdbmaps, "RYM", "a2695277c08e4535d2bf71d34cf9ac28", "446633")   ### [Bud Powell's Modernists]
    addDiscogs(mdbmaps, "RYM", "17dd63ebbd6ec04a04f7689ddfc9b647", "338994")   ### [His Savoy Ballroom Five]
    addDiscogs(mdbmaps, "RYM", "f1c2061fbda0460d2ab0fd056d691933", "908712")   ### [Eck Robertson and Family]
    addDiscogs(mdbmaps, "RYM", "4dab5dd58703d2aa74960ecd2f596b83", "661815")   ### [Sylvester Weaver]
    addDiscogs(mdbmaps, "RYM", "aec09a370049e6fda89fd43c3824d0e7", "4839830")   ### [Brilliant Quartette]
    addDiscogs(mdbmaps, "RYM", "325eed78dfbbecbe672c9981189e9c2b", "847625")   ### [J. Yorke AtLee]
    addDiscogs(mdbmaps, "RYM", "c52d53b6ec89fc86ac316e10fdda1bdf", "5824824")   ### [Cullen and Collins]
    addDiscogs(mdbmaps, "RYM", "c4ca78f1753020c798d098c6d304e5b1", "666107")   ### [Elvie Thomas]
    addDiscogs(mdbmaps, "RYM", "b9fbec73f6e105560c512bc937446081", "353252")   ### [Mississippi Jook Band]
    addDiscogs(mdbmaps, "RYM", "a42511559f8292644009f37ebf335abc", "436787")   ### [Charlie Jackson]
    addDiscogs(mdbmaps, "RYM", "05d291e75f0152c8e0ce6e3993f8d244", "801122")   ### [George P. Watson]
    addDiscogs(mdbmaps, "RYM", "b21957a69ecc06bdf9579364dfb2118e", "847629")   ### [Edison Male Quartette]
    addDiscogs(mdbmaps, "RYM", "0889f1094b161242bfad31fced49b2dc", "1862654")   ### [Ed Bell]
    addDiscogs(mdbmaps, "RYM", "9ef9bd6dd952d1e82bee374c1c68f6e1", "5721436")   ### [Toshiko Sekiya]
    addDiscogs(mdbmaps, "RYM", "c24b25d83aff5085d2b37d96baff3b3c", "1076121")   ### [John Thomas]
    addDiscogs(mdbmaps, "RYM", "99f1cf83494797df333a6285921e353a", "1996928")   ### [Earl Fuller's Famous Jazz Band]
    addDiscogs(mdbmaps, "RYM", "fa99e393c6660a8978d03707954ee161", "2736152")   ### [Jim Europe's 369th Infantry "Hellfighters" Band]
    addDiscogs(mdbmaps, "RYM", "a5de9809a44f794904dc9454d383c82c", "623155")   ### [Garfield Akers]    
    
    addDiscogs(mdbmaps, "RYM", "6405bd1e7f4d9543954c1e55c45f31f8", "2299153")   ### [Deirdre Ní Fhlionn]
    addDiscogs(mdbmaps, "RYM", "6089f0f0334fad7d79381da144e534d1", "135872")   ### [Hank Mobley and His All Stars]
    addDiscogs(mdbmaps, "RYM", "67c3729149a19b98af77c612dcf255b0", "3913110")   ### [Charlene Bartley]
    addDiscogs(mdbmaps, "RYM", "34cd32e8567369a07ca766fdb2209a20", "911144")   ### [Jeannie Robertson]
    addDiscogs(mdbmaps, "RYM", "28e6915244c24aa5f0d814d31e12a74c", "1003176")   ### [David Lloyd]
    addDiscogs(mdbmaps, "RYM", "1c71d2b7ba686b06ebf51140b31cd18f", "1970583")   ### [Marie-Josée Neuville]
    addDiscogs(mdbmaps, "RYM", "30657e52bbd657e4765bd8706f220539", "3683258")   ### [La Vergne]    
    addDiscogs(mdbmaps, "RYM", "2747f9b3d79d29690a6b209a4fcdd198", "376042")   ### [Shorty Rogers and His Giants]
    addDiscogs(mdbmaps, "RYM", "08712c79ded955a68286aadafe733131", "4833967")   ### [Dixie Kwankwa]
    addDiscogs(mdbmaps, "RYM", "607ab865a5ec9b6d4dad303bbc14ecec", "436588")   ### [Dick Schory's New Percussion Ensemble]
    addDiscogs(mdbmaps, "RYM", "8deb0fc42164c8a59d13ebcbfbb2be11", "665985")   ### [Yusef Lateef and His Men]
    addDiscogs(mdbmaps, "RYM", "2b2d1f90766ffc7be609af7ce9aa9c24", "927031")   ### [The Al Cohn Quintet]
    addDiscogs(mdbmaps, "RYM", "7f02b983e988456357896af81a45dc07", "897724")   ### [Buddy Bregman and His Orchestra]
    addDiscogs(mdbmaps, "RYM", "81fb468bc3a9c1e908a52b415090941d", "299191")   ### [Michel Legrand and His Orchestra]
    addDiscogs(mdbmaps, "RYM", "553fc674557321e4e35b09647bbee90a", "6299361")   ### [Fafá Lemos e sua orquestra]
    addDiscogs(mdbmaps, "RYM", "64c70423a94683f1caccb3aa52ed3ab5", "2362045")   ### [Orchestre philharmonique de Paris]
    addDiscogs(mdbmaps, "RYM", "029eb39b39a2dbe178a4f8e4b48ae95c", "1958975")   ### [Orchestre du Festival de Prades]
    addDiscogs(mdbmaps, "RYM", "d1c6caa86547cc5f3776fe0ed5cf281e", "1637813")   ### [His Pals Shelly Manne]

    addDiscogs(mdbmaps, "RYM", "29d621fbbf30da04691de89525a9b5cd", "278")   ### [DJ Peshay]    
    addDiscogs(mdbmaps, "RYM", "b5aa5281d053c376a0d3555eb5db45ff", "434143")   ### [Lil 'B]
    addDiscogs(mdbmaps, "RYM", "a452045cc731be869f11b911a3b13388", "1253377")   ### [sic]
    addDiscogs(mdbmaps, "RYM", "99a0005188d61cc428af09462863ec49", "4764735")   ### [NIIC]
    addDiscogs(mdbmaps, "RYM", "dcedf8aa36dfb5a933377f3a9a52c156", "4588904")   ### [DUCKWRTH]
    addDiscogs(mdbmaps, "RYM", "ecacfcbbe31cb94208d1a3e07c16abd1", "3057476")   ### [Joey B4DA\$\$]    
    addDiscogs(mdbmaps, "RYM", "73c7a3fa78dafa64ba16406afbda5948", "108050")   ### [Dan Johnston]
    addDiscogs(mdbmaps, "RYM", "84b804b1e9282ef8d0dbe49f64468809", "458405")   ### [The Outsiders]
    addDiscogs(mdbmaps, "RYM", "e078ae76fe46e4e16c774dd36b300bef", "302911")   ### [The Smoke]
    addDiscogs(mdbmaps, "RYM", "a9a1aeea91196a30228fddbd5b9e59ef", "280969")   ### [Eloy]
    addDiscogs(mdbmaps, "RYM", "72d27d9974163bedc37ad008e60f1ee8", "198152")   ### [Flipper]
    addDiscogs(mdbmaps, "RYM", "2e1fafa6e1648130158860a388c3163f", "443153")   ### [Siekiera]
    addDiscogs(mdbmaps, "RYM", "9048746abe8d495a04d998788bb96862", "262879")   ### [Shakti]
    addDiscogs(mdbmaps, "RYM", "3e27dbbcce65177c948dff6168e2f0cd", "3852")   ### [PRMLSCRM]
    addDiscogs(mdbmaps, "RYM", "83e95e8f6d88b5d97fd8b0f10086c548", "25557")   ### [e.s.t.]
    addDiscogs(mdbmaps, "RYM", "a728c3c5c6a102ad3a56e9a15445f810", "87652")   ### [(The) Melvins]
    addDiscogs(mdbmaps, "RYM", "cf9cf7161f01484b6adc057fa0164a90", "352674")   ### [Neko Saitō]
    addDiscogs(mdbmaps, "RYM", "1151e151ef604cfb46d06fa2f33efacc", "2876366")   ### [Éva Csizmadia]
    addDiscogs(mdbmaps, "RYM", "603c93aa41f9e997813b98943b6239f2", "2876355")   ### [Jardena Flückiger]
    addDiscogs(mdbmaps, "RYM", "5527b04659ae673f26b4583ae08de031", "2876363")   ### [Christoph Bösch]
    addDiscogs(mdbmaps, "RYM", "01903ec5cec2c504ffef6048a198ed11", "7173070")   ### [Ana Frango Elétrico]
    addDiscogs(mdbmaps, "RYM", "f43520b4fa39994c27ae6bb21905788c", "1149845")   ### [André O. Möller]
    addDiscogs(mdbmaps, "RYM", "4e4d4044d74e94ae63970ed73254588e", "7231890")   ### [rook]
    addDiscogs(mdbmaps, "RYM", "103e002d5346f49a44ff8723006a9113", "3337502")   ### [Àrsaidh]
    addDiscogs(mdbmaps, "RYM", "c8918941cb5d205269af1a63987f5c52", "6271575")   ### [Molchat doma]
    addDiscogs(mdbmaps, "RYM", "ff1fafb126a8fe74cb212745a75a8dd4", "4417063")   ### [２８１４]
    addDiscogs(mdbmaps, "RYM", "357e5c72f66aa5040fe0a376ea48188e", "43637")   ### [The Silver Mt. Zion Memorial Orchestra]
    addDiscogs(mdbmaps, "RYM", "d573f86d774c7e281826e4ab57b6a8c3", "2876730")   ### [The Fabulous Sidney Bechet and His Hot Six]
    addDiscogs(mdbmaps, "RYM", "7279748ead8c27dfb6af843aa142af36", "2778287")   ### [Eri Chiemi]
    addDiscogs(mdbmaps, "RYM", "735ac34b23c753af8454cfc5208f9c86", "6396510")   ### [Luck Ganriki]
    addDiscogs(mdbmaps, "RYM", "c52d60e86c79848954d225e3aafe438d", "3425915")   ### [Black Unity Trio]
    addDiscogs(mdbmaps, "RYM", "14f1bd8a1ccafc0cec90bd06e7a006e5", "328142")   ### [Jimmy "Fast Fingers" Dawkins]
    addDiscogs(mdbmaps, "RYM", "045387d57d67c42cfec24ddfcecb0192", "758374")   ### [Juan Peña «El Lebrijano»]
    addDiscogs(mdbmaps, "RYM", "ae6fed2cba48ce7c04697c51a5af0e50", "410281")   ### [Ali Touré dit Farka]
    addDiscogs(mdbmaps, "RYM", "3a4d3bf417686373d46be43d139d4462", "435555")   ### [ Czech Philharmonic Orchestra]
    addDiscogs(mdbmaps, "RYM", "490f06c583260a47676b90b4a40f8ac5", "389074")   ### [Jordan de la Sierra]
    addDiscogs(mdbmaps, "RYM", "a5665ff119482491eef094fd5c384cb0", "1012379")   ### [Kazimierz Pustelak]
    addDiscogs(mdbmaps, "RYM", "df66cfd03fc8dabb2fb16b9cf6a2dc6c", "393383")   ### [Iona Brown]
    addDiscogs(mdbmaps, "RYM", "a35f8891b68649a70fdfb82d11fefd2e", "393748")   ### [Jazz Q Praha]
    addDiscogs(mdbmaps, "RYM", "211dda01903421440a1d8d8c058e1b67", "854009")   ### [Markos Vamvakaris]
    addDiscogs(mdbmaps, "RYM", "9e4055f569856fd381823e7e2d43b4fd", "1749597")   ### [Osvaldo Berlingieri]
    addDiscogs(mdbmaps, "RYM", "1d236c331c0767fb2da0f51f0caab1da", "691520")   ### [The Radio Jazz Group]
    addDiscogs(mdbmaps, "RYM", "2df28b0c74b94b666722ef1c5441e4db", "1272586")   ### [The Festival Singers of Canada]
    addDiscogs(mdbmaps, "RYM", "d051b0496515f68e31db1b68785760fc", "839232")   ### [Martha Lipton]
    addDiscogs(mdbmaps, "RYM", "5462d44ca10aed289ef26cafdc65d83a", "867251")   ### [The Hungarian String Quartet]
    addDiscogs(mdbmaps, "RYM", "152b91fb93b3a82d168c6bd149e9186e", "805380")   ### [Государственный академический симфонический оркестр СССР]
    addDiscogs(mdbmaps, "RYM", "db09402bb536fcd7356b49f488282bb2", "832992")   ### [Evgeny Svetlanov]
    addDiscogs(mdbmaps, "RYM", "53a6c2512f334086a94cadddf80b2daf", "3759868")   ### [Dan Casamajor]
    addDiscogs(mdbmaps, "RYM", "231778a8b80df709a2b5124a35998c6b", "330155")   ### [The Amazing New Chico Hamilton Quintet]
    addDiscogs(mdbmaps, "RYM", "3ca431c888b9ac7a80f249811ea4056b", "854870")   ### [Rutgers University Choir]
    addDiscogs(mdbmaps, "RYM", "f0aa210a8c2afb4486ccd1ba22f28901", "617405")   ### [Gertie Charlent]
    addDiscogs(mdbmaps, "RYM", "89cf6f9e74bfee53ffb064d8064d7452", "495005")   ### [William Pearson]
    addDiscogs(mdbmaps, "RYM", "bb8e38b3af7421a15ba1b372321e32a4", "330155")   ### [The New Dynamic Chico Hamilton Quintet]
    addDiscogs(mdbmaps, "RYM", "7194ca36e5129a9ced0bcd24d80eac42", "862694")   ### [Jonathan Summers]
    addDiscogs(mdbmaps, "RYM", "58724807f902abd7a5c0b0096a2fceef", "826708")   ### [Maryvonne Le Dizès-Richard]
    addDiscogs(mdbmaps, "RYM", "6ca1b8e6addd5eca08feef30cc57769d", "3459608")   ### [Ferkat al Ard]
    addDiscogs(mdbmaps, "RYM", "cd53adf8d2ce3e6879ff722d84e0dca3", "2669509")   ### [Geraldo Filme]
    addDiscogs(mdbmaps, "RYM", "8c6c814a816f45569bd0973a4f919844", "1337625")   ### [Le Quatuor Talich]
    addDiscogs(mdbmaps, "RYM", "3945f50b7cb9f15109a867cf6103cb7d", "807180")   ### [Maksim Dunaevsky]
    addDiscogs(mdbmaps, "RYM", "95377c52d62f0bf710af6d239de53c82", "490279")   ### [CBSO Chorus]
    addDiscogs(mdbmaps, "RYM", "0005e399c80c3eb17874aa346c474229", "1253954")   ### [Torleif Lännerholm]
    addDiscogs(mdbmaps, "RYM", "d9b51b3f5a915209d0e056ee11d967c7", "1025047")   ### [Cecil Taylor Segments II (Orchestra of Two Continents)]
    addDiscogs(mdbmaps, "RYM", "90d4102d96dbcb7abd5004fdae52e3bb", "2986165")   ### [Sänger Freies Berlin]
    addDiscogs(mdbmaps, "RYM", "da1010471ac8d662896e4048344872b8", "1082066")   ### [Mazhar Fuat Özkan]
    addDiscogs(mdbmaps, "RYM", "89980cf77ff4decfdf423ee8662a0de9", "1977821")   ### [University of Utah Civic Chorale]
    addDiscogs(mdbmaps, "RYM", "144f430d7a803860899112cc7b38708e", "299241")   ### [Pandit Ravi Shankar]
    addDiscogs(mdbmaps, "RYM", "276556ce8b1f3eb3018bd6e0077bf694", "1025915")   ### [Steve Lacy Seven]
    addDiscogs(mdbmaps, "RYM", "d0f665049ba4651e507adc844ff94e68", "965186")   ### [Orquestra Fantasma]
    addDiscogs(mdbmaps, "RYM", "544d900c8df259cbfaf636a999a2a37a", "7777540")   ### [L'Eclipse De L'I.J.A.]
    addDiscogs(mdbmaps, "RYM", "7bf6c9f737696cb2381a442d99a1d5e7", "1926538")   ### [Zar1]
    addDiscogs(mdbmaps, "RYM", "8ed4b4bb9317fa7782a2471f36f69486", "20184")   ### [Paco De Lucia]    
    
    addDiscogs(mdbmaps, "RYM", "b1dba68bdc860bc36f21945f8ed21787", "1250466")   ### [Hunger]
    addDiscogs(mdbmaps, "RYM", "963f1bcbf601caf15fef71df06e9d6d3", "368476")   ### [Gun]
    addDiscogs(mdbmaps, "RYM", "4713bf884901b1f17aff0beb3ea3d45d", "260017")   ### [Judge]
    addDiscogs(mdbmaps, "RYM", "4fbedfbaff08203a1a8404ed1f6b3aca", "2823248")   ### [Lewis]
    addDiscogs(mdbmaps, "RYM", "7bde697a146d3200fa3d757e9a25acac", "260762")   ### [Dare]
    addDiscogs(mdbmaps, "RYM", "ea6de09b9281bed437b8e2f07f7234ef", "1725564")   ### [Sword]
    addDiscogs(mdbmaps, "RYM", "34d5177a7f86bfc33b38df308d28813d", "262348")   ### [Sacrilege]
    addDiscogs(mdbmaps, "RYM", "8c59a54dd4c14ca1cc031de4607cfca0", "274534")   ### [Deathrow]
    addDiscogs(mdbmaps, "RYM", "0f51166a61c1fe5e3875b3d8cf7f1b15", "309576")   ### [Faith]
    addDiscogs(mdbmaps, "RYM", "733245aa11e6205a9a87dc429f952be1", "1130554")   ### [Dark]
    addDiscogs(mdbmaps, "RYM", "99d683ddca28e77b6a85eadacf97b4bf", "445543")   ### [Armageddon]
    addDiscogs(mdbmaps, "RYM", "7d9454da1544f2f3aaae506ef538af2b", "83723")   ### [Milton]
    addDiscogs(mdbmaps, "RYM", "f2ce482d9ca2dd493ac1062b52cd5ce8", "426936")   ### [Khan]
    addDiscogs(mdbmaps, "RYM", "79b844f0c6023776c957420e462a90fe", "282438")   ### [Christopher Komeda]
    addDiscogs(mdbmaps, "RYM", "8532c8c0f2b94d7b547229e0e6248010", "1246724")   ### [Damon]
    addDiscogs(mdbmaps, "RYM", "0ef40707a184767980874a876ad620a5", "1437537")   ### [Chrysalis]
    addDiscogs(mdbmaps, "RYM", "c86476711239ccd6156cf14dd861a1f1", "178820")   ### [Sam Gopal]
    addDiscogs(mdbmaps, "RYM", "9e6ba40202dbdf9f179c23aa0eb33161", "291207")   ### [The End]
    addDiscogs(mdbmaps, "RYM", "3c1663b781106372b9a2f204847e4512", "1038775")   ### [Index]
    addDiscogs(mdbmaps, "RYM", "c917dd0d67be571dbd3dbdb508d5657f", "251844")   ### [Repulsion]
    
    addDiscogs(mdbmaps, "RYM", "6d07b9a4b2c4241ed722eba90cfe5ee1", "1435296")   ### [Nielsen/Pearson]
    addDiscogs(mdbmaps, "RYM", "3c6d17fab443663c9ff388a24eae7235", "6209540")   ### [Astor Piazzolla su bandoneón]
    addDiscogs(mdbmaps, "RYM", "9cb88e4fec99c4dbda607778cd04f275", "5561726")   ### [the Legendary Hassan]
    addDiscogs(mdbmaps, "RYM", "bb11cacf2aea138a2851cd9e28667168", "1340359")   ### [James Pease]    
    addDiscogs(mdbmaps, "RYM", "44a7a88b67058dd2058d19c1bd480537", "1176803")   ### [Ken Mackintosh, His Saxophone and His Orchestra]
    addDiscogs(mdbmaps, "RYM", "e433b9c1823795fbdfc737be3a34840f", "121035")   ### [The Wing & a Prayer Fife and Drum Corps.]
    addDiscogs(mdbmaps, "RYM", "bf4ee9d79988933d4c7cf8963c53588b", "506829")   ### [Brighouse & Rastrick Brass Band]
    addDiscogs(mdbmaps, "RYM", "bcb73412b833420bda7a1da8a8e09aca", "2197967")   ### [Mª Jesús y Su Acordeón]
    addDiscogs(mdbmaps, "RYM", "42f77434bb467353ba0b85b3aba85091", "30164")   ### [Menelik & la Tribu]
    addDiscogs(mdbmaps, "RYM", "67d4fff6442ebef6fbfbe98bb15ce2d3", "295749")   ### [Dr. Superman]
    addDiscogs(mdbmaps, "RYM", "7482600913d1c05702a4c6f77533cd08", "295748")   ### [Lady Sweet]    
    
    addDiscogs(mdbmaps, "RYM", "88b7ba22d690166c847b7919d4d4f2b5", "723719")   ### [Tony Crombie and His Rockets]
    addDiscogs(mdbmaps, "RYM", "afe87282a942cf8a30d320e41d1599ba", "8285952")   ### [The Cooldown Café]
    addDiscogs(mdbmaps, "RYM", "c3f95ba6854b76ec50d6889fc9e4c36d", "306455")   ### [mickey 3d]
    addDiscogs(mdbmaps, "RYM", "d9b58ffad14909dd33a0d0184f344471", "399844")   ### [SonbyFour]
    addDiscogs(mdbmaps, "RYM", "c9ed2286e413e3ba012e0aee56ebde18", "367246")   ### [ぱふゅ～む]
    addDiscogs(mdbmaps, "RYM", "3a7458610febd8e9392795e998df8e85", "1811918")   ### [The Japetts]
    addDiscogs(mdbmaps, "RYM", "76bd520b4aaab5e07858111a9886dc9e", "1548739")   ### [Jack Collier and Orchestra]
    addDiscogs(mdbmaps, "RYM", "ad768d31496fa7cc3d84e25bd70055f5", "619385")   ### [Álex de la Nuez]
    addDiscogs(mdbmaps, "RYM", "f81ddf3281f81bfc4895839dd2352e47", "6083792")   ### [Suzy de Domoy]
    addDiscogs(mdbmaps, "RYM", "aebd970134645599fbd52545ecb0da13", "31937")   ### [Capt. Hollywood]
    addDiscogs(mdbmaps, "RYM", "7cd416d3f01df87ca21e7b48eb8cfa7e", "1682736")   ### [Norberto de Nöah]
    addDiscogs(mdbmaps, "RYM", "aca01a4a40f400f4c606cd62d5ffb468", "3552965")   ### [Emilio Aragón]
    addDiscogs(mdbmaps, "RYM", "5881609baa116ba8943d23dd271a292f", "1117347")   ### [The Mark IV]
    addDiscogs(mdbmaps, "RYM", "456147be04b5a2ebef5f3f76be045faa", "5303577")   ### [Carte Blanche (ITL)]
    addDiscogs(mdbmaps, "RYM", "8f089d6c3e796fd53ca31fdbd1dfb0cd", "1159188")   ### [Billy Storm and The Valiants]
    addDiscogs(mdbmaps, "RYM", "1d3a9024b04e3fd6f131c28ea02d5184", "699393")   ### [Billy Ward and The Dominoes]
    addDiscogs(mdbmaps, "RYM", "bbc5c9b5e61c4186d6228415f0f193f7", "3824943")   ### [Hardrock Gunter and the Pebbles]
    addDiscogs(mdbmaps, "RYM", "4f3a10ee7c247b1c9a7e555cf8f540d0", "45869")   ### [Bob McFadden and Dor]
    addDiscogs(mdbmaps, "RYM", "17e07f31e811b063dfd86ae347b907ea", "1235021")   ### [Brian Poole and The Tremeloes]
    addDiscogs(mdbmaps, "RYM", "ba7aaadb0cb825dea2714a25940ab8b6", "634112")   ### [Little Iva]
    addDiscogs(mdbmaps, "RYM", "a18a8a5cc95444dcd06922671ee46613", "393118")   ### [David and Jonathan]
    addDiscogs(mdbmaps, "RYM", "55168fa912960fe3e9db3a3ca76733b5", "192462")   ### [Antoine]
    addDiscogs(mdbmaps, "RYM", "1afc57388f9de772136e6bf956845ae7", "408348")   ### [J. Bastós]
    addDiscogs(mdbmaps, "RYM", "163cd0cca3b15bd58745993809f977e0", "2676453")   ### [Arlo Stenmit and His Hammerkids]
    addDiscogs(mdbmaps, "RYM", "3fcb0061da867e5b012ae3fd30a85fa1", "1031477")   ### [Czar]
    addDiscogs(mdbmaps, "RYM", "ffbca6cb2ad5ea198e7624bc9ca82764", "139117")   ### [Höllenboer]
    addDiscogs(mdbmaps, "RYM", "cc52dab6e0d1ea82ccb044271850a8d5", "234725")   ### [Lou and the Hollywood Bananas]
    addDiscogs(mdbmaps, "RYM", "6d4f52f990a083bbeb5c9b8e5d3f2b50", "15877")   ### [The Originals]
    addDiscogs(mdbmaps, "RYM", "91a7c29be0544c1dd71eb507ed8c2443", "1227674")   ### [María Ostiz]
    addDiscogs(mdbmaps, "RYM", "5b9bbeda1db75153ffe09a32a5784991", "100707")   ### [Ochi Brown]
    addDiscogs(mdbmaps, "RYM", "2ff71a8bdf036e108bfc43743591d32b", "576633")   ### [Gérard Jugnot]
    addDiscogs(mdbmaps, "RYM", "6eb532e8acb8c9324b9eddd005a0e045", "195154")   ### [Cargo]
    addDiscogs(mdbmaps, "RYM", "b11ea421417f596144ac335cb6a41e13", "1438807")   ### [Rémy Tarrier]
    addDiscogs(mdbmaps, "RYM", "7382a1a7fbf5fe5de2e590f184ae00f5", "4197893")   ### [Los Chicos de la Bahía]
    addDiscogs(mdbmaps, "RYM", "d2748b8963432c7482ad0d4ccfbd5b99", "1337660")   ### [Alexa Leclère]
    addDiscogs(mdbmaps, "RYM", "2264cb32d1d60bf085fc1aa4c7d7da96", "256124")   ### [Roberto Jacketti and The Scooters]
    addDiscogs(mdbmaps, "RYM", "796a5f12490df95d24d62c7b179df7d6", "338834")   ### [Laroche-Valmont]
    addDiscogs(mdbmaps, "RYM", "7c0f068dc963ea8939a94acfa033f80a", "504794")   ### [Fred Sonnenschein und seine Freunde]
    addDiscogs(mdbmaps, "RYM", "a55aaa95972f68ad70a260b84d603b03", "541856")   ### [Everton 1985]
    addDiscogs(mdbmaps, "RYM", "d501992a0eac0ab701edc5a5c4659fc1", "802750")   ### [Burt Reynolds]    

    addDiscogs(mdbmaps, "RYM", "f4f4635c6de875049f6a6db1ae6be9e3", "7116273")   ### [D mol]
    addDiscogs(mdbmaps, "RYM", "ce8b8f8f3c49573b7e62b362a6b6ead9", "520366")   ### [the Tennessee Plowboy and His Guitar]
    addDiscogs(mdbmaps, "RYM", "75a89f957a6fb12a1578e80fab0e61b6", "5486163")   ### [Eris is My Homegirl]
    addDiscogs(mdbmaps, "RYM", "a07d21d0efdc8044efa64c47da6c1b2f", "51984")   ### [J.Lo]
    addDiscogs(mdbmaps, "RYM", "6d1e4dc787333df75924cce8d93e14f2", "2760780")   ### [Ch'ti Dj]
    addDiscogs(mdbmaps, "RYM", "416e23275dc8e922d101a61f1640b78f", "960446")   ### [Laín]
    addDiscogs(mdbmaps, "RYM", "5d054ebb125db368c62ea46c605b2408", "2623429")   ### [Vince Vance and the Valiants]
    addDiscogs(mdbmaps, "RYM", "84525519dac478a9c537608f09a480aa", "961163")   ### [Think]
    addDiscogs(mdbmaps, "RYM", "783271453265a7a55358ac8713f5f45f", "413545")   ### [Alex Band of The Calling]    
    addDiscogs(mdbmaps, "RYM", "271ec553c28bfa0d927056368dc06b16", "30120")   ### [The Tornadoes]
    addDiscogs(mdbmaps, "RYM", "7d35572c34388fb2277dac46fc7afa66", "1667684")   ### [Feel]
    addDiscogs(mdbmaps, "RYM", "851956bd45f002bdb4420a6ab6757712", "68187")   ### [Forrest]
    addDiscogs(mdbmaps, "RYM", "812de1880bcad0b693a8f46ee95118db", "511467")   ### [Climax]
    addDiscogs(mdbmaps, "RYM", "4268648ebf449ae439ddbf316b26f0a4", "312010")   ### [The Lords]
    addDiscogs(mdbmaps, "RYM", "c12a4c699482990d883923b839c22066", "1408132")   ### [Death]
    addDiscogs(mdbmaps, "RYM", "91d3e095cebd61384f50e56516fd0ba6", "130979")   ### [Gerardo]
    addDiscogs(mdbmaps, "RYM", "acc649ce007a708113a90e79162bfcec", "242071")   ### [The Genius]
    addDiscogs(mdbmaps, "RYM", "e9a8cde3e9ef434c6e8f1e739435c7e8", "2483549")   ### [Bobby Day & The Satellites]
    addDiscogs(mdbmaps, "RYM", "ae43c6bdb9d7426cdfa67dfd613fbcd9", "270699")   ### [Sagittarius]
    addDiscogs(mdbmaps, "RYM", "def3882f9a4da874f89a269963fc823b", "256846")   ### [The Triffids]

    addDiscogs(mdbmaps, "RYM", "8523f6dc1b8b40655d31e93486d6591e", "179709")   ### [Robert Shaw]
    addDiscogs(mdbmaps, "RYM", "822ec8ad59f623db072b82e125e39d0c", "192701")   ### [Galexia]
    addDiscogs(mdbmaps, "RYM", "84393e29b336c986155ebd0ffd4ee4db", "1564358")   ### [Afromental]
    addDiscogs(mdbmaps, "RYM", "ee71ddaa53532d469d4f9699d1d5c137", "4037041")   ### [Hirokazu Ando]
    addDiscogs(mdbmaps, "RYM", "554e840c384cac8a182c05e9c2378de3", "4748640")   ### [Saint Petersburg Philharmonic Orchestra]
    addDiscogs(mdbmaps, "RYM", "cd257c963a1466b5a6655fc4f7e676ae", "57629")   ### [Vera Hall Ward]
    addDiscogs(mdbmaps, "RYM", "1321b0e9da69a8ad356e486d8365dfe2", "1300812")   ### [The Glyndebourne Chorus]
    addDiscogs(mdbmaps, "RYM", "adeaccd4206b2afa2eb4e9e82fad8028", "3291882")   ### [Sébastien Patoche]
    addDiscogs(mdbmaps, "RYM", "965a4993a789fa5c5d8d7f41eb586da6", "2144667")   ### [Fearofdark]
    addDiscogs(mdbmaps, "RYM", "5ee331649e1f959a12d5ff6cdfe2d7d0", "2495802")   ### [Edward Scissortongue]
    addDiscogs(mdbmaps, "RYM", "00b547adaca250f54710856abbad38a2", "432780")   ### [Henri René and His Orchestra]
    addDiscogs(mdbmaps, "RYM", "8cae25a4a6329d217738a89f7acd8c46", "320803")   ### [String Choir]
    addDiscogs(mdbmaps, "RYM", "20dc235d527fbb43dafe157e9cf26dfa", "3245378")   ### [The All-Star Orchestra]
    addDiscogs(mdbmaps, "RYM", "ded43b7a83b1c5a1e611d19dc1f419fd", "92800")   ### [Rev. Jim Jones]
    addDiscogs(mdbmaps, "RYM", "88875b4dc622ddde2a53a2806a2bb44d", "703269")   ### [Orchestre philharmonique de Monte-Carlo]
    addDiscogs(mdbmaps, "RYM", "193cd160cb01a814b605898ca681d0ef", "621205")   ### [Sachin Dev Burman
    addDiscogs(mdbmaps, "RYM", "9bf76cbccc54055f6cc137cc28149b08", "1032099")   ### [Il Teatro degli Orrori]
    addDiscogs(mdbmaps, "RYM", "f5433bd351d2757c83e8265b0a516f9d", "1883046")   ### [Sinergia]
    addDiscogs(mdbmaps, "RYM", "8861c6812e0080d3bc6bb87f8eb7d660", "54120")   ### [UNKLESOUNDS]
    addDiscogs(mdbmaps, "RYM", "3af0cc5172b5ff2114ed779716bffde6", "870694")   ### [The Choir of the English Concert]
    addDiscogs(mdbmaps, "RYM", "e247c061346d6611684d70c66cc4c942", "17961")   ### [Chér]

    addDiscogs(mdbmaps, "RYM", "aff116ca3b5937bc30ab747a7b379602", "893904")   ### [Concertgebouw Orchestra]
    addDiscogs(mdbmaps, "RYM", "e714621d6b7a5418330f9542afc88844", "228830")   ### [Spanky and Our Gang]
    addDiscogs(mdbmaps, "RYM", "b1e813e3fcae6140016988f81f23f881", "3092753")   ### [Belathuzur]
    addDiscogs(mdbmaps, "RYM", "aaafb7362d3cf2f9cee63102516e342a", "834646")   ### [David Oistrakh]
    addDiscogs(mdbmaps, "RYM", "ee619d52dca8394b94a52c452c75bd70", "257235")   ### [Bob B. Soxx and The Blue Jeans]
    addDiscogs(mdbmaps, "RYM", "0079ac37e791cf12e2d4b98f25bfabce", "859446")   ### [Richard Lewis]
    addDiscogs(mdbmaps, "RYM", "9f315eef6eb0dfe2549652d0053bade9", "2740352")   ### [L' Orso]
    addDiscogs(mdbmaps, "RYM", "3fb8960893a5b864e5765f0bf1896c31", "1305084")   ### [Diox]
    addDiscogs(mdbmaps, "RYM", "d71a82e9bfacbdda1bf84f0c22d3ea1a", "51636")   ### [Priscilla]
    addDiscogs(mdbmaps, "RYM", "6b350977f1067ed1f5882c5fed19edd2", "3347876")   ### [I Shot the Duck Hunt Dog]
    addDiscogs(mdbmaps, "RYM", "c394a83b686fc5285a1544f8197412e2", "505712")   ### [Abacus]
    addDiscogs(mdbmaps, "RYM", "c7b78c1472fe38d484c9e7d647ec0a4c", "475266")   ### [Rapülők]
    addDiscogs(mdbmaps, "RYM", "adeaccd4206b2afa2eb4e9e82fad8028", "3291882")   ### [Sébastien Patoche]
    addDiscogs(mdbmaps, "RYM", "cb031f94529e688462505cbda40ea5a4", "910967")   ### [Ed Lee Natay]
    addDiscogs(mdbmaps, "RYM", "73321511963e256dc7fdda40893e2c4f", "1603295")   ### [Concert Arts Orchestra]
    addDiscogs(mdbmaps, "RYM", "8c0ade54b36deba2f65677a5a89320d0", "6034198")   ### [Nightmargin]
    addDiscogs(mdbmaps, "RYM", "f1575af90453a7a70738af0a994e538b", "1244097")   ### [Kevin Griffiths]

    addDiscogs(mdbmaps, "RYM", "aa34aa98a865925e175779552dd61057", "3287655")   ### [Keeponrockin404]
    addDiscogs(mdbmaps, "RYM", "2d23da5cf750364e22c8968832565498", "3777562")   ### [L' Officina della Camomilla]
    addDiscogs(mdbmaps, "RYM", "96000ddbf72bb02c8155d890ee5c71cf", "1195171")   ### [Nipsey Hu\$\$le]
    addDiscogs(mdbmaps, "RYM", "21ec1ac46bbe7c2f0711bd8056faa6f3", "5233346")   ### [Planta Carnívora]
    addDeezer(mdbmaps, "RYM", "f23523ee3ebbef85f10395397f9ff308", "7145243")   ### [Vitor Brauer]
    addDiscogs(mdbmaps, "RYM", "3f1e940b856674b4a9e096e0f8736de5", "1013639")   ### [GrubSon]
    addDiscogs(mdbmaps, "RYM", "d9f05b409239bdefe49b5e668ee9399c", "3213254")   ### [Amset]
    addDiscogs(mdbmaps, "RYM", "d01660f71c748a7c2a9c5ca9a352df9c", "5896892")   ### [Kay Martin]
    addDiscogs(mdbmaps, "RYM", "22a334605c4b5ad0e1f771311b8832c3", "1153060")   ### [The Speakers]
    addDiscogs(mdbmaps, "RYM", "5cded5c115febbc6dfe031ada359436e", "22856")   ### [Barrabás]

    addDiscogs(mdbmaps, "RYM", "8caffe1fbc8a714e0ff9b1aadd895ac2", "539271")   ### [Orchestre symphonique de Montréal]
    addDiscogs(mdbmaps, "RYM", "a76fb6fa61603216f2763599c2fc1186", "283125")   ### [Gennady Rozhdestvensky]
    addDiscogs(mdbmaps, "RYM", "46a3a98f2ed91689d5de8d262f35b324", "833794")   ### [Ivo Pogorelić]
    addDiscogs(mdbmaps, "RYM", "8378d9a5da76abef004f9cf745c17247", "4239692")   ### [Ryo Nagamatsu]
    
    addDiscogs(mdbmaps, "RYM", "1fb8ce8afb964937bc5ba2db5ea0df0b", "1480654")   ### [The Sqad]
    addDiscogs(mdbmaps, "RYM", "4c7674820ae5861dc630f74d0550c949", "163453")   ### [Aquarium]
    addDiscogs(mdbmaps, "RYM", "bf92e0fae5b27720c99575fdb2858c9d", "28795")   ### [O(+>]
    addDiscogs(mdbmaps, "RYM", "019c714546b64ce1464b667da4392a2f", "237756")   ### [Nagisa ni te]

    addDiscogs(mdbmaps, "RYM", "ab6f46e01d54a40b3bcf3898eabd8a89", "654126")   ### [Celia and The Mutations]
    addDiscogs(mdbmaps, "RYM", "1e2c5ad0732b6833dce8c73a14e62e77", "2184902")   ### [Tommy Fogerty and The Blue Velvets]
    addDiscogs(mdbmaps, "RYM", "898fa488a8ef71c5bae71e20f601d245", "334507")   ### [Little Brenda Lee]
    addDiscogs(mdbmaps, "RYM", "066678e819ff3d38fad4f89a76d09a9a", "995340")   ### [Luis Aguilé]
    addDiscogs(mdbmaps, "RYM", "811f0a0883e9b82cecd66bf4d1efc828", "528609")   ### [La Compagnie créole]

    addDiscogs(mdbmaps, "RYM", "4632cd96e8c71385c60e9c01196a2e53", "275015")   ### [Studio für elektronische Musik des Westdeutschen Rundfunks, Köln]
    addDiscogs(mdbmaps, "RYM", "7c364d3bf7ccbe1209b77e62ddb8d774", "2088698")   ### [Russ Garcia and His Vocal Choir]

    addDiscogs(mdbmaps, "RYM", "c938cf68f94fed75cc26549337750387", "645741")   ### [Arditti String Quartet]
    addDiscogs(mdbmaps, "RYM", "20d20d433cce4f470529ec7541aa3bde", "276345")   ### [Deceased...]
    addDeezer(mdbmaps, "RYM", "c0bbfdcc5b92b78f5f11f55882d911c8", "8002136")   ### [Ling Tosite Sigure]
    addDiscogs(mdbmaps, "RYM", "e512fcff2eeff54f4b637fd084f8a06b", "1566620")   ### [SubRosa]
    addDiscogs(mdbmaps, "RYM", "7c02717b30de8c1464b6f686ff1845a4", "5125")   ### [Scraping Foetus Off the Wheel]
    addDiscogs(mdbmaps, "RYM", "76dea25af68db8985aa56146aa74bb3d", "5868607")   ### [Seiko Oomori]
    addDiscogs(mdbmaps, "RYM", "ae87ffccd622c9401a91cf041de05c8c", "3782979")   ### [Wędrowcy~Tułacze~Zbiegi]
    addDiscogs(mdbmaps, "RYM", "7a8afe2961d7b5ecb852678161d09c6f", "1930677")   ### [Mass of the Fermenting Dregs]
    addDiscogs(mdbmaps, "RYM", "1f9d0f4fc63ba3bfaa977bb53d5ec297", "1792452")   ### [Chór Polskiego Radia w Krakowie]
    addDiscogs(mdbmaps, "RYM", "938151a2dc408797cf03a119c9cf41ff", "1272551")   ### [qebrµs]
    addDiscogs(mdbmaps, "RYM", "4a417f8bf4b890c720c3678384ae1577", "999446")   ### [Gaza]
    addDiscogs(mdbmaps, "RYM", "789a7608dfcf89fb127dac972139aa3c", "272542")   ### [Asphyx]
    addDiscogs(mdbmaps, "RYM", "e221271b326b0d9d0b473faf71048207", "4968274")   ### [father]
    addDiscogs(mdbmaps, "RYM", "81e01b185f9ca31d6b11677220199461", "264626")   ### [Cliff Jordan]    
    addDiscogs(mdbmaps, "RYM", "762821772c1072550d078a6d39fca7cf", "305667")   ### [Tin Pan Alley]
    addDiscogs(mdbmaps, "RYM", "0d93544c007400c690e0c0fe19251d18", "602138")   ### [Elias & His Zig Zag Jive Flutes]
    addDiscogs(mdbmaps, "RYM", "e384be6fa7c15b5b6e9aab5326d8629c", "1489439")   ### [Johnny Duncan & The Blue Grass Boys]
    addDiscogs(mdbmaps, "RYM", "d99c322ec9e64a15f6fb8bcf95a663f0", "521963")   ### [Ray Charles With Chorus and Orchestra]
    addDiscogs(mdbmaps, "RYM", "9c4b83cb02899c42820b58a3339abea3", "521963")   ### [Ray Charles With Orchestra and Chorus]
    addDiscogs(mdbmaps, "RYM", "79320017271ab5ed32ee94a56179dea7", "6025169")   ### [Shygirl]
    addDeezer(mdbmaps, "RYM", "04641d8d951d715ca5756000ff2db54d", "1418509")   ### [The Crooklyn Dodgers]
    addDeezer(mdbmaps, "RYM", "00433043c53d398788260b6b6d09d5cd", "357879")   ### [Domina]
    addDiscogs(mdbmaps, "RYM", "e24e3e28c82d52605bbdcf6731cd72fa", "98882")   ### [Double]
    addDiscogs(mdbmaps, "RYM", "1e8536e43402f9abe2b62c00d737f34a", "1508404")   ### [Virtue]
    addDiscogs(mdbmaps, "RYM", "4fa818e91d057c8debc5022e4452e58e", "473561")   ### [Deux]
    addDeezer(mdbmaps, "RYM", "48bb720d403ae154a110f562492ef384", "2366")   ### [Eric B. and Rakim]
    addDeezer(mdbmaps, "RYM", "74e3b69152a0166c815a1b81a1795ed7", "65383")   ### [Sträwberry Switchbläde]
    addDiscogs(mdbmaps, "RYM", "a1ea6d722062e7c45d23d37565dc139c", "240872")   ### [Double Dee]
    addDiscogs(mdbmaps, "RYM", "abc078064f6b0c58e3bfbf1634193203", "58096")   ### [Stretch]
    addDiscogs(mdbmaps, "RYM", "c42b0e8a4137bf545c46603870826940", "364861")   ### [The MASH]
    addDiscogs(mdbmaps, "RYM", "fe7c735cfc4d266af8722d2efab6c66d", "11650")   ### [Machine]
    addDiscogs(mdbmaps, "RYM", "9521e26abf89eeb11774270ef1fe0821", "256994")   ### [Avengers]
    addDiscogs(mdbmaps, "RYM", "114280692506bd05d4cfd7539287d56a", "444482")   ### [The Victims]
    addDiscogs(mdbmaps, "RYM", "a75df1d87dc99e8c1b7e4347754c114f", "257157")   ### [The Germs]
    addDiscogs(mdbmaps, "RYM", "d9716555865aab1315630873178a9116", "396928")   ### [Macabre]
    addDiscogs(mdbmaps, "RYM", "4640400f563f1bd44e8ac06eb1478db2", "263609")   ### [Rods]
    addDeezer(mdbmaps, "RYM", "1006f8b5f4f6349136744e20772df67b", "498213")   ### [Freaky]
    addDiscogs(mdbmaps, "RYM", "8464f05f95a78438d901f20f3bb6102c", "1391314")   ### [DyE]
    addDiscogs(mdbmaps, "RYM", "28ca1aff4e0848b6816e06cb63ac6313", "391187")   ### [The Fascinations]
    addDiscogs(mdbmaps, "RYM", "6f0c8fc897cbcf79d91e3aa73a7b9ecc", "4089130")   ### [Yubin]
    addDiscogs(mdbmaps, "RYM", "58de6b21791a14bf8d455512b58a5fe0", "2120637")   ### [Jack J]
    addDiscogs(mdbmaps, "RYM", "9656dda9976bea12537edd01394a69b5", "3141923")   ### [Liz]
    addDiscogs(mdbmaps, "RYM", "de8d0854ec9cdb690a21685c520bd313", "428943")   ### [Mama Cass Elliot]
    addDiscogs(mdbmaps, "RYM", "e480b8c771379c4f0d87a7a71612fd5a", "744898")   ### [Jerry Huffman]
    addDiscogs(mdbmaps, "RYM", "81c641a062289c6b6eb13768cf03f4ac", "607662")   ### [Dave "Diddlie" Day]
    addDiscogs(mdbmaps, "RYM", "6c5f3f2124352ff35fa1f72f9463900f", "1349319")   ### [Gary Crosby]
    addDiscogs(mdbmaps, "RYM", "cc2168c2b15e60fb8b7270e9caa10858", "1421291")   ### [The Avalons]
    addDiscogs(mdbmaps, "RYM", "00869fc7c59c5598535d4f59cb9ca515", "2063449")   ### [Chuck Miller]
    addDiscogs(mdbmaps, "RYM", "a72df6279de3f55526791a10580bbe93", "294687")   ### [Bobby Blue Bland]
    addDiscogs(mdbmaps, "RYM", "7b301a5f599813dd9117600b5ae9cf57", "3226218")   ### [Vann "Piano Man" Walls]
    addDiscogs(mdbmaps, "RYM", "c6274c2b0a6608c3930f1001ffb6cf79", "64677")   ### [The Capris]
    addDiscogs(mdbmaps, "RYM", "1414229535e5e79906bdaa687fe1ee9c", "2725176")   ### [Sugar Boy and His Cane Cutters]
    addDiscogs(mdbmaps, "RYM", "8b55bd482e160c12d8554f91c181eabd", "744896")   ### [Jody Chastain]
    addDiscogs(mdbmaps, "RYM", "51fb70b05a30560d5f56031d1f3d5272", "727109")   ### [The Bubble Puppy]
    addDiscogs(mdbmaps, "RYM", "a96f9983b487da6e9c0d61371e7c262f", "278460")   ### [The Keggs]
    addDiscogs(mdbmaps, "RYM", "76176c7dcda521a36efea7f1b333343c", "926540")   ### [The Riders of the Mark]
    addDiscogs(mdbmaps, "RYM", "ad5c4ca8acfa8dfb772c917f63caf6e3", "240895")   ### [The Foundations]
    addDiscogs(mdbmaps, "RYM", "4a09b73e2ba7d2516dc4eb508a4b28c5", "252519")   ### [The Groupies]
    addDiscogs(mdbmaps, "RYM", "db77e2c91f05859818bbc65341b1efaf", "280863")   ### [The Cascades]
    addDiscogs(mdbmaps, "RYM", "fba4dba8da199da5439c70b1a3915d2e", "2697011")   ### [Glen and Dave]
    addDiscogs(mdbmaps, "RYM", "f75c1ba98fbc60b882057eeac1174c92", "307510")   ### [The Wimple Winch]
    addDiscogs(mdbmaps, "RYM", "c1371cfb2f2c4b5f3d443f23fbb10002", "2327974")   ### [The 23rd Turnoff]
    addDiscogs(mdbmaps, "RYM", "ff65c9d025eff21ad5ae66386be16ac1", "755278")   ### [Lord Lebby]
    addDiscogs(mdbmaps, "RYM", "33606ff3a0c263997ab243da27914fc4", "375478")   ### [The Harp-Tones]
    addDiscogs(mdbmaps, "RYM", "abd1e7cae237a8b1e8dc539175c1b32b", "383313")   ### [The Schoolboys]
    addDiscogs(mdbmaps, "RYM", "fb97bb4278e02a846d88b2804b4e9845", "1413694")   ### [Keith Courvale]
    addDiscogs(mdbmaps, "RYM", "60e3f8c244af6e88095632d8cf7c575f", "508390")   ### [Jimmy Rogers and His Trio]
    addDiscogs(mdbmaps, "RYM", "1141505be46249c6f4368e39d3544d29", "6760947")   ### [The Beale Street Gang]    
    addDiscogs(mdbmaps, "RYM", "cb0d16623707c4013acfc97237e86926", "135399")   ### [Ray Smith]
    addDiscogs(mdbmaps, "RYM", "ae1386196ea4f4ac5d14a8266ede974e", "3706334")   ### [The Night Caps]
    addDiscogs(mdbmaps, "RYM", "f317dbb458d93511e36931339435fdb3", "383368")   ### [Frankie Lymon and the Teenagers]
    addDeezer(mdbmaps, "RYM", "f317dbb458d93511e36931339435fdb3", "66326")   ### [Frankie Lymon and the Teenagers]
    addDiscogs(mdbmaps, "RYM", "52420c7fe125a7116be609aa1815b2ad", "3992270")   ### [Easyfun]
    addDeezer(mdbmaps, "RYM", "52420c7fe125a7116be609aa1815b2ad", "7850520")   ### [Easyfun]
    addDiscogs(mdbmaps, "RYM", "3367885125b724966722f5a1e8417945", "570739")   ### [Mala]
    addDeezer(mdbmaps, "RYM", "3367885125b724966722f5a1e8417945", "65201")   ### [Mala]
    addDiscogs(mdbmaps, "RYM", "f9795ab6880d2c9736b641be97305cf5", "662431")   ### [Billy Riley and The Little Green Men]
    addDiscogs(mdbmaps, "RYM", "54bf926890e5387e818876765ed55300", "271132")   ### [Urban Jungle]
    addDiscogs(mdbmaps, "RYM", "57c4a29a954fc1f2f03ce6f3d5bebd90", "49294")   ### [The Soul Sonic Force]
    addDeezer(mdbmaps, "RYM", "57c4a29a954fc1f2f03ce6f3d5bebd90", "4787821")   ### [The Soul Sonic Force]
    addDiscogs(mdbmaps, "RYM", "7ffd4b599c15df806aa10a82135c174b", "383338")   ### [The Channels]
    addDeezer(mdbmaps, "RYM", "27e2f90d42fce6c7125d05d277d3c77a", "1380133")   ### [Elmore James and His Broom Dusters]
    addDiscogs(mdbmaps, "RYM", "ae1386196ea4f4ac5d14a8266ede974e", "3706334")   ### [The Night Caps]
    addDiscogs(mdbmaps, "RYM", "6f2a2844f9c7735595b3342ccf05a0f3", "3693069")   ### [Malton & Hamilton]
    addDiscogs(mdbmaps, "RYM", "f14cbb05dd9055044b5b1f38c9699ed5", "66302")   ### [PiL]
    addDeezer(mdbmaps, "RYM", "f14cbb05dd9055044b5b1f38c9699ed5", "455089")   ### [PiL]
    addDiscogs(mdbmaps, "RYM", "be4f5b206219e2bc875cce2456a8faec", "633398")   ### [USA MI]
    addDiscogs(mdbmaps, "RYM", "5c03d352e137adb452fec7cd64d05df7", "1394017")   ### [Roy ("Bald Head") Byrd]
    addDiscogs(mdbmaps, "RYM", "ff561b8942b87feba40a03a034f4d1b9", "4078404")   ### [Begiristain]
    addDiscogs(mdbmaps, "RYM", "494ef0a399d60509533601be3d45c5c7", "1471950")   ### [DoomThrone]
    addDiscogs(mdbmaps, "RYM", "8dd495749630a864c1adf7ed9068ca44", "263201")   ### [The L.A. Guns]
    addDeezer(mdbmaps, "RYM", "8dd495749630a864c1adf7ed9068ca44", "94963")   ### [The L.A. Guns]
    addDeezer(mdbmaps, "RYM", "16ad2629d260b8e9c199da2f026a5e76", "66994952")   ### [Korrozia Metalla]
    addDiscogs(mdbmaps, "RYM", "7340b8500d38286c8e9f5c073c466122", "80727")   ### [Sheila B. Devotion]
    addDeezer(mdbmaps, "RYM", "7340b8500d38286c8e9f5c073c466122", "3549")   ### [Sheila B. Devotion]
    addDiscogs(mdbmaps, "RYM", "fb385af8e7195d967dbb1c23d22158aa", "470098")   ### [I Cugini di Campagna]
    addDeezer(mdbmaps, "RYM", "fb385af8e7195d967dbb1c23d22158aa", "71646")   ### [I Cugini di Campagna]
    addDiscogs(mdbmaps, "RYM", "1924e936c39620ef15cae4e7047be80f", "368604")   ### [King Brothers]
    addDiscogs(mdbmaps, "RYM", "958a077ffc1f5abaeebf107e5a8adfd2", "1420163")   ### [Tom Glazer and the Do-Re-Mi Children's Chorus]
    addDiscogs(mdbmaps, "RYM", "710f42512024611e79c216f2bba42d89", "3118503")   ### [New Orleans Rhythm]    
    addDiscogs(mdbmaps, "RYM", "2e366b8d5a687ea05312368860f3bbbb", "296154")   ### [Elsa]
    addDiscogs(mdbmaps, "RYM", "635e6f146da4f888fea1e9900d749384", "2303563")   ### [Dave and the Derros]
    addDiscogs(mdbmaps, "RYM", "0b2178e7e2dd651f3e1aeea34035151a", "965883")   ### [Warwick Capper]
    addDiscogs(mdbmaps, "RYM", "47b36024b7024303835b1d08be1cb718", "1313160")   ### [El Norte]
    addDiscogs(mdbmaps, "RYM", "b199adeeba809cf59835c98e0ab0e5ba", "777447")   ### [30 Odd Foot of Grunts]
    addDiscogs(mdbmaps, "RYM", "99ffa679a997d771f183d7a4f36843c1", "308825")   ### [Kevin Morane]
    addDiscogs(mdbmaps, "RYM", "dca0cf58c2f0e240fb8cb308c11cf625", "1021148")   ### [Childliners]
    addDiscogs(mdbmaps, "RYM", "afa2dfc18e915d93fbb050d40d0ed73e", "1006801")   ### [Norbi]
    addDiscogs(mdbmaps, "RYM", "5dcd3dc01a90a38dd77fffa7ccd01b93", "445344")   ### [Chris Waddle]
    addDiscogs(mdbmaps, "RYM", "fa9d8a0d150a464b833049daa064c344", "3903635")   ### [Jesulín]
    addDiscogs(mdbmaps, "RYM", "798dc49732042367cdce2996cae274f8", "802749")   ### [The Bandit Band]
    addDiscogs(mdbmaps, "RYM", "150f684f51be94261aec9d6c9736f906", "218966")   ### [Images]
    addDiscogs(mdbmaps, "RYM", "14fdbeaacc12f9484b80e45b831264ca", "457008")   ### [Hakkûhbar]
    addDiscogs(mdbmaps, "RYM", "513a1ddd23559420a7cd9d78f9547684", "1345353")   ### [The Beau Denturies]
    addDiscogs(mdbmaps, "RYM", "323cf70c8866a309e94bd0f80cfcc515", "2836613")   ### [the Pommodores]
    addDiscogs(mdbmaps, "RYM", "5f7d0cf4a5858fa89ab9623cee323166", "437613")   ### [Wilfrid Brambell]
    addDiscogs(mdbmaps, "RYM", "7a872557295cfc3f7a7086f7c0f0c4b5", "366273")   ### [The Kosher Five]
    addDiscogs(mdbmaps, "RYM", "4a7636adceec374fa6372be7a395eb90", "1442118")   ### [Nela Pocisková]    
    addDeezer(mdbmaps, "RYM", "5820b50f2b57ea416986b51321b4f15a", "214954")   ### [dARI]
    addDiscogs(mdbmaps, "RYM", "f843b987aae855280e6b4f06505755ba", "322068")   ### [Manchester United Football Club]
    addDiscogs(mdbmaps, "RYM", "4d5540abdf793742c0ab2d486952f62b", "5943286")   ### [Threatin]    
    addDeezer(mdbmaps, "RYM", "cc40a99cfb60ac11efe53dfaf7192aa7", "2307081")   ### [Bart Baker]
    addDiscogs(mdbmaps, "RYM", "3ab8390b315e35b8d0feb8baae1c6b60", "613854")   ### [Kyo
    addDeezer(mdbmaps, "RYM", "9633df06d51223375c083678d3aa1f47", "4841295")   ### [Jumex]
    addDeezer(mdbmaps, "RYM", "bd335a99bf9bd07f0ecea434abc62e50", "50452132")   ### [Slayyyter]
    addDiscogs(mdbmaps, "RYM", "29665f3e314ac303defbd4424611cde3", "331401")   ### [The Robins]
    addDiscogs(mdbmaps, "RYM", "b9652f9fa2c850d9fe6da6fa9a4e0039", "4966057")   ### [Moon Mullins and his Night Raiders]
    addDiscogs(mdbmaps, "RYM", "079eb9a2f0db5ab134148f8c602b0bde", "1461247")   ### [The John Barry Seven and Orchestra]
    addDiscogs(mdbmaps, "RYM", "f7e73d71ee79a46dc2e5428e3390b9ed", "370771")   ### [The Beverly's All Stars]
    addDiscogs(mdbmaps, "RYM", "741041ef487bf0aef5f934ec4e69ff01", "157480")   ### [Luis Enríquez Bacalov]
    addDeezer(mdbmaps, "RYM", "4b16c7d324511b725977a4e19c50ca52", "3524")   ### [The Sweet]
    addDiscogs(mdbmaps, "RYM", "4b16c7d324511b725977a4e19c50ca52", "253929")   ### [The Sweet]
    addDeezer(mdbmaps, "RYM", "430fa4204c8da9ef1b33cd1c8d94a30b", "4183")   ### [Fatlip]
    addDiscogs(mdbmaps, "RYM", "430fa4204c8da9ef1b33cd1c8d94a30b", "53627")   ### [Fatlip]
    addDeezer(mdbmaps, "RYM", "a55c05d5618ad60e894f85d49077b897", "6840")   ### [The Clipse]
    addAllMusic(mdbmaps, "RYM", "d4e2cc671a40fd407ac5ffd13afe2619", "mn0003903838")   ### [Kim Lip]
    addDeezer(mdbmaps, "RYM", "4af2b4acd0ca8eede64f51f9e6e30c04", "11814761")   ### [Cartier'GOD]
    addDeezer(mdbmaps, "RYM", "c874e309f4461fc19542c20e5e2a6f43", "503190")   ### [Liturgy]
    addDiscogs(mdbmaps, "RYM", "0c6ef78b580aa5b30f0cff4594c3d1ed", "7606376")   ### [Sewerslvt]
    addDiscogs(mdbmaps, "RYM", "02bfaf56ddaf8a6cccf382834b76a456", "83725")   ### [Meirelles e os Copa 5]
    addDiscogs(mdbmaps, "RYM", "b605584f86d2db6de44565682761907f", "2583851")   ### [Memphis Slim and the House Rockers]
    addDiscogs(mdbmaps, "RYM", "2c43c2cd93785d8cfc0e56536f9a5541", "2582177")   ### [Professor Longhair and His Blues Scholars]
    addDiscogs(mdbmaps, "RYM", "bc8b9f7b2561460c702d22ad3a0c0a15", "596029")   ### [Lonnie Donegan and His Skiffle Group]
    addDiscogs(mdbmaps, "RYM", "0879feb9c0b1d5f3eead7873c56b248d", "450656")   ### [Jackie Brenston and His Delta Cats]
    addDiscogs(mdbmaps, "RYM", "96ffc21ae710d82d87118a7c81be8a8d", "388889")   ### [The Factory]
    addDiscogs(mdbmaps, "RYM", "82ec25cf11ec51d3b89737f0e76f34d4", "7145937")   ### [C'est la Key]
    addDiscogs(mdbmaps, "RYM", "ae25052ad0f5b8192425223041bcda63", "43032")   ### [Koji Kondo]
    addDiscogs(mdbmaps, "RYM", "3eb2a9f33044038f5ac0dfce95473d3f", "517226")   ### [Smarki Smark]
    addDiscogs(mdbmaps, "RYM", "401047f446fd94208fdbd8b326ff3ae9", "352678")   ### [Ko Otani]
    addDiscogs(mdbmaps, "RYM", "ca2577a5936067144a45e00da069170b", "109947")   ### [Mclusky]
    addDiscogs(mdbmaps, "RYM", "35916743cb13af35180fc4092a8af174", "3718032")   ### [Yu Miyake]
    addDiscogs(mdbmaps, "RYM", "6afbd86876892e2989d592f42830665e", "1625262")   ### [Mario Galaxy Orchestra]
    addDiscogs(mdbmaps, "RYM", "283a24c1889712bc4404cefc2585eaac", "1387807")   ### [Shibusashirazu]
    addDiscogs(mdbmaps, "RYM", "b8fdbd005a1ea5443b399b4902389be3", "833163")   ### [José Van Dam]
    addDiscogs(mdbmaps, "RYM", "48435035a72262a5c872c40127e4bcae", "5220036")   ### [Shōgo Sakai]
    addDiscogs(mdbmaps, "RYM", "b58586ce55750a36ce1e2846924567dd", "835650")   ### [Collegium Vocale Gent]
    addAllMusic(mdbmaps, "RYM", "166162c241859e2ac7df9e72c3a968c2", "mn0000142767")   ### [Dave Brubeck Quartet]
    addDiscogs(mdbmaps, "RYM", "166162c241859e2ac7df9e72c3a968c2", "251689")   ### [Dave Brubeck Quartet]
    addDiscogs(mdbmaps, "RYM", "a12c3ff6f6f1b321115187fbd2836167", "3943018")   ### [Professor Longhair and his New Orleans Boys]
    addAllMusic(mdbmaps, "RYM", "d3ed51828201f55461b8e50eb70a3ca0", "mn0001488326")   ### [Sun Ra and His Arkestra]
    addDiscogs(mdbmaps, "RYM", "d3ed51828201f55461b8e50eb70a3ca0", "2219395")   ### [Sun Ra and His Arkestra]
    addDiscogs(mdbmaps, "RYM", "47a2e9ff0265dfca51166c188d1dc6a0", "262128")   ### [Art Blakey and The Jazz Messengers]
    addDiscogs(mdbmaps, "RYM", "40a416471254ef5f86c722e7b61ce757", "521963")   ### [Ray Charles His Orchestra and Chorus]
    addDiscogs(mdbmaps, "RYM", "75c916c0bacddbcc17919985eb793deb", "287108")   ### [Mickey and Sylvia]
    addDeezer(mdbmaps, "RYM", "68d0b3546273c06aeeb390eda1211506", "2379021")   ### [Gosia Andrzejewicz]
    addDiscogs(mdbmaps, "RYM", "68d0b3546273c06aeeb390eda1211506", "1163486")   ### [Gosia Andrzejewicz]
    addDeezer(mdbmaps, "RYM", "fa6af02bf507a0fcdb38b679f0c8122d", "76577")   ### [Doda]
    addDeezer(mdbmaps, "RYM", "fc1c73048b67fda50174f53c23ffb9bb", "71203")   ### [Tony Martin]
    addDiscogs(mdbmaps, "RYM", "fc1c73048b67fda50174f53c23ffb9bb", "520764")   ### [Tony Martin]
    addDeezer(mdbmaps, "RYM", "f378d592733c455c132ef0125310216b", "248191")   ### [The Avons]
    addDiscogs(mdbmaps, "RYM", "f378d592733c455c132ef0125310216b", "324390")   ### [The Avons]
    addDeezer(mdbmaps, "RYM", "bce67689ce5606d76bf67f9e8d939ef1", "160609")   ### [Tommy Steele and The Steelmen]
    addDiscogs(mdbmaps, "RYM", "bce67689ce5606d76bf67f9e8d939ef1", "662149")   ### [Tommy Steele and The Steelmen]
    addDeezer(mdbmaps, "RYM", "2a0c745c899051ddfbb77783cf6ee779", "6073616")   ### [Ecco2K]
    addDiscogs(mdbmaps, "RYM", "2a0c745c899051ddfbb77783cf6ee779", "4905641")   ### [Ecco2K]
    addDeezer(mdbmaps, "RYM", "38dd191cc6a9586233f97f5fc3d5aa2a", "78598292")   ### [LOONA ODD EYE CIRCLE]
    addDiscogs(mdbmaps, "RYM", "38dd191cc6a9586233f97f5fc3d5aa2a", "6080850")   ### [LOONA ODD EYE CIRCLE]    
    addDeezer(mdbmaps, "RYM", "345a3a754d70941142c97ddc23875531", "74930292")   ### [Josephine Foster and the Supposed]
    addAllMusic(mdbmaps, "RYM", "345a3a754d70941142c97ddc23875531", "mn0001972461")   ### [Josephine Foster and the Supposed]
    addDeezer(mdbmaps, "RYM", "1d20ba9c582ce56a3ee6b58afac51a11", "253719")   ### [Beaver and Krause]
    addDiscogs(mdbmaps, "RYM", "1d20ba9c582ce56a3ee6b58afac51a11", "84683")   ### [Beaver and Krause]
    addAllMusic(mdbmaps, "RYM", "895cb1f647a19af849f485064fe3318f", "mn0001633598")   ### [Palace Music]
    addAllMusic(mdbmaps, "RYM", "41eed152d1d60026a09852a9be6707d8", "mn0000531986")   ### [Bowie]
    addAllMusic(mdbmaps, "RYM", "f8622b59427a58f6d10228b274130eb0", "mn0000503695")   ### [The Africa '70]
    addDeezer(mdbmaps, "RYM", "1e46268cc0f1f32a140be18ea04f9efe", "1153")   ### [Paco Ibáñez]
    addAllMusic(mdbmaps, "RYM", "1e46268cc0f1f32a140be18ea04f9efe", "mn0000548044")   ### [Paco Ibáñez]
    addDeezer(mdbmaps, "RYM", "99f6bc5d57d6feafe8eb0144d88d9b5e", "180374")   ### [Sixteen Horsepower]
    addDiscogs(mdbmaps, "RYM", "99f6bc5d57d6feafe8eb0144d88d9b5e", "207906")   ### [Sixteen Horsepower]
    addDeezer(mdbmaps, "RYM", "b0cbcf7d16e2aa86f275335cfc7a3fb9", "14985")   ### [Nits]
    addAllMusic(mdbmaps, "RYM", "b0cbcf7d16e2aa86f275335cfc7a3fb9", "mn0000355554")   ### [Nits]
    addDeezer(mdbmaps, "RYM", "be121b29e9bdc34f0c81c2f21f171936", "157515")   ### [Nektar]
    addAllMusic(mdbmaps, "RYM", "be121b29e9bdc34f0c81c2f21f171936", "mn0000380106")   ### [Nektar]
    addDiscogs(mdbmaps, "RYM", "5507ffc4752cd2ae73b6686fac4fe2d3", "1232916")   ### [Spriguns]
    addDeezer(mdbmaps, "RYM", "61f8fa1151a6ff2bc1b0caf9b049101c", "4068826")   ### [Eulenspygel]
    addDiscogs(mdbmaps, "RYM", "61f8fa1151a6ff2bc1b0caf9b049101c", "363905")   ### [Eulenspygel]