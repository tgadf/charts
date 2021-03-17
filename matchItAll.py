
def matchItAll(mdbmaps, thresholds, useAlbums=True, mdbmc=None, db=None, toMatch=None):
    if toMatch is None:
        toMatch   = mdbmc.getDataToMatch(db, maxValues=10000, maxAlbums=50000)

    if len(toMatch) == 0:
        return

    num_processes = 3
    if useAlbums is True:
        func = matchDBArtistWithAlbums
    else:
        func = matchDBArtistWithoutAlbums
    pfunc = partial(func, **thresholds) # Giving some arguments for kwargs
    #argument_list = list(inputs.items()) # [random.randint(0, 100) for _ in range(num_jobs)]
    dbName = list(toMatch.keys())[0]
    copyMapData(mdbmaps[dbName])

    argument_list = toMatch[dbName]
    if len(argument_list) == 0:
        return
    print("Running imap multiprocessing for {0} artists ...".format(len(argument_list)))
    result_list = multiProc(func=pfunc, argument_list=argument_list,
                                           num_processes=num_processes)


    start, cmt = clock("Saving...")
    saveMapData(mdbmaps[dbName], result_list)
    elapsed(start, cmt)
    print("\nSleeping for 10 seconds...\n")
    #sleep(10)
    
    #mdbmc.matchMutualMaps()

    
def matchDBArtistWithoutAlbums(item, *args, **kwargs):
    primaryKey = item[0]
    artistData = item[1]
    artistName   = artistData["ArtistName"]
    artistID     = primaryKey
    artistAlbums = None
    mdbMatcher = matchDBArtist(maindb)
    mdbMatcher.setArtistInfo(artistName, artistID, artistAlbums)
    mdbMatcher.setThresholds(matchNumArtistName=kwargs['numArtistName'], matchArtistNameCutoff=kwargs['artistNameCutoff'],
                             matchArtistAlbumCutoff=kwargs['artistAlbumCutoff'], matchNumArtistAlbums=kwargs['numArtistAlbums'],
                             matchScore=kwargs['score']),
    mcs    = mdbMatcher.findPotentialArtistNameMatchesWithoutAlbums()
    retval = [primaryKey,artistName,artistID,mcs]
    return retval


def matchDBArtistWithAlbums(item, *args, **kwargs):    
    #time.sleep(0.0025)

    
    primaryKey = item[0]
    artistData = item[1]
    artistName   = artistData["ArtistName"]
    artistID     = primaryKey
    artistAlbums = artistData["ArtistAlbums"]
    
    mdbMatcher = matchDBArtist(maindb)
    mdbMatcher.setArtistInfo(artistName, artistID, artistAlbums)
    mdbMatcher.setThresholds(matchNumArtistName=kwargs['numArtistName'], matchArtistNameCutoff=kwargs['artistNameCutoff'], 
                             matchArtistAlbumCutoff=kwargs['artistAlbumCutoff'], matchNumArtistAlbums=kwargs['numArtistAlbums'],
                             matchScore=kwargs['score'])
    mcs    = mdbMatcher.findPotentialArtistAlbumMatches()
    retval = [primaryKey,artistName,artistID,mcs]
    return retval


def multiProc(func, argument_list, num_processes):
    pool = Pool(processes=num_processes)
    result_list_tqdm = []
    for result in tqdm(pool.imap(func=func, iterable=argument_list), total=len(argument_list)):
        result_list_tqdm.append(result)
    return result_list_tqdm