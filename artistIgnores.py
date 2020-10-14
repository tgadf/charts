def getArtistIgnores(artist):
    
    ## Billboard
    if artist in ["Original Broadway Cast", "Soundtrack", "Who", "Music From The Television Event", "Various"]:
        return False        
    if artist in ["Original Broadway Cast Recording", "Original Cast"]:
        return False

    if artist in ["SANDAIME J SOUL BROTHERS from EXILE TRIBE Feat. Afrojack", "Sech, Darell, Nicky Jam, Ozuna & Anuel AA", "Bethel Music, Jonathan David Helser & Melissa Helser", "Delbert McClinton And Self-Made Men + Dana", "Meduza Featuring GOODBOYS", "VASSY & Disco Fries"]:
        return False
        #print("")
        #print(chartName)
    if artist in ["The JT Project Featuring Najee", "Roger Daltrey With Members Of The Who Band And Orchestra/Keith Levenson", "Gerald Causse & Nicolas Giusti", "King & Prince"]:
        return False
        #print("")
        #print(chartName)
    if artist in ["Dominican Sisters Of Mary, Mother Of The Eucharist", "Eric Buchholz/Slovak National Symphony Orchestra/Naigus/Strange/Rudisill/Peacock/Gonzales"]:
        return False
        #print("")
        #print(chartName)
    if artist in ["Kittel & Co.", "BeBe Winans Featuring Tobbi & Tommi Introducing Kiandra", "Jason Campbell Featuring Robin Campbell With Kirsten Campbell Wood, Saydi Driggers And The Phoenix Boys Choir (Stangelberger)"]:
        return False
        #print("")
        #print(chartName)
    if artist in ["Bruckner Orchester Linz Conducted By Dennis Russell Davies", "Dr. Kokastien", "Mormon Tabernacle Choir/Orchestra At Temple Square"]:
        return False
        #print("")
        #print(chartName)
    if artist in ["Various Artists", "Original Cast Recording"]:
        return False
        #print("")
        #print(chartName)
        
        
    ## Top 40
    if artist in ["Original Broadway Cast", "Soundtrack", "Who", "Music From The Television Event", "Various"]:
        return False
    if artist in ["Artists Stand Up To Cancer"]:
        return False
    if artist in ["Flight Of The Conchords", "Glee Cast"]:
        return False
    if artist in ["Various Artists"]:
        return False
    if artist.startswith("American Idol Season"):
        return False
    if len(artist.strip()) == 0:
        return False

        
    return True