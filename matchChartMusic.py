from matchAlbums import matchAlbums
from listUtils import getFlatList

class chartArtistData:
    def __init__(self, artist, albums):
        self.artist = artist
        self.albums = albums

class matchChartMusic:
    def __init__(self, mdb, debug=False):
        self.debug = debug
        self.mdb   = mdb
        
        self.results  = {}
        self.cad      = None
        
        
    def getResults(self):
        return self.results
        
        
    def setChartArtistData(self, chartArtist, chartAlbums):
        self.cad = chartArtistData(chartArtist, chartAlbums)
        
        
    def matchChartArtistByName(self, ratioCut=0.95, returnData=True):
        chartArtist       = self.cad.artist
        chartArtistAlbums = self.cad.albums
        
        
        ######################################################################
        #### Get Potential DB Artists
        ######################################################################
        artistNameDBIDs = self.mdb.getArtistIDs(chartArtist, num=50, cutoff=ratioCut)
        
        
        ######################################################################
        #### Get Database Albums
        ######################################################################
        matches = {}
        for db,artistDBartists in artistNameDBIDs.items():
            matches[db] = None
            if len(artistDBartists) == 1:
                artistIDs = list(artistDBartists.values())[0]
                if len(artistIDs) == 1:
                    matches[db] = artistIDs[0]
                
        return matches

        
    def matchChartArtist(self, albumType=None, ratioCut=0.95, returnData=True):
        chartArtist       = self.cad.artist
        chartArtistAlbums = self.cad.albums
        
        
        ######################################################################
        #### Get Potential DB Artists
        ######################################################################
        artistNameDBIDs = self.mdb.getArtistIDs(chartArtist, num=50, cutoff=0.7)
        
        
        ######################################################################
        #### Get Database Albums
        ######################################################################
        matches = {}
        for db,artistDBartists in artistNameDBIDs.items():
            
            dbMatches = {}
            for artistDBartist,artistDBIDs in artistDBartists.items():
                for artistDBID in artistDBIDs:
                    dbMatches[artistDBID] = {}
                    artistDBAlbumsFromID = self.mdb.getArtistAlbumsFromID(db, artistDBID)

                    for mediaType, mediaTypeAlbums in artistDBAlbumsFromID.items():
                        if albumType is not None:
                            if mediaType not in self.mdb.getDBAlbumTypeNames(db, albumType):
                                continue

                        ma = matchAlbums(cutoff=ratioCut)
                        ma.match(chartArtistAlbums, mediaTypeAlbums)
                        #ma.show(debug=True)
                        
                        dbMatches[artistDBID][mediaType] = ma
                        
            matches[db] = dbMatches
            
            
        ######################################################################
        #### Find Best Match
        ######################################################################
        retval = {}
        for db,dbdata in matches.items():
            retval[db] = None
            bestMatch = {"ID": None, "Matches": 0, "Score": 0.0}
            for artistDBID,artistDBData in dbdata.items():
                for mediaType,ma in artistDBData.items():
                    if ma.near == 0:
                        continue
                    if ma.near > bestMatch["Matches"]:
                        bestMatch = {"ID": artistDBID, "Matches": ma.near, "Score": ma.score}
                    elif ma.near == bestMatch["Matches"]:
                        if ma.score > bestMatch["Score"]:
                            bestMatch = {"ID": artistDBID, "Matches": ma.near, "Score": ma.score}

            if bestMatch["ID"] is not None:
                retval[db] = bestMatch["ID"]
                #print("mdb.add(\"{0}\", \"{1}\", \"{2}\")".format(self.cad.artist, db, bestMatch["ID"]))
                
        if returnData:
            return retval
        self.results[self.cad.artist] = retval
    
    
    
    def manuallyMatchUnknownArtist(self, unknownArtist, albums, cutoff=0.8):
        self.setChartArtistData(unknownArtist, albums)
        unMatchedAlbums = self.cad.albums        
        
        ######################################################################
        #### Get Unknown Artist Albums and Potential DB Artists
        ######################################################################
        artistNameDBIDs = self.mdb.getArtistIDs(unknownArtist, cutoff=cutoff)
        
        print("Unknown Artist:   {0}".format(unknownArtist))
        try:
            print("UnMatched Albums: {0}".format(", ".join(unMatchedAlbums)))
        except:
            print("Could not show the unMatched Albums below:")
            print("-> ",unMatchedAlbums," <-")
        print("="*50)
        print(artistNameDBIDs)
        for db,artistDBartists in artistNameDBIDs.items():
            print("="*50)
            print("   {0}".format(db))
            for artistDBartist,artistDBIDs in artistDBartists.items():
                print("      {0}".format(artistDBartist))
                for artistDBID in artistDBIDs:
                    artistDBAlbumsFromID = self.mdb.getArtistAlbumsFromID(db, artistDBID)
                    albums = [list(mediaTypeAlbums.values()) for mediaTypeAlbums in artistDBAlbumsFromID.values()]
                    print("mdb.add(\"{0}\", \"{1}\", \"{2}\")".format(unknownArtist, db, artistDBID))
                    print("         {0: <45}\t{1}".format(artistDBID, getFlatList(albums)))


