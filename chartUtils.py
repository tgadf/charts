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
    iterItems.update({2: {"Max": 3, "Vals": 500}})
    iterItems.update({1: {"Max": 2, "Vals": 500}})
    return iterItems


def getThresholdsWithoutAlbums(cutoff=0.9):
    return {'numArtistName': 5, 'artistNameCutoff': cutoff, 'artistAlbumCutoff': None, 'numArtistAlbums': None, 'score': None}
    
    
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

def addMusicBrainz(mdbmaps, chartType, amID, url):
    try:
        int(url)
        dbID = url
    except:
        dbID = maindb.getArtistDBIDFromUtil("MusicBrainz", url)
    if dbID is None:
        return
    mdbmaps[chartType].addArtistDataByKey(amID, "MusicBrainz", dbID)