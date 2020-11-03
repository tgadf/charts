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
        
        self.results   = {}
        self.cad       = None
        self.dbartists = None
        
        
    def setMatchedChartArtists(self, dbartists):
        self.dbartists = dbartists
        
        
    def getResults(self):
        return self.results
        
        
    def setChartArtistData(self, chartArtist, chartAlbums):
        self.cad = chartArtistData(chartArtist, chartAlbums)
        
        
    def matchChartArtistByName(self, dbs=None, num=3, ratioCut=0.95, returnData=True):
        chartArtist       = self.cad.artist
        chartArtistAlbums = self.cad.albums
        
        if self.mdb.isKnown(chartArtist):
            return self.mdb.getArtistData(chartArtist)
        
        
        ######################################################################
        #### Get Potential DB Artists
        ######################################################################
        if dbs is None:
            artistNameDBIDs = self.mdb.getArtistIDs(chartArtist, num=50, cutoff=0.7)
        else:
            if isinstance(dbs, list):
                artistNameDBIDs = self.mdb.getArtistIDsFromDBs(chartArtist, dbs=dbs, num=50, cutoff=0.7)
            else:
                raise ValueError("DBs must be a list")
        #print("")
        #print("ArtistNameDBIDs: {0}".format(artistNameDBIDs))
        
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
                    if isinstance(matches[db], dict):
                        try:
                            matches[db] = matches[db]["ID"]
                        except:
                            raise ValueError("No ID in {0}".format(matches[db]))
                    else:
                        pass
                    
        #print("Matches: {0}".format(matches))
        #print("")
        return matches

    
    def getFullArtistMatchDF(self, artists):
        retval = {artistName: {k: None for k in self.mdb.getDBs()} for artistName in artists}
        return retval
        
        
    def matchChartArtistByKnown(self, albumType=None, ratioCut=0.95, returnData=True):
        chartArtist       = self.cad.artist
        chartArtistAlbums = self.cad.albums
        
        if self.mdb.isKnown(chartArtist):
            artistData = self.mdb.getArtistData(chartArtist)
            retval = {k: None if v is None else v.get("ID") for k,v in artistData.items()}
        else:
            retval = {k: None for k in self.mdb.getDBs()}

        return retval
        
        
    def matchChartArtist(self, dbs=None, albumType=None, ratioCut=0.95, returnData=True):
        chartArtist       = self.cad.artist
        chartArtistAlbums = self.cad.albums
        
        if self.mdb.isKnown(chartArtist):
            return self.mdb.getArtistData(chartArtist)
        
            
        
        
        ######################################################################
        #### Get Potential DB Artists
        ######################################################################
        if dbs is None:
            artistNameDBIDs = self.mdb.getArtistIDs(chartArtist, num=50, cutoff=0.7)
        else:
            if isinstance(dbs, list):
                artistNameDBIDs = self.mdb.getArtistIDsFromDBs(chartArtist, dbs=dbs, num=50, cutoff=0.7)
            else:
                raise ValueError("DBs must be a list")
        
        
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


                    

                    
    def getArtistDBMatchLists(self, dbartist):
        dbArtistData = self.dbartists.get(dbartist)
        retval       = {"Matched": [], "Unmatched": []}
        albumTypesData = {k: [] for k in [1,2,3,4]}
        for db,dbIDdata in dbArtistData.items():
            try:
                int(dbIDdata)
                retval["Matched"].append(db)
            except:
                retval["Unmatched"].append(db)
        return retval
    
                    
    def getMatchedArtistAlbumsFromDB(self, dbartist, merge=True):
        dbArtistData   = self.dbartists.get(dbartist)
        dbsToSearch    = self.getArtistDBMatchLists(dbartist)
        albumTypesData = {k: [] for k in [1,2,3,4]}
        for db in dbsToSearch["Matched"]:
            dbIDdata = dbArtistData[db]
            try:                
                dbID = dbIDdata
            except:
                raise ValueError("This db {0} should already be known for {1}".format(db, dbartist))

            dbAlbumsData = self.mdb.getArtistAlbumsFromID(db, dbID)

            for albumType in albumTypesData.keys():
                for mediaType, mediaTypeAlbums in dbAlbumsData.items():
                    if mediaType not in self.mdb.getDBAlbumTypeNames(db, albumType):
                        continue                
                    #print(db,albumType,mediaType,mediaTypeAlbums)
                    albumTypesData[albumType] += list(mediaTypeAlbums.values())

        albumTypesData = {k: list(set(v)) for k,v in albumTypesData.items()}

        ############################
        ## Merge Albums
        ############################
        if merge is True:
            artistAlbums = getFlatList(albumTypesData.values())
        else:
            artistAlbums = albumTypesData

        return artistAlbums

            
    def searchForMutualDBEntries(self, chartType, cutoff=0.8, maxAdds=50):
        if self.dbartists is None:
            raise ValueError("Must set dbartist")
        dbartists = self.dbartists
            
        ######################################################################
        #### Get Map of Artists and Unmatched Albums
        ######################################################################
        cnts      = 0
        print("Searching for mutual DB matches for {0} artists".format(len(dbartists)))
        for ia,dbartist in enumerate(dbartists):
            if ia % 100 == 0:
                print("# Finished {0}/{1}".format(ia,len(dbartists)))
            if cnts >= maxAdds:
                break
            artistAlbums = self.getMatchedArtistAlbumsFromDB(dbartist, merge=True)
            dbsToSearch  = self.getArtistDBMatchLists(dbartist)
            #print(dbartist,"\t",dbsToSearch)
            
            ############################
            ## Loop Over Unmatched DBs
            ############################
            for db in dbsToSearch["Unmatched"]:
                dbMatches = {}
                artistDBartists = self.mdb.getArtistDBIDs(dbartist, db, num=10, cutoff=cutoff, debug=False)
                
                for artistDBartist,artistDBIDs in artistDBartists.items():
                    #print('  ',db,'\t',artistDBartist)
                    for artistDBID in artistDBIDs:
                        #print('    ',artistDBID)
                        dbMatches[artistDBID] = {}
                        artistDBAlbumsFromID = self.mdb.getArtistAlbumsFromID(db, artistDBID)

                        albumTypesData = {k: [] for k in [1,2,3,4]}
                        for albumType in albumTypesData.keys():
                            for mediaType, mediaTypeAlbums in artistDBAlbumsFromID.items():
                                if mediaType not in self.mdb.getDBAlbumTypeNames(db, albumType):
                                    continue
                                albumTypesData[albumType] += list(mediaTypeAlbums.values())

                        albumTypesData = {k: list(set(v)) for k,v in albumTypesData.items()}
                        dbArtistAlbums = getFlatList(albumTypesData.values())
            

                        ma = matchAlbums(cutoff=cutoff)
                        ma.match(artistAlbums, dbArtistAlbums)
                        #ma.show(debug=True)
                        
                        dbMatches[artistDBID] = ma
                
                if len(dbMatches) > 0:
                    bestMatch = {"ID": None, "Matches": 0, "Score": 0.0}
                    for artistDBID,ma in dbMatches.items():
                        if ma.near == 0:
                            continue
                        if ma.near > bestMatch["Matches"]:
                            bestMatch = {"ID": artistDBID, "Matches": ma.near, "Score": ma.score}
                        elif ma.near == bestMatch["Matches"]:
                            if ma.score > bestMatch["Score"]:
                                bestMatch = {"ID": artistDBID, "Matches": ma.near, "Score": ma.score}

                    if bestMatch["ID"] is not None:
                        cnts += 1
                        print("matchedChartResults{0}[\"{1}\"][\"{2}\"] = '{3}'".format(chartType, dbartist, db, bestMatch["ID"]))


