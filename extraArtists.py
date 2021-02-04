from chartUtils import addAllMusic, addDiscogs, addDeezer

def extraKnownArtists(mdbmaps, chartType):
    if chartType == "Billboard":
        return extraAddsForBillboard(mdbmaps, chartType)
    if chartType == "BillboardYE":
        return extraAddsForBillboardYE(mdbmaps, chartType)
    if chartType == "Top40":
        return extraAddsForTop40(mdbmaps, chartType)
    if chartType == "Spotify":        
        return extraAddsForSpotify(mdbmaps, chartType)
        
        

def extraAddsForSpotify(mdbmaps, chartType):
    print("Adding known artist data for {0}".format(chartType))

    
    if chartType == "Spotify":
        addAllMusic(mdbmaps, "Spotify", "cb93fcbd3ab132ac5f5e531955b18314", "mn0001225951")   ### [Mustard]
        ### Want Her  ,  Pure Water (with Migos)  ,  100 Bands (feat. Quavo, 21 Savage, YG & Meek Mill)  ,  Baguettes in the Face (feat. NAV, Playboi Carti & A Boogie Wit da Hoodie)  ,  On GOD (with YG & Tyga feat. A$AP Ferg & A$AP Rocky)  ,  Ballin' (with Roddy Ricch)
        ### Want Her  ---> [['Mustard']]
        ### Pure Water (with Migos)  ---> [['Mustard']]
        ### 100 Bands (feat. Quavo, 21 Savage, YG & Meek Mill)  ---> [['Mustard']]
        ### Baguettes in the Face (feat. NAV, Playboi Carti & A Boogie Wit da Hoodie)  ---> [['Mustard']]
        ### On GOD (with YG & Tyga feat. A$AP Ferg & A$AP Rocky)  ---> [['Mustard']]
        ### Ballin' (with Roddy Ricch)  ---> [['Mustard']]


        addAllMusic(mdbmaps, "Spotify", "7431b4cd1d5849d221baaa7888604a2e", "mn0003622501")   ### [Smokepurpp]
        ### Audi.  ,  123 (with Murda Beatz)  ,  123  ,  Nephew (feat. Lil Pump)  ,  What I Please (feat. Denzel Curry)
        ### Audi.  ---> [['Smokepurpp']]
        ### 123 (with Murda Beatz)  ---> [['Smokepurpp']]
        ### 123  ---> [['Smokepurpp']]
        ### Nephew (feat. Lil Pump)  ---> [['Smokepurpp']]
        ### What I Please (feat. Denzel Curry)  ---> [['Smokepurpp']]

        addAllMusic(mdbmaps, "Spotify", "30662e7c962665273622d2ccd451c3f6", "mn0003487740")   ### [MadeinTYO]
        ### Uber Everywhere  ,  Skateboard P  ,  Skateboard P (feat. Big Sean)  ,  Ned Flanders (feat. A$AP Ferg)
        ### Uber Everywhere  ---> [['MadeinTYO']]
        ### Skateboard P  ---> [['MadeinTYO']]
        ### Skateboard P (feat. Big Sean)  ---> [['MadeinTYO']]
        ### Ned Flanders (feat. A$AP Ferg)  ---> [['MadeinTYO']][GASHAI]

        addAllMusic(mdbmaps, "Spotify", "a04480bfdbafbc14b45846754ba8740e", "mn0003244210")   ### [GASHI]
        ### Disrespectful  ,  Creep On Me
        ### Disrespectful  ---> [['21 Savage', 'GASHI']]
        ### Creep On Me  ---> [['GASHI']]

        addAllMusic(mdbmaps, "Spotify", "404f6b7df28cbd293554f353dc5976b2", "mn0003888541")   ### [Bankrol Hayden]
        ### Costa Rica  ,  Costa Rica (feat. The Kid LAROI) - Remix
        ### Costa Rica  ---> [['Bankrol Hayden']]
        ### Costa Rica (feat. The Kid LAROI) - Remix  ---> [['Bankrol Hayden']]

        addAllMusic(mdbmaps, "Spotify", "dd9d8d514ab3ca6bc2ec2c9480cd67bf", "mn0003749776")   ### [Tyla Yaweh]
        ### Tommy Lee (feat. Post Malone)  ,  Stuntin' On You (feat. DaBaby)
        ### Tommy Lee (feat. Post Malone)  ---> [['Tyla Yaweh']]
        ### Stuntin' On You (feat. DaBaby)  ---> [['Tyla Yaweh']]

        addAllMusic(mdbmaps, "Spotify", "1909ad8603f5b973026a364c6d6cee8e", "mn0003594453")   ### [Ashnikko]
        ### STUPID (feat. Yung Baby Tate)  ,  Daisy
        ### STUPID (feat. Yung Baby Tate)  ---> [['Ashnikko']]
        ### Daisy  ---> [['Ashnikko']]

        addAllMusic(mdbmaps, "Spotify", "7d31d398fcbd69ec4487460ce593ab44", "mn0003750925")   ### [The Carters]
        ### APESHIT  ,  BOSS
        ### APESHIT  ---> [['The Carters']]
        ### BOSS  ---> [['The Carters']]

        addAllMusic(mdbmaps, "Spotify", "c595fb8cc61d6b512b253fc4ad505b32", "mn0003455720")   ### [Chris Lane]
        ### Take Back Home Girl (Feat. Tori Kelly)  ,  I Don't Know About You
        ### Take Back Home Girl (Feat. Tori Kelly)  ---> [['Chris Lane']]
        ### I Don't Know About You  ---> [['Chris Lane']]

        addAllMusic(mdbmaps, "Spotify", "c21f0a059e5d5a86e989d3384dc0040d", "mn0003938306")   ### [StaySolidRocky]
        ### Party Girl  ,  Party Girl (Remix)
        ### Party Girl  ---> [['StaySolidRocky']]
        ### Party Girl (Remix)  ---> [['StaySolidRocky']]

        addAllMusic(mdbmaps, "Spotify", "ef9f608a3737c743051a6a27cc74d8e4", "mn0004015271")   ### [Popp Hunna]
        ### Adderall (Corvette Corvette) - Remix
        ### Adderall (Corvette Corvette) - Remix  ---> [['Popp Hunna']]

        addAllMusic(mdbmaps, "Spotify", "f215decc2db538a85c1cdd3159a21fba", "mn0003873918")   ### [Sleepy Hallow]
        ### Deep End Freestyle
        ### Deep End Freestyle  ---> [['Sleepy Hallow']]

        addAllMusic(mdbmaps, "Spotify", "c83e0d312315ea129a3e5039add19073", "mn0003911872")   ### [J.I the Prince of N.Y]
        ### Need Me
        ### Need Me  ---> [['J.I the Prince of N.Y']]

        addAllMusic(mdbmaps, "Spotify", "b6fbc16cce329059ad1fe561da88d6a3", "mn0003951825")   ### [Curtis Waters]
        ### Stunnin' (feat. Harm Franklin)
        ### Stunnin' (feat. Harm Franklin)  ---> [['Curtis Waters']]

        addAllMusic(mdbmaps, "Spotify", "d29ca9cdac21c8e5c6b0a2b62d4c212d", "mn0003534795")   ### [Phillipa Soo]
        ### Helpless
        ### Helpless  ---> [['Phillipa Soo']]
        

        addDiscogs(mdbmaps, "Spotify", "e7925c4250ca95e91af6ca783dff9516", "8481312")    ### [CORPSE]
        ### E-GIRLS ARE RUINING MY LIFE!
        ### E-GIRLS ARE RUINING MY LIFE!  ---> [['CORPSE']]

        addDiscogs(mdbmaps, "Spotify", "a37667aa00e1298bcd90842d6acdb936", "7849641")    ### [DripReport]
        ### Skechers
        ### Skechers  ---> [['DripReport']]

        addAllMusic(mdbmaps, "Spotify", "8090d641474442accd7daefe0d39a6af", "mn0003454592")   ### [Delacey]
        ### Cruel Intentions
        ### Cruel Intentions  ---> [['Delacey']]

        addAllMusic(mdbmaps, "Spotify", "dea18355b230604c18f98c431d7fcd21", "mn0003442795")   ### [Quinn XCII]
        ### Coffee
        ### Coffee  ---> [['Quinn XCII']]

        addAllMusic(mdbmaps, "Spotify", "02bcf7cb8f6918b713138598e5444689", "mn0003970104")   ### [Claire Rosinkranz]
        ### Backyard Boy
        ### Backyard Boy  ---> [['Claire Rosinkranz']]

        addAllMusic(mdbmaps, "Spotify", "51a204ac9d8bb7b95ddae0d61002ea77", "mn0003986042")   ### [WhoHeem]
        ### Lets Link
        ### Lets Link  ---> [['WhoHeem']]

        addAllMusic(mdbmaps, "Spotify", "6f780f98c2702093c33c2bf81f53d3c3", "mn0003966083")   ### [salem ilese]
        ### Mad at Disney
        ### Mad at Disney  ---> [['salem ilese']]

        addAllMusic(mdbmaps, "Spotify", "84a805a953729bbc0639a777d2a36123", "mn0003992265")   ### [Ritt Momney]
        ### Put Your Records On
        ### Put Your Records On  ---> [['Ritt Momney']]

        addAllMusic(mdbmaps, "Spotify", "e71f9a48fd5c08b24dffbaa46d6e29d1", "mn0003550123")   ### [Nebu Kiniza]
        ### Gassed Up
        ### Gassed Up  ---> [['Nebu Kiniza']]

        addAllMusic(mdbmaps, "Spotify", "b2bb9af81483d1c2efb5e5320a239478", "mn0003549339")   ### [DJ ESCO]
        ### Too Much Sauce (feat. Future & Lil Uzi Vert)
        ### Too Much Sauce (feat. Future & Lil Uzi Vert)  ---> [['DJ ESCO']]

        addAllMusic(mdbmaps, "Spotify", "0980eca80d39428c6b1a1c3e3ac0a0d6", "mn0003556388")   ### [Olivia Rodrigo]
        ### All I Want - From "High School Musical: The Musical: The Series"
        ### All I Want - From "High School Musical: The Musical: The Series"  ---> [['Olivia Rodrigo']]

        addAllMusic(mdbmaps, "Spotify", "4909cfb2b7dc19f8b0caccc07ed7d598", "mn0003903987")   ### [TOKYO’S REVENGE]
        ### GOODMORNINGTOKYO!
        ### GOODMORNINGTOKYO!  ---> [['TOKYO’S REVENGE']]

        addAllMusic(mdbmaps, "Spotify", "ead60268db963c273d2b5d666c34ef5c", "mn0003443300")   ### [VÉRITÉ]
        ### Somebody Else
        ### Somebody Else  ---> [['VÉRITÉ']]

        addAllMusic(mdbmaps, "Spotify", "6d0bbb8db0d2122b10f15dc6e07dd0c1", "mn0003371039")   ### [Marc E. Bassy]
        ### You & Me
        ### You & Me  ---> [['Marc E. Bassy']]

        addAllMusic(mdbmaps, "Spotify", "94007de7c4d6728a02333bcb8c8ab8a3", "mn0003388290")   ### [MiC LOWRY]
        ### Oh Lord
        ### Oh Lord  ---> [['MiC LOWRY']]

        addAllMusic(mdbmaps, "Spotify", "0eeafcb3df1cb188f5f3afd2f95647d2", "mn0003482938")   ### [KREAM]
        ### Taped up Heart (feat. Clara Mae)
        ### Taped up Heart (feat. Clara Mae)  ---> [['KREAM']]

        addAllMusic(mdbmaps, "Spotify", "e9776f010afe5ca14ef1593a7db12bd6", "mn0003542365")   ### [Stanaj]
        ### Romantic - NOTD Remix
        ### Romantic - NOTD Remix  ---> [['Stanaj']]

        addAllMusic(mdbmaps, "Spotify", "317eac9167db21afebe597b2d71dece8", "mn0003623901")   ### [Loote]
        ### High Without Your Love
        ### High Without Your Love  ---> [['Loote']]

        addAllMusic(mdbmaps, "Spotify", "09d50537d19631fdf33b5b2e2196e25f", "mn0003637690")   ### [NexXthursday]
        ### Sway (feat. Quavo & Lil Yachty)
        ### Sway (feat. Quavo & Lil Yachty)  ---> [['NexXthursday']]

        addAllMusic(mdbmaps, "Spotify", "ccf1bc510a363d579ee936fb5537165d", "mn0003664364")   ### [Tay-K]
        ### The Race
        ### The Race  ---> [['Tay-K', '22 Savage']]

        addAllMusic(mdbmaps, "Spotify", "5f5c67ff48ada0e786f18c88a2d12928", "mn0003739509")   ### [Chad Focus]
        ### Get to the Money
        ### Get to the Money  ---> [['Chad Focus']]

        addAllMusic(mdbmaps, "Spotify", "53a6de61e271b6e9690efa70a8beb864", "mn0003674623")   ### [Chucho Flash]
        ### Tu Sabes Que Te Quiero
        ### Tu Sabes Que Te Quiero  ---> [['Chucho Flash']]

        addAllMusic(mdbmaps, "Spotify", "187a9b1acebe60867145dcc096312cb8", "mn0000065620")   ### [Bobby "Boris" Pickett]
        ### Monster Mash
        ### Monster Mash  ---> [['Bobby "Boris" Pickett']]

        addAllMusic(mdbmaps, "Spotify", "14daf890c1544fb7ce4eb3422ce01ddf", "mn0003976796")   ### [22 Savage]
        ### The Race
        ### The Race  ---> [['Tay-K', '22 Savage']]

        addDiscogs(mdbmaps, "Spotify", "7e301f86bbb9e2e5a95c89463444a6d4", "845430")    ### [Mykola Dmytrovych Leontovych]
        ### Carol of the Bells
        ### Carol of the Bells  ---> [['Mykola Dmytrovych Leontovych']]        

        addAllMusic(mdbmaps, "Spotify", "0ac003e8bfb15af86807b2370d89d499", "mn0003991858")   ### [HVME]
        ### Goosebumps
        ### Goosebumps  ---> [['HVME']]

        addAllMusic(mdbmaps, "Spotify", "85270e55dead1c69b2f3f1b028cfa5c0", "mn0003783963")   ### [Andrew Andraos]
        ### Amazing Grace
        ### Amazing Grace  ---> [['Andrew Andraos']]

        addDiscogs(mdbmaps, "Spotify", "2d456076ddf63af9a011730017640a28", "8093594")    ### [Wilbur Soot]
        ### Your New Boyfriend
        ### Your New Boyfriend  ---> [['Wilbur Soot']]

        addAllMusic(mdbmaps, "Spotify", "b94c78e453b1caf5350dd89465e3ec57", "mn0003303922")   ### [Trey Lewis]
        ### Dicked Down in Dallas
        ### Dicked Down in Dallas  ---> [['Trey Lewis']]

        addAllMusic(mdbmaps, "Spotify", "aa3de59b4cbd42f239a25a753da6d6d2", "mn0003996751")   ### [347aidan]
        ### Dancing in My Room
        ### Dancing in My Room  ---> [['347aidan']]

        addAllMusic(mdbmaps, "Spotify", "47f5229f12e90cc1c3d7c43f27318aa3", "mn0004005659")   ### [Fousheé]
        ### Deep End
        ### Deep End  ---> [['Fousheé']]

        addAllMusic(mdbmaps, "Spotify", "76e1c7316d38224af8b740f53a7ee3ec", "mn0003890057")   ### [Ant Saunders]
        ### Yellow Hearts
        ### Yellow Hearts  ---> [['Ant Saunders']]

        addAllMusic(mdbmaps, "Spotify", "51732044ce01bbd865643834bd0a348b", "mn0003504703")   ### [Blue Ivy]
        ### BROWN SKIN GIRL
        ### BROWN SKIN GIRL  ---> [['Blue Ivy']]

        addAllMusic(mdbmaps, "Spotify", "644ec747591292fe2198244beb274e58", "mn0003849095")   ### [Ambjaay]
        ### Uno
        ### Uno  ---> [['Ambjaay']]

        addAllMusic(mdbmaps, "Spotify", "c0bde33feb703015ca4d3d0ae1fc9585", "mn0003824736")   ### [Shordie Shordie]
        ### Bitchuary
        ### Bitchuary  ---> [['Shordie Shordie']]

        addAllMusic(mdbmaps, "Spotify", "e0251f7d87571e7fe5ed02a60815cd54", "mn0003859093")   ### [Ashley O]
        ### On A Roll
        ### On A Roll  ---> [['Ashley O']]

        addAllMusic(mdbmaps, "Spotify", "c403314702c6a6af3d0f9fec374c9107", "mn0003836062")   ### [Luh Kel]
        ### Wrong
        ### Wrong  ---> [['Luh Kel']]

        addAllMusic(mdbmaps, "Spotify", "ce3c103c18f37437fb4f28bd1f2fc759", "mn0003061304")   ### [FLETCHER]
        ### Undrunk
        ### Undrunk  ---> [['FLETCHER']]

        addAllMusic(mdbmaps, "Spotify", "60bd3578cba114079d0c96ac68993625", "mn0003757508")   ### [YK Osiris]
        ### Worth It
        ### Worth It  ---> [['YK Osiris']]

        addAllMusic(mdbmaps, "Spotify", "c5686ff1b88412a406250a5fdfb7d7db", "mn0003368290")   ### [JID]
        ### Off Deez (with J. Cole)
        ### Off Deez (with J. Cole)  ---> [['JID']]

        addAllMusic(mdbmaps, "Spotify", "97a8f2d05cc8b772d0e7a8d4cc8c2bcd", "mn0003795890")   ### [K-DA]
        ### POP/STARS  ,  THE BADDEST  ,  MORE
        ### POP/STARS  ---> [['K-DA']]
        ### THE BADDEST  ---> [['K-DA']]
        ### MORE  ---> [['K-DA']]

        addAllMusic(mdbmaps, "Spotify", "9fe6b1eff3e2d72672e0b90136028207", "mn0001192847")   ### [Cochise]
        ### Hatchback
        ### Hatchback  ---> [['Cochise']]

        addAllMusic(mdbmaps, "Spotify", "d4a51703580b7098940d075f060eee9a", "mn0003982360")   ### [Lil Eazzyy]
        ### Onna Come Up
        ### Onna Come Up  ---> [['Lil Eazzyy']]

        addAllMusic(mdbmaps, "Spotify", "e8e00686b62a5d14852f08931994c041", "mn0002633829")   ### [The Citizens of Halloween]
        ### This Is Halloween
        ### This Is Halloween  ---> [['The Citizens of Halloween']]

        addAllMusic(mdbmaps, "Spotify", "7ce15ad96dba948863a2d0f494fbedad", "mn0000790820")   ### [Tool]
        ### Fear Inoculum  ,  Pneuma  ,  Invincible  ,  7empest
        ### Fear Inoculum  ---> [['Tool']]
        ### Pneuma  ---> [['Tool']]
        ### Invincible  ---> [['Tool']]
        ### 7empest  ---> [['Tool']]

        addAllMusic(mdbmaps, "Spotify", "72adaf67153b86d1c69a8d24032803ca", "mn0002690553")   ### [The Neighbourhood]
        ### Sweater Weather  ,  Daddy Issues
        ### Sweater Weather  ---> [['The Neighbourhood']]
        ### Daddy Issues  ---> [['The Neighbourhood']]


        addAllMusic(mdbmaps, "Spotify", "cccdb9fca3982c5eb3b6c3947e18301f", "mn0000484880")   ### [Sugarland]
        addDiscogs(mdbmaps, "Spotify", "cccdb9fca3982c5eb3b6c3947e18301f", "1026918")    ### [Sugarland]
        ### Babe (feat. Taylor Swift)
        ### Babe (feat. Taylor Swift)  ---> [['Sugarland']]        



        addAllMusic(mdbmaps, "Spotify", "73c7633383116147ed0a763b1b74cbf2", "mn0000479329")   ### [JAY1]
        ### Becky  ,  Your Mrs  ,  Mocking It  ,  4AM in Coventry  ,  Million Bucks  ,  Flex (feat. JB Scofield)  ,  TEE (feat. Loski)
        ### Becky  ---> [['JAY1']]
        ### Your Mrs  ---> [['JAY1']]
        ### Mocking It  ---> [['JAY1']]
        ### 4AM in Coventry  ---> [['JAY1']]
        ### Million Bucks  ---> [['JAY1']]
        ### Flex (feat. JB Scofield)  ---> [['JAY1']]
        ### TEE (feat. Loski)  ---> [['JAY1']]


        addAllMusic(mdbmaps, "Spotify", "7f4284d9f3a1ee0baf72b8c9039f72a1", "mn0003921045")   ### [Russ Millions]
        ### Gun Lean  ,  Gun Lean Remix  ,  Keisha & Becky - Russ splash x Tion Wayne  ,  Keisha & Becky - Remix
        ### Gun Lean  ---> [['Russ Millions']]
        ### Gun Lean Remix  ---> [['Russ Millions']]
        ### Keisha & Becky - Russ splash x Tion Wayne  ---> [['Russ Millions']]
        ### Keisha & Becky - Remix  ---> [['Russ Millions']]


        addAllMusic(mdbmaps, "Spotify", "141955193f7d55ce60b96a1fb76ad095", "mn0003785719")   ### [Unknown T]
        ### Homerton B  ,  Leave Dat Trap  ,  Fresh Home
        ### Homerton B  ---> [['Unknown T']]
        ### Leave Dat Trap  ---> [['Unknown T']]
        ### Fresh Home  ---> [['Unknown T']]


        addAllMusic(mdbmaps, "Spotify", "11d638dc87f98af49a429b96406d64eb", "mn0003744107")   ### [Nathan Dawe]
        ### Flowers (feat. Jaykae and MALIKA)  ,  Lighter (feat. KSI)  ,  No Time For Tears
        ### Flowers (feat. Jaykae and MALIKA)  ---> [['Nathan Dawe']]
        ### Lighter (feat. KSI)  ---> [['Nathan Dawe']]
        ### No Time For Tears  ---> [['Nathan Dawe']]


        addAllMusic(mdbmaps, "Spotify", "f5555049e17c6246892df23b08ea3266", "mn0003833704")   ### [Poundz]
        ### Opp Thot  ,  Smooth Criminal
        ### Opp Thot  ---> [['Poundz']]
        ### Smooth Criminal  ---> [['Poundz']]


        addAllMusic(mdbmaps, "Spotify", "bc0cf311cb91ac62c6120d00289602b2", "mn0003859136")   ### [dutchavelli]
        ### Bando Diaries  ,  Cool With Me (feat. M1llionz)
        ### Bando Diaries  ---> [['dutchavelli']]
        ### Cool With Me (feat. M1llionz)  ---> [['dutchavelli']]


        addAllMusic(mdbmaps, "Spotify", "807893de7df8a5bb87f88d6a813f8b83", "mn0001285653")   ### [Abra Cadabra]
        ### On Deck  ,  On Deck (Remix) [feat. Rv, Kush, Double Lz, Bandokay, Lowkey OFB & Dezzie]
        ### On Deck  ---> [['Abra Cadabra']]
        ### On Deck (Remix) [feat. Rv, Kush, Double Lz, Bandokay, Lowkey OFB & Dezzie]  ---> [['Abra Cadabra']]


        addAllMusic(mdbmaps, "Spotify", "bc6d2d2796ffe78f23f0ec5f72e67aa0", "mn0003806139")   ### [220 KID]
        ### Don’t Need Love (with GRACEY)  ,  Too Many Nights (with JC Stewart)
        ### Don’t Need Love (with GRACEY)  ---> [['220 KID']]
        ### Too Many Nights (with JC Stewart)  ---> [['220 KID']]


        addAllMusic(mdbmaps, "Spotify", "5876088f590ec4cb98dbcbfd6a563d41", "mn0002357372")   ### [iLL BLU]
        ### Magic (feat. Bandokay & Double Lz)  ,  Dumpa (feat. M24 & Unknown T)
        ### Magic (feat. Bandokay & Double Lz)  ---> [['iLL BLU']]
        ### Dumpa (feat. M24 & Unknown T)  ---> [['iLL BLU']]


        addAllMusic(mdbmaps, "Spotify", "1fa2b8ca2df3351d2b85841fd55258bc", "mn0003674019")   ### [GRM Daily]
        ### Faith In My Killy (feat. Nafe Smallz, Yxng Bane, Blade Brown and Skrapz)  ,  Burning (feat. M Huncho & Dutchavelli)
        ### Faith In My Killy (feat. Nafe Smallz, Yxng Bane, Blade Brown and Skrapz)  ---> [['GRM Daily']]
        ### Burning (feat. M Huncho & Dutchavelli)  ---> [['GRM Daily']]


        addAllMusic(mdbmaps, "Spotify", "131baf3d898edef624286c8d9a122840", "mn0003871593")   ### [S1mba]
        ### Rover (feat. DTG)  ,  Loose (feat. KSI)
        ### Rover (feat. DTG)  ---> [['S1mba']]
        ### Loose (feat. KSI)  ---> [['S1mba']]


        addAllMusic(mdbmaps, "Spotify", "c6481697def4687298cdb5039a85b611", "mn0000682814")   ### [Wiley]
        ### Boasty (feat. Idris Elba)  ,  My One (feat. Tory Lanez, Kranium & Dappy)
        ### Boasty (feat. Idris Elba)  ---> [['Wiley']]
        ### My One (feat. Tory Lanez, Kranium & Dappy)  ---> [['Wiley']]


        addAllMusic(mdbmaps, "Spotify", "053e7f172bd3663a9e28adaddce5e047", "mn0003866043")   ### [AJ]
        ### London (feat. EO)  ,  Bad & Boujie
        ### London (feat. EO)  ---> [['AJ']]
        ### Bad & Boujie  ---> [['AJ']]


        addAllMusic(mdbmaps, "Spotify", "defae11fa424040967297a4c30b73e74", "mn0001528780")   ### [Tana]
        ### Ride & Clutch, Pt. 2
        ### Ride & Clutch, Pt. 2  ---> [['Tana']]


        addAllMusic(mdbmaps, "Spotify", "91952418fd8753818b0acd9a96cde4ff", "mn0003008243")   ### [Loski]
        ### Flavour - feat. Stormzy
        ### Flavour - feat. Stormzy  ---> [['Loski']]


        addAllMusic(mdbmaps, "Spotify", "d7f735673693de240595e768d3d14f4e", "mn0003977082")   ### [Shane Codd]
        ### Get Out My Head
        ### Get Out My Head  ---> [['Shane Codd']]


        addAllMusic(mdbmaps, "Spotify", "1631c2706858f89242e213249919a2b8", "mn0003964565")   ### [Fumez The Engineer]
        ### A92 x Fumez The Engineer - Plugged In Freestyle
        ### A92 x Fumez The Engineer - Plugged In Freestyle  ---> [['Fumez The Engineer']]


        addAllMusic(mdbmaps, "Spotify", "abcad60325d200edaaab4ad5b5c86744", "mn0003984838")   ### [Central Cee]
        ### Loading
        ### Loading  ---> [['Central Cee']]


        addAllMusic(mdbmaps, "Spotify", "0629b1021faba98e8061f06aff65bc99", "mn0002917211")   ### [Wes Nelson]
        ### See Nobody
        ### See Nobody  ---> [['Wes Nelson']]


        addAllMusic(mdbmaps, "Spotify", "82777a3fcdb5e48a348b6715672375ff", "mn0003687507")   ### [Austyn Johnson]
        ### A Million Dreams (Reprise)
        ### A Million Dreams (Reprise)  ---> [['Austyn Johnson']]


        addAllMusic(mdbmaps, "Spotify", "405898df141f105644964b32523115b8", "mn0003912421")   ### [M1llionz]
        ### B1llionz
        ### B1llionz  ---> [['M1llionz']]


        addAllMusic(mdbmaps, "Spotify", "c2294b9cc837be7f77bb9f79bc200854", "mn0003438435")   ### [BANNERS]
        ### Someone To You
        ### Someone To You  ---> [['BANNERS']]


        addAllMusic(mdbmaps, "Spotify", "31b60b7357735a04262a3b9d6407ca91", "mn0003879917")   ### [Meekz]
        ### Like Me
        ### Like Me  ---> [['Meekz']]


        addAllMusic(mdbmaps, "Spotify", "8c5054583e581cd9a24b9a49f12f056e", "mn0003905942")   ### [Imanbek]
        ### I'm Just Feelin' (Du Du Du)
        ### I'm Just Feelin' (Du Du Du)  ---> [['Imanbek']]


        addDiscogs(mdbmaps, "Spotify", "e4c2d7cea0b98481c848980260510946", "193236")    ### [Kano]
        ### Teardrops
        ### Teardrops  ---> [['Bring Me The Horizon', 'Kano']]


        addDiscogs(mdbmaps, "Spotify", "698d6e279f6031c41db95a0cbb5e411e", "8042209")    ### [Niko B]
        ### Who's That What's That
        ### Who's That What's That  ---> [['Niko B']]


        addDiscogs(mdbmaps, "Spotify", "97d7a9f713ebe909109ae05321148ab1", "3388648")    ### [Daði Freyr]
        ### Think About Things
        ### Think About Things  ---> [['Daði Freyr']]


        addAllMusic(mdbmaps, "Spotify", "c33cdbc6fbd897070729820f7971cbc9", "mn0003938222")   ### [Live Lounge Allstars]
        ### Times Like These - BBC Radio 1 Stay Home Live Lounge
        ### Times Like These - BBC Radio 1 Stay Home Live Lounge  ---> [['Live Lounge Allstars']]


        addAllMusic(mdbmaps, "Spotify", "d1aa5e04dec3d807227cc0b65982cb79", "mn0003552272")   ### [K-Trap]
        ### Big Mood
        ### Big Mood  ---> [['K-Trap']]


        addAllMusic(mdbmaps, "Spotify", "7493b31bd17ed97c69773b35f465c638", "mn0003710623")   ### [T MULLA]
        ### Droptop
        ### Droptop  ---> [['T MULLA']]


        addAllMusic(mdbmaps, "Spotify", "5aa86605bc50513a69ce75e49948e085", "mn0003817316")   ### [Lil Pino]
        ### Mya Mills
        ### Mya Mills  ---> [['Lil Pino']]


        addAllMusic(mdbmaps, "Spotify", "ef7245b63b2086a4fb999ef6a0e465e2", "mn0003552079")   ### [Solardo]
        ### XTC
        ### XTC  ---> [['Solardo']]


        addAllMusic(mdbmaps, "Spotify", "2ace910065d30e830222c14e6a4cc9cb", "mn0003823048")   ### [OFB]
        ### OT Boppin
        ### OT Boppin  ---> [['OFB']]        
        

        addAllMusic(mdbmaps, "Spotify", "312b6432b166164d00afb27127304f22", "mn0001426855")   ### [Arcángel]
        ### Infeliz  ,  Sigues Con El - Remix
        ### Infeliz  ---> [['Arcángel']]
        ### Sigues Con El - Remix  ---> [['Arcángel']]


        addAllMusic(mdbmaps, "Spotify", "1ddcf28818af378823ee96fea9b8b57e", "mn0003061063")   ### [ITZY]
        ### WANNABE  ,  Not Shy
        ### WANNABE  ---> [['ITZY']]
        ### Not Shy  ---> [['ITZY']]


        addAllMusic(mdbmaps, "Spotify", "fec8e6cbdec78eab79dc358721312943", "mn0002498091")   ### [Super Yei]
        ### Lean (feat. Towy, Osquel, Beltito & Sammy & Falsetto)
        ### Lean (feat. Towy, Osquel, Beltito & Sammy & Falsetto)  ---> [['Super Yei']]


        addAllMusic(mdbmaps, "Spotify", "28d01893e8e2517c139834a0e4035daa", "mn0003766281")   ### [KHEA]
        ### Ayer Me Llamó Mi Ex (feat. Lenny Santos)
        ### Ayer Me Llamó Mi Ex (feat. Lenny Santos)  ---> [['KHEA']]


        addAllMusic(mdbmaps, "Spotify", "ad747df45c2aa7fcd95b9a77070a1fcc", "mn0003847186")   ### [Jerry Di]
        ### Mi Cuarto
        ### Mi Cuarto  ---> [['Jerry Di']]


        addAllMusic(mdbmaps, "Spotify", "0292e339e0a67aa0c152fd2062d7e4cb", "mn0003438447")   ### [Kofs]
        ### Bande organisée
        ### Bande organisée  ---> [['Kofs', '13 Organisé']]


        addAllMusic(mdbmaps, "Spotify", "4e8f08bc2348ac3fa2ce18e7347ac408", "mn0003658500")   ### [Jonas Esticado]
        ### Investe Em Mim
        ### Investe Em Mim  ---> [['Jonas Esticado']]


        addAllMusic(mdbmaps, "Spotify", "89f18cd59ce4d2a2f7d05ece8daeb3e5", "mn0003895005")   ### [Matuê]
        ### Máquina do Tempo
        ### Máquina do Tempo  ---> [['Matuê']]


        addAllMusic(mdbmaps, "Spotify", "774326914e3c57a1d4eef1d4a1fd54b8", "mw0003442236")   ### [13 Organisé]
        ### Bande organisée
        ### Bande organisée  ---> [['Kofs', '13 Organisé']]


        addAllMusic(mdbmaps, "Spotify", "e4bb88861d1bfb00819acf8a3be333b0", "mn0001532590")   ### [Trueno]
        ### Mamichula - con Nicki Nicole
        ### Mamichula - con Nicki Nicole  ---> [['Trueno']]


        addAllMusic(mdbmaps, "Spotify", "19dc7457492bd975f33600c1f9edfe46", "mn0003853654")   ### [KASIMIR1441]
        ### Ohne Dich
        ### Ohne Dich  ---> [['KASIMIR1441']]


        addAllMusic(mdbmaps, "Spotify", "fd8679f633beb399a4a00e1c7d07eaa3", "mn0003697169")   ### [Masked Wolf]
        ### Astronaut In The Ocean
        ### Astronaut In The Ocean  ---> [['Masked Wolf']]


        addAllMusic(mdbmaps, "Spotify", "4ae4e5641068315b64e4c8fb9356b47a", "mn0003940181")   ### [Erica Banks]
        ### Buss It
        ### Buss It  ---> [['Erica Banks']]


        addAllMusic(mdbmaps, "Spotify", "fd801fec146ef66fde3a9795f759c35f", "mn0003410535")   ### [Macloud]
        ### XXL
        ### XXL  ---> [['Dababy', 'Miksu / Macloud']]


        addAllMusic(mdbmaps, "Spotify", "5722322ead81a33eb1c8e7a41ed615de", "mn0003782793")   ### [Miksu]
        ### XXL
        ### XXL  ---> [['Dababy', 'Miksu / Macloud']]


        addAllMusic(mdbmaps, "Spotify", "10cd304b76e3c4126978c2b975cac44c", "mn0003463011")   ### [twocolors]
        ### Lovefool
        ### Lovefool  ---> [['twocolors']]


        addAllMusic(mdbmaps, "Spotify", "cafe2533b6f738dbbc661795688e0af0", "mn0003925202")   ### [Jay Wheeler]
        ### La Curiosidad
        ### La Curiosidad  ---> [['Jay Wheeler']]


        addAllMusic(mdbmaps, "Spotify", "89a70e8bbafb856731e98f5d0b5045be", "mn0003986185")   ### [Juanfran]
        ### Como Llora
        ### Como Llora  ---> [['Juanfran']]


        addAllMusic(mdbmaps, "Spotify", "f6dd5c457d6da71970a0b9a23084a0fe", "mn0003829095")   ### [Alex Rose]
        ### Jangueo
        ### Jangueo  ---> [['Anuel AA', 'Alex Rose']]


        addAllMusic(mdbmaps, "Spotify", "f73d72613142250e985c096899e2ccbb", "mn0003723186")   ### [Dímelo Flow]
        ### Sigues Con El
        ### Sigues Con El  ---> [['Dímelo Flow']]


        addAllMusic(mdbmaps, "Spotify", "2bfbee0da4a4281bebc8454499bf016c", "mn0003811954")   ### [PEDRO SAMPAIO]
        ### SENTADÃO
        ### SENTADÃO  ---> [['PEDRO SAMPAIO']]


        addAllMusic(mdbmaps, "Spotify", "a5ac2a8caeaf0a668df57a804f607161", "mn0003891767")   ### [Alz X 38]
        ### Change
        ### Change  ---> [['J. Cole', 'nf', 'D-Block Europe', 'Alz X 38']]


        addAllMusic(mdbmaps, "Spotify", "a8d56e2ec054ae69ed725b98f4f786a6", "mn0003363732")   ### [SHIRIN DAVID]
        ### 90-60-111
        ### 90-60-111  ---> [['SHIRIN DAVID']]


        addAllMusic(mdbmaps, "Spotify", "1e7d35868cc54e2ac217a5f0e251d991", "mn0003897348")   ### [Pashanim]
        ### Airwaves
        ### Airwaves  ---> [['Pashanim']]


        addAllMusic(mdbmaps, "Spotify", "6f15fe59e3fb47ad5f1b55f148b51134", "mn0003493826")   ### [AK AUSSERKONTROLLE]
        ### In meinem Benz
        ### In meinem Benz  ---> [['AK AUSSERKONTROLLE']]


        addAllMusic(mdbmaps, "Spotify", "eebf5a3d51f7dc6e2714fd0185fc9d65", "mn0000853061")   ### [KALIM]
        ### SKRR
        ### SKRR  ---> [['KALIM']]


        addAllMusic(mdbmaps, "Spotify", "5953876340ac213d6dd15ee1f2798915", "mn0004006085")   ### [Harry Nach]
        ### Tak Tiki Tak
        ### Tak Tiki Tak  ---> [['Harry Nach']]


        addDiscogs(mdbmaps, "Spotify", "d577d056cc54afb1c28af43e1d4cd973", "2456567")    ### [Conkarah]
        ### Banana (feat. Shaggy) - DJ FLe - Minisiren Remix
        ### Banana (feat. Shaggy) - DJ FLe - Minisiren Remix  ---> [['Conkarah']]


        addAllMusic(mdbmaps, "Spotify", "678d99ad93cd3df65d2a5a3f0e4a7597", "mn0003980128")   ### [Niack]
        ### Na Raba Toma Tapão  ,  Oh Juliana
        ### Na Raba Toma Tapão  ---> [['Niack']]
        ### Oh Juliana  ---> [['Niack']]


        addAllMusic(mdbmaps, "Spotify", "e626427a6f002107c2cb619aaefdccbb", "mn0000032881")   ### [Shiv]
        ### Auto Blu
        ### Auto Blu  ---> [['Shiv']]


        addAllMusic(mdbmaps, "Spotify", "7f03a659bed08ab2da7f1e76ee783bd2", "mn0002057608")   ### [Bosh]
        ### Djomb - Bien ou quoi
        ### Djomb - Bien ou quoi  ---> [['Bosh']]


        addDiscogs(mdbmaps, "Spotify", "ece9beb19448a79c8ac0c3800402c9c3", "1216736")    ### [Shablo]
        ### M' Manc (con Geolier & Sfera Ebbasta)
        ### M' Manc (con Geolier & Sfera Ebbasta)  ---> [['Shablo']]


        addDiscogs(mdbmaps, "Spotify", "fabb0fd80f0e22bc95798a9c0c468237", "8633514")    ### [Boza]
        ### Hecha Pa' Mi
        ### Hecha Pa' Mi  ---> [['Boza']]        


        addAllMusic(mdbmaps, "Spotify", "7c710dee81ac023efb1889ec191f5356", 'mn0000663567')   ### [Node]
        ### Pakker Bar  ,  Zebah (feat. Gilli)  ,  De Snakker  ,  Blæst  ,  Al Fuego  ,  Gi Mig Det Hele  ,  Indifférent (feat. Sivas)  ,  JVB  ,  Carnalismo (feat. Gilli & Branco)  ,  For Mig Selv (feat. Gilli)  ,  Demawa  ,  Habibi  ,  Didi (feat. Hkeem & Lamix)  ,  Cambiarme  ,  Mariah  ,  Opa  ,  No Romantico (feat. si_el_bien)  ,  Skub Det Ud  ,  Diana  ,  Vil Du - Recorded At Spotify Studios Stockholm  ,  Super Mario  ,  Samme Vej  ,  Ra Ta Ta Ta (feat. Stepz)  ,  Mafiosa  ,  Limbo (feat. Gilli)  ,  Bilen Skrider (feat. Orgi-E)  ,  Avatar  ,  Pull Up  ,  Klasse 1
        ### Pakker Bar  ---> [['Node']]
        ### Zebah (feat. Gilli)  ---> [['Node']]
        ### De Snakker  ---> [['Node']]
        ### Blæst  ---> [['Node']]
        ### Al Fuego  ---> [['Node']]
        ### Gi Mig Det Hele  ---> [['Node']]
        ### Indifférent (feat. Sivas)  ---> [['Node']]
        ### JVB  ---> [['Node']]
        ### Carnalismo (feat. Gilli & Branco)  ---> [['Node']]
        ### For Mig Selv (feat. Gilli)  ---> [['Node']]
        ### Demawa  ---> [['Node']]
        ### Habibi  ---> [['Node']]
        ### Didi (feat. Hkeem & Lamix)  ---> [['Node']]
        ### Cambiarme  ---> [['Node']]
        ### Mariah  ---> [['Node']]
        ### Opa  ---> [['Node']]
        ### No Romantico (feat. si_el_bien)  ---> [['Node']]
        ### Skub Det Ud  ---> [['Node']]
        ### Diana  ---> [['Node']]
        ### Vil Du - Recorded At Spotify Studios Stockholm  ---> [['Node']]
        ### Super Mario  ---> [['Node']]
        ### Samme Vej  ---> [['Node', 'Beko', 'Karl William']]
        ### Ra Ta Ta Ta (feat. Stepz)  ---> [['Node']]
        ### Mafiosa  ---> [['Node']]
        ### Limbo (feat. Gilli)  ---> [['Node']]
        ### Bilen Skrider (feat. Orgi-E)  ---> [['Node']]
        ### Avatar  ---> [['Node']]
        ### Pull Up  ---> [['Node']]
        ### Klasse 1  ---> [['Node']]


        addAllMusic(mdbmaps, "Spotify", "1e669cf2d7b18eda3926730c090c878b", "mn0003886957")   ### [Kabza De Small]
        ### Umshove  ,  Nana Thula  ,  Alalahi  ,  Qoqoqo  ,  Lorch  ,  Abuyile Amakhosi  ,  Sandton  ,  Indaba Ka Bani  ,  Phoyisa - Live  ,  eMcimbini - Live  ,  Hello - Live  ,  Sponono  ,  Buyile  ,  Ilog Drum  ,  Nia Lo  ,  Sthandwa  ,  Masupa  ,  Thinking About You  ,  Why Ngikufela  ,  Wena  ,  Need You Tonight  ,  Duze  ,  Qula  ,  Ipiano  ,  Impilo  ,  Ndofaya  ,  eMcimbini
        ### Umshove  ---> [['Kabza De Small']]
        ### Nana Thula  ---> [['Kabza De Small']]
        ### Alalahi  ---> [['Kabza De Small']]
        ### Qoqoqo  ---> [['Kabza De Small']]
        ### Lorch  ---> [['Kabza De Small']]
        ### Abuyile Amakhosi  ---> [['Kabza De Small']]
        ### Sandton  ---> [['Kabza De Small']]
        ### Indaba Ka Bani  ---> [['Kabza De Small']]
        ### Phoyisa - Live  ---> [['Kabza De Small']]
        ### eMcimbini - Live  ---> [['Kabza De Small']]
        ### Hello - Live  ---> [['Kabza De Small']]
        ### Sponono  ---> [['Kabza De Small']]
        ### Buyile  ---> [['Kabza De Small']]
        ### Ilog Drum  ---> [['Kabza De Small']]
        ### Nia Lo  ---> [['Kabza De Small']]
        ### Sthandwa  ---> [['Kabza De Small']]
        ### Masupa  ---> [['Kabza De Small']]
        ### Thinking About You  ---> [['Kabza De Small']]
        ### Why Ngikufela  ---> [['Kabza De Small']]
        ### Wena  ---> [['Kabza De Small']]
        ### Need You Tonight  ---> [['Kabza De Small']]
        ### Duze  ---> [['Kabza De Small']]
        ### Qula  ---> [['Kabza De Small']]
        ### Ipiano  ---> [['Kabza De Small']]
        ### Impilo  ---> [['Kabza De Small']]
        ### Ndofaya  ---> [['Kabza De Small']]
        ### eMcimbini  ---> [['Kabza De Small']]


        addAllMusic(mdbmaps, "Spotify", "2bea51b6d21f1b764984d19fff498990", "mn0003712369")   ### [Artigeardit]
        ### Joggingsæt  ,  Airbag  ,  Lov Mig 1 Ting  ,  Gothersgade  ,  Idiot (feat. Karl William)  ,  Søvne  ,  Bagsæde  ,  Aquafina (feat. Lord Siva)  ,  Grønkjær  ,  Bankråd  ,  Kom Af Sig Selv  ,  Intro  ,  La' Den Ringe  ,  #%_! Dig Selv  ,  Beslutninger  ,  Check (feat. Christos)  ,  Følelsen  ,  Stensikker  ,  Den Værste  ,  I Nat (Artigeardit X Medina)  ,  BABY  ,  ELVIS (feat. Carmon)
        ### Joggingsæt  ---> [['Artigeardit']]
        ### Airbag  ---> [['Artigeardit']]
        ### Lov Mig 1 Ting  ---> [['Artigeardit']]
        ### Gothersgade  ---> [['Artigeardit']]
        ### Idiot (feat. Karl William)  ---> [['Artigeardit']]
        ### Søvne  ---> [['Artigeardit']]
        ### Bagsæde  ---> [['Artigeardit']]
        ### Aquafina (feat. Lord Siva)  ---> [['Artigeardit']]
        ### Grønkjær  ---> [['Artigeardit']]
        ### Bankråd  ---> [['Artigeardit']]
        ### Kom Af Sig Selv  ---> [['Artigeardit']]
        ### Intro  ---> [['Big Sean', 'J. Cole', '21 Savage', 'Meek Mill', 'Khalid', 'Quality Control', 'Artigeardit', 'D-Block Europe', 'Skepta', 'Nines']]
        ### La' Den Ringe  ---> [['Artigeardit']]
        ### #%_! Dig Selv  ---> [['Artigeardit']]
        ### Beslutninger  ---> [['Artigeardit']]
        ### Check (feat. Christos)  ---> [['Artigeardit']]
        ### Følelsen  ---> [['KESI', 'Artigeardit']]
        ### Stensikker  ---> [['Artigeardit']]
        ### Den Værste  ---> [['Artigeardit']]
        ### I Nat (Artigeardit X Medina)  ---> [['Artigeardit']]
        ### BABY  ---> [['Artigeardit', 'Giggs']]
        ### ELVIS (feat. Carmon)  ---> [['Artigeardit']]


        addDeezer(mdbmaps, "Spotify", "d4bf59b77bfc801f3c084f61320e2997", "1210215")
        ### Solskin  ,  Way Way  ,  Ca Ca  ,  Zum Zum  ,  Drama (feat. Sivas)  ,  Desert Eagle  ,  Bang Bang (feat. NODE)  ,  La La  ,  Ligeglad  ,  Rosa  ,  Is  ,  Mama  ,  Vito  ,  Bombay  ,  Glemmer Aldrig - Recorded At Spotify Studios Stockholm  ,  Udsigt  ,  Po Po  ,  Solskin 2.0  ,  Vi Ku  ,  Skyline  ,  Lacazette
        ### Solskin  ---> [['ZK']]
        ### Way Way  ---> [['ZK']]
        ### Ca Ca  ---> [['ZK']]
        ### Zum Zum  ---> [['ZK']]
        ### Drama (feat. Sivas)  ---> [['ZK']]
        ### Desert Eagle  ---> [['ZK']]
        ### Bang Bang (feat. NODE)  ---> [['ZK']]
        ### La La  ---> [['ZK']]
        ### Ligeglad  ---> [['ZK']]
        ### Rosa  ---> [['ZK']]
        ### Is  ---> [['ZK']]
        ### Mama  ---> [['Jonas Blue', 'ZK', 'Boohle']]
        ### Vito  ---> [['ZK']]
        ### Bombay  ---> [['ZK']]
        ### Glemmer Aldrig - Recorded At Spotify Studios Stockholm  ---> [['ZK']]
        ### Udsigt  ---> [['ZK']]
        ### Po Po  ---> [['ZK']]
        ### Solskin 2.0  ---> [['ZK']]
        ### Vi Ku  ---> [['ZK']]
        ### Skyline  ---> [['ZK']]
        ### Lacazette  ---> [['ZK']]


        addAllMusic(mdbmaps, "Spotify", "73024e0286fba7b566a8a2598620a0b0", "mn0003085199")   ### [ATYPISK]
        ### Vi En  ,  1919  ,  Pengeseddel (feat. Branco)  ,  Varme Tider  ,  Sammen Er Vi (feat. Kaka)  ,  Chopper Tale (feat. Branco & Gilli)  ,  Øjne På Mig  ,  Så På  ,  Aldrig For Sjov (feat. Branco & Gilli)  ,  Øje For Øje (feat. Branco)  ,  Tillid  ,  Hurtig Bane  ,  Fri Fod  ,  Tørstig  ,  Plata O Plomo  ,  Kærlighed (feat. Gilli & Kesi)  ,  Lærte Hende Alt (feat. Lærke Emilie)  ,  Fra Gaden (feat. Benny Jamz)  ,  Risiko (feat. Branco)  ,  Fra Start
        ### Vi En  ---> [['ATYPISK']]
        ### 1919  ---> [['ATYPISK']]
        ### Pengeseddel (feat. Branco)  ---> [['ATYPISK']]
        ### Varme Tider  ---> [['ATYPISK']]
        ### Sammen Er Vi (feat. Kaka)  ---> [['ATYPISK']]
        ### Chopper Tale (feat. Branco & Gilli)  ---> [['ATYPISK']]
        ### Øjne På Mig  ---> [['ATYPISK']]
        ### Så På  ---> [['ATYPISK']]
        ### Aldrig For Sjov (feat. Branco & Gilli)  ---> [['ATYPISK']]
        ### Øje For Øje (feat. Branco)  ---> [['ATYPISK']]
        ### Tillid  ---> [['ATYPISK']]
        ### Hurtig Bane  ---> [['ATYPISK']]
        ### Fri Fod  ---> [['ATYPISK']]
        ### Tørstig  ---> [['ATYPISK']]
        ### Plata O Plomo  ---> [['ATYPISK']]
        ### Kærlighed (feat. Gilli & Kesi)  ---> [['ATYPISK']]
        ### Lærte Hende Alt (feat. Lærke Emilie)  ---> [['ATYPISK']]
        ### Fra Gaden (feat. Benny Jamz)  ---> [['ATYPISK']]
        ### Risiko (feat. Branco)  ---> [['ATYPISK']]
        ### Fra Start  ---> [['ATYPISK']]
        []

        addAllMusic(mdbmaps, "Spotify", "239657d6dcb352033cd0ef60407f6118", "mn0000026044")   ### [Stepz]
        ### Cinco De Mayo  ,  Endnu (feat. Gilli, Benny Jamz & Branco)  ,  Samurai (feat. Sivas)  ,  Panorama  ,  BeBe  ,  5 End 100  ,  Terminal 3  ,  Rute 141  ,  Cara Mia (feat. Sivas & KESI)  ,  Dobbel Op  ,  Ny Dag  ,  Guap  ,  Moncler  ,  Nix Normal  ,  Cullinan  ,  Replay
        ### Cinco De Mayo  ---> [['Stepz']]
        ### Endnu (feat. Gilli, Benny Jamz & Branco)  ---> [['Stepz']]
        ### Samurai (feat. Sivas)  ---> [['Stepz']]
        ### Panorama  ---> [['Stepz']]
        ### BeBe  ---> [['Stepz']]
        ### 5 End 100  ---> [['Stepz']]
        ### Terminal 3  ---> [['Stepz']]
        ### Rute 141  ---> [['Stepz']]
        ### Cara Mia (feat. Sivas & KESI)  ---> [['Stepz']]
        ### Dobbel Op  ---> [['Stepz']]
        ### Ny Dag  ---> [['Stepz']]
        ### Guap  ---> [['Stepz']]
        ### Moncler  ---> [['Stepz']]
        ### Nix Normal  ---> [['Stepz']]
        ### Cullinan  ---> [['Stepz']]
        ### Replay  ---> [['Lady Gaga', 'Stepz', 'Iyaz']]


        addDeezer(mdbmaps, "Spotify", "906b827d308e78d95b238caa87f95cce", "1239800")    ### [Molo]
        ### Nu (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  Udenfor (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  Bølgen (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  Skejsen (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  Dedikeret (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  Stilen Lagt (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  Fryse (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  Udsigt (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  Ik Sådan Nogen (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  Formidable (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  Safari (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ,  LIV$TIL (feat. Benny Jamz, Gilli & MellemFingaMuzik)
        ### Nu (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### Udenfor (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### Bølgen (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### Skejsen (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### Dedikeret (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### Stilen Lagt (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### Fryse (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### Udsigt (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### Ik Sådan Nogen (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### Formidable (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### Safari (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]
        ### LIV$TIL (feat. Benny Jamz, Gilli & MellemFingaMuzik)  ---> [['Molo']]


        addDeezer(mdbmaps, "Spotify", "9e511416cd94110a0daca4e09c3c717b", "869166")    ### [RH]
        ### Fremtiden  ,  Min Vej (feat. Gio)  ,  For Sent  ,  Epidemi  ,  Gimade (feat. AMRO)  ,  Fidélité  ,  Plan B  ,  Mata Le (feat. Jamaika)  ,  Mon Ami  ,  Klovne  ,  600 Heste  ,  Bedøvende
        ### Fremtiden  ---> [['RH']]
        ### Min Vej (feat. Gio)  ---> [['RH']]
        ### For Sent  ---> [['RH']]
        ### Epidemi  ---> [['RH']]
        ### Gimade (feat. AMRO)  ---> [['RH']]
        ### Fidélité  ---> [['RH']]
        ### Plan B  ---> [['RH']]
        ### Mata Le (feat. Jamaika)  ---> [['RH']]
        ### Mon Ami  ---> [['RH', 'Samra']]
        ### Klovne  ---> [['RH']]
        ### 600 Heste  ---> [['RH']]
        ### Bedøvende  ---> [['RH']]


        addDeezer(mdbmaps, "Spotify", "6cb8136331a0bbd6afacc58667196267", "6339")    ### [Omar]
        ### Bar Sig Til (feat. Artigeardit)  ,  Samme Sprog  ,  Ik Noget Nyt  ,  Walalkey  ,  Bedre Dage (feat. PAY)  ,  Ka Du Ik  ,  Ligemeget (feat. Fouli)  ,  Dem  ,  Slanger (feat. PAY)  ,  Psycho (feat. Artigeardit)  ,  Fokuseret
        ### Bar Sig Til (feat. Artigeardit)  ---> [['Omar']]
        ### Samme Sprog  ---> [['Omar']]
        ### Ik Noget Nyt  ---> [['Omar']]
        ### Walalkey  ---> [['Omar']]
        ### Bedre Dage (feat. PAY)  ---> [['Omar']]
        ### Ka Du Ik  ---> [['Omar']]
        ### Ligemeget (feat. Fouli)  ---> [['Omar']]
        ### Dem  ---> [['Omar']]
        ### Slanger (feat. PAY)  ---> [['Omar']]
        ### Psycho (feat. Artigeardit)  ---> [['Omar']]
        ### Fokuseret  ---> [['Omar']]


        addDeezer(mdbmaps, "Spotify", "2e533e87b92707c70235004d2fabb6c5", "351626")    ### [AMAL]
        ### 1 DOLLAR & 1 DRØM  ,  IK BAR HÆNGE  ,  MARIJA  ,  KLIK KLIK KLIK  ,  NÅR DU DØR  ,  LØBER LÆNGDEN  ,  SOM DU SMILER  ,  J'AI MAL  ,  VEAF  ,  ASKIM BENIM
        ### 1 DOLLAR & 1 DRØM  ---> [['AMAL']]
        ### IK BAR HÆNGE  ---> [['AMAL']]
        ### MARIJA  ---> [['AMAL']]
        ### KLIK KLIK KLIK  ---> [['AMAL']]
        ### NÅR DU DØR  ---> [['AMAL']]
        ### LØBER LÆNGDEN  ---> [['AMAL']]
        ### SOM DU SMILER  ---> [['AMAL']]
        ### J'AI MAL  ---> [['AMAL']]
        ### VEAF  ---> [['AMAL']]
        ### ASKIM BENIM  ---> [['AMAL']]


        addDeezer(mdbmaps, "Spotify", "3efe48be47f55609586d2b4a291d4ee4", "1204851")    ### [Volkan]
        ### Flyva  ,  Arrivederci  ,  For Længe (feat. RH)  ,  Stille & Rolex  ,  Voldsomt  ,  Khouya  ,  Fem  ,  Muy Frio (feat. RH)  ,  Alperne
        ### Flyva  ---> [['Volkan']]
        ### Arrivederci  ---> [['Volkan']]
        ### For Længe (feat. RH)  ---> [['Volkan']]
        ### Stille & Rolex  ---> [['Volkan']]
        ### Voldsomt  ---> [['Volkan']]
        ### Khouya  ---> [['Volkan']]
        ### Fem  ---> [['Volkan']]
        ### Muy Frio (feat. RH)  ---> [['Volkan']]
        ### Alperne  ---> [['Volkan']]


        addAllMusic(mdbmaps, "Spotify", "760802628f4a15ed4591c24ec5b1e073", "mn0003736648")   ### [Clara]
        ### What They Say  ,  Suffocating  ,  Foolish  ,  Crazy  ,  Legend  ,  Thank Me Later  ,  Nobody's Lover (feat. Lord Siva)  ,  Girl Like You
        ### What They Say  ---> [['Clara']]
        ### Suffocating  ---> [['Clara']]
        ### Foolish  ---> [['Clara']]
        ### Crazy  ---> [['Lil Pump', 'Clara', 'Lost Frequencies']]
        ### Legend  ---> [['Twenty One Pilots', 'Clara']]
        ### Thank Me Later  ---> [['Clara']]
        ### Nobody's Lover (feat. Lord Siva)  ---> [['Clara']]
        ### Girl Like You  ---> [['Clara']]


        addDeezer(mdbmaps, "Spotify", "ae7b222d2107022421a0ea24cbb5ffcb", "60752")    ### [Blak]
        ### Ik' Min Skyld  ,  Nede Mette  ,  Slem Igen (feat. Ceci Luca) - Hedegaard Remix  ,  Banken  ,  Skyldig  ,  Hele Dagen  ,  11 År  ,  Gerningssted
        ### Ik' Min Skyld  ---> [['Blak']]
        ### Nede Mette  ---> [['Blak']]
        ### Slem Igen (feat. Ceci Luca) - Hedegaard Remix  ---> [['Blak']]
        ### Banken  ---> [['Blak']]
        ### Skyldig  ---> [['Blak']]
        ### Hele Dagen  ---> [['Blak']]
        ### 11 År  ---> [['Blak']]
        ### Gerningssted  ---> [['Blak']]


        addAllMusic(mdbmaps, "Spotify", "885135a7c04f86cdfb519e2cd6855e1c", "mn0003572540")   ### [Noah Carter]
        ### Do You  ,  Come Alive  ,  No Favors / 5000  ,  Smoothies  ,  Search  ,  Gary Payton  ,  Top Shelf
        ### Do You  ---> [['Noah Carter']]
        ### Come Alive  ---> [['Hugh Jackman', 'Noah Carter']]
        ### No Favors / 5000  ---> [['Noah Carter']]
        ### Smoothies  ---> [['Noah Carter']]
        ### Search  ---> [['Noah Carter']]
        ### Gary Payton  ---> [['Noah Carter']]
        ### Top Shelf  ---> [['Noah Carter']]


        addDeezer(mdbmaps, "Spotify", "331732a22d5edd349e097d4a3c0466f4", "5925837")    ### [Gobs]
        ### Startede Sammen  ,  Drømte  ,  Savnet  ,  Señorita (feat. Fouli)  ,  Kbh Til LA  ,  Rejsen  ,  Champagne
        ### Startede Sammen  ---> [['Gobs']]
        ### Drømte  ---> [['Gobs']]
        ### Savnet  ---> [['Gobs']]
        ### Señorita (feat. Fouli)  ---> [['Gobs']]
        ### Kbh Til LA  ---> [['Gobs']]
        ### Rejsen  ---> [['Gobs']]
        ### Champagne  ---> [['Gobs']]


        addDeezer(mdbmaps, "Spotify", "0168fb5b812f2e94aa3e479b377006f3", "13839133")    ### [Milbo]
        ### Heldig  ,  Elsker Når Hun Danser  ,  Altid På  ,  Populær (feat. Skinz)  ,  25 timer  ,  Aldrig Aldrig  ,  Ride Or Die (feat. MAS)
        ### Heldig  ---> [['Milbo']]
        ### Elsker Når Hun Danser  ---> [['Milbo']]
        ### Altid På  ---> [['Milbo']]
        ### Populær (feat. Skinz)  ---> [['Milbo']]
        ### 25 timer  ---> [['Milbo']]
        ### Aldrig Aldrig  ---> [['Milbo']]
        ### Ride Or Die (feat. MAS)  ---> [['Milbo']]


        addDeezer(mdbmaps, "Spotify", "aaeecd720212db31efbece05993c5819", "11474064")    ### [Gigis]
        ### Gertrud  ,  Flæk  ,  Brobizz  ,  Salaam  ,  Urørlig  ,  Lytter Ik
        ### Gertrud  ---> [['Gigis']]
        ### Flæk  ---> [['Gigis']]
        ### Brobizz  ---> [['Gigis']]
        ### Salaam  ---> [['Gigis', 'Krept & Konan']]
        ### Urørlig  ---> [['Gigis']]
        ### Lytter Ik  ---> [['Gigis']]


        addAllMusic(mdbmaps, "Spotify", "65bdaa203d0f2e03e6aee6bcd28e4ade", "mn0003564552")   ### [DJ Maphorisa]
        ### Midnight Starring (feat. DJ Tira, Busiswa & Moonchild Sanelly)  ,  iWalk Ye Phara (feat. Moonchild Sanelly, K.O & Zulu Mkhathini)  ,  Amantombazane  ,  Vula Vala  ,  Koko  ,  iThemba'lam
        ### Midnight Starring (feat. DJ Tira, Busiswa & Moonchild Sanelly)  ---> [['DJ Maphorisa']]
        ### iWalk Ye Phara (feat. Moonchild Sanelly, K.O & Zulu Mkhathini)  ---> [['DJ Maphorisa']]
        ### Amantombazane  ---> [['DJ Maphorisa']]
        ### Vula Vala  ---> [['DJ Maphorisa']]
        ### Koko  ---> [['DJ Maphorisa']]
        ### iThemba'lam  ---> [['DJ Maphorisa']]


        addAllMusic(mdbmaps, "Spotify", "1b23786eb12e2cd293ae6152b1d0957a", "mn0003093833")   ### [Samthing Soweto]
        ### Akulaleki  ,  AmaDM  ,  Omama Bomthandazo  ,  Sebenzela nina  ,  Lotto  ,  Weekend
        ### Akulaleki  ---> [['Samthing Soweto']]
        ### AmaDM  ---> [['Samthing Soweto']]
        ### Omama Bomthandazo  ---> [['Samthing Soweto']]
        ### Sebenzela nina  ---> [['Samthing Soweto']]
        ### Lotto  ---> [['Samthing Soweto']]
        ### Weekend  ---> [['Joey Moe', 'Samthing Soweto']]


        addDeezer(mdbmaps, "Spotify", "acdce78b99d3f53d2291fdcf105095eb", "62884")    ### [AKA]
        ### StarSigns  ,  Beyonce  ,  Amen  ,  Fela in Versace  ,  Fela In Versace  ,  Jika
        ### StarSigns  ---> [['AKA']]
        ### Beyonce  ---> [['AKA']]
        ### Amen  ---> [['AKA']]
        ### Fela in Versace  ---> [['AKA']]
        ### Fela In Versace  ---> [['AKA']]
        ### Jika  ---> [['AKA']]


        addAllMusic(mdbmaps, "Spotify", "8ce1a3375a87fcc6c1f2e003309b4be5", "mn0003882785")   ### [Josef Og Elias]
        ### Shorty Ringer  ,  Brandvarm  ,  Weekend Hver Dag  ,  Min Bror (Josef Og Elias X ICEKIID)  ,  King Kong
        ### Shorty Ringer  ---> [['Josef Og Elias']]
        ### Brandvarm  ---> [['Josef Og Elias']]
        ### Weekend Hver Dag  ---> [['Josef Og Elias']]
        ### Min Bror (Josef Og Elias X ICEKIID)  ---> [['Josef Og Elias']]
        ### King Kong  ---> [['Josef Og Elias']]


        addAllMusic(mdbmaps, "Spotify", "ada00995d67c9beda7a36282e7347bcd", "mn0002006338")   ### [Black Coffee]
        ### Drive (feat. Delilah Montagu) - Edit  ,  LaLaLa  ,  SBCNCSLY  ,  Ready For You  ,  You Need Me
        ### Drive (feat. Delilah Montagu) - Edit  ---> [['Black Coffee']]
        ### LaLaLa  ---> [['Black Coffee']]
        ### SBCNCSLY  ---> [['Black Coffee']]
        ### Ready For You  ---> [['Black Coffee']]
        ### You Need Me  ---> [['Black Coffee']]


        addDeezer(mdbmaps, "Spotify", "d8aa0eef0707f16dde1ed5d8dc4e88fc", "270477")    ### [FOOL]
        ### Outcast  ,  Strapped  ,  Worry  ,  WDWGFH  ,  Kids
        ### Outcast  ---> [['FOOL']]
        ### Strapped  ---> [['FOOL']]
        ### Worry  ---> [['FOOL']]
        ### WDWGFH  ---> [['FOOL']]
        ### Kids  ---> [['FOOL']]


        addDeezer(mdbmaps, "Spotify", "0b06b30f3d7f755031dd7b08ee89145a", "76314052")   ### [Elaine]
        ### You're the One  ,  Risky  ,  I Just Wanna Know  ,  Changes  ,  I/You
        ### You're the One  ---> [['Elaine']]
        ### Risky  ---> [['Elaine']]
        ### I Just Wanna Know  ---> [['Elaine']]
        ### Changes  ---> [['Justin Bieber', 'A$AP Rocky', 'Elaine']]
        ### I/You  ---> [['Elaine']]


        addAllMusic(mdbmaps, "Spotify", "4f86336aacb0cbca1557001e9a1d9512", "mn0003285383")   ### [Cassper Nyovest]
        ### Gets Getsa 2.0  ,  Who Got The Block Hot?  ,  Gets Getsa  ,  Good For That  ,  To Whom it May Concern
        ### Gets Getsa 2.0  ---> [['Cassper Nyovest']]
        ### Who Got The Block Hot?  ---> [['Cassper Nyovest']]
        ### Gets Getsa  ---> [['Cassper Nyovest']]
        ### Good For That  ---> [['Cassper Nyovest']]
        ### To Whom it May Concern  ---> [['Cassper Nyovest']]


        addAllMusic(mdbmaps, "Spotify", "f12418f0b4888d8f49e4e7edaa8f7d13", "mn0003690636")   ### [Sun-El Musician]
        ### Bamthathile  ,  Ntaba ezikude  ,  Into Ingawe  ,  Ubomi Abumanga  ,  Garden
        ### Bamthathile  ---> [['Sun-El Musician']]
        ### Ntaba ezikude  ---> [['Sun-El Musician']]
        ### Into Ingawe  ---> [['Sun-El Musician']]
        ### Ubomi Abumanga  ---> [['Sun-El Musician']]
        ### Garden  ---> [['Sun-El Musician']]


        addAllMusic(mdbmaps, "Spotify", "ba4b654bf11b352faddd68b28c201783", "mn0003430531")   ### [Prince Kaybee]
        ### Club Controller  ,  Banomoya  ,  Fetch Your Life - Edit  ,  Gugulethu
        ### Club Controller  ---> [['Prince Kaybee']]
        ### Banomoya  ---> [['Prince Kaybee']]
        ### Fetch Your Life - Edit  ---> [['Prince Kaybee']]
        ### Gugulethu  ---> [['Prince Kaybee']]


        addAllMusic(mdbmaps, "Spotify", "8d6d671b3986ebe40558f03775f2c183", "mn0003775611")   ### [Mlindo The Vocalist]
        ### AmaBlesser (feat. DJ Maphorisa)  ,  Egoli (feat. Sjava)  ,  Macala (Radio Version) (feat. Sfeesoh, Kwesta & Thabsie)  ,  Usbahle
        ### AmaBlesser (feat. DJ Maphorisa)  ---> [['Mlindo The Vocalist']]
        ### Egoli (feat. Sjava)  ---> [['Mlindo The Vocalist']]
        ### Macala (Radio Version) (feat. Sfeesoh, Kwesta & Thabsie)  ---> [['Mlindo The Vocalist']]
        ### Usbahle  ---> [['Mlindo The Vocalist']]


        addAllMusic(mdbmaps, "Spotify", "15de7a244cb4ca23613f6d5dab2f0291", "mn0003873360")   ### [Shooter Gang]
        ### Mask På  ,  Sinaloa Stil  ,  Click  ,  Pokerface
        ### Mask På  ---> [['Shooter Gang']]
        ### Sinaloa Stil  ---> [['Shooter Gang']]
        ### Click  ---> [['Shooter Gang']]
        ### Pokerface  ---> [['Shooter Gang']]


        addAllMusic(mdbmaps, "Spotify", "6be6bd47ef1cedc7b02c57bcc9efd799", "mn0003886123")   ### [I$WAAL]
        ### STANDARD  ,  WHIP WHOP  ,  ZERO  ,  BAD BITCH (feat. Jimilian)
        ### STANDARD  ---> [['I$WAAL']]
        ### WHIP WHOP  ---> [['I$WAAL']]
        ### ZERO  ---> [['I$WAAL']]
        ### BAD BITCH (feat. Jimilian)  ---> [['I$WAAL']]


        addAllMusic(mdbmaps, "Spotify", "2ae55bdaf0ae8926d6728d5c6062cdb2", "mn0003618222")   ### [BasedBoys]
        ### Gizpræsidenter  ,  Ingen Bekymringer  ,  Det' så svært  ,  Min Aften
        ### Gizpræsidenter  ---> [['BasedBoys']]
        ### Ingen Bekymringer  ---> [['BasedBoys']]
        ### Det' så svært  ---> [['BasedBoys']]
        ### Min Aften  ---> [['BasedBoys']]


        addDeezer(mdbmaps, "Spotify", "177f5ea67ca05c0c3ba7e860d46e90ce", "75490692")    ### [Jung]
        ### Blitz, Baby  ,  Hun Kommer Tilbage  ,  Jeg Skal Nok Vente
        ### Blitz, Baby  ---> [['Jung']]
        ### Hun Kommer Tilbage  ---> [['Jung']]
        ### Jeg Skal Nok Vente  ---> [['Jung']]


        addAllMusic(mdbmaps, "Spotify", "b6e19b38494fb84735a7125adbaf9aab", "mn0004002963")   ### [Mr JazziQ]
        ### Vsop  ,  Ulazi  ,  Monate
        ### Vsop  ---> [['Mr JazziQ']]
        ### Ulazi  ---> [['Mr JazziQ']]
        ### Monate  ---> [['Mr JazziQ']]


        addAllMusic(mdbmaps, "Spotify", "0512f8eb5527c38e59c91152ce2d28c3", "mn0003725991")   ### [Marco Rahim]
        ### Drop Top Porsche  ,  Fættermand (feat. AMRO)  ,  Skakmat (feat. Stepz)
        ### Drop Top Porsche  ---> [['Marco Rahim']]
        ### Fættermand (feat. AMRO)  ---> [['Marco Rahim']]
        ### Skakmat (feat. Stepz)  ---> [['Marco Rahim']]


        addDeezer(mdbmaps, "Spotify", "8a86cade8484c8006cf0608a042c3023", "2055001")    ### [NAVID]
        ### Rum Bum Bum  ,  Chin Chan Chun  ,  Rum Bum Bum - Hedegaard Remix
        ### Rum Bum Bum  ---> [['NAVID']]
        ### Chin Chan Chun  ---> [['NAVID']]
        ### Rum Bum Bum - Hedegaard Remix  ---> [['NAVID']]


        addAllMusic(mdbmaps, "Spotify", "cd2a4480cfa17155df3047df24fdb0c0", "mn0003873183")   ### [Focalistic]
        ### Ke Star  ,  Onoroko  ,  Ke Star (feat. Vigro Deep)
        ### Ke Star  ---> [['Focalistic']]
        ### Onoroko  ---> [['Focalistic']]
        ### Ke Star (feat. Vigro Deep)  ---> [['Focalistic']]


        addDeezer(mdbmaps, "Spotify", "1066ab13e5f08f597d6b784c4e1ce971", "1765231")    ### [Beko]
        ### Ayo  ,  Azizam  ,  Samme Vej
        ### Ayo  ---> [['Beko']]
        ### Azizam  ---> [['Beko']]
        ### Samme Vej  ---> [['Node', 'Beko', 'Karl William']]


        addAllMusic(mdbmaps, "Spotify", "848fb1581db341bc3f6dd2ed9a9b7f99", "mn0003885968")   ### [Xabski]
        ### Ludo  ,  Energi  ,  Svømning
        ### Ludo  ---> [['Xabski']]
        ### Energi  ---> [['Xabski']]
        ### Svømning  ---> [['Xabski']]


        addAllMusic(mdbmaps, "Spotify", "169e695f7abad47a6bc7f036835d0830", "mn0003629959")   ### [Blaq Diamond]
        ### Ibhanoyi  ,  Love Letter  ,  Summeryomuthi
        ### Ibhanoyi  ---> [['Blaq Diamond']]
        ### Love Letter  ---> [['Blaq Diamond']]
        ### Summeryomuthi  ---> [['Blaq Diamond']]


        addAllMusic(mdbmaps, "Spotify", "7ef6d6b3a605104cb3ace7c6899f8ffa", "mn0003460346")   ### [Jeppe Loftager]
        ### Kender du Emma?  ,  Fødselsdag (Hvem Bliver Du Kysset Af)  ,  Svaghed
        ### Kender du Emma?  ---> [['Jeppe Loftager']]
        ### Fødselsdag (Hvem Bliver Du Kysset Af)  ---> [['Jeppe Loftager']]
        ### Svaghed  ---> [['Jeppe Loftager']]


        addDeezer(mdbmaps, "Spotify", "e30a6d1d63a24c9c89cd814ce1169060", "2503781")    ### [Chris Burton]
        ### Love Letters  ,  What Sucks About Love (feat. Tory Lanez)  ,  Little Sister
        ### Love Letters  ---> [['Chris Burton']]
        ### What Sucks About Love (feat. Tory Lanez)  ---> [['Chris Burton']]
        ### Little Sister  ---> [['Chris Burton']]


        addAllMusic(mdbmaps, "Spotify", "74501cd011befca4607286a3970344d9", "mn0003451786")   ### [James TW]
        ### When You Love Someone  ,  You & Me  ,  Last Christmas
        ### When You Love Someone  ---> [['James TW']]
        ### You & Me  ---> [['Marc E. Bassy', 'James TW']]
        ### Last Christmas  ---> [['Ariana Grande', 'Wham!', 'James TW']]


        addAllMusic(mdbmaps, "Spotify", "d01ddff3f996a33a29d11c3acb74a495", "mn0002070367")   ### [Alphabeat]
        ### X-Mas (Let's Do It Again)  ,  Shadows  ,  I Don't Know What's Cool Anymore
        ### X-Mas (Let's Do It Again)  ---> [['Alphabeat']]
        ### Shadows  ---> [['Alphabeat']]
        ### I Don't Know What's Cool Anymore  ---> [['Alphabeat']]


        addAllMusic(mdbmaps, "Spotify", "064f90e7c32e8e8615b6cf19d17d02e2", "mn0002116456")   ### [Snotkop]
        ### Cool Soos Koos Kombuis  ,  Dropit Soos 'n Disprin
        ### Cool Soos Koos Kombuis  ---> [['Snotkop']]
        ### Dropit Soos 'n Disprin  ---> [['Snotkop']]


        addAllMusic(mdbmaps, "Spotify", "6803a3aa379992e6e0a9db4b27a7033f", "mn0003901079")   ### [Lamin]
        ### Tour (feat. KESI)  ,  Daggerin' (Lamin X ICEKIID)
        ### Tour (feat. KESI)  ---> [['Lamin']]
        ### Daggerin' (Lamin X ICEKIID)  ---> [['Lamin']]


        addAllMusic(mdbmaps, "Spotify", "684fa06cb2b06bb49c6ca8d898874cd9", "mn0003845662")   ### [Simsey]
        ### Alo (feat. Carmon)  ,  Jaloux (feat. ATYPISK)
        ### Alo (feat. Carmon)  ---> [['Simsey']]
        ### Jaloux (feat. ATYPISK)  ---> [['Simsey']]


        addDeezer(mdbmaps, "Spotify", "4f76a2b512fc327dfa68446fcb633336", "10583427")    ### [Balken]
        ### Zum Zum - Balken Remix  ,  Dejlig - Balken Remix
        ### Zum Zum - Balken Remix  ---> [['Balken']]
        ### Dejlig - Balken Remix  ---> [['Balken']]


        addAllMusic(mdbmaps, "Spotify", "2093f336c7ffb7a93f25530ffce014d0", "mn0003850136")   ### [Emil Lange]
        ### 10 År (feat. Klamfyr)  ,  Fuck Dig (feat. Tobias Rahim)
        ### 10 År (feat. Klamfyr)  ---> [['Emil Lange']]
        ### Fuck Dig (feat. Tobias Rahim)  ---> [['Emil Lange']]


        addAllMusic(mdbmaps, "Spotify", "285e0da8c682a2f79c60ae5f6e7fc882", "mn0003892988")   ### [Giveon]
        ### LIKE I WANT YOU  ,  Stuck On You
        ### LIKE I WANT YOU  ---> [['Giveon']]
        ### Stuck On You  ---> [['Giveon']]


        addDeezer(mdbmaps, "Spotify", "66d1495badb87218903836596bbb06a4", "603678")    ### [Michael Williams]
        ### Nino  ,  Bonita
        ### Nino  ---> [['Michael Williams']]
        ### Bonita  ---> [['Michael Williams']]


        addAllMusic(mdbmaps, "Spotify", "1ee93146774077500f3c58508ab6a85d", "mn0003822224")   ### [Drew Sycamore]
        ### Perfect Disaster  ,  I Wanna Be Dancing
        ### Perfect Disaster  ---> [['Drew Sycamore']]
        ### I Wanna Be Dancing  ---> [['Drew Sycamore']]


        addAllMusic(mdbmaps, "Spotify", "13817359f21eb540aa453826ed411751", "mn0003373404")   ### [Timo Odv]
        ### Move  ,  Feel Your Love
        ### Move  ---> [['Timo Odv']]
        ### Feel Your Love  ---> [['Timo Odv']]


        addAllMusic(mdbmaps, "Spotify", "4b26474d2e4b26a7d65099f3e7b7dd3b", "mn0003895940")   ### [De Mthuda]
        ### Shesha  ,  Ebumnandini
        ### Shesha  ---> [['De Mthuda']]
        ### Ebumnandini  ---> [['De Mthuda']]


        addAllMusic(mdbmaps, "Spotify", "3b375491b2e75adeadade0109cae468e", "mn0000670852")   ### [GoldFish]
        ### Hold Your Kite (feat. Sorana)  ,  Colours & Lights
        ### Hold Your Kite (feat. Sorana)  ---> [['GoldFish']]
        ### Colours & Lights  ---> [['GoldFish']]


        addAllMusic(mdbmaps, "Spotify", "cb4e0ba55451048f4f19a5a825f2ccd4", "mn0004002971")   ### [JazziDisciples]
        ### Sgubu Se Monati  ,  My Sunday
        ### Sgubu Se Monati  ---> [['JazziDisciples']]
        ### My Sunday  ---> [['JazziDisciples']]


        addDeezer(mdbmaps, "Spotify", "77eea2d04d8a7220c60c8ea02be1cec8", "8141048")    ### [Thor Farlov]
        ### Mansion  ,  Alene
        ### Mansion  ---> [['Thor Farlov']]
        ### Alene  ---> [['Thor Farlov']]


        addDeezer(mdbmaps, "Spotify", "37d457c6423b49912f2bc0d71a298d15", "11120032")    ### [Mas Music]
        ### Zaka  ,  Mthande
        ### Zaka  ---> [['Mas Music']]
        ### Mthande  ---> [['Mas Music']]


        addAllMusic(mdbmaps, "Spotify", "9eb8c2cbf58e7848a9c344ecf39ce356", "mn0003411196")   ### [Isaac Kasule]
        ### Fallit (feat. Sivas)  ,  Pas Oublié (feat. Gilli)
        ### Fallit (feat. Sivas)  ---> [['Isaac Kasule']]
        ### Pas Oublié (feat. Gilli)  ---> [['Isaac Kasule']]


        addAllMusic(mdbmaps, "Spotify", "955f4e9179a127e8a6a4808001a32e34", "mn0004002970")   ### [Reece Madlisa]
        ### Jazzidisciples (Zlele)  ,  Sithi Sithi
        ### Jazzidisciples (Zlele)  ---> [['Reece Madlisa']]
        ### Sithi Sithi  ---> [['Reece Madlisa']]


        addAllMusic(mdbmaps, "Spotify", "9f279be3a3c621eccec555c5614678ca", "mn0003412807")   ### [Ricus Nel]
        ### Hardekole  ,  Boerepompie (feat. Snotkop)
        ### Hardekole  ---> [['Ricus Nel']]
        ### Boerepompie (feat. Snotkop)  ---> [['Ricus Nel']]


        addAllMusic(mdbmaps, "Spotify", "9b1eca1be6b4575776d545e49f12a32a", "mn0002608284")   ### [Kelly Khumalo]
        ### Empini  ,  Empini - Edit
        ### Empini  ---> [['Kelly Khumalo']]
        ### Empini - Edit  ---> [['Kelly Khumalo']]


        addDeezer(mdbmaps, "Spotify", "ab4d8fc064bdc03bce732cda17e8fe1f", "98981472")    ### [Beni]
        ### Cheitana (feat. Gio)  ,  Ma Jolie
        ### Cheitana (feat. Gio)  ---> [['Beni']]
        ### Ma Jolie  ---> [['Beni']]


        addAllMusic(mdbmaps, "Spotify", "8d1b38910a56f321d10739daa406b449", "mn0003956781")   ### [Major League Djz]
        ### Dinaledi  ,  Le Plane E’Landile
        ### Dinaledi  ---> [['Major League Djz']]
        ### Le Plane E’Landile  ---> [['Major League Djz']]


        addAllMusic(mdbmaps, "Spotify", "ffce4bde553379fbd57c471010cdcb63", "mn0002861500")   ### [HEDEGAARD]
        ### That´s Me  ,  Ready To Love You
        ### That´s Me  ---> [['HEDEGAARD']]
        ### Ready To Love You  ---> [['HEDEGAARD']]


        addAllMusic(mdbmaps, "Spotify", "8ebec88165699b72c01d2f26c5192768", "mn0003586416")   ### [Zookeepers]
        ### Drunk On You  ,  Can't Fall Asleep
        ### Drunk On You  ---> [['Zookeepers']]
        ### Can't Fall Asleep  ---> [['Zookeepers']]


        addDeezer(mdbmaps, "Spotify", "85731aa32adc54ed3c257d8db8dcd1a4", "14790809")    ### [Gio]
        ### Marrakech  ,  LaMa (feat. Murro)
        ### Marrakech  ---> [['Gio']]
        ### LaMa (feat. Murro)  ---> [['Gio']]


        addDeezer(mdbmaps, "Spotify", "3c81ac6732239f285b5e559224133243", "12724627")    ### [ATkel]
        ### Habebe (feat. Volkan)  ,  La Familia Primero
        ### Habebe (feat. Volkan)  ---> [['ATkel']]
        ### La Familia Primero  ---> [['ATkel']]


        addAllMusic(mdbmaps, "Spotify", "734e3800a87d090780aec76e322ef2f0", "mn0002048866")   ### [LIGA]
        ### POP  ,  Du Er Ikke Alene
        ### POP  ---> [['Lil Uzi Vert', 'LIGA']]
        ### Du Er Ikke Alene  ---> [['LIGA']]


        addDeezer(mdbmaps, "Spotify", "006a55c78562344ab4e1a779f1d8cac5", "803672")    ### [Ritalin]
        ### Ja Dak  ,  Gider Æt
        ### Ja Dak  ---> [['Ritalin']]
        ### Gider Æt  ---> [['Ritalin']]


        addDeezer(mdbmaps, "Spotify", "ddf509010274ba110ddc7a77f2822d38", "132799")    ### [Amanda]
        ### Tror Vi Er Nem´  ,  Rager Ikke Dig
        ### Tror Vi Er Nem´  ---> [['Amanda']]
        ### Rager Ikke Dig  ---> [['Amanda']]


        addDeezer(mdbmaps, "Spotify", "b60ac25003e11eb902aa52593edb2178", "66193912")    ### [Jobe London]
        ### Sukendleleni
        ### Sukendleleni  ---> [['Jobe London']]


        addDeezer(mdbmaps, "Spotify", "a06dd0fe9e5d9a424d1f4d81772038b0", "65215352")    ### [Zero12Finest]
        ### Baby Are You Coming?
        ### Baby Are You Coming?  ---> [['Zero12Finest']]


        addAllMusic(mdbmaps, "Spotify", "4089e4925a2cf3eb064fa3fd9d559ef8", "mn0003048983")   ### [Biggy]
        ### Dames
        ### Dames  ---> [['Biggy']]


        addAllMusic(mdbmaps, "Spotify", "82426023c2dd222263bc4ca5af76093f", "mn0002960608")   ### [DJ Zinhle]
        ### Umlilo
        ### Umlilo  ---> [['DJ Zinhle']]


        addDeezer(mdbmaps, "Spotify", "a288feae6e45ad337f030f777a685619", "125372")    ### [DaVido]
        ### Blow My Mind
        ### Blow My Mind  ---> [['DaVido']]


        addAllMusic(mdbmaps, "Spotify", "25bdb124fc719d1b9e79961dc5acacf4", "mn0002567285")   ### [Francois van Coke]
        ### Dagdrome in Suburbia
        ### Dagdrome in Suburbia  ---> [['Francois van Coke']]


        addAllMusic(mdbmaps, "Spotify", "e2679962c255a62fb0ee075daf443eb8", "mn0003285389")   ### [Tshego]
        ### No Ties
        ### No Ties  ---> [['Tshego']]


        addAllMusic(mdbmaps, "Spotify", "f9552f717a2d42eba94f276fbe8d400c", "mn0003684465")   ### [Elandré]
        ### Vuur Op Die Water
        ### Vuur Op Die Water  ---> [['Elandré']]


        addDeezer(mdbmaps, "Spotify", "fb65afbb673243b5592897cb2edcebb3", "63800582")    ### [KayGee DaKing]
        ### Kokota
        ### Kokota  ---> [['KayGee DaKing']]


        addDeezer(mdbmaps, "Spotify", "5f54f13ea3b06395c8aebe93bb5dbe38", "4699636")    ### [Appel]
        ### Nonna
        ### Nonna  ---> [['Appel']]


        addDiscogs(mdbmaps, "Spotify", "d621546a8974db85455e7f7d1796ac13", "5585998")    ### [Sjava]
        ### Umama
        ### Umama  ---> [['Sjava']]


        addDeezer(mdbmaps, "Spotify", "9df1e649179da009a815044fcb52e32e", "53068722")    ### [Kwiish SA]
        ### Iskhathi - Main Mix
        ### Iskhathi - Main Mix  ---> [['Kwiish SA']]


        addDeezer(mdbmaps, "Spotify", "75dc27f745f113c489f72495a5467fa4", "14819565")    ### [Holly Rey]
        ### Deeper
        ### Deeper  ---> [['Holly Rey']]


        addDeezer(mdbmaps, "Spotify", "f6f22ed8e4165dc8b408d0d8c4ab2a22", "14643871")    ### [Shado M]
        ### Inhliziyo Yami Ithi Hey
        ### Inhliziyo Yami Ithi Hey  ---> [['Shado M']]


        addDeezer(mdbmaps, "Spotify", "47aa70f2ed41231bd68d545ce603bd21", "66139742")    ### [Semi Tee]
        ### Labantwana Ama Uber
        ### Labantwana Ama Uber  ---> [['Semi Tee']]


        addAllMusic(mdbmaps, "Spotify", "939cc4877cb7b69c4fb863e7bc313424", "mn0003958998")   ### [Sista Prod]
        ### Eyes Blue Like The Atlantic (feat. Subvrbs)
        ### Eyes Blue Like The Atlantic (feat. Subvrbs)  ---> [['Sista Prod']]


        addDeezer(mdbmaps, "Spotify", "87521eb52615ae1b898839ed7315cb77", "158304422")    ### [Mduduzi]
        ### Isiginci
        ### Isiginci  ---> [['Mduduzi']]


        addDeezer(mdbmaps, "Spotify", "69b5ab2b898fc0777a5cd46ee969f054", "50371262")    ### [Ami Faku]
        ### Ubuhle Bakho
        ### Ubuhle Bakho  ---> [['Ami Faku']]


        addAllMusic(mdbmaps, "Spotify", "9d7a94984cae8d121c2ef0844d52d994", "mn0003969902")   ### [Tyler ICU]
        ### Bella Ciao
        ### Bella Ciao  ---> [['Tyler ICU']]


        addDeezer(mdbmaps, "Spotify", "e285d966fbbfb5d8164659f95173d6f1", "174717372")    ### [Soa mattrix]
        ### Uthando
        ### Uthando  ---> [['Soa mattrix', 'Soa Mattrix']]


        addDeezer(mdbmaps, "Spotify", "c8510c6d44e23781be22e44208b9fdfe", "174717372")    ### [Soa Mattrix]
        ### Uthando
        ### Uthando  ---> [['Soa mattrix', 'Soa Mattrix']]


        addDeezer(mdbmaps, "Spotify", "ffd43fb33c135040b990fa400a667431", "151450112")    ### [Synth Peter]
        ### Doef Doef (feat. Katinka, Loufi, What The Faf & Wortel Kombat)
        ### Doef Doef (feat. Katinka, Loufi, What The Faf & Wortel Kombat)  ---> [['Synth Peter']]


        addDeezer(mdbmaps, "Spotify", "cd50dde80b239af08cfb3d4959a55aa4", "11413962")    ### [Manqonqo]
        ### Eyadini
        ### Eyadini  ---> [['Manqonqo']]


        addDeezer(mdbmaps, "Spotify", "493a727e000cd52505230be40a20564b", "78499372")    ### [Mapara A Jazz]
        ### John Vuli Gate (feat. Ntosh Gazi & Colano)
        ### John Vuli Gate (feat. Ntosh Gazi & Colano)  ---> [['Mapara A Jazz']]


        addDeezer(mdbmaps, "Spotify", "6a0373b2f1ea877d1a335494ccfe421b", "5632419")    ### [Riky Rick]
        ### UNGAZINCISHI (feat. Focalistic & Tyler ICU)
        ### UNGAZINCISHI (feat. Focalistic & Tyler ICU)  ---> [['Riky Rick']]


        addDeezer(mdbmaps, "Spotify", "a717abfcdaa126abe21f2547ce40c991", "50188832")    ### [Aubrey Qwana]
        ### Molo
        ### Molo  ---> [['Aubrey Qwana']]


        addDeezer(mdbmaps, "Spotify", "fc1ad419775a7176efb8f3ca4eff831f", "147595512")    ### [Miss Pru DJ]
        ### Price to Pay
        ### Price to Pay  ---> [['Miss Pru DJ']]


        addDeezer(mdbmaps, "Spotify", "e8b0d06414830b53826c4cf0648a75f7", "111864442")    ### [KDDO]
        ### eWallet (feat. Cassper Nyovest)
        ### eWallet (feat. Cassper Nyovest)  ---> [['KDDO']]


        addDeezer(mdbmaps, "Spotify", "9c0ae5b3f748406163cbfbcc31a9ec70", "80240272")    ### [DBN Gogo]
        ### French Kiss
        ### French Kiss  ---> [['DBN Gogo']]


        addDeezer(mdbmaps, "Spotify", "4c0eff1f1c8ea91d298e8f0d3e3be7ad", "5607221")    ### [Jub Jub]
        ### Ndikhokhele
        ### Ndikhokhele  ---> [['Jub Jub']]


        addDeezer(mdbmaps, "Spotify", "c37f56772b3e61e4f8b7ed4fb115b58b", "9686762")    ### [Big Zulu]
        ### Mali Eningi
        ### Mali Eningi  ---> [['Big Zulu']]


        addDeezer(mdbmaps, "Spotify", "ba1bf3f879eb094a5bbfd4e3bf0027ca", "50980022")    ### [Alfa Kat]
        ### Phone Yam
        ### Phone Yam  ---> [['Alfa Kat']]


        addDeezer(mdbmaps, "Spotify", "9056ef2ff71b082c2ee11d1fef47b0da", "62760832")    ### [Musa Keys]
        ### Samarian Boy
        ### Samarian Boy  ---> [['Musa Keys']]


        addDeezer(mdbmaps, "Spotify", "cdd7186458504974cb50b68efd0a91a6", "10318006")    ### [Max Hurrell]
        ### ZOL
        ### ZOL  ---> [['Max Hurrell']]


        addDeezer(mdbmaps, "Spotify", "fc62defc73305f0bfb3610ad7e65e5da", "14377487")    ### [AVAION]
        ### Pieces
        ### Pieces  ---> [['AVAION']]


        addDeezer(mdbmaps, "Spotify", "dde737a9ab2106e25a0222e42aa20345", "78335872")    ### [Dj Sunco]
        ### Koko Mmatswale
        ### Koko Mmatswale  ---> [['Dj Sunco']]


        addDeezer(mdbmaps, "Spotify", "3356c87d305a4934943821dfce2dab5b", "668841")    ### [Azana]
        ### Your Love
        ### Your Love  ---> [['David Guetta', 'Azana']]


        addDeezer(mdbmaps, "Spotify", "a6277ac94ebb8800f0795ba0bc059bf8", "68905302")    ### [Vigro Deep]
        ### International
        ### International  ---> [['Vigro Deep']]


        addDeezer(mdbmaps, "Spotify", "607a261aebc02ca36c8da08a9af43729", "11313734")    ### [Luu Nineleven]
        ### Friends With Benefits - Umjolo
        ### Friends With Benefits - Umjolo  ---> [['Luu Nineleven']]


        addDeezer(mdbmaps, "Spotify", "559256522431642f4de7383724b57b2b", "49276612")    ### [Boohle]
        ### Mama
        ### Mama  ---> [['Jonas Blue', 'ZK', 'Boohle']]

        addDeezer(mdbmaps, "Spotify", "6339aef25635becb9a2ea6a8e28e4423", "12279542")    ### [Sithelo]
        ### Forever
        ### Forever  ---> [['Tory Lanez', 'Lewis Capaldi', 'NLE Choppa', 'Sithelo']]


        addDeezer(mdbmaps, "Spotify", "0f03200d304f5a0c3bcc10068a8af4f6", "4745094")    ### [DJ Tira]
        ### Thank You Mr DJ
        ### Thank You Mr DJ  ---> [['DJ Tira']]


        addDeezer(mdbmaps, "Spotify", "229a5cd77f92d12cc16441d66714557e", "11435622")    ### [DJ Big Sky]
        ### Fire
        ### Fire  ---> [['KIDS SEE GHOSTS', 'DJ Big Sky']]


        addDeezer(mdbmaps, "Spotify", "7eb2bc95d16ef236f592c4ae51688969", "10096298")    ### [Zain SA]
        ### Ina Iyeza
        ### Ina Iyeza  ---> [['Zain SA']]


        addDeezer(mdbmaps, "Spotify", "a6b7c514243c48c282577f6ca516d1a5", "12402518")    ### [Vusinator]
        ### Gigabyte - Radio Edit
        ### Gigabyte - Radio Edit  ---> [['Vusinator']]


        addDeezer(mdbmaps, "Spotify", "112260dab08a6d602068745af6eca9ab", "109258522")    ### [Zandimaz]
        ### Emathandweni
        ### Emathandweni  ---> [['Zandimaz']]


        addDeezer(mdbmaps, "Spotify", "75f3efa9b69db131b523b79281bd22db", "67791072")    ### [Bernice West]
        ### Sonop-Blom
        ### Sonop-Blom  ---> [['Bernice West']]


        addDeezer(mdbmaps, "Spotify", "42ed843a1c693461ea069d8ac44713b6", "4976003")    ### [Rethabile Khumalo]
        ### Ntyilo Ntyilo
        ### Ntyilo Ntyilo  ---> [['Rethabile Khumalo']]


        addDeezer(mdbmaps, "Spotify", "b30c49df9494e464d535272407520136", "1162622")    ### [Fyr Og Flamme]
        ### Menneskeforbruger
        ### Menneskeforbruger  ---> [['Fyr Og Flamme']]


        addDeezer(mdbmaps, "Spotify", "a3f0639155282965d9aa75df67c29e5a", "10592265")    ### [King Monada]
        ### Malwedhe
        ### Malwedhe  ---> [['King Monada']]


        addDeezer(mdbmaps, "Spotify", "222a8bff5ea6adaf4dab014ee2e81ce6", "14856543")    ### [Mr. Mum]
        ### Sæt dig på mit ansigt
        ### Sæt dig på mit ansigt  ---> [['Mr. Mum']]


        addDeezer(mdbmaps, "Spotify", "c24a3776ee8f55d8b50e4b578af39d3c", "83653352")    ### [Kimbo]
        ### Ego
        ### Ego  ---> [['Kimbo']]


        addDeezer(mdbmaps, "Spotify", "352709a992be8247dbf79bd191c95344", "450138")    ### [Mille]
        ### Til næste år
        ### Til næste år  ---> [['Mille']]


        addDeezer(mdbmaps, "Spotify", "3ef0fe6c3a3797504880a0627e6ec1cb", "14060755")    ### [Anna Ritsmar]
        ### Starlight
        ### Starlight  ---> [['Anna Ritsmar']]


        addDeezer(mdbmaps, "Spotify", "eb265b3544025b9182400cc7fda097f9", "14040663")    ### [BaseBoys]
        ### Level 1000
        ### Level 1000  ---> [['BaseBoys']]


        addDeezer(mdbmaps, "Spotify", "b87c9d3bb557de5690f18e58d4d4f5b4", "13706055")    ### [Shorta Kigger]
        ### Min Dodo Ringer
        ### Min Dodo Ringer  ---> [['Shorta Kigger']]


        addDeezer(mdbmaps, "Spotify", "5514b2316d259d30b17292aba9825ca6", "10550919")    ### [Bar Z]
        ### Åh Nej (feat. Benny Jamz)
        ### Åh Nej (feat. Benny Jamz)  ---> [['Bar Z']]


        addDeezer(mdbmaps, "Spotify", "5cc08574fc7451dd9969b6e118121813", "4877593")    ### [Poo Bear]
        ### Hard 2 Face Reality
        ### Hard 2 Face Reality  ---> [['Poo Bear']]


        addDeezer(mdbmaps, "Spotify", "4a34812d5f24c256a2313b6b492200d3", "6882019")    ### [GULEED]
        ### BÖRJA OM (feat. Gilli)
        ### BÖRJA OM (feat. Gilli)  ---> [['GULEED']]


        addDeezer(mdbmaps, "Spotify", "dc76ca3a69837c0075b2bc1ad9ba40ed", "464655")    ### [Reem]
        ### Kill the Love
        ### Kill the Love  ---> [['Reem']]


        addDeezer(mdbmaps, "Spotify", "a2c700d339984e3f5942be0bea0283ee", "9420538")    ### [SHY Martin]
        ### Lose You Too
        ### Lose You Too  ---> [['SHY Martin']]


        addDeezer(mdbmaps, "Spotify", "705c0cf64342deeb96a56879df507084", "10875608")    ### [Chatle]
        ### Para (feat. ATYPISK)
        ### Para (feat. ATYPISK)  ---> [['Chatle']]


        addDeezer(mdbmaps, "Spotify", "d2bec07a7ea23c351dc7e0821e1dd822", "11010740")    ### [AWADA]
        ### Stjæle Eller Eje (feat. Gilli & Toko)
        ### Stjæle Eller Eje (feat. Gilli & Toko)  ---> [['AWADA']]


        addDeezer(mdbmaps, "Spotify", "c1d48f7d231fd387c40fdcedc5fd5168", "4631718")    ### [Murro]
        ### Har Det (feat. Omar)
        ### Har Det (feat. Omar)  ---> [['Murro']]


        addDeezer(mdbmaps, "Spotify", "de465f34fb15c5231b8bda39a6c6566e", "247790")    ### [Uffe Holm]
        ### Englebarn (Hollys Jul) feat. Holly
        ### Englebarn (Hollys Jul) feat. Holly  ---> [['Uffe Holm']]


        addDeezer(mdbmaps, "Spotify", "ecdc476daa38e4b5c05aa8add488231f", "4053148")    ### [Karen Gardelli]
        ### Alletiders Jul
        ### Alletiders Jul  ---> [['Karen Gardelli']]


        addDeezer(mdbmaps, "Spotify", "a88f03dbc7cd3326b9e8854bc3bc492b", "13968747")    ### [Jaxstyle]
        ### Fortnite
        ### Fortnite  ---> [['Jaxstyle']]


        addDeezer(mdbmaps, "Spotify", "b6e43231ccd5efa631ee6796519b263a", "13660095")    ### [Le Mo]
        ### Hvid Jul
        ### Hvid Jul  ---> [['Le Mo']]


        addDeezer(mdbmaps, "Spotify", "b4df70a25b24028d47d08224e3dc3403", "956707")    ### [Rasmus Bjerg]
        ### En Rigtig Drengejul
        ### En Rigtig Drengejul  ---> [['Rasmus Bjerg']]


        addDeezer(mdbmaps, "Spotify", "19fdbc13a0bd6037d45ac10fad5a7f88", "157478")    ### [Mc Einar]
        ### Jul Det' Cool
        ### Jul Det' Cool  ---> [['Mc Einar']]


        addDeezer(mdbmaps, "Spotify", "e833e619b02fb7471d80224c9ef411f5", "74080")    ### [Julie]
        ### Jesus & Josefine
        ### Jesus & Josefine  ---> [['Julie']]


        addDeezer(mdbmaps, "Spotify", "3ef801bb5e6abb84fc8878a28e0e8b08", "1607647")    ### [SJUR]
        ### Let Me Love You (feat. Chris Crone)
        ### Let Me Love You (feat. Chris Crone)  ---> [['SJUR']]


        addDeezer(mdbmaps, "Spotify", "9c8ef75901e30b366ce4736175e2c841", "7416422")    ### [Life of Dillon]
        ### Sex for Breakfast
        ### Sex for Breakfast  ---> [['Life of Dillon']]


        addDeezer(mdbmaps, "Spotify", "c1b5cc67d8c00401cb953f3bd56d4a0d", "7628466")    ### [Mugisho]
        ### Play with You
        ### Play with You  ---> [['Mugisho']]


        addDeezer(mdbmaps, "Spotify", "0c27b5a934e93aedca6528dc9c9303a9", "11974555")    ### [Ida Una]
        ### One
        ### One  ---> [['Lewis Capaldi', 'Ida Una']]


        addDeezer(mdbmaps, "Spotify", "9930fd8d6c2449122199e07941259b63", "11100192")    ### [Fætr]
        ### Farlig
        ### Farlig  ---> [['Fætr']]


        addDeezer(mdbmaps, "Spotify", "373fbb0b10865894fcef65132c366ce4", "8407236")    ### [Mads B]
        ### Gokkesok
        ### Gokkesok  ---> [['Mads B']]


        addDeezer(mdbmaps, "Spotify", "b330e0d99ee5455ccc1e792d3bc85800", "11516399")    ### [Hemlig Elsker]
        ### Cocktailkort
        ### Cocktailkort  ---> [['Hemlig Elsker']]


        addDeezer(mdbmaps, "Spotify", "9702ce4d632f91f778c610c595f31c88", "10628251")    ### [Anders Hemmingsen]
        ### Det Forår
        ### Det Forår  ---> [['Anders Hemmingsen']]


        addDeezer(mdbmaps, "Spotify", "60c902bdfb02000a90b68722f8360f36", "4470116")    ### [Micky Skeel]
        ### Camilla
        ### Camilla  ---> [['Micky Skeel']]


        addDeezer(mdbmaps, "Spotify", "2c8a5c6c160d57eda734acbd15efaae5", "11032126")    ### [Benjamin Rihan]
        ### Nok for mig
        ### Nok for mig  ---> [['Benjamin Rihan']]


        addDeezer(mdbmaps, "Spotify", "9a1af9dce4d3dffa5230c0118d66cccb", "9520034")    ### [Eebz]
        ### Catalonia
        ### Catalonia  ---> [['Eebz']]


        addDeezer(mdbmaps, "Spotify", "ef79d8fffd61437747abbd9911cf5034", "8228900")    ### [Lulleaux]
        ### Contact
        ### Contact  ---> [['Lulleaux']]


        addDeezer(mdbmaps, "Spotify", "bff0c03fa59a68dd364600ecff6696b6", "11412994")    ### [Louis Valuta]
        ### DENDER (feat. Emil Stabil)
        ### DENDER (feat. Emil Stabil)  ---> [['Louis Valuta']]


        addDeezer(mdbmaps, "Spotify", "f8b40fae4828e5d52d2ecae1634a3946", "13438113")    ### [bobby shams]
        ### blå
        ### blå  ---> [['bobby shams']]


        addDeezer(mdbmaps, "Spotify", "afb168079f174ca010315013a1464daa", "1662463")    ### [SODA]
        ### Bedste veninder
        ### Bedste veninder  ---> [['SODA']]


        addDeezer(mdbmaps, "Spotify", "9008540367650b8f963ecdbc6eb3099a", "12546410")    ### [De To Musketerer]
        ### Hånder
        ### Hånder  ---> [['De To Musketerer']]


        addDeezer(mdbmaps, "Spotify", "4e6f762fa36e459d1c0dda5fb1fa5dba", "5078978")    ### [Vusi Nova]
        ### As'phelelanga
        ### As'phelelanga  ---> [['Vusi Nova']]


        addDeezer(mdbmaps, "Spotify", "96fc905f26eec4c3c46514264bb2e2fc", "115052182")    ### [Sikkerhedsstyrelsen]
        ### Nytår Igen (feat. Jesu Brødre, Lina Rafn, Niels Olsen, Klam Vandmand & Shambs)
        ### Nytår Igen (feat. Jesu Brødre, Lina Rafn, Niels Olsen, Klam Vandmand & Shambs)  ---> [['Sikkerhedsstyrelsen']]


        addDeezer(mdbmaps, "Spotify", "44a23569d1038c4027611537fa68bfa2", "1931991")    ### [Dani M.]
        ### Trylleri
        ### Trylleri  ---> [['Dani M.']]


        addDeezer(mdbmaps, "Spotify", "c7e0a4f1a2f75c0d598d9c87f9a404fc", "4509646")    ### [Niels Brandt]
        ### Hele Verden Fra Forstanden
        ### Hele Verden Fra Forstanden  ---> [['Niels Brandt']]


        addDeezer(mdbmaps, "Spotify", "30c1f2da90cf405474b1aac94b3ef26f", "10367426")    ### [Mads Christian]
        ### Ligesom Mig (feat. Sean Kingston)
        ### Ligesom Mig (feat. Sean Kingston)  ---> [['Mads Christian']]


        addDeezer(mdbmaps, "Spotify", "231f7741ee6eee918c88b45569faaf35", "8141050")    ### [Anthon Edwards]
        ### Holder Os Vågne (Anthon Edwards x Burhan G)
        ### Holder Os Vågne (Anthon Edwards x Burhan G)  ---> [['Anthon Edwards']]


        addDeezer(mdbmaps, "Spotify", "32c9d36403849da0f28fe73060c2d336", "4320492")    ### [Miklo]
        ### Lazy Bop
        ### Lazy Bop  ---> [['Miklo']]


        addDeezer(mdbmaps, "Spotify", "c2ff22025fbb1d90a54f28d9cfa74991", "1403787")    ### [Pyrus]
        ### Cool Jul
        ### Cool Jul  ---> [['Pyrus']]


        addDeezer(mdbmaps, "Spotify", "0616e80cba1d712a832219436a5e2a1e", "7898578")    ### [ROZES]
        ### Christmas (Baby Please Come Home)
        ### Christmas (Baby Please Come Home)  ---> [['Mariah Carey', 'Darlene Love', 'ROZES']]


        addDeezer(mdbmaps, "Spotify", "e0c30f4b07c739498d6a9ddb3025731f", "99548022")    ### [Red Velvet - Irene & Seulgi]
        ### Monster
        ### Monster  ---> [['D-Block Europe', 'Nines', 'Red Velvet - Irene & Seulgi']]


        addDeezer(mdbmaps, "Spotify", "e22902b1c269624fe7205b7525b7d127", "12668577")    ### [Baby Bino]
        ### Lil Ting (feat. Lille Høg & Chanelbigs)
        ### Lil Ting (feat. Lille Høg & Chanelbigs)  ---> [['Baby Bino']]


        addDeezer(mdbmaps, "Spotify", "10cc5fe4c9b87dded6eab101efa299da", "58559502")    ### [Petter Ferraz]
        ### Amor ou o Litrão
        ### Amor ou o Litrão  ---> [['Petter Ferraz']]


        addDeezer(mdbmaps, "Spotify", "0f827c8a738fa91b9e16188aa8cab8eb", "7574470")    ### [Lady Zamar]
        ### Collide
        ### Collide  ---> [['Lady Zamar']]


        addDeezer(mdbmaps, "Spotify", "96a6273236ce76a0332b51273ce3290a", "13388321")    ### [Dladla Mshunqisi]
        ### Pakisha
        ### Pakisha  ---> [['Dladla Mshunqisi']]


        addDeezer(mdbmaps, "Spotify", "ab3fc2516e8f31c020f84529a9c297d6", "4513567")    ### [DJ Ganyani]
        ### Emazulwini
        ### Emazulwini  ---> [['DJ Ganyani']]


        addDeezer(mdbmaps, "Spotify", "80e0f32a714d5a5fe7e13a5fc5278107", "50743432")    ### [Boity]
        ### Wuz Dat?
        ### Wuz Dat?  ---> [['Boity']]


        addDeezer(mdbmaps, "Spotify", "94a0f039ba07392c142f9491ed13cbbc", "995382")    ### [Kyle Watson]
        ### You Boy - Radio Edit
        ### You Boy - Radio Edit  ---> [['Kyle Watson']]


        addDeezer(mdbmaps, "Spotify", "7ca8aab1a20e018e7d3181e4d99a59b3", "11984162")    ### [DJ Sumbody]
        ### Monate Mpolaye
        ### Monate Mpolaye  ---> [['DJ Sumbody']]


        addDeezer(mdbmaps, "Spotify", "1df5125b970f1523e3989dfcf557dc8e", "267808")    ### [Ranji]
        ### Can't Sleep - Radio Version
        ### Can't Sleep - Radio Version  ---> [['Ranji']]


        addDeezer(mdbmaps, "Spotify", "b04a58ab770549080ac1cfa6bf1ebca2", "8032209")    ### [Tobias Rahim]
        ### Jesus
        ### Jesus  ---> [['Tobias Rahim']]


        addDeezer(mdbmaps, "Spotify", "ea4baa3a2288393684147ff1c016061c", "662763")    ### [Papito]
        ### Si Si Maria
        ### Si Si Maria  ---> [['Papito']]


        addDeezer(mdbmaps, "Spotify", "ee4949e1ae2c9a8d6bb885baf1739b7d", "66062032")    ### [Jerome]
        ### Light
        ### Light  ---> [['Big Sean', 'San Holo', 'Jerome']]


        addDeezer(mdbmaps, "Spotify", "8aef8b25f88d5496281dbfd062ad84fd", "4536319")    ### [De Danske Hyrder]
        ### Billige Bajer
        ### Billige Bajer  ---> [['De Danske Hyrder']]


        addDeezer(mdbmaps, "Spotify", "cf0d301fe45cd1e4cca6fa1eb5dcb8a4", "56772872")    ### [Winati]
        ### Sweet Dreams (Are Made of This)
        ### Sweet Dreams (Are Made of This)  ---> [['Winati']]


        addDeezer(mdbmaps, "Spotify", "8dfe16a38efcddbe2845897dba8dd69b", "9632982")    ### [PASSION]
        ### Oceaner
        ### Oceaner  ---> [['PASSION']]


        addDeezer(mdbmaps, "Spotify", "39ff26d8512d64f27a471c888e0ae3e7", "9846246")    ### [Pind]
        ### Plastic
        ### Plastic  ---> [['Future', 'Pind']]


        addDeezer(mdbmaps, "Spotify", "84073e643c911b92ce18a8be7d2bc61a", "1211128")    ### [BOUA]
        ### Natten Rammer
        ### Natten Rammer  ---> [['BOUA']]


        addDeezer(mdbmaps, "Spotify", "069056d845d3929d12b47f54c6f33fed", "293356")    ### [Maximillian]
        ### Ripples
        ### Ripples  ---> [['Maximillian']]


        addDeezer(mdbmaps, "Spotify", "b0374d0c1519615f13206980e882827e", "68762982")    ### [Calby]
        ### Burnout
        ### Burnout  ---> [['Calby']]


        addDeezer(mdbmaps, "Spotify", "148ff356d0ccf4bc5ecc56a8eae7e92f", "7393970")    ### [Tyrees Tyr]
        ### Prioritet
        ### Prioritet  ---> [['Tyrees Tyr']]


        addDeezer(mdbmaps, "Spotify", "20c880c21611ee3b3c247d95c81391dd", "86073762")    ### [Young Juu]
        ### Kender Ham Godt
        ### Kender Ham Godt  ---> [['Young Juu']]


        addDeezer(mdbmaps, "Spotify", "51a9bf8e74ef6d582c9395c84d3c577d", "82575932")    ### [JAAIIL]
        ### Superhelten
        ### Superhelten  ---> [['JAAIIL']]


        addDeezer(mdbmaps, "Spotify", "94bc10a30dd428bf0d0b783af02c61d3", "5092928")    ### [Siff]
        ### Mit hjerte der griner
        ### Mit hjerte der griner  ---> [['Siff']]


        addDeezer(mdbmaps, "Spotify", "eb7cf54e893e7d730c86eb117d6a5ba2", "77252552")    ### [Baloosh]
        ### Soldat
        ### Soldat  ---> [['Baloosh']]


        addDeezer(mdbmaps, "Spotify", "dace305eaa2344ac793a1fafa2c9b2e2", "4091600")    ### [andreas odbjerg]
        ### føler mig selv 100
        ### føler mig selv 100  ---> [['andreas odbjerg']]


        addDeezer(mdbmaps, "Spotify", "aa6e6733375922787f441ad4e3d4aa6b", "94429902")    ### [Alma]
        ### The Last Dance (Cover) - X Factor Denmark 2020
        ### The Last Dance (Cover) - X Factor Denmark 2020  ---> [['Alma']]


        addDeezer(mdbmaps, "Spotify", "21c6d28a42b19f87bf72d38f84a4c2be", "50670732")    ### [Sinds]
        ### Corolla (feat. Branco)
        ### Corolla (feat. Branco)  ---> [['Sinds']]

        addDeezer(mdbmaps, "Spotify", "516f9c07da4a807ce092ccf09a942c81", "14544939")    ### [DON x LEE x BARBER]
        ### Gucci Bag Sikini  ,  Raketter  ,  Præg På Kortet
        ### Gucci Bag Sikini  ---> [['DON x LEE x BARBER']]
        ### Raketter  ---> [['DON x LEE x BARBER']]
        ### Præg På Kortet  ---> [['DON x LEE x BARBER']]

        addDeezer(mdbmaps, "Spotify", "30c9d44373e320dfb6f0a4d13b6fed0d", "98163582")    ### [NextYoungin]
        ### 3 Musketeers
        ### 3 Musketeers  ---> [['NextYoungin']]


        addDeezer(mdbmaps, "Spotify", "f0ec83f9c509cb9862c971c3e123ec8b", "13660239")    ### [Trey & Zay]
        ### Ikk Min Skyld
        ### Ikk Min Skyld  ---> [['Trey & Zay']]


        addDeezer(mdbmaps, "Spotify", "e3746bb69c4f7aec91780021e0a11e5b", "2192521")    ### [Pascal & Pearce]
        ### Running Wild
        ### Running Wild  ---> [['Pascal & Pearce']]


        addDeezer(mdbmaps, "Spotify", "32b329ec7b290cd91db0684e80a68a50", "84292982")    ### [Tarcísio do Acordeon]
        ### Meia Noite (Você tem meu Whatsapp)
        ### Meia Noite (Você tem meu Whatsapp)  ---> [['Tarcísio do Acordeon']]

        addDeezer(mdbmaps, "Spotify", "0f1196d42f701ee87e38d757c5a1b33b", "12671285")    ### [Dj 4rain]
        ### Play the Beat
        ### Play the Beat  ---> [['Dj 4rain']]

        addDeezer(mdbmaps, "Spotify", "e499d2757000299b81dc3d721e9029fe", "555414")    ### [PS1]
        ### Fake Friends (feat. Alex Hosking)
        ### Fake Friends (feat. Alex Hosking)  ---> [['PS1']]

        addDeezer(mdbmaps, "Spotify", "d93533a4eb1153440f7fb91f39d79d85", "84950802")    ### [Tobi & Manny]
        ### Destined For Greatness
        ### Destined For Greatness  ---> [['Tobi & Manny']]


        addDeezer(mdbmaps, "Spotify", "40dccd1672ccbbd3d4989a1712fd3f2c", "1583091")    ### [D&A]
        ### Boombadah basta
        ### Boombadah basta  ---> [['D&A']]

        addDeezer(mdbmaps, "Spotify", "0c95330885e7f788a0fdfc854765c7a1", "15294119")    ### [Kinneret]
        ### No Wind Resistance!
        ### No Wind Resistance!  ---> [['Kinneret']]


        addDeezer(mdbmaps, "Spotify", "caaacf07acc18df642a7e4e7e5fbb112", "82575942")    ### [Karla & Liva]
        ### Brug din fantasi
        ### Brug din fantasi  ---> [['Karla & Liva']]

        addDeezer(mdbmaps, "Spotify", "231eabd5b8b973996092951acaef4d41", "67704502")    ### [Paradise Hotel 2019]
        ### Don Julio (feat. Bro)
        ### Don Julio (feat. Bro)  ---> [['Paradise Hotel 2019']]


        addDeezer(mdbmaps, "Spotify", "d7fa398803c81281d72154a739f25b24", "7455976")    ### [GAMPER & DADONI]
        ### Bittersweet Symphony (feat. Emily Roberts)
        ### Bittersweet Symphony (feat. Emily Roberts)  ---> [['GAMPER & DADONI']]


        addDeezer(mdbmaps, "Spotify", "0c44bd96e12e836af5e433b9df08279f", "13353835")    ### [Mika & Tobias]
        ### Ikke mere mælk
        ### Ikke mere mælk  ---> [['Mika & Tobias']]


        addDeezer(mdbmaps, "Spotify", "b1b45eb564304da1344f4ef27f75db33", "117111442")    ### [Young Stoner Life]
        ### Take It To Trial (feat. Yak Gotti)
        ### Take It To Trial (feat. Yak Gotti)  ---> [['Young Stoner Life']]
        

        addDeezer(mdbmaps, "Spotify", "db775f026a0b814326b63b35efb09cd0", "713451")    ### [Nines]
        ### Pride  ,  Airplane Mode (feat. NSG)  ,  Clout  ,  NIC (feat. Tiggs Da Author)  ,  Energy (feat. Skrapz)  ,  Realist (feat. Nafe Smallz and Fundz)  ,  Ringaling (feat. Headie One and Odeal)  ,  Money Ain’t A Thing (feat. Roy Woods)  ,  Monster  ,  Don’t Change (feat. NorthSideBenji)  ,  Intro  ,  Lights (feat. Louis Rei)  ,  Flavours  ,  All Stars 2 (feat. Clavish, Frosty, Q2T and Chappo CSB)  ,  Flex (feat. NorthSideBenji and REID B2WN)  ,  Outro  ,  Stalker Interlude (feat. Cherrie)
        ### Pride  ---> [['Nines']]
        ### Airplane Mode (feat. NSG)  ---> [['Nines']]
        ### Clout  ---> [['Nines']]
        ### NIC (feat. Tiggs Da Author)  ---> [['Nines']]
        ### Energy (feat. Skrapz)  ---> [['Nines']]
        ### Realist (feat. Nafe Smallz and Fundz)  ---> [['Nines']]
        ### Ringaling (feat. Headie One and Odeal)  ---> [['Nines']]
        ### Money Ain’t A Thing (feat. Roy Woods)  ---> [['Nines']]
        ### Monster  ---> [['D-Block Europe', 'Nines', 'Red Velvet - Irene & Seulgi']]
        ### Don’t Change (feat. NorthSideBenji)  ---> [['Nines']]
        ### Intro  ---> [['Big Sean', 'J. Cole', '21 Savage', 'Meek Mill', 'Khalid', 'Quality Control', 'Artigeardit', 'D-Block Europe', 'Skepta', 'Nines']]
        ### Lights (feat. Louis Rei)  ---> [['Nines']]
        ### Flavours  ---> [['Nines']]
        ### All Stars 2 (feat. Clavish, Frosty, Q2T and Chappo CSB)  ---> [['Nines']]
        ### Flex (feat. NorthSideBenji and REID B2WN)  ---> [['Nines']]
        ### Outro  ---> [['Nines']]
        ### Stalker Interlude (feat. Cherrie)  ---> [['Nines']]


        addAllMusic(mdbmaps, "Spotify", "d2eaaacfa7b7ec934d3db3fa316eda15", "mn0003350306")   ### [Dreamville]
        ### Down Bad (feat. JID, Bas, J. Cole, EARTHGANG & Young Nudy)  ,  Under The Sun (with J. Cole & Lute feat. DaBaby)  ,  Costa Rica (with Bas & JID feat. Guapdad 4000, Reese LAFLARE, Jace, Mez, Smokepurpp, Buddy & Ski Mask The Slump God)  ,  Sunset (with J. Cole feat. Young Nudy)  ,  Wells Fargo (with JID & EARTHGANG feat. Buddy & Guapdad 4000) - Interlude  ,  LamboTruck (with Cozz feat. REASON & Childish Major)  ,  Oh Wow...Swerve (with J. Cole feat. Zoink Gang, KEY! & Maxo Kream)  ,  Swivel (with EARTHGANG) - From The Album "Mirrorland"  ,  1993 (with J. Cole, JID, Cozz & EARTHGANG feat. Smino & Buddy)  ,  Don't Hit Me Right Now (with Bas & Cozz feat. Yung Baby Tate, Guapdad 4000 & Buddy)  ,  Got Me (with Ari Lennox & Omen feat. Ty Dolla $ign & Dreezy)  ,  Sacrifices (with EARTHGANG & J. Cole feat. Smino & Saba)  ,  Sleep Deprived (with Lute & Omen feat. Mez & DaVionne)  ,  Rembrandt...Run It Back (with JID & J. Cole feat. Vince Staples)  ,  Ladies, Ladies, Ladies (with JID feat. T.I.)  ,  Self Love (with Ari Lennox & Bas feat. Baby Rose)
        ### Down Bad (feat. JID, Bas, J. Cole, EARTHGANG & Young Nudy)  ---> [['Dreamville']]
        ### Under The Sun (with J. Cole & Lute feat. DaBaby)  ---> [['Dreamville']]
        ### Costa Rica (with Bas & JID feat. Guapdad 4000, Reese LAFLARE, Jace, Mez, Smokepurpp, Buddy & Ski Mask The Slump God)  ---> [['Dreamville']]
        ### Sunset (with J. Cole feat. Young Nudy)  ---> [['Dreamville']]
        ### Wells Fargo (with JID & EARTHGANG feat. Buddy & Guapdad 4000) - Interlude  ---> [['Dreamville']]
        ### LamboTruck (with Cozz feat. REASON & Childish Major)  ---> [['Dreamville']]
        ### Oh Wow...Swerve (with J. Cole feat. Zoink Gang, KEY! & Maxo Kream)  ---> [['Dreamville']]
        ### Swivel (with EARTHGANG) - From The Album "Mirrorland"  ---> [['Dreamville']]
        ### 1993 (with J. Cole, JID, Cozz & EARTHGANG feat. Smino & Buddy)  ---> [['Dreamville']]
        ### Don't Hit Me Right Now (with Bas & Cozz feat. Yung Baby Tate, Guapdad 4000 & Buddy)  ---> [['Dreamville']]
        ### Got Me (with Ari Lennox & Omen feat. Ty Dolla $ign & Dreezy)  ---> [['Dreamville']]
        ### Sacrifices (with EARTHGANG & J. Cole feat. Smino & Saba)  ---> [['Dreamville']]
        ### Sleep Deprived (with Lute & Omen feat. Mez & DaVionne)  ---> [['Dreamville']]
        ### Rembrandt...Run It Back (with JID & J. Cole feat. Vince Staples)  ---> [['Dreamville']]
        ### Ladies, Ladies, Ladies (with JID feat. T.I.)  ---> [['Dreamville']]
        ### Self Love (with Ari Lennox & Bas feat. Baby Rose)  ---> [['Dreamville']]


        addAllMusic(mdbmaps, "Spotify", "c5ab98618a55273dd422120ebb6759dd", "mn0003608280")   ### [Fredo]
        ### All I Ever Wanted (feat. Dave)  ,  Survival of the Fittest  ,  Mmhm  ,  Property Picking  ,  BMT  ,  Morning  ,  All I Ever Wanted (feat. Dave) - Edit  ,  It's Like  ,  Doing the Most (feat. Lil Dotz)  ,  Freddy  ,  Netflix & Chill  ,  Scorpion  ,  Hickory Dickory Dock  ,  Daily Duppy (feat. GRM Daily)
        ### All I Ever Wanted (feat. Dave)  ---> [['Fredo']]
        ### Survival of the Fittest  ---> [['Fredo']]
        ### Mmhm  ---> [['Fredo']]
        ### Property Picking  ---> [['Fredo']]
        ### BMT  ---> [['Fredo']]
        ### Morning  ---> [['Fredo']]
        ### All I Ever Wanted (feat. Dave) - Edit  ---> [['Fredo']]
        ### It's Like  ---> [['Fredo']]
        ### Doing the Most (feat. Lil Dotz)  ---> [['Fredo']]
        ### Freddy  ---> [['Fredo']]
        ### Netflix & Chill  ---> [['Fredo']]
        ### Scorpion  ---> [['Fredo']]
        ### Hickory Dickory Dock  ---> [['Fredo']]
        ### Daily Duppy (feat. GRM Daily)  ---> [['Fredo', 'J Hus', 'Aitch']]


        addAllMusic(mdbmaps, "Spotify", "9b13ec1938dd55abe4ac8016f7cd4add", "mn0003831796")   ### [iann dior]
        ### gone girl  ,  Sick and Tired  ,  Prospect (ft. Lil Baby)  ,  Sick and Tired (ft. Machine Gun Kelly and Travis Barker)  ,  Pretty Girls  ,  Holding On
        ### gone girl  ---> [['iann dior']]
        ### Sick and Tired  ---> [['iann dior']]
        ### Prospect (ft. Lil Baby)  ---> [['iann dior']]
        ### Sick and Tired (ft. Machine Gun Kelly and Travis Barker)  ---> [['iann dior']]
        ### Pretty Girls  ---> [['iann dior']]
        ### Holding On  ---> [['iann dior']]


        addDeezer(mdbmaps, "Spotify", "f3ac90c0c8754411c8568855e282758f", "58568762")    ### [Camilo]
        ### Tutu  ,  Favorito  ,  Por Primera Vez  ,  El Mismo Aire - con Pablo Alborán  ,  Vida de Rico  ,  BEBÉ
        ### Tutu  ---> [['Camilo']]
        ### Favorito  ---> [['Camilo']]
        ### Por Primera Vez  ---> [['Camilo']]
        ### El Mismo Aire - con Pablo Alborán  ---> [['Camilo']]
        ### Vida de Rico  ---> [['Camilo']]
        ### BEBÉ  ---> [['Camilo']]


        addDeezer(mdbmaps, "Spotify", "9b8c2fb10557c1afa63ee0b1dcc038d0", "174348")    ### [Rudimental]
        ### These Days (feat. Jess Glynne, Macklemore & Dan Caplen)  ,  Sun Comes Up (feat. James Arthur)  ,  These Days (feat. Jess Glynne, Macklemore & Dan Caplen) - AJR Remix  ,  Come Over (feat. Anne-Marie & Tion Wayne)  ,  Let Me Live (feat. Anne-Marie & Mr Eazi)
        ### These Days (feat. Jess Glynne, Macklemore & Dan Caplen)  ---> [['Rudimental']]
        ### Sun Comes Up (feat. James Arthur)  ---> [['Rudimental']]
        ### These Days (feat. Jess Glynne, Macklemore & Dan Caplen) - AJR Remix  ---> [['Rudimental']]
        ### Come Over (feat. Anne-Marie & Tion Wayne)  ---> [['Rudimental']]
        ### Let Me Live (feat. Anne-Marie & Mr Eazi)  ---> [['Rudimental']]


        addDeezer(mdbmaps, "Spotify", "afc079aca597ffc2cf0d9ff6b238493e", "1018354")    ### [Jaden]
        ### Breakfast (feat. A$AP Rocky)  ,  Icon  ,  GHOST  ,  Falling For You with Justin Bieber
        ### Breakfast (feat. A$AP Rocky)  ---> [['Jaden']]
        ### Icon  ---> [['Jaden']]
        ### GHOST  ---> [['Jaden']]
        ### Falling For You with Justin Bieber  ---> [['Jaden']]


        addAllMusic(mdbmaps, "Spotify", "1bda2352db021f2f1c458d5b0d0a3d2a", "mn0003666177")   ### [Tion Wayne]
        ### Drive By  ,  2 ON 2 - Tion Wayne x JAY1  ,  I Dunno (feat. Dutchavelli & Stormzy)  ,  Deluded (feat. MIST)
        ### Drive By  ---> [['Tion Wayne']]
        ### 2 ON 2 - Tion Wayne x JAY1  ---> [['Tion Wayne']]
        ### I Dunno (feat. Dutchavelli & Stormzy)  ---> [['Tion Wayne']]
        ### Deluded (feat. MIST)  ---> [['Tion Wayne']]


        addDeezer(mdbmaps, "Spotify", "d0338be794417cbcd282faacdf56e7b2", "103925422")    ### [Shelley FKA DRAM]
        ### Broccoli (feat. Lil Yachty)  ,  Cash Machine  ,  Ill Nana (feat. Trippie Redd)
        ### Broccoli (feat. Lil Yachty)  ---> [['Shelley FKA DRAM']]
        ### Cash Machine  ---> [['Shelley FKA DRAM']]
        ### Ill Nana (feat. Trippie Redd)  ---> [['Shelley FKA DRAM']]


        addDeezer(mdbmaps, "Spotify", "e119b28369d7338f2fb711d5ba5af521", "68294032")    ### [City Girls]
        ### Twerk (feat. Cardi B)  ,  Act Up  ,  Pussy Talk
        ### Twerk (feat. Cardi B)  ---> [['City Girls']]
        ### Act Up  ---> [['City Girls']]
        ### Pussy Talk  ---> [['City Girls']]


        addDeezer(mdbmaps, "Spotify", "7f960d8077f47e6211a1b6101da49c44", "186333922")    ### [Myke Towers]
        ### Girl  ,  Diosa  ,  Bandido
        ### Girl  ---> [['Myke Towers']]
        ### Diosa  ---> [['Myke Towers']]
        ### Bandido  ---> [['Myke Towers']]


        addAllMusic(mdbmaps, "Spotify", "36ef0b95471fba19bb05672eaa6b508b", "mn0003635492")    ### [Luísa Sonza]
        ### BRABA  ,  MODO TURBO
        ### BRABA  ---> [['Luísa Sonza']]
        ### MODO TURBO  ---> [['Luísa Sonza']]


        addDeezer(mdbmaps, "Spotify", "888a58e5175178be30c36430f3d6e251", "12632197")    ### [Luciano]
        ### Mios mit Bars  ,  Never Know (feat. SHIRIN DAVID)
        ### Mios mit Bars  ---> [['Luciano']]
        ### Never Know (feat. SHIRIN DAVID)  ---> [['Luciano']]


        addDeezer(mdbmaps, "Spotify", "a1e6008f768d61088c23320a31d36da6", "11471022")    ### [Rich Music LTD]
        ### Quizas  ,  Perreo en La Luna
        ### Quizas  ---> [['Rich Music LTD']]
        ### Perreo en La Luna  ---> [['Rich Music LTD']]


        addDeezer(mdbmaps, "Spotify", "936ca415b10063a7cd43c9d48ada2418", "61474832")    ### [Os Barões Da Pisadinha]
        ### Recairei - Ao Vivo  ,  Basta Você Me Ligar - Ao Vivo
        ### Recairei - Ao Vivo  ---> [['Os Barões Da Pisadinha']]
        ### Basta Você Me Ligar - Ao Vivo  ---> [['Os Barões Da Pisadinha']]


        addDeezer(mdbmaps, "Spotify", "03b8317039fc009fc4c0a8a8313e568e", "7806020")    ### [Hearts & Colors]
        ### Lighthouse - Andrelli Remix  ,  For The Love
        ### Lighthouse - Andrelli Remix  ---> [['Hearts & Colors']]
        ### For The Love  ---> [['Hearts & Colors']]


        addAllMusic(mdbmaps, "Spotify", "a8e652cd43dc34ab4bdb692d56466f9e", "mn0003449425")   ### [Nea!]
        addDeezer(mdbmaps, "Spotify", "a8e652cd43dc34ab4bdb692d56466f9e", "5522988")    ### [Nea!]
        ### Some Say  ,  Some Say - Felix Jaehn Remix
        ### Some Say  ---> [['Nea!']]
        ### Some Say - Felix Jaehn Remix  ---> [['Nea!']]


        addDeezer(mdbmaps, "Spotify", "dc4240109e2af8013c233430b6aaa337", "13817211")    ### [Tate McRae]
        ### you broke me first  ,  stupid
        ### you broke me first  ---> [['Tate McRae']]
        ### stupid  ---> [['Tate McRae']]


        addDeezer(mdbmaps, "Spotify", "5a9df0171095c2d1afcdf5d1d9940e96", "7418694")    ### [Renée Elise Goldsberry]
        ### Satisfied  ,  The Schuyler Sisters
        ### Satisfied  ---> [['Renée Elise Goldsberry']]
        ### The Schuyler Sisters  ---> [['Renée Elise Goldsberry']]


        addDeezer(mdbmaps, "Spotify", "725df10a8a0db29dc019cff55134352c", "419254")    ### [Kina]
        ### Get You The Moon (feat. Snøw)  ,  Can We Kiss Forever?
        ### Get You The Moon (feat. Snøw)  ---> [['Kina']]
        ### Can We Kiss Forever?  ---> [['Kina']]


        addDeezer(mdbmaps, "Spotify", "15e047fa2c584fa6ef1c2cfd9f9b5a5f", "5128930")    ### [Remedee]
        ### Love of My Life (feat. Not3s & Young Adz)
        ### Love of My Life (feat. Not3s & Young Adz)  ---> [['Remedee']]


        addDeezer(mdbmaps, "Spotify", "547ffddc954a43b9759e2442b8d1b53b", "49141701")    ### [Only The Family]
        ### Crazy Story
        ### Crazy Story  ---> [['Only The Family']]


        addDeezer(mdbmaps, "Spotify", "18ce2abc5a3a677421e6bb9e343574c9", "11033960")    ### [Dadá Boladão]
        ### Surtada - Remix Brega Funk
        ### Surtada - Remix Brega Funk  ---> [['Dadá Boladão']]


        addDeezer(mdbmaps, "Spotify", "27deaa920a8bc22fd532b7c35d2dee8f", "65303292")    ### [Gambi]
        ### Dans l'espace (feat. Heuss l'Enfoiré)
        ### Dans l'espace (feat. Heuss l'Enfoiré)  ---> [['Gambi']]


        addDeezer(mdbmaps, "Spotify", "3796439c84cc6cf5962fff10473969e6", "483061")    ### [Bas]
        ### Tribe (with J. Cole)
        ### Tribe (with J. Cole)  ---> [['Bas']]


        addAllMusic(mdbmaps, "Spotify", "3fc03e0fcd8f66f63f768776bad7f8c5", "mn0002970632")   ### [BEN & TAN]
        addDeezer(mdbmaps, "Spotify", "3fc03e0fcd8f66f63f768776bad7f8c5", "83104852")    ### [BEN & TAN]
        ### YES
        ### YES  ---> [['BEN & TAN']]


        addDeezer(mdbmaps, "Spotify", "c54b8fef28b706d7a5523126b3661f10", "50258612")    ### [MC Kevin o Chris]
        ### Medley da Gaiola - DENNIS Remix  ,  Eu Vou pro Baile da Gaiola  ,  Tu Tá na Gaiola - Radio Edit  ,  Finalidade Era Ficar em Casa  ,  Dentro do Carro  ,  Vamos pra Gaiola  ,  Sobe Balão Desce Princesa  ,  Ela É do Tipo  ,  Evoluiu  ,  Namorar Não Dá  ,  Resenha lá em casa  ,  Morena Cor do Pecado  ,  Ela É do Tipo (feat. Drake) - Remix  ,  Romance Proibido - Ao Vivo  ,  Pode Jogar  ,  Romance Proibido
        ### Medley da Gaiola - DENNIS Remix  ---> [['MC Kevin o Chris']]
        ### Eu Vou pro Baile da Gaiola  ---> [['MC Kevin o Chris']]
        ### Tu Tá na Gaiola - Radio Edit  ---> [['MC Kevin o Chris']]
        ### Finalidade Era Ficar em Casa  ---> [['MC Kevin o Chris']]
        ### Dentro do Carro  ---> [['MC Kevin o Chris']]
        ### Vamos pra Gaiola  ---> [['MC Kevin o Chris']]
        ### Sobe Balão Desce Princesa  ---> [['MC Kevin o Chris']]
        ### Ela É do Tipo  ---> [['MC Kevin o Chris']]
        ### Evoluiu  ---> [['MC Kevin o Chris']]
        ### Namorar Não Dá  ---> [['MC Kevin o Chris']]
        ### Resenha lá em casa  ---> [['MC Kevin o Chris']]
        ### Morena Cor do Pecado  ---> [['MC Kevin o Chris']]
        ### Ela É do Tipo (feat. Drake) - Remix  ---> [['MC Kevin o Chris']]
        ### Romance Proibido - Ao Vivo  ---> [['MC Kevin o Chris']]
        ### Pode Jogar  ---> [['MC Kevin o Chris']]
        ### Romance Proibido  ---> [['MC Kevin o Chris']]


        addDeezer(mdbmaps, "Spotify", "e192061642f69f993f2a80f614b334b7", "7765128")    ### [ANAVITÓRIA]
        ### Agora Eu Quero Ir  ,  Singular  ,  Trevo (Tu)  ,  Cor De Marte  ,  Fica  ,  Fica - Bonus Track  ,  Ai, Amor  ,  Porque Eu Te Amo  ,  Cecília  ,  Calendário  ,  Outrória  ,  Perdoa  ,  Pupila  ,  relicário  ,  Me conta da tua janela  ,  não passa vontade
        ### Agora Eu Quero Ir  ---> [['ANAVITÓRIA']]
        ### Singular  ---> [['ANAVITÓRIA']]
        ### Trevo (Tu)  ---> [['ANAVITÓRIA']]
        ### Cor De Marte  ---> [['ANAVITÓRIA']]
        ### Fica  ---> [['ANAVITÓRIA']]
        ### Fica - Bonus Track  ---> [['ANAVITÓRIA']]
        ### Ai, Amor  ---> [['ANAVITÓRIA']]
        ### Porque Eu Te Amo  ---> [['ANAVITÓRIA']]
        ### Cecília  ---> [['ANAVITÓRIA']]
        ### Calendário  ---> [['ANAVITÓRIA']]
        ### Outrória  ---> [['ANAVITÓRIA']]
        ### Perdoa  ---> [['ANAVITÓRIA']]
        ### Pupila  ---> [['ANAVITÓRIA']]
        ### relicário  ---> [['ANAVITÓRIA']]
        ### Me conta da tua janela  ---> [['ANAVITÓRIA']]
        ### não passa vontade  ---> [['ANAVITÓRIA']]


        addDeezer(mdbmaps, "Spotify", "cccfbce4f5b1fc2b0c9714715951173f", "4448284")    ### [DENNIS]
        ### Malandramente  ,  Automaticamente  ,  Coração Tá Gelado (feat. MC TH)  ,  Um Brinde (feat. Marília Mendonça & Maiara & Maraisa)  ,  Vou Pegar  ,  Só Você  ,  Eu Te Amo Tanto  ,  Agora é Tudo Meu  ,  Sou Teu Fã  ,  Ninguém Conta Pra Ninguém  ,  Apimentadíssima  ,  Te Prometo  ,  Isso Que é Vida
        ### Malandramente  ---> [['DENNIS']]
        ### Automaticamente  ---> [['DENNIS']]
        ### Coração Tá Gelado (feat. MC TH)  ---> [['DENNIS']]
        ### Um Brinde (feat. Marília Mendonça & Maiara & Maraisa)  ---> [['DENNIS']]
        ### Vou Pegar  ---> [['DENNIS']]
        ### Só Você  ---> [['DENNIS', 'Leo Santana', 'MC Rogerinho']]
        ### Eu Te Amo Tanto  ---> [['DENNIS']]
        ### Agora é Tudo Meu  ---> [['DENNIS']]
        ### Sou Teu Fã  ---> [['DENNIS']]
        ### Ninguém Conta Pra Ninguém  ---> [['DENNIS']]
        ### Apimentadíssima  ---> [['DENNIS']]
        ### Te Prometo  ---> [['DENNIS']]
        ### Isso Que é Vida  ---> [['DENNIS']]


        addDeezer(mdbmaps, "Spotify", "e36c00d0c30e3e95d4fdd3e6fdd611fb", "5918943")    ### [Mc Livinho]
        ### Tudo de Bom  ,  Cheia de Marra  ,  Tenebrosa  ,  Fazer Falta  ,  Tchau e Bença  ,  Esse Dom  ,  Azul Piscina  ,  Rebeca  ,  Irmã Gostosa  ,  Hoje Eu Vou Parar Na Gaiola  ,  Se Prepara 2
        ### Tudo de Bom  ---> [['Mc Livinho']]
        ### Cheia de Marra  ---> [['Mc Livinho']]
        ### Tenebrosa  ---> [['Mc Livinho']]
        ### Fazer Falta  ---> [['Mc Livinho']]
        ### Tchau e Bença  ---> [['Mc Livinho']]
        ### Esse Dom  ---> [['Mc Livinho']]
        ### Azul Piscina  ---> [['Mc Livinho']]
        ### Rebeca  ---> [['Mc Livinho']]
        ### Irmã Gostosa  ---> [['Mc Livinho']]
        ### Hoje Eu Vou Parar Na Gaiola  ---> [['Mc Livinho']]
        ### Se Prepara 2  ---> [['Mc Livinho']]


        addDeezer(mdbmaps, "Spotify", "6c0d044b61b4c03d8b9cfd1b477f4cd7", "1444643")    ### [Jerry Smith]
        ### Pode Se Soltar  ,  Troféu do Ano  ,  Nossa Que Absurdo  ,  Menina Braba  ,  Não Se Apaixona  ,  Kikadinha  ,  Vou Falar Pra Tu  ,  Quem Tem o Dom  ,  Os Boys Amam O Ex Chora  ,  Bumbum Granada
        ### Pode Se Soltar  ---> [['Jerry Smith']]
        ### Troféu do Ano  ---> [['Jerry Smith']]
        ### Nossa Que Absurdo  ---> [['Jerry Smith']]
        ### Menina Braba  ---> [['Jerry Smith']]
        ### Não Se Apaixona  ---> [['Jerry Smith']]
        ### Kikadinha  ---> [['Jerry Smith']]
        ### Vou Falar Pra Tu  ---> [['Jerry Smith']]
        ### Quem Tem o Dom  ---> [['Jerry Smith']]
        ### Os Boys Amam O Ex Chora  ---> [['Jerry Smith']]
        ### Bumbum Granada  ---> [["Mc's Zaac & Jerry Smith"]]


        addDeezer(mdbmaps, "Spotify", "28415568dbefa7a338bafbb7cd9e483e", "8403120")    ### [Mc Don Juan]
        ### Oh Novinha  ,  Lei do Retorno  ,  A Gente Brigou  ,  Se Eu Tiver Solteiro  ,  Amar Amei  ,  Os Opostos Se Atraem  ,  To Gostando Tanto de Você  ,  Bye Bye  ,  Sai Pra Lá  ,  Vai Ter Que Aguentar
        ### Oh Novinha  ---> [['Mc Don Juan']]
        ### Lei do Retorno  ---> [['Mc Don Juan']]
        ### A Gente Brigou  ---> [['Mc Don Juan']]
        ### Se Eu Tiver Solteiro  ---> [['Mc Don Juan']]
        ### Amar Amei  ---> [['Mc Don Juan']]
        ### Os Opostos Se Atraem  ---> [['Mc Don Juan']]
        ### To Gostando Tanto de Você  ---> [['Mc Don Juan']]
        ### Bye Bye  ---> [['Mc Don Juan']]
        ### Sai Pra Lá  ---> [['Mc Don Juan']]
        ### Vai Ter Que Aguentar  ---> [['Mc Don Juan']]


        addDeezer(mdbmaps, "Spotify", "e454489dc33686e16c66bf855deffc1e", "12896823")    ### [Pineapple StormTv]
        ### Poesia Acústica #3: Capricorniana  ,  Poesia Acústica #4: Todo Mundo Odeia Acústico  ,  Poesia Acústica #6: Era uma Vez  ,  Você Não Ama Ninguém  ,  Canção Infantil  ,  Poesia Acústica #7: Céu Azul  ,  Poesia Acústica #8: Amor e Samba  ,  Poesia Acústica - Paris  ,  Poesia Acústica #9: Melhor Forma  ,  Poesia Acústica 10: Recomeçar
        ### Poesia Acústica #3: Capricorniana  ---> [['Pineapple StormTv']]
        ### Poesia Acústica #4: Todo Mundo Odeia Acústico  ---> [['Pineapple StormTv']]
        ### Poesia Acústica #6: Era uma Vez  ---> [['Pineapple StormTv']]
        ### Você Não Ama Ninguém  ---> [['Pineapple StormTv']]
        ### Canção Infantil  ---> [['Pineapple StormTv']]
        ### Poesia Acústica #7: Céu Azul  ---> [['Pineapple StormTv']]
        ### Poesia Acústica #8: Amor e Samba  ---> [['Pineapple StormTv']]
        ### Poesia Acústica - Paris  ---> [['Pineapple StormTv']]
        ### Poesia Acústica #9: Melhor Forma  ---> [['Pineapple StormTv']]
        ### Poesia Acústica 10: Recomeçar  ---> [['Pineapple StormTv']]


        addDeezer(mdbmaps, "Spotify", "3aa9736661f70b6db7f291368dbeba82", "54330242")    ### [Grupo Menos É Mais]
        ### Melhor Eu Ir / Ligando os Fatos / Sonho de Amor / Deixa Eu Te Querer - Ao Vivo  ,  Fatalmente / Separação / Temporal - Ao Vivo  ,  Tempo de Aprender / Energia Surreal / Não Pedi Pra Me Apaixonar - Ao Vivo  ,  Recaída  ,  Vai Me Dando Corda - Ao Vivo  ,  Pot-Pourri: Melhor Eu Ir / Ligando Os Fatos / Sonho de Amor / Deixa Eu Te Querer - Ao Vivo  ,  Pot-Pourri: Tempo de Aprender / Energia Surreal / Não Pedi Pra Me Apaixonar / Deixa Acontecer - Ao Vivo  ,  Adorei
        ### Melhor Eu Ir / Ligando os Fatos / Sonho de Amor / Deixa Eu Te Querer - Ao Vivo  ---> [['Grupo Menos É Mais']]
        ### Fatalmente / Separação / Temporal - Ao Vivo  ---> [['Grupo Menos É Mais']]
        ### Tempo de Aprender / Energia Surreal / Não Pedi Pra Me Apaixonar - Ao Vivo  ---> [['Grupo Menos É Mais']]
        ### Recaída  ---> [['Grupo Menos É Mais']]
        ### Vai Me Dando Corda - Ao Vivo  ---> [['Grupo Menos É Mais']]
        ### Pot-Pourri: Melhor Eu Ir / Ligando Os Fatos / Sonho de Amor / Deixa Eu Te Querer - Ao Vivo  ---> [['Grupo Menos É Mais']]
        ### Pot-Pourri: Tempo de Aprender / Energia Surreal / Não Pedi Pra Me Apaixonar / Deixa Acontecer - Ao Vivo  ---> [['Grupo Menos É Mais']]


        addDeezer(mdbmaps, "Spotify", "c3c2fee2ed2b90b15559cf2fe290d21a", "5454687")    ### [Hungria Hip Hop]
        ### Coração de Aço  ,  Não Troco  ,  Beijo Com Trap  ,  Chovendo Inimigo  ,  Um Pedido  ,  Amor e Fé - Acústico  ,  Um Brinde pra Nós
        ### Coração de Aço  ---> [['Hungria Hip Hop']]
        ### Não Troco  ---> [['Hungria Hip Hop']]
        ### Beijo Com Trap  ---> [['Hungria Hip Hop']]
        ### Chovendo Inimigo  ---> [['Hungria Hip Hop']]
        ### Um Pedido  ---> [['Hungria Hip Hop']]
        ### Amor e Fé - Acústico  ---> [['Hungria Hip Hop']]
        ### Um Brinde pra Nós  ---> [['Hungria Hip Hop']]


        addDeezer(mdbmaps, "Spotify", "a8957d2b795d9ce2b9ce8e9c105214c5", "5817388")    ### [Vitão]
        ### Caderninho  ,  Café  ,  Embrasa  ,  Edredom  ,  Complicado  ,  7 Chamadas  ,  Flores
        ### Caderninho  ---> [['Vitão']]
        ### Café  ---> [['Vitão']]
        ### Embrasa  ---> [['Vitão']]
        ### Edredom  ---> [['Vitão']]
        ### Complicado  ---> [['Vitão']]
        ### 7 Chamadas  ---> [['Vitão']]
        ### Flores  ---> [['Vitão']]


        addDeezer(mdbmaps, "Spotify", "ce6b0fcfbfe491d0f041f651c0b2789b", "262833")    ### [IZA]
        ### Pesadão (Participação especial Marcelo Falcão)  ,  Ginga (Participação especial de Rincon Sapiência)  ,  Bateu (Participação especial de Ruxell)  ,  Dona de mim  ,  Brisa  ,  Meu talismã
        ### Pesadão (Participação especial Marcelo Falcão)  ---> [['IZA']]
        ### Ginga (Participação especial de Rincon Sapiência)  ---> [['IZA']]
        ### Bateu (Participação especial de Ruxell)  ---> [['IZA']]
        ### Dona de mim  ---> [['IZA']]
        ### Brisa  ---> [['IZA']]
        ### Meu talismã  ---> [['IZA']]


        addDeezer(mdbmaps, "Spotify", "3cc7512b8b8e3d08ddc79bc24f0f7b39", "11922823")    ### [UM44K]
        ### 4 da manhã  ,  Nossa música  ,  Solução  ,  Grupo bom  ,  Tudo que sonhamos
        ### 4 da manhã  ---> [['UM44K']]
        ### Nossa música  ---> [['UM44K']]
        ### Solução  ---> [['UM44K']]
        ### Grupo bom  ---> [['UM44K']]
        ### Tudo que sonhamos  ---> [['UM44K']]


        addDeezer(mdbmaps, "Spotify", "7042b99191e72f4e0b460c4a0c3a386a", "13552757")    ### [MC Paulin da Capital]
        ### Eu Achei  ,  Mulher Cativante  ,  Morena  ,  SET DJ GM 2.0  ,  Os Mandrake Curte a Vida
        ### Eu Achei  ---> [['MC Paulin da Capital']]
        ### Mulher Cativante  ---> [['MC Paulin da Capital']]
        ### Morena  ---> [['Vitor Kley', 'Pezão', 'MC Paulin da Capital']]
        ### SET DJ GM 2.0  ---> [['MC Paulin da Capital']]
        ### Os Mandrake Curte a Vida  ---> [['MC Paulin da Capital']]


        addDeezer(mdbmaps, "Spotify", "4cb02ca3a3eda63bf7b84ed8c48e99cf", "7351232")    ### [Lexa]
        ### Sapequinha  ,  Provocar  ,  Só Depois do Carnaval  ,  Chama Ela (feat. Pedro Sampaio)  ,  Aquecimento da Lexa
        ### Sapequinha  ---> [['Lexa']]
        ### Provocar  ---> [['Lexa']]
        ### Só Depois do Carnaval  ---> [['Lexa']]
        ### Chama Ela (feat. Pedro Sampaio)  ---> [['Lexa']]
        ### Aquecimento da Lexa  ---> [['Lexa']]


        addDeezer(mdbmaps, "Spotify", "d458eab92baed6ed1e33633b0b47e280", "11136556")    ### [Baco Exu do Blues]
        ### Me Desculpa Jay Z  ,  Flamingos  ,  Bluesman  ,  Queima Minha Pele  ,  Girassóis de Van Gogh
        ### Me Desculpa Jay Z  ---> [['Baco Exu do Blues']]
        ### Flamingos  ---> [['Baco Exu do Blues']]
        ### Bluesman  ---> [['Baco Exu do Blues']]
        ### Queima Minha Pele  ---> [['Baco Exu do Blues']]
        ### Girassóis de Van Gogh  ---> [['Baco Exu do Blues']]


        addDeezer(mdbmaps, "Spotify", "e241d579493d1d3c11e1cd8040674d6a", "13025953")    ### [WC no Beat]
        ### Meu Mundo  ,  Nossa Que Isso (feat. Mc Rebecca & MC Rogê)  ,  BALANÇA (feat. Pedro Sampaio)  ,  SEM LIMITES  ,  BALANÇA
        ### Meu Mundo  ---> [['WC no Beat']]
        ### Nossa Que Isso (feat. Mc Rebecca & MC Rogê)  ---> [['WC no Beat']]
        ### BALANÇA (feat. Pedro Sampaio)  ---> [['WC no Beat']]
        ### SEM LIMITES  ---> [['WC no Beat']]
        ### BALANÇA  ---> [['WC no Beat']]


        addDeezer(mdbmaps, "Spotify", "c0571f0ebfbd74bfeb54e13959346741", "13139755")    ### [MC JottaPê]
        ### Sentou e Gostou  ,  Eterna Sacanagem  ,  Bate Palma  ,  Nem Guindaste  ,  Ménage
        ### Sentou e Gostou  ---> [['MC JottaPê']]
        ### Eterna Sacanagem  ---> [['MC JottaPê']]
        ### Bate Palma  ---> [['MC JottaPê']]
        ### Nem Guindaste  ---> [['MC JottaPê']]
        ### Ménage  ---> [['MC JottaPê']]


        addDeezer(mdbmaps, "Spotify", "95a2a5c802758e9f2c8761f7edcdadf1", "9596260")    ### [Dj Guuga]
        ### Vidrado Em Você  ,  7 Dias 7 Corpos  ,  Cabaré  ,  Ta Apaixonado Babaca
        ### Vidrado Em Você  ---> [['Dj Guuga']]
        ### 7 Dias 7 Corpos  ---> [['Dj Guuga']]
        ### Cabaré  ---> [['Dj Guuga']]
        ### Ta Apaixonado Babaca  ---> [['Dj Guuga']]


        addDeezer(mdbmaps, "Spotify", "58b1be9190abc201770618f3a10f0001", "7554724")    ### [Costa Gold]
        ### Nada Bom II  ,  Dás Arábia, Pt. 2  ,  Irmão DQbrada!  ,  Uau!
        ### Nada Bom II  ---> [['Costa Gold']]
        ### Dás Arábia, Pt. 2  ---> [['Costa Gold']]
        ### Irmão DQbrada!  ---> [['Costa Gold']]
        ### Uau!  ---> [['Costa Gold']]


        addDeezer(mdbmaps, "Spotify", "1376c567f2863d7dc459f14e2259696a", "10672471")    ### [Mano Walter]
        ### Não Deixo Não  ,  Juramento do Dedinho  ,  Então Vem Cá - Ao Vivo  ,  Fingindo Maturidade - Ao Vivo
        ### Não Deixo Não  ---> [['Mano Walter']]
        ### Juramento do Dedinho  ---> [['Mano Walter']]
        ### Então Vem Cá - Ao Vivo  ---> [['Mano Walter']]
        ### Fingindo Maturidade - Ao Vivo  ---> [['Mano Walter']]


        addDeezer(mdbmaps, "Spotify", "a4edd8f5827956ce28295f63fb5671fa", "1107447")    ### [Orochi]
        ### Balão  ,  Acende o Isqueiro  ,  Amor de Fim de Noite  ,  Mitsubishi
        ### Balão  ---> [['Orochi']]
        ### Acende o Isqueiro  ---> [['Orochi']]
        ### Amor de Fim de Noite  ---> [['Orochi']]
        ### Mitsubishi  ---> [['Orochi']]


        addDeezer(mdbmaps, "Spotify", "ff269d9a5ac2c852f71495cdb576df7b", "5832280")    ### [Xand Avião]
        ### Casal Raiz - Ao Vivo  ,  Algo Mais (Amante) - Ao Vivo  ,  Ela Aperta a Minha Mente  ,  Surra de Cama
        ### Casal Raiz - Ao Vivo  ---> [['Xand Avião']]
        ### Algo Mais (Amante) - Ao Vivo  ---> [['Xand Avião']]
        ### Ela Aperta a Minha Mente  ---> [['Xand Avião']]
        ### Surra de Cama  ---> [['Xand Avião']]


        addDeezer(mdbmaps, "Spotify", "435ff6dc0e86bb99af2f13e7a2a9e826", "398961")    ### [Pk]
        ### Quando a vontade bater (Participação especial de PK Delas)  ,  Do jeito que tu gosta  ,  Indomável (Participação especial de Belo)  ,  Tudo de bom
        ### Quando a vontade bater (Participação especial de PK Delas)  ---> [['Pk']]
        ### Do jeito que tu gosta  ---> [['Pk']]
        ### Indomável (Participação especial de Belo)  ---> [['Pk']]
        ### Tudo de bom  ---> [['Pk']]


        addDeezer(mdbmaps, "Spotify", "5decc01916c5a93c4a8924f25a5cd266", "10640291")    ### [1Kilo]
        ### Deixe Me Ir - Acústico  ,  Duro Igual Concreto  ,  Tenta Vir - Acústico  ,  Só por Hoje
        ### Deixe Me Ir - Acústico  ---> [['1Kilo']]
        ### Duro Igual Concreto  ---> [['1Kilo']]
        ### Tenta Vir - Acústico  ---> [['1Kilo']]
        ### Só por Hoje  ---> [['1Kilo']]

        
        
        
        mdbmaps["Spotify"].save()
        
        
def extraAddsForBillboard(mdbmaps, chartType):
    print("Adding known artist data for {0}".format(chartType))


    if chartType == "Billboard":
        addAllMusic(mdbmaps, "Billboard", "89eab0113dd350e54cc04867d4cbcc04", "mn0000184098")   ### [John McDermott]
        addDiscogs(mdbmaps, "Billboard", "89eab0113dd350e54cc04867d4cbcc04", "1436273")    ### [John McDermott]
        ## The Irish Tenors: Home For Christmas  ,  The Irish Tenors: Live In Belfast  ,  The Irish Tenors: Ellis Island  ,  The Irish Tenors: Live In Belfast  ,  The Irish Tenors: Ellis Island

        addAllMusic(mdbmaps, "Billboard", "b66b1bfa1a8b0725ba1f139b87ad3a4c", "mn0000231468")   ### [Loon]
        ### I Need A Girl (Part Two)  ,  I Don't Wanna Know

        addAllMusic(mdbmaps, "Billboard", "a6fbf98a79a048834d50ce68d67ad442", "mn0000621112")   ### Mya
        addDiscogs(mdbmaps, "Billboard", "a6fbf98a79a048834d50ce68d67ad442", "28738")    ### Mya
        ### Case Of The Ex (Whatcha Gonna Do)  ,  Lady Marmalade

        addAllMusic(mdbmaps, "Billboard", "832b5faffd094a5ab3b22f67d40db4b7", "mn0001049094")   ### [RKM]
        ### Masterpiece: Nuestra Obra Maestra

        addDiscogs(mdbmaps, "Billboard", "808c8b3a9909c7d7a3e5753792d1b995", "150433")    ### [LV]
        ### Gangsta's Paradise (From "Dangerous Minds")        

        addAllMusic(mdbmaps, "Billboard", "5dab93d7de7fdc41568fc96e979119e3", "mn0003740957")   ### [Dave Rowland]
        ### The Door Is Always Open  ,  Tear Time  ,  Golden Tears        
                
        addAllMusic(mdbmaps, "Billboard", "ba6cb719ca53bf4f57ecdcd6bd342bf5", "mn0000233423")   ### [Magoo]
        ### Up Jumps Da Boogie  ,  Promiscuous  ,  Give It To Me  ,  The Way I Are  ,  Apologize  ,  4 Minutes  ,  Say Something
                
        addAllMusic(mdbmaps, "Billboard", "0a241c0c620c9e4ca09d08411fee5d05", "mn0001225951")   ### [Mustard]
        ### Perfect Ten  ,  Ballin'

        addDiscogs(mdbmaps, "Billboard", "45908a9da68e8f594c1d999e8567a3bf", "4995184")    ### [John P. Kee & The New Life Community Choir]
        ### We Walk By Faith  ,  Blessed By Association  ,  Life And Favor

        addAllMusic(mdbmaps, "Billboard", "4096687a46c1090d4a07bc966950532d", "mn0000062200")   ### [Bernie Williams]
        ### Go For It  ,  Ritmo De Otono

        addAllMusic(mdbmaps, "Billboard", "4eb35c41efdc8495ebca5e64cb723217", "mn0003744642")   ### [Jeff Ryan]
        ### Up And Up

        addAllMusic(mdbmaps, "Billboard", "16e8a230f1803bf0b17e07f6e39225e3", "mn0000015398")   ### [Paul Brown]
        ### Winelite  ,  The Rhythm Method  ,  The Funky Joint  ,  Put It Where You Want It  ,  Hush  ,  Boogaloo  ,  Backstage Pass  ,  Piccadilly Circus

        addAllMusic(mdbmaps, "Billboard", "99ccbacd8a76cd01ae7f124c403d252b", "mn0000066318")   ### [Paul Taylor]
        ### Burnin'  ,  Push To Start  ,  Supernova

        addAllMusic(mdbmaps, "Billboard", "f26553a1fbca28fe7eac06b302323598", "mn0000772721")   ### [Incognito]
        ### Let's Take It Back
        
        addAllMusic(mdbmaps, "Billboard", "06a8a5a8878d609887f852796a1c1be5", "mn0001426855")   ### [Arcángel]
        ### Sentimiento, Elegancia & Maldad  ,  Tu Cuerpo Me Hace Bien  ,  Diosa de Los Corazones  ,  Zum Zum
        ### Sentimiento, Elegancia & Maldad  ---> [['Arcángel']]
        ### Tu Cuerpo Me Hace Bien  ---> [['Arcángel']]
        ### Diosa de Los Corazones  ---> [['Arcangel /Zion & Lennox/Lobo/RKM & Ken-Y']]
        ### Zum Zum  ---> [['Daddy Yankee x RKM & Ken-Y x Arcangel']]


        addAllMusic(mdbmaps, "Billboard", "1a437e23ad6fb8d3077e86589b52a1a3", "mn0000306033")   ### [Lucero]
        ### Siempre Contigo  ,  Un Lu* Jo
        ### Siempre Contigo  ---> [['Lucero']]
        ### Un Lu* Jo  ---> [['Lucero & Joan Sebastian']]


        addAllMusic(mdbmaps, "Billboard", "4b8310b8cd692ffb4a081e8bb4f69ed9", "mn0000005455")   ### [Pandora]
        ### Desde El Dia Que Te Fuiste
        ### Desde El Dia Que Te Fuiste  ---> [['Pandora']]


        addAllMusic(mdbmaps, "Billboard", "ebec67096eb6d66f673ff4737c9b379c", "mn0000268299")   ### [Jose Y Durval]
        ### Guadalupe
        ### Guadalupe  ---> [['Jose Y Durval']]


        addAllMusic(mdbmaps, "Billboard", "e75095d73c04898447d4658e618263f3", "mn0000345971")   ### [Jessie Morales: El Original De La Sierra]
        ### Homenaje A Chalino Sanchez
        ### Homenaje A Chalino Sanchez  ---> [['Jessie Morales: El Original De La Sierra']]


        addAllMusic(mdbmaps, "Billboard", "bff236756e7bf0dd73d59584e3e1bfe7", "mn0002311921")   ### [Rogelio Martinez "EL RM"]
        ### Y Sigues Siendo Tu
        ### Y Sigues Siendo Tu  ---> [['Rogelio Martinez "EL RM"']]


        addAllMusic(mdbmaps, "Billboard", "9a20d2762ec197db57a9ace82dea2134", "mn0002130081")   ### [Pee-Wee]
        ### Yo Soy
        ### Yo Soy  ---> [['Pee-Wee']]addAllMusic(mdbmaps, "Billboard", "d2122c257dd5b8a3c4c0ac06b2abd0e2", "")
        

        ### [The Chimes]
        addAllMusic(mdbmaps, "Billboard", "d2122c257dd5b8a3c4c0ac06b2abd0e2", "mn0001888760")    ### [The Chimes]
        ### 1-2-3/Underestimate  ,  Heaven
        ### 1-2-3/Underestimate  ---> [['The Chimes']]
        ### Heaven  ---> [['Bryan Adams', 'Depeche Mode', 'BeBe & CeCe Winans', 'The Chimes', 'Mary Mary', 'DJ Sammy', 'Los Lonely Boys', 'Avicii', 'Kane Brown']]


        addAllMusic(mdbmaps, "Billboard", "c7abc7c97d4756cc3d9425e76643d158", "mn0000462782")   ### [Res]
        ### They-Say Vision  ,  How I Do
        ### They-Say Vision  ---> [['Res']]
        ### How I Do  ---> [['Res']]

        addDiscogs(mdbmaps, "Billboard", "8c1e675216bcf1c7a182edb14d75c265", "3358")    ### [Cassius]
        ### The Sound Of Violence  ,  Together
        ### The Sound Of Violence  ---> [['Cassius With Steve Edwards']]
        ### Together  ---> [['Connie Francis', 'Bob Sinclar & Steve Edwards']]

        addAllMusic(mdbmaps, "Billboard", "9ab14919e655dc9669042291d6771569", "mn0000041463")   ### [Andy Bell]
        ### Aftermath (Here We Go)  ,  True Original
        ### Aftermath (Here We Go)  ---> [['Dave Aude Featuring Andy Bell']]
        ### True Original  ---> [['Dave Aude Featuring Andy Bell']]

        addDiscogs(mdbmaps, "Billboard", "6c9e35fa812bd11f2496be3aa1076cd2", "3295635")    ### [Kimberly Davis]
        ### My Fire  ,  You're Good For Me
        ### My Fire  ---> [['Nile Rodgers ::: Tony Moran ::: Kimberly Davis']]
        ### You're Good For Me  ---> [['Tony Moran Featuring Kimberly Davis']]

        addDiscogs(mdbmaps, "Billboard", "a4952315ff2618cc4b878de65a4dfe6a", "60146")    ### [Fever]
        ### BEAT OF THE NIGHT/PUMP IT UP
        ### BEAT OF THE NIGHT/PUMP IT UP  ---> [['Fever']]

        addAllMusic(mdbmaps, "Billboard", "d79329a688889810aa7ee43aef41c59b", "mn0000290969")   ### [Lime]
        ### Your Love / You're My Magician
        ### Your Love / You're My Magician  ---> [['Lime']]

        addDiscogs(mdbmaps, "Billboard", "e8b586570af23bcd228f54f4af667358", "132019")    ### [Slingshot]
        ### Do It Again/Billie Jean
        ### Do It Again/Billie Jean  ---> [['Slingshot']]

        addAllMusic(mdbmaps, "Billboard", "23a9f0052fdd983b94cc46e3aa4d7e10", "mn0002030753")   ### [Shape: UK]
        ### Back To Basics
        ### Back To Basics  ---> [['Christina Aguilera', 'Shape: UK']]

        addDiscogs(mdbmaps, "Billboard", "c858d2c428f54d66c563a498860fbf56", "76373")    ### [Dany]
        ### Found Love
        ### Found Love  ---> [['Double Dee Featuring Dany']]

        addDiscogs(mdbmaps, "Billboard", "261a823373b1c2d3538e401b824a0705", "7336674")    ### [Gia]
        ### One Night
        ### One Night  ---> [['WTS Featuring Gia']]

        addAllMusic(mdbmaps, "Billboard", "7e4fd4c27bbef1f16e101365a1abbad6", "mn0003069858")   ### [HiFi Sean]
        ### Testify!
        ### Testify!  ---> [['HiFi Sean Featuring Crystal Waters']]


        addAllMusic(mdbmaps, "Billboard", "88479115f3901acb361ca20c0c0af151", "mn0000071018")   ### [Ilegales]
        ### Yo No Soy Un Monstruo  ,  Ayantame  ,  Pasarla Bien
        ### Yo No Soy Un Monstruo  ---> [['Elvis Crespo Featuring Ilegales']]
        ### Ayantame  ---> [['Ilegales Featuring El Potro Alvarez']]
        ### Pasarla Bien  ---> [['Ilegales Featuring El Potro Alvarez']]

        addDiscogs(mdbmaps, "Billboard", "7d2fc8d4574b4f6972941478c183494e", "2435865")    ### [Bronco]
        ### Cronica De Dos Grandes  ,  Cronica De Dos Grandes: Recuerdos Con Amor  ,  Cronica De Dos Grandes: Los Inicios De Nuestra Historia
        ### Cronica De Dos Grandes  ---> [['Bronco/Los Bukis']]
        ### Cronica De Dos Grandes: Recuerdos Con Amor  ---> [['Bronco/Los Bukis']]
        ### Cronica De Dos Grandes: Los Inicios De Nuestra Historia  ---> [['Bronco/Los Bukis']]

        addAllMusic(mdbmaps, "Billboard", "308451bef86fcd177e3faf211de994ce", "mn0003485703")   ### [Nacho]
        ### Bailame  ,  Toy Enamorao
        ### Bailame  ---> [['Nacho']]
        ### Toy Enamorao  ---> [['Mozart La Para Featuring Sharlene & Nacho']]

        addAllMusic(mdbmaps, "Billboard", "cb0c429ff2c1e5ce5f122fd3bc3ba9c7", "mn0002807645")   ### [T-ara]
        ### Bo peep Bo peep  ,  Sketch
        ### Bo peep Bo peep  ---> [['T-ara']]
        ### Sketch  ---> [['T-ara']]

        addDiscogs(mdbmaps, "Billboard", "a6436db0cd5a1fe24fa821f2ccf5f7cf", "188261")    ### [Ali]
        ### Air Force Ones  ,  A Real Labour Of Love
        ### Air Force Ones  ---> [['Nelly Featuring Kyjuan, Ali & Murphy Lee']]
        ### A Real Labour Of Love  ---> [['UB40 Featuring Ali, Astro & Mickey']]

        addAllMusic(mdbmaps, "Billboard", "1f6381c06850170b54c95e6a596ffb28", "mn0003782313")   ### [Ken Tackey]
        ### Gyakuten Lovers
        ### Gyakuten Lovers  ---> [['Ken Tackey']]

        addAllMusic(mdbmaps, "Billboard", "0ac87a2703773df3ee90f35051976d6e", "mn0003205412")   ### [Yuan Yawei]
        ### Moonlight
        ### Moonlight  ---> [['Wilber Pan & Yuan Yawei']]

        addAllMusic(mdbmaps, "Billboard", "37bc20cf1fd6fce7883914b6cdb2ab1d", "mn0002103368")   ### [Anibal de Gracia]
        ### Dejando Huellas
        ### Dejando Huellas  ---> [['Anibal de Gracia y Sus Invitados']]

        addAllMusic(mdbmaps, "Billboard", "0b7cdd3b8df5ac9a2b33e2e252593f4a", "mn0000733706")   ### [Ez El Ezeta]
        ### Midnight
        ### Midnight  ---> [['Coldplay', 'Ez El Ezeta Featuring Nengo Flow & Kevin Lyttle']]

        addAllMusic(mdbmaps, "Billboard", "c751a299bc9b7926f25dd12c5c16c40b", "mn0002996592")   ### [Los de La Nazza]
        ### Si El Mundo Se Acabara
        ### Si El Mundo Se Acabara  ---> [['Los de La Nazza Featuring Justin Quiles']]

        addAllMusic(mdbmaps, "Billboard", "f0ea2c0f6ed64d3d6bc31d1f381092b0", "mn0001577226")   ### [Cantor Yitzchak Meir Helfgot]
        ### Eternal Echoes: Songs And Dance For The Soul
        ### Eternal Echoes: Songs And Dance For The Soul  ---> [['Itzhak Perlman/Cantor Yitzchak Meir Helfgot']]

        addAllMusic(mdbmaps, "Billboard", "3c2a14f3f9126d17f7f2fdbfd3e04295", "mn0000501845")   ### [Joe Vasconcelos]
        ### La Zalamera
        ### La Zalamera  ---> [['Chichi Peralta With Joe Vasconcelos']]

        addAllMusic(mdbmaps, "Billboard", "5652a045de2d2b66d9d2d658b0a2c964", "mn0000392577")   ### [R. Ayala]
        addDiscogs(mdbmaps, "Billboard", "5652a045de2d2b66d9d2d658b0a2c964", "5845005")    ### [R. Ayala]
        ### Arriba El Norte...
        ### Arriba El Norte...  ---> [['V. Fernandez/R. Ayala']]

        addAllMusic(mdbmaps, "Billboard", "d03d6af3ef8c0c4d1e104fe65d94cfb0", "mn0003671497")   ### [Matsuri Nine.]
        ### Uchouten Shooter
        ### Uchouten Shooter  ---> [['Matsuri Nine.']]

        addDiscogs(mdbmaps, "Billboard", "75d13abe72774129842a4beff75739ea", "7964912")    ### [The Elovaters]
        ### Defy Gravity
        ### Defy Gravity  ---> [['The Elovaters']]

        addAllMusic(mdbmaps, "Billboard", "ae1cfe75bb6f91da7d223452168a3d59", "mn0000199162")   ### [Vicious]
        ### Destination Brooklyn
        ### Destination Brooklyn  ---> [['Vicious']]

        addAllMusic(mdbmaps, "Billboard", "1d5e1f09e81138a1f8efc590f757fc8e", "mn0003255680")   ### [Kakigoori]
        ### Naminori
        ### Naminori  ---> [['Kakigoori']]

        addAllMusic(mdbmaps, "Billboard", "2ea031bee81e2e013e5cdb82f59c124c", "mn0003524387")   ### [Xantos]
        ### Bailame Despacio
        ### Bailame Despacio  ---> [['Xantos']]

        addAllMusic(mdbmaps, "Billboard", "3932c5031c30efcdfff5f6dea5b44452", "mn0002532879")   ### [Silvio Mora]
        ### Yo Quiero Volver
        ### Yo Quiero Volver  ---> [['Silvio Mora']]

        addAllMusic(mdbmaps, "Billboard", "bee91a30c653a9d5146bdce553318cf4", "mn0003636549")   ### [Hwang ChiYeul]
        ### The Furthest Distance
        ### The Furthest Distance  ---> [['Hwang ChiYeul']]

        addAllMusic(mdbmaps, "Billboard", "bc53a647a9083dd5b5669d1c977944c9", "mn0003572459")   ### [Karry Wang]
        ### Miss Of Sky Wheel
        ### Miss Of Sky Wheel  ---> [['Karry Wang']]

        addDiscogs(mdbmaps, "Billboard", "79c1d5700483a888cef4cc3c96777392", "2838190")    ### [George Donaldson]
        ### The Road
        ### The Road  ---> [['George Donaldson']]

        addAllMusic(mdbmaps, "Billboard", "986fe93fe00284401d2834780e8f5c38", "6233904")   ### [Leo Ieiri]
        ### Kimi Ga Kureta Natsu
        ### Kimi Ga Kureta Natsu  ---> [['Leo Ieiri']]

        addAllMusic(mdbmaps, "Billboard", "7270cf68e89cab0f5febe2edaed0b7d6", "mn0003487021")   ### [Subaru Shibuya]
        ### Kioku
        ### Kioku  ---> [['Subaru Shibuya']]

        addAllMusic(mdbmaps, "Billboard", "7df88a23e1041266b20b6f78e34581fc", "mn0003295536")   ### [WINNER]
        ### 2014 S/S
        ### 2014 S/S  ---> [['WINNER']]

        addAllMusic(mdbmaps, "Billboard", "42bb5146be764807cc62ea7cd44bff02", "mn0002503541")   ### [CNBLUE]
        ### Re:BLUE: CNBLUE 4th Mini Album (EP)
        ### Re:BLUE: CNBLUE 4th Mini Album (EP)  ---> [['CNBLUE']]

        addAllMusic(mdbmaps, "Billboard", "57a364f91a9d29cf1180c8afa29b6249", "mn0002863637")   ### [Kyary Pamyu Pamyu]
        ### Ninjyari Ban Ban
        ### Ninjyari Ban Ban  ---> [['Kyary Pamyu Pamyu']]

        addAllMusic(mdbmaps, "Billboard", "21687fa84e6dfabb24632243e8833816", "mn0002960027")   ### [Golden Bomber]
        ### Dance My Generation
        ### Dance My Generation  ---> [['Golden Bomber']]

        addDiscogs(mdbmaps, "Billboard", "a626013386ca6bc138efacdf05aa7a96", "380314")    ### [Mickey]
        ### A Real Labour Of Love
        ### A Real Labour Of Love  ---> [['UB40 Featuring Ali, Astro & Mickey']]

        addDeezer(mdbmaps, "Billboard", "7229ea37a1a8f87bce43dfe553fecd5b", "2737281")    ### [James Wilson]
        ### Songs For The Church  ,  Wait On The Lord  ,  Give Me Jesus
        ### Songs For The Church  ---> [['James Wilson']]
        ### Wait On The Lord  ---> [['James Wilson Featuring Brooke Staten']]
        ### Give Me Jesus  ---> [['James Wilson Featuring Draylin Young']]


        addDeezer(mdbmaps, "Billboard", "5396115fee88d97c51bee14ae2088b35", "316")    ### [Thrice]
        ### To Be Everywhere Is To Be Nowhere  ,  Palms
        ### To Be Everywhere Is To Be Nowhere  ---> [['Thrice']]
        ### Palms  ---> [['Thrice']]


        addDeezer(mdbmaps, "Billboard", "a0ec3ffe08120ccf0c9b5345714a5c51", "2743")    ### [LTD]
        ### Something To Love  ,  (Every Time I Turn Around) Back In Love Again
        ### Something To Love  ---> [['LTD']]
        ### (Every Time I Turn Around) Back In Love Again  ---> [['LTD']]


        addDiscogs(mdbmaps, "Billboard", "fa00044058206494d4335094632fe4eb", "83751")    ### [Boss]
        ### Deeper  ,  Recipe Of A Hoe
        ### Deeper  ---> [['Boss', 'Anthony Nelson & The Overcomer']]
        ### Recipe Of A Hoe  ---> [['Boss']]


        addDeezer(mdbmaps, "Billboard", "66dca5283eac29a7b8c9714ed919bb78", "442981")    ### [Red Sun Rising]
        ### The Otherside  ,  Emotionless
        ### The Otherside  ---> [['Red Sun Rising']]
        ### Emotionless  ---> [['Red Sun Rising']]


        addDeezer(mdbmaps, "Billboard", "6cde371c9f96a16c4221ecaf6ee34f5c", "15432")    ### [Consequence]
        ### Don't Quit Your Day Job  ,  Gone
        ### a  ---> [['Consequence']]
        ### Gone  ---> [['Red', "Kanye West Featuring Cam'ron & Consequence"]]


        addDeezer(mdbmaps, "Billboard", "55be138b7b3faad5764a62dc13c9c402", "1236346")    ### [John Reilly]
        ### Joyful Noise
        ### Joyful Noise  ---> [['Flame Featuring Lecrae & John Reilly']]


        addDeezer(mdbmaps, "Billboard", "b470feb6f3d72bfae87a83e16dd83886", "76640")    ### [Sons of the Desert]
        ### I Hope You Dance
        ### I Hope You Dance  ---> [['Lee Ann Womack', 'Lee Ann Womack With Sons Of The Desert']]


        addDiscogs(mdbmaps, "Billboard", "0f5996206ed17aee986e961e69109699", "268902")    ### [Paul McCoy]
        ### Bring Me To Life
        ### Bring Me To Life  ---> [['Evanescence Featuring Paul McCoy']]


        addAllMusic(mdbmaps, "Billboard", "172d1fbe2511219acd80e391536e87a2", "mn0003322275")   ### [I LOVE MAKONNEN]
        addDeezer(mdbmaps, "Billboard", "172d1fbe2511219acd80e391536e87a2", "6901127")    ### [I LOVE MAKONNEN]
        ### Tuesday
        ### Tuesday  ---> [['I LOVE MAKONNEN Featuring Drake']]


        addDeezer(mdbmaps, "Billboard", "8ee259441c323be544eb3b8c50c0af30", "13669055")    ### [LIL PHAG]
        ### resERECTION (EP)
        ### resERECTION (EP)  ---> [['LIL PHAG']]


        addDeezer(mdbmaps, "Billboard", "07c0deba90ed751e5c2ec92d0d60d7dd", "59218332")    ### [Brooke Staten]
        ### Wait On The Lord
        ### Wait On The Lord  ---> [['James Wilson Featuring Brooke Staten']]


        addDeezer(mdbmaps, "Billboard", "3863015a37429bd36794583e155c242d", "6307368")    ### [Steffany Gretzinger]
        ### Good & Loved
        ### Good & Loved  ---> [['Travis Greene Featuring Steffany Gretzinger']]


        addDeezer(mdbmaps, "Billboard", "6c999baddd68939e501aa0561d3e0eda", "4052173")    ### [King Bach]
        ### Medicine
        ### Medicine  ---> [['King Bach']]


        addAllMusic(mdbmaps, "Billboard", "3bb7b26b6dee914d5d35651092ebbd38", "mn0000567190")   ### [Questian Mark & The Mysterians]
        addDeezer(mdbmaps, "Billboard", "3bb7b26b6dee914d5d35651092ebbd38", "123941")    ### [Questian Mark & The Mysterians]
        ### 96 Tears
        ### 96 Tears  ---> [['Questian Mark & The Mysterians']]


        addDeezer(mdbmaps, "Billboard", "9a0fdd63c4aa97fc9716413a6111c187", "148184")    ### [Enchantment]
        ### It's You That I Need
        ### It's You That I Need  ---> [['Enchantment']]


        addDeezer(mdbmaps, "Billboard", "ef9d8e82a6937e87668db5702cd43b2f", "1816301")    ### [UMC's]
        ### Blue Cheese
        ### Blue Cheese  ---> [["UMC's"]]


        addDeezer(mdbmaps, "Billboard", "7087547bca580c898106d8f7eb761f58", "251366")    ### [Michael Peterson]
        ### From Here To Eternity
        ### From Here To Eternity  ---> [['Michael Peterson']]


        addDeezer(mdbmaps, "Billboard", "dd6d9c8273de500d5019cb6c2d3a443e", "211037")    ### [Bill & Gloria Gaither]
        ### Let Freedom Ring: Live From Carnegie Hall
        ### Let Freedom Ring: Live From Carnegie Hall  ---> [['Bill & Gloria Gaither']]


        addDeezer(mdbmaps, "Billboard", "ee476cb24bebb0cbe4d7061b0d33a707", "1533511")    ### [Rock Star Supernova]
        ### Rock Star Supernova
        ### Rock Star Supernova  ---> [['Rock Star Supernova']]


        addDeezer(mdbmaps, "Billboard", "31aa5ad81b2a6342572b6bd54425deae", "390649")    ### [Iration]
        ### Fresh Grounds (EP)
        ### Fresh Grounds (EP)  ---> [['Iration']]


        addDeezer(mdbmaps, "Billboard", "62fe13f7952a052298750c432e191a08", "4037981")    ### [Trinidad James]
        ### Don't Be S.A.F.E.
        ### Don't Be S.A.F.E.  ---> [['Trinidad James']]


        addDeezer(mdbmaps, "Billboard", "4fdc8908f2ee7ad25e35f2ad9531c681", "15080705")    ### [Dennis Reed & Gap]
        ### Necessary
        ### Necessary  ---> [['Dennis Reed & Gap']]


        addDeezer(mdbmaps, "Billboard", "8dafa71fa9a51e9418124a225aa9aed2", "712900")    ### [KONGOS]
        ### Come With Me Now
        ### Come With Me Now  ---> [['KONGOS']]


        addDeezer(mdbmaps, "Billboard", "71e904485de1ca65917eb99f886f9c4d", "69608322")    ### [Marty]
        ### Marty For President (EP)
        ### Marty For President (EP)  ---> [['Marty']]


        addDeezer(mdbmaps, "Billboard", "7a85a9d8804e19413bab514f5f51dfb9", "8322164")    ### [Donnie Trumpet & The Social Experiment]
        ### Sunday Candy
        ### Sunday Candy  ---> [['Donnie Trumpet & The Social Experiment']]


        addDeezer(mdbmaps, "Billboard", "4891617ed29a8fe8a1775bd2b17c71b2", "668525")    ### [The Internet]
        ### Special Affair
        ### Special Affair  ---> [['The Internet']]


        addAllMusic(mdbmaps, "Billboard", "c5281bc610aaf5fcb1be3ea9b5aef4a7", "mn0000046177")   ### [Bo Donaldson And The Heywoods]
        addDeezer(mdbmaps, "Billboard", "c5281bc610aaf5fcb1be3ea9b5aef4a7", "1078918")    ### [Bo Donaldson And The Heywoods]
        ### Billy, Don't Be A Hero
        ### Billy, Don't Be A Hero  ---> [['Bo Donaldson And The Heywoods']]


        addDeezer(mdbmaps, "Billboard", "5e374f537637dfbb639dcb7d363e896b", "566096")    ### [Last Call]
        ### Victory
        ### Victory  ---> [['Tye Tribbett & G.A.', 'Fred Jerkins Featuring Last Call']]




        
        if False:
            ### Case Of The Ex (Whatcha Gonna Do)

            addAllMusic(mdbmaps, "Billboard", "d6cac33cc3555e4e1f5ce0d2b3cae450", "mn0001481616")   ### [Connor Christian & Southern Gothic]
            addDiscogs(mdbmaps, "Billboard", "d6cac33cc3555e4e1f5ce0d2b3cae450", "4558282")    ### [Connor Christian & Southern Gothic]
            ### New Hometown

            ### The Irish Tenors: Home For Christmas  ,  The Irish Tenors: Live In Belfast  ,  The Irish Tenors: Ellis Island  ,  The Irish Tenors: Live In Belfast  ,  The Irish Tenors: Ellis Island

            addDiscogs(mdbmaps, "Billboard", "b66b1bfa1a8b0725ba1f139b87ad3a4c", "92281")    ### [Loon]
            ### I Need A Girl (Part Two)  ,  I Don't Wanna Know

            ### Masterpiece: Nuestra Obra Maestra

            addDiscogs(mdbmaps, "Billboard", "8d31f7e1853f2b2a38cb37cdc92ac03d", "1813760")    ### [Lil Peanut]
            ### Lean Wit It, Rock Wit It

            addDiscogs(mdbmaps, "Billboard", "5903a04a9d6f7e1f2434dd13def9c352", "1702929")    ### [Nayer]
            ### Give Me Everything  ,  Hey Mama

            addAllMusic(mdbmaps, "Billboard", "ce6a59b7abc5d76a683bf2aa188adf74", "mn0000178007")   ### [Russell Moore]
            ### Timeless Hits From The Past: Bluegrassed

            addAllMusic(mdbmaps, "Billboard", "0b1e4a71bbd133e8050ba86a4492b04b", "mn0003744509")   ### [Ranna Royce]
            ### The Whoodlum Ball

            addAllMusic(mdbmaps, "Billboard", "8a34e0d5cd9db90fc3f598b5f615854d", "mn0003712915")   ### [Smith And Hay]
            ### The Whoodlum Ball

            addAllMusic(mdbmaps, "Billboard", "4ce403673af609f4b3edb411124ac331", "mn0003259234")   ### [OCD: Moosh & Twist]

            addAllMusic(mdbmaps, "Billboard", "d7069e334141b398d6204597eb9c1401", "mn0002908858")   ### [Myles Kennedy And The Conspirators]
            ### Apocalyptic Love  ,  You're A Lie  ,  World On Fire  ,  Living The Dream

            addAllMusic(mdbmaps, "Billboard", "7f2a3d27565fbcf78578a36856d29954", "mn0000403784")   ### [LeCrae]
            ### Live & Let Live

            addDiscogs(mdbmaps, "Billboard", "45908a9da68e8f594c1d999e8567a3bf", "4995184")    ### [John P. Kee & The New Life Community Choir]
            ### We Walk By Faith  ,  Blessed By Association  ,  Life And Favor

            #89eab0113dd350e54cc04867d4cbcc04	None	None	None	None	None	None	None	None	None	None	None	0
            addAllMusic(mdbmaps, "Billboard", "89eab0113dd350e54cc04867d4cbcc04", "mn0000184098")   ### [John McDermott]
            addDiscogs(mdbmaps, "Billboard", "89eab0113dd350e54cc04867d4cbcc04", "1436273")    ### [John McDermott]

            #5dab93d7de7fdc41568fc96e979119e3	None	None	None	None	None	None	None	None	None	None	None	0
            ### The Door Is Always Open  ,  Tear Time  ,  Golden Tears

            #a6fbf98a79a048834d50ce68d67ad442	None	None	None	None	None	None	None	None	None	None	None	0
            addAllMusic(mdbmaps, "Billboard", "a6fbf98a79a048834d50ce68d67ad442", "mn0000621112")   ### [Mya]
            ### Case Of The Ex (Whatcha Gonna Do)  ,  Lady Marmalade

            #b66b1bfa1a8b0725ba1f139b87ad3a4c	None	None	None	None	None	None	None	None	None	None	None	0
            ### I Need A Girl (Part One)  ,  I Need A Girl (Part Two)

            #5903a04a9d6f7e1f2434dd13def9c352	None	None	None	None	None	None	None	None	None	None	None	0
            addAllMusic(mdbmaps, "Billboard", "5903a04a9d6f7e1f2434dd13def9c352", "mn0002960843")   ### [Nayer]
            ### Give Me Everything  ,  Hey Mama

            #808c8b3a9909c7d7a3e5753792d1b995	None	None	None	None	None	None	None	None	None	None	None	0
            ### Gangsta's Paradise (From "Dangerous Minds")

            #832b5faffd094a5ab3b22f67d40db4b7	None	None	None	None	None	None	None	None	None	None	None	0        
            addAllMusic(mdbmaps, "Billboard", "832b5faffd094a5ab3b22f67d40db4b7", "mn0001049094")   ### [RKM]
            ### Masterpiece: Nuestra Obra Maestra


        
        #addAllMusic(mdbmaps, "Billboard", "fa00044058206494d4335094632fe4eb", "mn0000771069")   ### Boss
        ### Deeper  ,  Recipe Of A Hoe
        #addDiscogs(mdbmaps, "Billboard", "265d96f09b9e09bd2ea57aa249d40bd6", "4995184")    ### [New Life]
        ### Blessed By Association
        
        #addAllMusic(mdbmaps, "Billboard", "5dab93d7de7fdc41568fc96e979119e3", "mn0003740957")   ### [Dave Rowland]
        ### The Door Is Always Open  ,  Tear Time  ,  Golden Tears



        #addAllMusic(mdbmaps, "Billboard", "d80e9d8084288fd5741a6aa3d66f4791", "mn0000469634")   ### [Rev. F.C. Barnes]
        ### Rough Side Of The Mountain

        #addDiscogs(mdbmaps, "Billboard", "716be2f511125c5a2f9b1f551625796a", "391684")    ### [Rev. J.Cleveland]
        ### Having Church

        #addAllMusic(mdbmaps, "Billboard", "e491dd7ccd6078de34241c26285b3a67", "mn0001214814")   ### [V.I.P. Music]
        ### Stand!

        #addAllMusic(mdbmaps, "Billboard", "efad7602aac6e53f2a5ff7245e82b2e3", "mn0000326045")   ### [Radical For Christ]
        #addDiscogs(mdbmaps, "Billboard", "efad7602aac6e53f2a5ff7245e82b2e3", "598023")    ### [Radical For Christ]
        ### (Pages Of Life) Chapters I & II  ,  Purpose By DesignaddAllMusic(mdbmaps, "Billboard", "2560abe831fb977fd5f9fb8cf376f754", "mn0000387219")   ### [Norma Jean]

        #addAllMusic(mdbmaps, "Billboard", "26f06a68470482961ce0948b25a130df", "mn0000774908")   ### [J. Moss]
        ### We Must Praise  ,  V2...

        #addAllMusic(mdbmaps, "Billboard", "25a9d8b57fd0df9d2e6d6702976b5cdd", "mn0000593009")   ### [Youth For Christ]
        ### The Struggle Is Over

        #addAllMusic(mdbmaps, "Billboard", "9d63b29d7ff8a3801b434b371008fef2", "mn0000454193")   ### [pureNRG]
        ### The Real Thing

        #addAllMusic(mdbmaps, "Billboard", "0facb34dfb2037ab9c12a1edfa4d5207", "mn0000131293")   ### [Passion Worship Band]
        ### Passion: Awakening

        #addAllMusic(mdbmaps, "Billboard", "26c7048587d4a152411db397edf8813b", "mn0003547921")   ### [Bishop T.D. Jakes]
        #addDiscogs(mdbmaps, "Billboard", "26c7048587d4a152411db397edf8813b", "448274")    ### [Bishop T.D. Jakes]

        #addAllMusic(mdbmaps, "Billboard", "f48a161c0063d474c2eab5dc2e5195cd", "mn0003442077")   ### [Thomas Miles aka Nephew Tommy]
        ### Presents: Prank Phone Calls Vol 5: Church Folks Gotta Laugh Too  ,  Presents: Prank Phone Calls: Church Folks Gotta Laugh Too Vol 2

        #addAllMusic(mdbmaps, "Billboard", "efee2dea144675a9daea006446b60011", "mn0002817738")   ### [Brian Brushwood Justin Robert Young]
        ### Night Attack 2: Enjoy The Garden  ,  Night Attack (Live)

        #addAllMusic(mdbmaps, "Billboard", "8a8f1ba4fa40b97993e05516b6cbd260", "mn0003232100")   ### [Deitrick Haddon's LXW (League Of Xtraordinary Worshippers)]
        ### Deitrick Haddon's LXW
        
        #addAllMusic(mdbmaps, "Billboard", "7ca86f084b469e552a767a3b582bed15", "mn0001081792")   ### [Swoope]
        ### Sinema

        #addAllMusic(mdbmaps, "Billboard", "84c774e5a41773f191b62bbc09774dab", "mn0003465054")   ### [Braiden Sunshine]
        ### Amazing Grace

        #addAllMusic(mdbmaps, "Billboard", "62fa94e3fb88cdeb88e50b1f2ae64cfe", "mn0000563196")   ### [Myron Butler & Levi]
        ### On Purpose

        #addAllMusic(mdbmaps, "Billboard", "514877cce2b057728c36e0c14a26f0bc", "mn0003586280")   ### [My Dad Wrote A Porno]
        ### My Dad Wrote A Christmas Porno

        #addAllMusic(mdbmaps, "Billboard", "3a799a523bc6e3e6e953894a176b7d97", "mn0003874962")   ### [Fresh Start Worship]
        ### Mention
        

        #addAllMusic(mdbmaps, "Billboard", "d8f8476e6164eabe4fb4ab3ba3f3b7d9", "mn0002558731")   ### [Suzy Rock]
        ### Fuego

        #addAllMusic(mdbmaps, "Billboard", "60021b6a1be2c390a233cce11db4b5b9", "mn0002867667")   ### [Them Idiots]
        ### Whirled Tour

        #addAllMusic(mdbmaps, "Billboard", "99c44622cf1137d8ffff21a66c3d3028", "mn0000175286")   ### [D. Parton]
        ### Higher Medley

        #addAllMusic(mdbmaps, "Billboard", "66694ccf7b6dfaed0f263e8f9569ef71", "mn0003288960")   ### [Dimitri McDowell]
        #addDiscogs(mdbmaps, "Billboard", "66694ccf7b6dfaed0f263e8f9569ef71", "4123531")    ### [Dimitri McDowell]
        ### Sweet Victory

        #addAllMusic(mdbmaps, "Billboard", "30f2dacc35fad2a476eb8db246f243f5", "mn0002447683")   ### [Mr. Talkbox]
        ### Feel It

        #addAllMusic(mdbmaps, "Billboard", "7008c483e43dff7585e75c0588dce00f", "mn0000494388")   ### [GabeReal]
        ### Eye Of The Storm

        #addAllMusic(mdbmaps, "Billboard", "4831b39973a020abf296356f3abfe702", "mn0001467056")   ### [Ryan Stevenson]
        ### Eye Of The Storm
        
        #addAllMusic(mdbmaps, "Billboard", "fc61047e5a0c49d67bc6c28515f740f6", "mn0003520491")   ### [Lindy Conant]
        ### Every Nation

        #addAllMusic(mdbmaps, "Billboard", "5cf648bdbb963bf9021e2ccfa0b5e811", "mn0003528162")   ### [The Circuit Riders]
        ### Every Nation

        #addAllMusic(mdbmaps, "Billboard", "31c5c26ecfd994d64599a8c74fcb0e0c", "mn0003595666")   ### [GEI]
        ### Hang On

        #addAllMusic(mdbmaps, "Billboard", "e7fdd33db429c91d51fbb11f05b6b708", "mn0002743423")   ### [Le'Andria]
        ### Grace

        #addAllMusic(mdbmaps, "Billboard", "3f4e690b965dfa3c6690758607cabd39", "mn0003662860")   ### [Vincent Bohanan]
        ### We Win: The Kingdom Declaration

        #addAllMusic(mdbmaps, "Billboard", "17ade4a4fbc717fa2101363ee7fd37c3", "mn0000178135")   ### [The Edwin Hawkins' Singers]
        ### Oh Happy Day

        #addAllMusic(mdbmaps, "Billboard", "1bfaab8fb3874f792cc5510b2b95b028", "mn0003864623")   ### [Tobbi & Tommi]

        #addAllMusic(mdbmaps, "Billboard", "3f4e690b965dfa3c6690758607cabd39", "mn0003542519")   ### [Vincent Bohanan]
        ### We Win: The Kingdom Declaration

        #addAllMusic(mdbmaps, "Billboard", "c346d5028767e3a4fda0260b4d1c1f97", "mn0000731951")   ### [Anita Wilson Accompanied By The Company]
        ### Sunday Song

        #addAllMusic(mdbmaps, "Billboard", "9d63b29d7ff8a3801b434b371008fef2", "mn0000454193")   ### [pureNRG]
        ### The Real Thing

        #addAllMusic(mdbmaps, "Billboard", "1bfaab8fb3874f792cc5510b2b95b028", "mn0003864623")   ### [Tobbi & Tommi]
        ### He Promised Me

        #ba6cb719ca53bf4f57ecdcd6bd342bf5	None	None	None	None	None	None	None	None	None	None	None	0
        
        mdbmaps["Billboard"].save()
        
        
def extraAddsForTop40(mdbmaps, chartType):
    if chartType == "Top40":      
        
        addAllMusic(mdbmaps, "Top40", "00d5d59798eeffef591f272260b0bbcc", "mn0000124572")   ### [Chuck-N-Blood]
        ### My Dogs

        addAllMusic(mdbmaps, "Top40", "21da687c5162d957e0e8aaa39eff1e80", "mn0003750925")   ### [The Carters]
        ### Apes**t  ,  Everything Is Love

        addAllMusic(mdbmaps, "Top40", "c00c9a5d2e3053716de9b79898cb5691", "mn0001225951")   ### [Mustard]
        ### Perfect Ten  ,  Ballin'

        addAllMusic(mdbmaps, "Top40", "78f1feb9204bce3173d42798bc9bcb91", "mn0001808325")   ### [Kobe Bryant]
        ### Hold Me

        addAllMusic(mdbmaps, "Top40", "5edcd28a4505dc29e4edebd67052e614", "mn0000795894")   ### [Dolla]
        ### Cry For Me

        addAllMusic(mdbmaps, "Top40", "5a888aa5d5b0835533b2a73dd895b461", "mn0002528230")   ### [DCUP]
        ### We No Speak Americano

        addAllMusic(mdbmaps, "Top40", "7bcb752a835787affb80072d61387b22", "mn0001411030")   ### [Hollis]
        ### White Walls

        addAllMusic(mdbmaps, "Top40", "c0051ae12f6048a807213c44b434aa1d", "mn0003348925")   ### [Jennifer Lawrence]
        ### The Hanging Tree

        addAllMusic(mdbmaps, "Top40", "1f9b34897f6440e2484f1ac5e00953f7", "mn0003462822")   ### [Gnash]
        ### I Hate U, I Love U  ,  Lights Down Low

        addAllMusic(mdbmaps, "Top40", "9d337e01e83fc2b9d9fcbd6930bfb107", "mn0003715465")   ### [Casper Magico]
        ### Te Bote  ,  Otro Trago

        addAllMusic(mdbmaps, "Top40", "7670c11b0a85e757c3cd25e1cb4f0d2b", "mn0003496227")   ### [Dakota]
        ### Fast Car  ,  Perfect Strangers  ,  By Your Side  ,  Mama  ,  Rise  ,  Back And Forth  ,  Polaroid  ,  Ritual

        addAllMusic(mdbmaps, "Top40", "29c175308260a766645f88a48fda8cb5", "mn0002141576")   ### [Sasha]
        ### Coming Home  ,  Airdrawn Dagger

        addAllMusic(mdbmaps, "Top40", "20cf770061e851a2768a67afad49a089", "mn0001884165")   ### [Chris Malinchak]
        ### So Good To Me  ,  If U Got It

        addAllMusic(mdbmaps, "Top40", "80891387fa9995ead4c3a41b8eb58cac", "mn0003165846")   ### [Islove]
        ### Goodbye

        addAllMusic(mdbmaps, "Top40", "927d313b814225911b0cc45f6d101384", "mn0003525593")   ### [Neales]
        ### I'll Be There
        
        addDiscogs(mdbmaps, "Top40", "000a8119d7146d68b89c0a1190ec7e11", "7474592")    ### [Young T & Bugsey]
        ### Don't Rush

        addDiscogs(mdbmaps, "Top40", "8869a02f414bf8aa44ffa2491e057c18", "5690424")    ### [Sile Seoige]
        ### Maybe This Christmas  ,  Alabama & Friends  ,  The Breeze - An Appreciation Of JJ Cale
        ### Maybe This Christmas  ---> [['Sile Seoige & Friends']]
        ### Alabama & Friends  ---> [['Alabama & Friends']]
        ### The Breeze - An Appreciation Of JJ Cale  ---> [['Eric Clapton & Friends']]


        addAllMusic(mdbmaps, "Top40", "23766e9564639a78dd2aa4469c656e33", "mn0000186917")   ### [Gabriella]
        ### Breaking Free
        ### Breaking Free  ---> [['Zac Efron & Vanessa Anne Hudgens', 'Troy & Gabriella']]


        addAllMusic(mdbmaps, "Top40", "ee06f338805166cc652a5ffa29bfcaa4", "mn0000792831")   ### [Shane Macgowan]
        ### Dirty Old Town/road To Paradise
        ### Dirty Old Town/road To Paradise  ---> [['Jimmy Johnstone & Shane Macgowan']]


        addDiscogs(mdbmaps, "Top40", "338160050dd8760f6e21fd314da0c262", "282163")    ### [Glen Keating]
        ### The Munster Song
        ### The Munster Song  ---> [['Glen Keating & Greg Ryan']]


        addDiscogs(mdbmaps, "Top40", "8f7bba2ad693b7bd7a54e9f5561df5fd", "670431")    ### [Redone]
        ### Kick Ass
        ### Kick Ass  ---> [['Mika Vs. Redone']]


        addAllMusic(mdbmaps, "Top40", "61e0cad6ba67b77cf03b21bdcc855000", "mn0001072817")   ### [Ndubz]
        ### We Dance On
        ### We Dance On  ---> [['N-Dubz', 'Ndubz & Bodyrox']]


        addAllMusic(mdbmaps, "Top40", "8c59920da3b9afafbe8064702b8ae417", "mn0000866772")   ### [Levada Louca]
        ### Telephone
        ### Telephone  ---> [['Lady Gaga', 'Levada Louca & Belo']]


        addAllMusic(mdbmaps, "Top40", "f9902337667b007c4cb0bd56853d6f77", "mn0001499382")   ### [Don Mescall]
        ### Catch Your Fall
        ### Catch Your Fall  ---> [['Aslan & Don Mescall']]


        addDiscogs(mdbmaps, "Top40", "3a78a66700126f076bc9880499d46098", "6754053")    ### [Theresa Rex]
        ### What I Like About You
        ### What I Like About You  ---> [['Jonas Blue & Theresa Rex']]


        addAllMusic(mdbmaps, "Top40", "45ec0da62cf46f95d1d19d6477e15223", "mn0003492788")   ### [Lewisham & Greenwich NHS Choir]
        ### A Bridge Over You
        ### A Bridge Over You  ---> [['Lewisham & Greenwich NHS Choir']]


        addAllMusic(mdbmaps, "Top40", "b3a0765a3d6a1f9b5f0218cc1a78167d", "mn0001585547")   ### [DJ Champion]
        ### No Heaven
        ### No Heaven  ---> [['DJ Champion']]


        addAllMusic(mdbmaps, "Top40", "4101fb8a2e7d70d355cb78bb670cafb2", "mn0000615641")   ### [N Trance]
        ### Set You Free
        ### Set You Free  ---> [['Gary Allan', 'N Trance']]


        addAllMusic(mdbmaps, "Top40", "d4afc32b214e23fb75edc998fa24f102", "mn0000116049")   ### [D'side]
        ### Stronger Together
        ### Stronger Together  ---> [["D'side"]]


        addAllMusic(mdbmaps, "Top40", "0edfaa56ae9a7023ef89e6dc038b27e7", "mn0000556741")   ### [Marshals]
        ### Make Her Cry
        ### Make Her Cry  ---> [['Marshals']]


        addDiscogs(mdbmaps, "Top40", "ef5682c651f7c5295bc121ad58f18381", "1627595")    ### [St. Julien]
        ### Just Because
        ### Just Because  ---> [["Jane's Addiction", 'St. Julien']]


        addAllMusic(mdbmaps, "Top40", "50eab1669ad5105c900ba050d23f7b37", "mn0002085581")   ### [Ruth-anne]
        ### Take Me Away
        ### Take Me Away  ---> [['Stonebridge', 'DJ S.K.T.', 'Fefe Dobson', 'Ruth-anne']]


        addAllMusic(mdbmaps, "Top40", "123b17da9b4f0bc068b6211be4ba6eeb", "mn0002334760")   ### [Erick]
        ### The Beat Is Rockin
        ### The Beat Is Rockin  ---> [['Erick']]


        addDiscogs(mdbmaps, "Top40", "0f4330d2f262dae9ff367c6c07b07ebd", "1551192")    ### [Temper Trap]
        ### Sweet Disposition
        ### Sweet Disposition  ---> [['Temper Trap']]


        addAllMusic(mdbmaps, "Top40", "08de644904d4cf3503bdb90e1095eb0a", "mn0003330733")   ### [High Hopes Choir]
        ### High Hopes
        ### High Hopes  ---> [['Bruce Springsteen', 'Panic! At The Disco', 'Kodaline', 'High Hopes Choir']]


        addAllMusic(mdbmaps, "Top40", "1b7dbb15e26894ee42a4088cd348af5c", "mn0002840885")   ### [Frankie Sandford]
        ### Dreaming
        ### Dreaming  ---> [['Frankie Sandford ::: Calvin Goldspink']]


        addAllMusic(mdbmaps, "Top40", "7eac99ffb3a009020ae826491a7328a2", "mn0002300128")   ### [Calvin Goldspink]
        ### Dreaming
        ### Dreaming  ---> [['Frankie Sandford ::: Calvin Goldspink']]


        addAllMusic(mdbmaps, "Top40", "a937fec3aae407f22faf4d34080e3c53", "mn0001093965")   ### [Frank Skinner]
        ### 3 Lions
        ### 3 Lions  ---> [['The Lightning Seeds ::: David Baddiel ::: Frank Skinner']]


        addAllMusic(mdbmaps, "Top40", "3772bea79ec33ccc235bd5eb74ec4188", "mn0000662225")   ### [H2O]
        ### What's It Gonna Be
        ### What's It Gonna Be  ---> [['H2O & Platinum']]


        addAllMusic(mdbmaps, "Top40", "2bb54463a4b2619f4cddb21626fd43f3", "mn0000443133")   ### [Donaeo]
        ### Linguo
        ### Linguo  ---> [['Giggs & Donaeo']]


        addDiscogs(mdbmaps, "Top40", "5a56911227b3087c65fa0c64cfc22858", "7175745")    ### [Rani]
        ### Post Malone
        ### Post Malone  ---> [['Sam Feldt & Rani']]


        addAllMusic(mdbmaps, "Top40", "b44c3d5c561812173cb1fadc6bbadad0", "mn0000663567")   ### [Node]
        ### Pakker Bar  ,  Blaest  ,  Al Fuego  ,  Gi Mig Det Hele  ,  JVB  ,  Demawa  ,  Mariah  ,  Opa  ,  Diana  ,  Super Mario  ,  De Snakker  ,  Lay Lay  ,  De Ved Godt  ,  Indifferent  ,  Gi Mig Det Hele  ,  Carnalismo  ,  For Mig Selv  ,  Limbo  ,  Oui  ,  Bang Bang  ,  Ingenting At Sige
        ### Pakker Bar  ---> [['Node']]
        ### Blaest  ---> [['Node']]
        ### Al Fuego  ---> [['Node']]
        ### Gi Mig Det Hele  ---> [['Node', 'Node & Sivas']]
        ### JVB  ---> [['Node']]
        ### Demawa  ---> [['Node']]
        ### Mariah  ---> [['Node']]
        ### Opa  ---> [['Node']]
        ### Diana  ---> [['One Direction', 'Node']]
        ### Super Mario  ---> [['Node']]
        ### De Snakker  ---> [['Node & Stepz']]
        ### Lay Lay  ---> [['Pay & Node']]
        ### De Ved Godt  ---> [['Fouli & Node']]
        ### Indifferent  ---> [['Node & Sivas']]
        ### Gi Mig Det Hele  ---> [['Node', 'Node & Sivas']]
        ### Carnalismo  ---> [['NODE, Branco & Gilli']]
        ### For Mig Selv  ---> [['NODE & Gilli']]
        ### Limbo  ---> [['Scarlet Pleasure', 'NODE & Gilli']]
        ### Oui  ---> [['Jeremih', 'Sivas, Node & Gilli']]
        ### Bang Bang  ---> [['will.i.am', 'Jessie J, Ariana Grande & Nicki Minaj', 'Clemens', 'ZK & Node']]
        ### Ingenting At Sige  ---> [['Gilli & Node']]


        addAllMusic(mdbmaps, "Top40", "94a91dcb424b476f725b107e3d561dd2", "mn0003085199")   ### [A Typisk]
        ### Tillid  ,  Hurtig Bane  ,  Aldrig For Sjov  ,  Plata O Plomo  ,  Kaerlighed
        ### Tillid  ---> [['A Typisk']]
        ### Hurtig Bane  ---> [['A Typisk']]
        ### Aldrig For Sjov  ---> [['A Typisk, Branco & Gilli']]
        ### Plata O Plomo  ---> [['A Typisk & Gilli']]
        ### Kaerlighed  ---> [['A Typisk, Gilli & Kesi']]


        addDiscogs(mdbmaps, "Top40", "244b104a4ecf5d29056a30135da49164", "5558809")    ### [Amanda]
        ### Everybody Doesn't  ,  Tror Vi Er Nem  ,  Blau
        ### Everybody Doesn't  ---> [['Amanda']]
        ### Tror Vi Er Nem  ---> [['Amanda']]
        ### Blau  ---> [['Amanda & Sido']]


        addDiscogs(mdbmaps, "Top40", "9547f484677db99f07f0d2ce639fbcdb", "2644206")    ### [KESI]
        ### Dumme Penge  ,  Vagn Op  ,  Euro
        ### Dumme Penge  ---> [['KESI & Don Stefano']]
        ### Vagn Op  ---> [['KESI & Don Stefano']]
        ### Euro  ---> [['Branco & KESI']]


        addDiscogs(mdbmaps, "Top40", "cf2ec7a5779606dc225eb1ff52a125b5", "610327")    ### [Six]
        ### There's A Whole Lot Of Loving Going On  ,  Let Me Be The One
        ### There's A Whole Lot Of Loving Going On  ---> [['Six']]
        ### Let Me Be The One  ---> [['Six', 'Simon Casey']]


        addDiscogs(mdbmaps, "Top40", "682ff892fde0720742da7539be5cbfd4", "3769696")    ### [Mellemfingamuzik]
        ### Livstil  ,  Safari
        ### Livstil  ---> [['Molo, Benny Jamz, Gilli & Mellemfingamuzik']]
        ### Safari  ---> [['Maxwell, RAF Camora & Bonez MC', 'Molo, Benny Jamz, Gilli & Mellemfingamuzik']]


        addDiscogs(mdbmaps, "Top40", "964b8471bb5b3317ff80c658789fb5c6", "2178850")    ### [Nadja Ga]
        ### Min Indre Stemme  ,  Wanna Be Loved
        ### Min Indre Stemme  ---> [['Michael Rune & Nadja Ga']]
        ### Wanna Be Loved  ---> [['Michael Rune & Nadja Ga']]


        addDiscogs(mdbmaps, "Top40", "5702f798cedf95408e7998cae7160f75", "5094759")    ### [Adhd]
        ### KranAlarm  ,  Vafler
        ### KranAlarm  ---> [['Jesu Brodre & Adhd']]
        ### Vafler  ---> [['Albert Dyrlund, Sidney Lee & Jesu Brodre']]


        addDiscogs(mdbmaps, "Top40", "5f6a0d2ee2e29501ee8668e87c668653", "8290907")    ### [David O'connor]
        ### Don't Look Back In Anger  ,  On Borrowed Wings
        ### Don't Look Back In Anger  ---> [['Oasis', "David O'connor"]]
        ### On Borrowed Wings  ---> [["David O'connor"]]


        addDiscogs(mdbmaps, "Top40", "be31dd84b00112c792101e2ed6bd66b3", "1086751")    ### [Donna & Joe]
        ### Love  ,  Heaven
        ### Love  ---> [['Keyshia Cole', 'Michael Bublé', 'Kendrick Lamar', 'Lana Del Rey', 'The Beatles', 'Donna & Joe', 'Charlie Wilson']]
        ### Heaven  ---> [['Nu Flavor', 'Depeche Mode', 'DJ Sammy', 'DJ Sammy', 'Los Lonely Boys', 'Emeli Sandé', 'Avicii', 'Kane Brown', 'Rebecca Ferguson', 'Donna & Joe', 'Walkmen']]

        
        addDiscogs(mdbmaps, "Top40", "cec35a4d1e39f4804f0329f8a891b635", "606524")    ### [Johnson]
        ### Hey Shorty  ,  Sjus
        ### Hey Shorty  ---> [['Kato, U$o & Johnson']]
        ### Sjus  ---> [['Kato, Ida Corr, Camille Jones & Johnson']]


        addDiscogs(mdbmaps, "Top40", "00d39e303b291175cb7dc306b9316607", "1003686")    ### [Kyla]
        ### One Dance  ,  Boom
        ### One Dance  ---> [['Drake, Wizkid & Kyla']]
        ### Boom  ---> [['Major Lazer, MOTi, Ty Dolla $ign, Wizkid & Kranium', 'Sisse Marie']]


        addAllMusic(mdbmaps, "Top40", "c2a35b01b931ff0ea34c41bb944ed7ad", "mn0000302025")   ### [Rune Rk]
        ### Har Det Hele  ,  Nar Tiden Gar Baglaens
        ### Har Det Hele  ---> [['Rune Rk, Karen & Jooks']]
        ### Nar Tiden Gar Baglaens  ---> [['Clara Sofie & Rune Rk']]


        addDiscogs(mdbmaps, "Top40", "906b28e54bbb4b4cf8c91f488d978719", "5024518")    ### [Emile Kruse]
        ### Air Tonight  ,  Nik & Jay
        ### Air Tonight  ---> [['Emile Kruse & Benjamin Hav']]
        ### Nik & Jay  ---> [['Nik & Jay', 'Topgunn & Benjamin Hav']]


        addDiscogs(mdbmaps, "Top40", "b4ac9bf7c517d486d0dfbb31267e4d3f", "6257928")    ### [Pattersutter]
        ### Nae  ,  Langt Ude
        ### Nae  ---> [['Ude Af Kontrol & Pattersutter']]
        ### Langt Ude  ---> [['Ude Af Kontrol & Faustix']]


        addAllMusic(mdbmaps, "Top40", "ff33e0cca2bc86ca1c8aca2edf6ad878", "mn0000175401")   ### [M.V.P.]
        ### Bounce Shake Move Stop  ,  Roc Ya Body 'mic Check 1, 2'
        ### Bounce Shake Move Stop  ---> [['M.V.P.']]
        ### Roc Ya Body 'mic Check 1, 2'  ---> [['M.V.P.']]


        addDiscogs(mdbmaps, "Top40", "c3eb573746b90008c43fb9ed843e01c4", "396225")    ### [U$o]
        ### Hey Shorty  ,  Sjus
        ### Hey Shorty  ---> [['Kato, U$o & Johnson']]
        ### Sjus  ---> [['Kato, Ida Corr, Camille Jones & Johnson']]


        addDiscogs(mdbmaps, "Top40", "a5e6e308d31db00836b85dec9a28fac6", "120009")    ### [lum]
        ### Dance!
        ### Dance!  ---> [['Goleo Vi/lum']]


        addDiscogs(mdbmaps, "Top40", "9cc336f08daf6b60fdc7df51c4951cd7", "771237")    ### [Soren Huss]
        ### Ocean Of You
        ### Ocean Of You  ---> [['Nik & Jay & Soren Huss']]


        addDiscogs(mdbmaps, "Top40", "2f8ef80aa737b08ccbf4a4f597272dd4", "585244")    ### [Jimmy Jorgensen]
        ### Stjernestov
        ### Stjernestov  ---> [['Jimmy Jorgensen, Chapper & Annika']]


        addDiscogs(mdbmaps, "Top40", "9361a0dd987d763afb7ebda59733dd4b", "164681")    ### [Michael Andr]
        ### Mad World
        ### Mad World  ---> [['Michael Andrews & Gary Jules', 'Adam Lambert', 'Gary Jules With Michael Andr', 'Michael Parsberg']]


        addDiscogs(mdbmaps, "Top40", "8c4759f7357435c07209f893bd031627", "500375")    ### [Goleo Vi]
        ### Dance!
        ### Dance!  ---> [['Goleo Vi/lum']]


        addDiscogs(mdbmaps, "Top40", "df5925386d5e772c54fab9c8ee4afc1a", "2449670")    ### [Bjornskov]
        ### Dimitto (Let Go)
        ### Dimitto (Let Go)  ---> [['Kato, Safri Duo & Bjornskov']]


        addDiscogs(mdbmaps, "Top40", "ea6d8ca839c5321096bf52075b5913a3", "1091530")    ### [Blaes Bukki]
        ### Ga Vaek
        ### Ga Vaek  ---> [['Jokeren & Blaes Bukki']]


        addAllMusic(mdbmaps, "Top40", "dff7682d6b7f9e652467f1d387940420", "mn0002116244")   ### [Michael Caro]
        ### Pas Pa Mikkel
        ### Pas Pa Mikkel  ---> [['Paprika Steen & Michael Caro']]


        addDiscogs(mdbmaps, "Top40", "8293b2b928ccdcfda3a5b282235ed4ba", "489717")    ### [L.o.c.]
        ### Hospital
        ### Hospital  ---> [['Nephew & L.o.c.']]


        addAllMusic(mdbmaps, "Top40", "f101734989e2fb6b8dd4f0192a44424e", "mn0001546498")   ### [Sha]
        ### Verdammt Ich Lieb Dich
        ### Verdammt Ich Lieb Dich  ---> [['Sha']]


        addDiscogs(mdbmaps, "Top40", "c88659abef342c45aaeee57a7208f24b", "3871612")    ### [Jimillian]
        ### Slem Igen
        ### Slem Igen  ---> [['Blak, Jimillian & Ceci Luca']]


        addDiscogs(mdbmaps, "Top40", "cde97ecc04c4fb0ab06efcceb6ba1766", "393367")    ### [Monday]
        ### Tuesday
        ### Tuesday  ---> [['I Love Makonnen & Drake', 'Burak Yeter & Danelle Sandoval', 'Monday/turning Japanese']]


        addDiscogs(mdbmaps, "Top40", "f7a9e3bb639bf960c442d3854cc8e7f7", "709641")    ### [Herrelandsholdet]
        ### Hele Danmark Op At Sta
        ### Hele Danmark Op At Sta  ---> [['Thomas Helmig & Herrelandsholdet']]


        addDiscogs(mdbmaps, "Top40", "9c0415d6fbfcac5c210c5cb9cd921ffd", "4181123")    ### [Fruhstuck Bei Stefanie]
        ### Summerfeeling Pur (Ich Bin Brauner Wie Du!)
        ### Summerfeeling Pur (Ich Bin Brauner Wie Du!)  ---> [['Fruhstuck Bei Stefanie & Udo Martens']]


        addAllMusic(mdbmaps, "Top40", "56fb2c6c60bd0165fcec8d4622f92b80", "mn0002139381")   ### [Buergermeister]
        ### Locker Macha
        ### Locker Macha  ---> [['Buergermeister']]


        addDiscogs(mdbmaps, "Top40", "bb4ac57918a08f80cb48be770d9e9979", "5134105")    ### [Cinco De Mayo]
        ### Stepz
        ### Stepz  ---> [['Cinco De Mayo']]


        addDiscogs(mdbmaps, "Top40", "853397c4ed3d2cd920a67cc9c17067f5", "1883733")    ### [M0]
        ### Pilgrim
        ### Pilgrim  ---> [['M0']]


        addAllMusic(mdbmaps, "Top40", "31c4d92d280c3a99ad3e1a44e9adaf5a", "mn0003793253")   ### [Mathias Og Henriette]
        ### Set Fire To The Third Bar
        ### Set Fire To The Third Bar  ---> [['Mathias Og Henriette']]


        addAllMusic(mdbmaps, "Top40", "0d437db44c23416f96cf5975535f221f", "mn0001963267")   ### [B.a.n.g.e.r.s]
        ### VIP
        ### VIP  ---> [['B.a.n.g.e.r.s']]


        addAllMusic(mdbmaps, "Top40", "2c045db8ead27ec90b26be684dee48a8", "mn0002329134")   ### [Blaojne]
        addDiscogs(mdbmaps, "Top40", "2c045db8ead27ec90b26be684dee48a8", "100681")    ### [Blaojne]
        ### Vil Ha' Dig
        ### Vil Ha' Dig  ---> [['Blaojne']]


        addDiscogs(mdbmaps, "Top40", "ce330beec86bfeb671dc2a2d08562025", "1943966")    ### [Fresh]
        ### Pa Vej
        ### Pa Vej  ---> [['Fresh']]


        addDiscogs(mdbmaps, "Top40", "396a9170c68a28370c6a415e5cb0acdd", "6119064")    ### [LOTTE]
        ### Auf Das, Was Da Noch Kommt
        ### Auf Das, Was Da Noch Kommt  ---> [['LOTTE']]


        addDiscogs(mdbmaps, "Top40", "112cbf6ca3a878116b385274aa05438d", "1482382")    ### [RAF]
        ### Gotham City
        ### Gotham City  ---> [['R. Kelly', 'RAF']]


        addDiscogs(mdbmaps, "Top40", "a07c6ac1b552021b88cfd2e02e78ade3", "5072342")    ### [Laura Van Den Elzen]
        ### Gluecksmoment
        ### Gluecksmoment  ---> [['Laura Van Den Elzen']]


        addDiscogs(mdbmaps, "Top40", "dce6aefe16db0f22d8509a37392fbda0", "34669")    ### [Mia.]
        ### Fallschirm
        ### Fallschirm  ---> [['Mia.']]


        addDiscogs(mdbmaps, "Top40", "a5d240665753e6ec5149a4cfec868fe1", "518132")    ### [Black Fooss]
        ### He Deit Et Wih Un Do Deit Et Wih
        ### He Deit Et Wih Un Do Deit Et Wih  ---> [['Black Fooss']]


        addDiscogs(mdbmaps, "Top40", "5016655838213c82095f3cd9941ab8a8", "86482")    ### [J-luv]
        ### Vergiss Mich
        ### Vergiss Mich  ---> [['Bushido & J-luv']]


        addDiscogs(mdbmaps, "Top40", "014056a5b370a16da25725557f53497b", "1399728")    ### [Zipfelbuben]
        ### Hier Im Dschungel
        ### Hier Im Dschungel  ---> [['Zipfelbuben & Dschungel-allstars 2009']]


        addDiscogs(mdbmaps, "Top40", "2cfa11ab68fa15392a28ba3473bfafd5", "1383823")    ### [Dschungel-allstars 2009]
        ### Hier Im Dschungel
        ### Hier Im Dschungel  ---> [['Zipfelbuben & Dschungel-allstars 2009']]


        addDiscogs(mdbmaps, "Top40", "a9d6b7af886dba4eaa94ee0e6a0400f9", "264574")    ### [The Frank and Walters]
        ### Miles & Miles
        ### Miles & Miles  ---> [['The Frank and Walters']]


        addAllMusic(mdbmaps, "Top40", "c74211123c6662f96a81ef1dd607613b", "mn0003687505")   ### [The Greatest Showman Ensemble]
        ### This Is Me
        ### This Is Me  ---> [['Dream', 'Demi Lovato & Joe Jonas', 'Keala Settle', 'Monrose', 'Keala Settle & The Greatest Showman Ensemble']]

        addDiscogs(mdbmaps, "Top40", "977d879a9ef599db0179842a90eb0829", "2986568")    ### [Nik & Ras]
        ### Fugt I Fundamentet  ,  Hvad Der Sker Her
        ### Fugt I Fundamentet  ---> [['Nik & Ras']]
        ### Hvad Der Sker Her  ---> [['Nik & Ras']]

        addAllMusic(mdbmaps, "Top40", "27b4e2613c000e26afc0dcbf6ab8137a", "mn0001560738")   ### [Milk & Honey]
        addDiscogs(mdbmaps, "Top40", "27b4e2613c000e26afc0dcbf6ab8137a", "506822")    ### [Milk & Honey]
        ### Didi
        ### Didi  ---> [['Milk & Honey']]

        addDiscogs(mdbmaps, "Top40", "4fb5ad8251f32ebc71a4caa19a79671c", "1404551")    ### [Rald Schmitz]
        ### Schaun Und Das Schaf
        ### Schaun Und Das Schaf  ---> [['Rald Schmitz']]

        addDiscogs(mdbmaps, "Top40", "35a5e92b985eb2530625c792eb8794fd", "2261153")    ### [Ell & Nikki]
        ### Running Scared
        ### Running Scared  ---> [['Ell & Nikki']]

        addDiscogs(mdbmaps, "Top40", "108e43f1076de906cdd8ba014d4b16ff", "2068922")    ### [Bonez Mc]
        ### Gottseidank
        ### Gottseidank  ---> [['Trettmann, Bonez Mc & RAF Camora']]

        addDiscogs(mdbmaps, "Top40", "225ac6dbdf0fffd4a9e113da51ca214d", "6081758")    ### [Brudi30]
        ### Ghetto
        ### Ghetto  ---> [['Samra, Capital Bra, Brudi30 & Kalazh44']]

        addDiscogs(mdbmaps, "Top40", "446d29ccb5a2a3de8ac79412defdc3b0", "4255795")    ### [YouNotUs]
        ### Narcotic
        ### Narcotic  ---> [['YouNotUs, Janieck & Senex']]

        addDiscogs(mdbmaps, "Top40", "c3516450970181d37943c2cd92289bfd", "4367398")    ### [Anthony]
        ### Do Ya
        ### Do Ya  ---> [['Anthony & Jasmin']]

        addDiscogs(mdbmaps, "Top40", "df31d4c938e84e9804579b48368955ba", "4453381")    ### [Eicka Jane]
        ### Hojre Og Venstre
        ### Hojre Og Venstre  ---> [['Skinz & Eicka Jane', 'Skinz & Ericka Jane']]

        addDiscogs(mdbmaps, "Top40", "5921f9df84764cd6c69a4f92a205f390", "7671579")    ### [Lolo]
        ### Pub G
        ### Pub G  ---> [['Lolo, Branco & Larry 44']]

        addAllMusic(mdbmaps, "Top40", "9be0a055a02f9facc0f0fb7fc693c793", "mn0000753347")   ### [Snap!]
        ### Rhythm Is A Dancer  ,  The Power Of Bhangra 2003
        ### Rhythm Is A Dancer  ---> [['Snap!']]
        ### The Power Of Bhangra 2003  ---> [['Snap!']]

        addAllMusic(mdbmaps, "Top40", "a0c07f2c1e5e8b60724c92fb83410552", "mn0003380067")   ### [Coleman Hell]
        ### 2 Heads
        ### 2 Heads  ---> [['Coleman Hell']]

        addDeezer(mdbmaps, "Top40", "768af9dd3025f4e218099084284a501b", "54647592")    ### [Mero]
        ### Baller Los  ,  Hobby Hobby  ,  Wolke 10  ,  Jay Jay  ,  Wie Buffon  ,  Hops  ,  Gib Ihn  ,  Mill'n  ,  Auf Dem Weg  ,  Enes Meral  ,  Intro (Ya Hero Ya Mero)  ,  Malediven  ,  Olabilir  ,  Mein Kopf  ,  No Name  ,  Meine Hand  ,  Ferrari  ,  Traume Werden Wahr  ,  Ole Ole  ,  Kein Plan  ,  Kafa Leyla
        ### Baller Los  ---> [['Mero']]
        ### Hobby Hobby  ---> [['Mero']]
        ### Wolke 10  ---> [['Mero']]
        ### Jay Jay  ---> [['Mero']]
        ### Wie Buffon  ---> [['Mero']]
        ### Hops  ---> [['Mero']]
        ### Gib Ihn  ---> [['Mero']]
        ### Mill'n  ---> [['Mero']]
        ### Auf Dem Weg  ---> [['Mero']]
        ### Enes Meral  ---> [['Mero']]
        ### Intro (Ya Hero Ya Mero)  ---> [['Mero']]
        ### Malediven  ---> [['Mero']]
        ### Olabilir  ---> [['Mero']]
        ### Mein Kopf  ---> [['Mero']]
        ### No Name  ---> [["Ryan O'Shaughnessy", 'Mero']]
        ### Meine Hand  ---> [['Mero']]
        ### Ferrari  ---> [['Eno & Mero']]
        ### Traume Werden Wahr  ---> [['Mero & Brado']]
        ### Ole Ole  ---> [['Capital Bra', 'Mero & Brado']]
        ### Kein Plan  ---> [['Loredana & Mero']]
        ### Kafa Leyla  ---> [['Brado & Mero']]


        addDeezer(mdbmaps, "Top40", "52752c575988eb5edea512020cec4858", "2211")    ### [Nena]
        ### Ich Werde Dich Lieben  ,  Wir Sind Wahr  ,  Du Bist So Gut Fur Mich  ,  In Meinem Leben  ,  Heroes/Helden  ,  Das Ist Nicht Alles  ,  Genau Jetzt  ,  Haus Der Drei Sonnen  ,  Strobo Pop  ,  Anyplace, Anywhere, Anytime
        ### Ich Werde Dich Lieben  ---> [['Nena']]
        ### Wir Sind Wahr  ---> [['Nena']]
        ### Du Bist So Gut Fur Mich  ---> [['Nena']]
        ### In Meinem Leben  ---> [['Nena']]
        ### Heroes/Helden  ---> [['Nena']]
        ### Das Ist Nicht Alles  ---> [['Nena']]
        ### Genau Jetzt  ---> [['Nena']]
        ### Haus Der Drei Sonnen  ---> [['Nena & Heppner']]
        ### Strobo Pop  ---> [['Die Atzen Frauenarzt & Nena']]
        ### Anyplace, Anywhere, Anytime  ---> [['Nena & Kim Wilde']]


        addDeezer(mdbmaps, "Top40", "e309c2e3fc905eae304b71e10e82eb99", "75530")    ### [Dream]
        ### He Loves U Not  ,  This Is Me  ,  Shawty Is A 10  ,  Falsetto  ,  I Luv Your Girl  ,  Love VS Money
        ### He Loves U Not  ---> [['Dream']]
        ### This Is Me  ---> [['Dream', 'Demi Lovato & Joe Jonas', 'Keala Settle', 'Monrose', 'Keala Settle & The Greatest Showman Ensemble']]
        ### Shawty Is A 10  ---> [['Dream']]
        ### Falsetto  ---> [['Dream']]
        ### I Luv Your Girl  ---> [['Dream']]
        ### Love VS Money  ---> [['Dream']]


        addDeezer(mdbmaps, "Top40", "8df03772e7cf5b3390e10574a0a90db2", "1407")    ### [Frames]
        ### Falling Slowly  ,  Headlong  ,  Fake  ,  Finally  ,  Sideways Down
        ### Falling Slowly  ---> [['Glen Hansard & Marketa Irglova', 'Frames']]
        ### Headlong  ---> [['Frames']]
        ### Fake  ---> [['Simply Red', 'Frames']]
        ### Finally  ---> [['Frames']]
        ### Sideways Down  ---> [['Frames']]


        addDeezer(mdbmaps, "Top40", "40841ab93e4bc05dbd354f23e76fa1ae", "537158")    ### [Sean Og]
        ### I Still Love You Without Your Car  ,  The Answer  ,  Promises We Hold  ,  I Know
        ### I Still Love You Without Your Car  ---> [['Sean Og']]
        ### The Answer  ---> [['Sean Og']]
        ### Promises We Hold  ---> [['Sean Og']]
        ### I Know  ---> [['Shift K3Y', 'Sean Og']]


        addDeezer(mdbmaps, "Top40", "1f50464766f3a9ce94f1754b0463ec8f", "182603")    ### [Sarah]
        ### Genau Hier  ,  Min Ojesten  ,  Engel  ,  Okay
        ### Genau Hier  ---> [['Sarah']]
        ### Min Ojesten  ---> [['Sarah']]
        ### Engel  ---> [['Sarah', 'Rasmus Seebach']]
        ### Okay  ---> [['Nivea', 'Sarah']]


        addDeezer(mdbmaps, "Top40", "c3e16affa11432c13e8be7cc6c8d736b", "261212")    ### [XX]
        ### Islands  ,  On Hold  ,  Coexist  ,  I See You
        ### Islands  ---> [['XX']]
        ### On Hold  ---> [['XX']]
        ### Coexist  ---> [['XX']]
        ### I See You  ---> [['XX']]


        addDeezer(mdbmaps, "Top40", "fbf1e430c96f43c82045103a7c1407fd", "253597")    ### [George Murphy]
        ### The Moon Going Home  ,  The Land You Love The Best  ,  Something Outta Nothing
        ### The Moon Going Home  ---> [['George Murphy']]
        ### The Land You Love The Best  ---> [['George Murphy']]
        ### Something Outta Nothing  ---> [['George Murphy']]


        addDeezer(mdbmaps, "Top40", "03ece6e9a07c0a5915cfe676a05567a2", "543560")    ### [Kaka]
        ### Bang Bang (Reggaejam)  ,  En Sidste Sang  ,  Gi' Mig Et Smil
        ### Bang Bang (Reggaejam)  ---> [['Kaka']]
        ### En Sidste Sang  ---> [['Kaka']]
        ### Gi' Mig Et Smil  ---> [['Wafande & Kaka']]


        addAllMusic(mdbmaps, "Top40", "cdcec0b0558677aa394a85b105a3699c", "mn0000084053")   ### [The Jam]
        addDeezer(mdbmaps, "Top40", "cdcec0b0558677aa394a85b105a3699c", "3944")    ### [The Jam]
        ### The Sound Of  ,  Snap  ,  Right In The Night
        ### The Sound Of  ---> [['The Jam', 'Bread']]
        ### Snap  ---> [['The Jam']]
        ### Right In The Night  ---> [['Jam & Spoon']]


        addDeezer(mdbmaps, "Top40", "410637b6027dc82a2ce4a93308e58dca", "90401")    ### [Aura]
        ### Something From Nothing  ,  Song For Sophie  ,  I Will Love You Monday
        ### Something From Nothing  ---> [['Aura']]
        ### Song For Sophie  ---> [['Aura Dione', 'Aura']]
        ### I Will Love You Monday  ---> [['Aura Dione', 'Aura']]


        addAllMusic(mdbmaps, "Top40", "91f266ac5ec2839f80f07b9c5385c524", "mn0000057556")   ### [Bill & Gloria Gaither]
        ### Let Freedom Ring: Live From Carnegie Hall  ,  God Bless America: Live From Carnegie Hall
        ### Let Freedom Ring: Live From Carnegie Hall  ---> [['Bill & Gloria Gaither']]
        ### God Bless America: Live From Carnegie Hall  ---> [['Bill & Gloria Gaither']]


        addDeezer(mdbmaps, "Top40", "856bd94164974e377d780028096bc128", "70715")    ### [Martin]
        ### The 1  ,  Show The World
        ### The 1  ---> [['Martin']]
        ### Show The World  ---> [['Martin']]


        addDeezer(mdbmaps, "Top40", "f9793851d6cb8247b6b003a729ce9dc6", "264387")    ### [Nash]
        ### Klassik  ,  Crack, Koks, Piece Unternehmen
        ### Klassik  ---> [['Nash']]
        ### Crack, Koks, Piece Unternehmen  ---> [['Nash & Azet']]


        addDeezer(mdbmaps, "Top40", "6f21b97f1010287aa78ee44d6046702f", "77424")    ### [Karen]
        ### Saekken I Katten  ,  Har Det Hele
        ### Saekken I Katten  ---> [['Karen']]
        ### Har Det Hele  ---> [['Rune Rk, Karen & Jooks']]


        addDeezer(mdbmaps, "Top40", "50201d87ecab39af8f2f0aabc1cffc24", "166116")    ### [Jasmin]
        ### Mit Rette Element  ,  Do Ya
        ### Mit Rette Element  ---> [['Jasmin']]
        ### Do Ya  ---> [['Anthony & Jasmin']]


        addDiscogs(mdbmaps, "Top40", "f7c1455d4147cbf4dc094aa9c2a39356", "3594438")    ### [Zoo]
        ### Poison/I Believe  ,  I Wanna Be Your Lover
        ### Poison/I Believe  ---> [['Zoo']]
        ### I Wanna Be Your Lover  ---> [['Zoo']]


        addAllMusic(mdbmaps, "Top40", "35d8d65ac040e8756273c2f76884e5f5", "mn0003842449")   ### [Beast Coast]
        ### The Only Place  ,  Escape From New York
        ### The Only Place  ---> [['Beast Coast']]
        ### Escape From New York  ---> [['Beast Coast']]


        addDeezer(mdbmaps, "Top40", "c4d67d31024c80e72927ac50751161f7", "16891")    ### [Nicole]
        ### Make It Hot  ,  Come To Me
        ### Make It Hot  ---> [['Nicole', 'VS']]
        ### Come To Me  ---> [['P. Diddy & Nicole']]


        addDiscogs(mdbmaps, "Top40", "b1b3b97ec0478725400c7c8729607be9", "3037345")    ### [Carol Anthony]
        ### Showdown  ,  Wrong
        ### Showdown  ---> [['Jody Lei', 'Carol Anthony']]
        ### Wrong  ---> [['Depeche Mode', 'Carol Anthony']]


        addDeezer(mdbmaps, "Top40", "154e9916e9dc4d52c6dcc9ea8c5934f7", "211032")    ### [Departure]
        ### All Mapped Out  ,  Lump In My Throat
        ### All Mapped Out  ---> [['Departure']]
        ### Lump In My Throat  ---> [['Departure']]


        addDeezer(mdbmaps, "Top40", "a52581e5c20a50979faeecde53d01381", "247134")    ### [Yasmin]
        ### On My Own  ,  Finish Line
        ### On My Own  ---> [['Peach Union', 'Yasmin', 'Hedley']]
        ### Finish Line  ---> [['Yasmin']]


        addDeezer(mdbmaps, "Top40", "86058aed9a9a3acf13a9a98a36b7e7b1", "16065")    ### [Louise]
        ### Pandora's Kiss  ,  Changing Faces - The Best Of
        ### Pandora's Kiss  ---> [['Louise']]
        ### Changing Faces - The Best Of  ---> [['Louise']]


        addDeezer(mdbmaps, "Top40", "f4223a2e29ad572bdd62408309749e55", "4068228")    ### [M.A.D.]
        ### Toyboy  ,  Fame & TV
        ### Toyboy  ---> [['M.A.D.']]
        ### Fame & TV  ---> [['M.A.D.']]


        addDeezer(mdbmaps, "Top40", "dd0c42047d7063ec53285cda72c0610d", "3244121")    ### [Tough Love]
        ### So Freakin' Tight  ,  Pony (Jump On It)
        ### So Freakin' Tight  ---> [['Tough Love']]
        ### Pony (Jump On It)  ---> [['Tough Love & Ginuwine']]


        addDeezer(mdbmaps, "Top40", "e29a4723271638f34847fc292ffa48c3", "271117")    ### [James Fox]
        ### Hold On To Our Love  ,  Bluebirds Flying High
        ### Hold On To Our Love  ---> [['James Fox']]
        ### Bluebirds Flying High  ---> [['James Fox & Cardiff City Fc']]


        addDeezer(mdbmaps, "Top40", "95b9824e26389cf67674f50cb242ef70", "205804")    ### [Unk]
        ### Walk It Out  ,  2 Step
        ### Walk It Out  ---> [['Unk']]
        ### 2 Step  ---> [['Unk']]


        addAllMusic(mdbmaps, "Top40", "914aff29bbb33d9bd8742b9b8d7bbb7c", "mn0001453952")   ### [Chima]
        addDeezer(mdbmaps, "Top40", "914aff29bbb33d9bd8742b9b8d7bbb7c", "283635")    ### [Chima]
        ### Morgen  ,  Ausflug Ins Blaue
        ### Morgen  ---> [['Herbert Grönemeyer', 'Chima']]
        ### Ausflug Ins Blaue  ---> [['Chima']]


        addDiscogs(mdbmaps, "Top40", "9545ffea8117bf350955621bae797917", "39162")   ### [Clever]
        addDeezer(mdbmaps, "Top40", "9545ffea8117bf350955621bae797917", "1261918")    ### [Clever]
        ### Forever
        ### Forever  ---> [['Donell Jones', 'Chris Brown', 'Drake & Kanye West', 'Justin Bieber, Post Malone & Clever', 'Medina', 'Alesso']]


        addDeezer(mdbmaps, "Top40", "a0eaef106d85a20c4f40697e6be08ade", "1219224")    ### [Rory & The Island]
        ### Jimmy's Winning Matches
        ### Jimmy's Winning Matches  ---> [['Rory & The Island']]


        addDeezer(mdbmaps, "Top40", "7b9aa21b6614e8381a912da660081515", "4791900")    ### [Jordan Egan]
        ### Easy For An Angel
        ### Easy For An Angel  ---> [['Jordan Egan']]


        addDeezer(mdbmaps, "Top40", "6ce57bb13155b6a976267ae7fea24a81", "5061058")    ### [The Suspects and Guests]
        ### The River
        ### The River  ---> [['Good Charlotte', 'Davin Herbrüggen', 'The Suspects and Guests']]


        addDiscogs(mdbmaps, "Top40", "dc9afe97092e87a01ec4127299268b14", "97648")    ### [Tone]
        ### Hold Me
        ### Hold Me  ---> [['Brian McKnight, Tone & Kobe Bryant']]


        addDeezer(mdbmaps, "Top40", "331b04fbaf10fec210a976adb4b1d562", "62971")    ### [Heavy]
        ### What Makes A Good Man?
        ### What Makes A Good Man?  ---> [['Heavy']]


        addDeezer(mdbmaps, "Top40", "4534407ec1d2e60bd79803fcac70ddab", "5613402")    ### [Jimmy Magee]
        ### These Old Eyes Have Seen It All
        ### These Old Eyes Have Seen It All  ---> [['Jimmy Magee']]


        addDeezer(mdbmaps, "Top40", "93e2f319eb80a4d47ed7830e34472de8", "164956192")    ### [Steffany Gretzinger]
        ### The Undoing
        ### The Undoing  ---> [['Steffany Gretzinger']]


        addDeezer(mdbmaps, "Top40", "d027967af998dd89ee301fbfadc2a9c6", "7274")    ### [Down]
        ### Down Iv: Part II
        ### Down Iv: Part II  ---> [['Down']]


        addDeezer(mdbmaps, "Top40", "aaa8882482fb1c672c7048f6ad980017", "72652862")    ### [Poppy Fields]
        ### 45 Rpm
        ### 45 Rpm  ---> [['Poppy Fields']]

        addDeezer(mdbmaps, "Top40", "84ea1e6425431af3e3c9132c3ef0dff2", "5359329")    ### [Presentation Secondary School Clonmel]
        ### My Hero
        ### My Hero  ---> [['Presentation Secondary School Clonmel']]


        addDeezer(mdbmaps, "Top40", "23a4949a6ef2a59b0a1992d55a5e7119", "100307")    ### [Versatile]
        ### Prefontaine
        ### Prefontaine  ---> [['Versatile']]


        addDeezer(mdbmaps, "Top40", "387f8b95bf312f4e1f06c3fa8a2e702d", "7204178")    ### [The Zog Chorus]
        ### We All Stand Together
        ### We All Stand Together  ---> [['The Zog Chorus']]


        addDeezer(mdbmaps, "Top40", "d571e0c4adaf9473e43a55048b524222", "248033")    ### [Chuckie]
        ### Let The Bass Kick In Miami Bitch
        ### Let The Bass Kick In Miami Bitch  ---> [['Chuckie & Lmfao']]


        addDeezer(mdbmaps, "Top40", "83e36a7fbb4e47d90df2c7a5f41ceca5", "5283366")    ### [Avener]
        ### Fade Out Lines
        ### Fade Out Lines  ---> [['Avener']]


        addDiscogs(mdbmaps, "Top40", "d8af7b562fb5b6896e9caf208a7631fe", "2500803")    ### [Daisy Dares You]
        ### Number One Enemy
        ### Number One Enemy  ---> [['Daisy Dares You & Chipmunk']]

        addDeezer(mdbmaps, "Top40", "3771c6784980f14a97a79960df44683f", "7416924")    ### [Emzee A]
        ### Lose Your Mind
        ### Lose Your Mind  ---> [['Hijackers & Sadbh & Emzee A']]

        addDeezer(mdbmaps, "Top40", "ea418f0376767c59aea193fb88f2fbed", "11807729")    ### [Audrey Trainor]
        ### Falling Up
        ### Falling Up  ---> [["James O'Connor & Audrey Trainor"]]

        addDeezer(mdbmaps, "Top40", "f39917252c23494a2bffc34608080e34", "4566327")    ### [Edmee]
        ### Listen To Your Heart
        ### Listen To Your Heart  ---> [['D.H.T.', 'DHT & Edmee']]


        addDeezer(mdbmaps, "Top40", "13568fea713fb70f4a72987863820910", "67704502")    ### [Paradise Hotel 2019]
        ### Don Julio
        ### Don Julio  ---> [['Paradise Hotel 2019 & Bro']]


        addDeezer(mdbmaps, "Top40", "a552723762e26b8bf2ff3cf00abb742e", "76729")    ### [Vera]
        ### Paris
        ### Paris  ---> [['Paris Hilton', 'The Chainsmokers', 'Lord Siva & Vera']]


        addDeezer(mdbmaps, "Top40", "e20047c96a03c801a7a761d639303baa", "105146")    ### [Christina]
        ### Let Love Be Love
        ### Let Love Be Love  ---> [['S.O.A.P.', 'S.O.A.P., Juice, Christina & Remee']]

        addDeezer(mdbmaps, "Top40", "747e53fad10278c0be9f12e5064e1a8a", "9435020")    ### [Ung Cezar]
        ### La Ma Li
        ### La Ma Li  ---> [['Jamaika & Ung Cezar, Carmon']]


        addDeezer(mdbmaps, "Top40", "59755826fe21e0d913917f38e519bd97", "4037981")    ### [Trinidad James]
        ### All Gold Everything
        ### All Gold Everything  ---> [['Trinidad James']]


        addDiscogs(mdbmaps, "Top40", "b091868e0d9e66c4f3cfc3d57c0e15c1", "6754464")    ### [Pauline]
        ### Kun Os To
        ### Kun Os To  ---> [['Jokeren & Pauline']]


        addDiscogs(mdbmaps, "Top40", "fdef672eb79aa1e42d68559231f9e91a", "2891027")    ### [Contiez]
        ### Trumpsta
        ### Trumpsta  ---> [['Contiez & Treyy G']]


        addDiscogs(mdbmaps, "Top40", "376424d25e7c667172ea571a9bd5ecf7", "34061")   ### [DT8]
        addDeezer(mdbmaps, "Top40", "376424d25e7c667172ea571a9bd5ecf7", "16653")    ### [DT8]
        ### Destination
        ### Destination  ---> [['Ronan Keating', 'DT8']]


        addDeezer(mdbmaps, "Top40", "298dc80023436fd7d1327755dc0f3aea", "5406531")    ### [Virginia To Vegas]
        ### We Are Stars
        ### We Are Stars  ---> [['Virginia To Vegas & Alyssa Reid']]


        addAllMusic(mdbmaps, "Top40", "df7a414766c07b227b947fe19d735cca", "mn0000527296")   ### [P.I.]
        ### Shake That Body
        ### Shake That Body  ---> [['P.I. & Elephant Man']]


        addDiscogs(mdbmaps, "Top40", "9ffc319f3524de0eb5857b3a041e89d8", "4115550")   ### [Rin]
        ### Keine Liebe
        ### Keine Liebe  ---> [['Rin & Bausa']]


        addDiscogs(mdbmaps, "Top40", "6c757d349b981f59ce15f8050351c33b", "286345")   ### [Androids]
        ### Do It With Madonna
        ### Do It With Madonna  ---> [['Androids']]


        addDiscogs(mdbmaps, "Top40", "2580311e731b9bca913825f23a494d96", "4511617")    ### [Alina]
        ### Kleine Taschenlampe Brenn
        ### Kleine Taschenlampe Brenn  ---> [['Christian Petru & Alina']]


        addDeezer(mdbmaps, "Top40", "f8c6ee3fdec7c8e8d68666db7bd07a5b", "1217914")    ### [Zion & Lennox]
        ### Subeme La Radio
        ### Subeme La Radio  ---> [['Enrique Iglesias, Descemer Bueno, Zion & Lennox']]


        addDeezer(mdbmaps, "Top40", "04b0ea321844b974fa623332ec9e81a8", "1234739")    ### [Nadine]
        ### Insatiable
        ### Insatiable  ---> [['Darren Hayes', 'Nadine']]


        addDiscogs(mdbmaps, "Top40", "5b813121e727842a70d17d40279c8060", "3915565")    ### [Tieks]
        ### Sunshine
        ### Sunshine  ---> [['S Club 7', 'Twista', "Lil' Flip & Lea", 'Gareth Gates', 'Tieks & Dan Harkna']]


        addDeezer(mdbmaps, "Top40", "e6852c19581c5c2842941d6585011de8", "507529")    ### [New Sunset Hotel]
        ### The Bitter End
        ### The Bitter End  ---> [['Placebo', 'New Sunset Hotel']]


        addDeezer(mdbmaps, "Top40", "1ee6a7f79efe291ad8bc9ba50f14ee39", "110592")    ### [Tarja]
        ### I Walk Alone
        ### I Walk Alone  ---> [['Tarja']]


        addDeezer(mdbmaps, "Top40", "f70f7318448d90d9e2648fa729d0ccd9", "7569860")    ### [Mendoza]
        ### Love Druggie
        ### Love Druggie  ---> [['Mendoza']]

        addDeezer(mdbmaps, "Top40", "87019c83d1d9002251d5e0123d73de2f", "4158299")    ### [Ladywell Primary School]
        ### O Holy Night
        ### O Holy Night  ---> [['Ladywell Primary School', 'Jackie Evancho']]

        addDeezer(mdbmaps, "Top40", "70fd12ba96ac516bed74bb1918828f96", "7215388")    ### [Wealdstone Raider]
        ### Got No Fans
        ### Got No Fans  ---> [['Wealdstone Raider']]


        addDeezer(mdbmaps, "Top40", "18a4ef47c6e65a8cd0686f17dcb5a2d6", "458443")    ### [Mike Sheridan]
        ### Med Sma Skridt
        ### Med Sma Skridt  ---> [['Mike Sheridan']]


        addDeezer(mdbmaps, "Top40", "b6f0eeb7241d52315a563b41a83f03ab", "12544804")    ### [LIV'n'G]
        ### Smile For Bradley
        ### Smile For Bradley  ---> [["LIV'n'G"]]


        addDeezer(mdbmaps, "Top40", "3203329df817eab4fd383d2515def0c7", "61557012")    ### [RSPB]
        ### Let Nature Sing
        ### Let Nature Sing  ---> [['RSPB']]


        addDeezer(mdbmaps, "Top40", "3de5a67ac001eda9da009b4269f64d72", "84950802")    ### [Tobi & Manny]
        ### Destined For Greatness
        ### Destined For Greatness  ---> [['Tobi & Manny']]


        addDeezer(mdbmaps, "Top40", "8476f77796a006e9d4cbafa3404aebac", "55142")    ### [Virgo]
        ### Bubbles
        ### Bubbles  ---> [['Biffy Clyro', 'Virgo']]


        addDeezer(mdbmaps, "Top40", "7befb4ecd12fe5e883dc1785be298dab", "134048")    ### [Fabric Bent]
        ### Jukebox
        ### Jukebox  ---> [['Fabric Bent', 'Cat Power']]


        addDiscogs(mdbmaps, "Top40", "9d224a59b3df753402c55e6974c203b5", "1335584")   ### [Eddy Bar]
        addDeezer(mdbmaps, "Top40", "9d224a59b3df753402c55e6974c203b5", "152363")    ### [Eddy Bar]
        ### Verliebt
        ### Verliebt  ---> [['Eddy Bar']]


        addDeezer(mdbmaps, "Top40", "c039dcafb38ef291cd3576f6f2d96498", "14492701")    ### [Ransom]
        ### Lil Tecca
        ### Lil Tecca  ---> [['Ransom']]


        addDeezer(mdbmaps, "Top40", "538d641f7c607731ce3c97de84888ddc", "10904")    ### [Trooper]
        ### We're Here For A Good Time
        ### We're Here For A Good Time  ---> [['Trooper']]


        addAllMusic(mdbmaps, "Top40", "576086654e3dac2a5660989c51366659", "mn0000043629")   ### [Bushido Produziert Sonny Black]
        addDeezer(mdbmaps, "Top40", "576086654e3dac2a5660989c51366659", "143975")    ### [Bushido Produziert Sonny Black]
        ### Eine Chance / Zu Gangsta
        ### Eine Chance / Zu Gangsta  ---> [['Bushido Produziert Sonny Black']]


        addDeezer(mdbmaps, "Top40", "d4e420120a039e03455ee8536740a0a0", "2128")    ### [Goldfinger]
        ### Darrin's Coconut Ass
        ### Darrin's Coconut Ass  ---> [['Goldfinger']]


        addDeezer(mdbmaps, "Top40", "d9de59336d2d408662aa03ad71e870b1", "4036827")    ### [Andreas Kummert]
        ### Simple Man
        ### Simple Man  ---> [['Andreas Kummert']]


        addDeezer(mdbmaps, "Top40", "5edc174fb5fefd278c05b53dbd1bd2e0", "14740207")    ### [Prince Karma]
        ### Later Bitches
        ### Later Bitches  ---> [['Prince Karma']]


        addDeezer(mdbmaps, "Top40", "603304c35dea9d2995f5ea307fc3e437", "5361924")    ### [Judith Van Hel]
        ### F**kin' Beautiful
        ### F**kin' Beautiful  ---> [['Judith Van Hel']]


        addDeezer(mdbmaps, "Top40", "18e08ec319bb5434ce1be10ede35b88d", "15224255")    ### [KMN Gang]
        ### KMN Member
        ### KMN Member  ---> [['KMN Gang']]


        addDeezer(mdbmaps, "Top40", "043c614068c79f134a62512dd92dd205", "4747977")    ### [Meltem Acikgoz]
        ### Explosion In My Heart
        ### Explosion In My Heart  ---> [['Meltem Acikgoz']]


        addDeezer(mdbmaps, "Top40", "f97c6800d97bc9b645de82758b1b616e", "4844456")    ### [Minds Of 99]
        ### Som Fluer
        ### Som Fluer  ---> [['Minds Of 99']]


        addDeezer(mdbmaps, "Top40", "1f84610afa18b37896d9cb8c3ffb929a", "9356090")    ### [POL1Z1STENS0HN]
        ### Ich Hab Polizei
        ### Ich Hab Polizei  ---> [['POL1Z1STENS0HN']]


        addAllMusic(mdbmaps, "Top40", "7dbc379090f7843f537ea0df634b1aad", "mn0000748795")   ### [Shifty]
        addDeezer(mdbmaps, "Top40", "7dbc379090f7843f537ea0df634b1aad", "6677")    ### [Shifty]
        ### Slide Along Side
        ### Slide Along Side  ---> [['Shifty']]


        addDeezer(mdbmaps, "Top40", "a17bf82b0c99a5d6a9fdb61e1cba475b", "567150")    ### [Leanne Moore]
        ### On Wings
        ### On Wings  ---> [['Leanne Moore']]


        addDeezer(mdbmaps, "Top40", "3a9adb2ba05512379660af30c4499d9e", "255246")    ### [Seneca]
        ### Clarity
        ### Clarity  ---> [['Zedd', 'Seneca']]


        addDeezer(mdbmaps, "Top40", "18091df6740eb23606268e1fe70a832e", "262682")    ### [Dustin The Turkey]
        ### Irelande Douze Points
        ### Irelande Douze Points  ---> [['Dustin The Turkey']]


        addDeezer(mdbmaps, "Top40", "ab0121020ea6f52f5dcc2b0ad8417684", "1569593")    ### [Kanyu Tree]
        ### Tanglewood
        ### Tanglewood  ---> [['Kanyu Tree']]


        addDeezer(mdbmaps, "Top40", "1feb0b498fd6b76e794cd4994499bd66", "471918")    ### [Scuba Dice]
        ### Holiday
        ### Holiday  ---> [['Green Day', 'Dizzee Rascal', 'DJ Antoine & Akon', "Mad'house", 'Scuba Dice']]


        addDeezer(mdbmaps, "Top40", "3531e20a4eaab8cd5b085fc9605f6fba", "261093")    ### [Martin Staunton Band]
        ### My Luck Is About To Change
        ### My Luck Is About To Change  ---> [['Martin Staunton Band']]


        addDeezer(mdbmaps, "Top40", "8d229bc5952f811627abcecf1a1d9f6d", "404641")    ### [Soul Control]
        ### Chocolate
        ### Chocolate  ---> [['Kylie Minogue', 'Snow Patrol', 'Soul Control', 'The 1975']]


        addAllMusic(mdbmaps, "Top40", "c87cad8f7c42f2e678a0c18782869407", "mn0001951902")   ### [Conway Sisters]
        addDeezer(mdbmaps, "Top40", "c87cad8f7c42f2e678a0c18782869407", "5441329")    ### [Conway Sisters]
        ### Miss You
        ### Miss You  ---> [['Aaliyah', 'Louis Tomlinson', 'Conway Sisters']]


        addDeezer(mdbmaps, "Top40", "bf39144a5e6eb48401d5732ec4edddf4", "15811")    ### [Delirious]
        ### History Maker
        ### History Maker  ---> [['Delirious']]


        addDeezer(mdbmaps, "Top40", "d1029792b9078894873b1965b343540c", "262762")    ### [Walls]
        ### To The Bright And Shining Sun
        ### To The Bright And Shining Sun  ---> [['Walls']]


        addDiscogs(mdbmaps, "Top40", "009bc268f4161c893c3469d0f475fa03", "393367")    ### [The Revs]
        ### Tuesday
        ### Tuesday  ---> [['I Love Makonnen & Drake', 'Burak Yeter & Danelle Sandoval', 'The Revs']]


        #addAllMusic(mdbmaps, "Top40", "fc3c86e99326e364c73c36b59c14fb0c", "mn0000470452")   ### [Music]
        #addAllMusic(mdbmaps, "Top40", "f0f3461c81e52c4e94f8bd2a200e0e6e", "mn0001260391")   ### [Howard Brown]
        #addAllMusic(mdbmaps, "Top40", "58ee67ae2b6cec123858e75a2c499ac1", "mn0001902858")   ### [ZHU]
        #addAllMusic(mdbmaps, "Top40", "b55d253d763717f7f3d036930160a5bf", "mn0003450633")   ### [Joe Weller]
        #addAllMusic(mdbmaps, "Top40", "00d21da421c333e9275a9b1eecc0190a", "mn0003461700")   ### [Reggie N Bollie]
        #addAllMusic(mdbmaps, "Top40", "45bdd07b18f741171b8f823cb5531b1b", "mn0000288296")   ### [K-Os]
        #addAllMusic(mdbmaps, "Top40", "2f658d7ad8a74a64fca02906b03f0985", "mn0001549688")   ### [Kuz]
        #addAllMusic(mdbmaps, "Top40", "d0bb0f381518f02cf6a1f40d59737e9d", "mn0002499825")   ### [Longo & Wainwright]
        #addAllMusic(mdbmaps, "Top40", "b6ea04ff4ed93b06ddc3a4d3d34b674e", "mn0002897901")   ### [Pardon My Striptease]
        #addAllMusic(mdbmaps, "Top40", "0f45947e8594b1226b9d50053601883b", "mn0000284904")   ### [Saffron Hill]
        #addAllMusic(mdbmaps, "Top40", "c291c883c9e68d96e616007fab615656", "mn0001466009")   ### [The Sunshine Girls]
        #addAllMusic(mdbmaps, "Top40", "6b03a6d10e22e2dde3f5abc658ffafc6", "mn0000489876")   ### [Pogues]
        #addAllMusic(mdbmaps, "Top40", "d1b1c19a7e61652d30de30746345e837", "mn0002123512")   ### [Good The Bad]
        #addAllMusic(mdbmaps, "Top40", "add9f11466ff3ee0774b7ffbc244106c", "mn0000470062")   ### [Corenell]
        #addAllMusic(mdbmaps, "Top40", "beeb2ef4da5a01f2fd88ffecd74b4fb9", "mn0000387383")   ### [Matthew Gerrard]
        #addAllMusic(mdbmaps, "Top40", "f47310ec752e58e809eb26edd0ee8995", "mn0000678402")   ### [Hercules]
        #addAllMusic(mdbmaps, "Top40", "a5c79ea8bbb13a12a93720b36196ebfb", "mn0000090205")   ### [KOP Choir]
        #addAllMusic(mdbmaps, "Top40", "7bb4e254695e8be9aca8a2f048e57ace", "mn0001385485")   ### [Sir Terry Wogan]
        #addAllMusic(mdbmaps, "Top40", "f48714af964dcf0160692580cd8742a9", "mn0000726348")   ### [B.o.B.]
        #addAllMusic(mdbmaps, "Top40", "5245c98825431442b0adbb71b5675234", "mn0002672644")   ### [Jessica Lowndes]
        #addAllMusic(mdbmaps, "Top40", "b0081d72d709361b53f6c0a56db61e77", "mn0003185852")   ### [Clement Marfo]
        #addAllMusic(mdbmaps, "Top40", "243afb56fb3c22843893bcf5c2a01751", "mn0003024414")   ### [Ms. D]
        #addAllMusic(mdbmaps, "Top40", "d60e5078ec5e8e2f49172b85fd26bc1b", "mn0000691648")   ### [Will.I.am]
        #addAllMusic(mdbmaps, "Top40", "9b4f8beb2d7f9ca05bcfbd920c9263c0", "mn0002229182")   ### [Alex Evans]
        #addAllMusic(mdbmaps, "Top40", "d8c6f7db6b8eccc5dd4ef201d69cd0f4", "mn0001087003")   ### [Michael Molloy]
        #addAllMusic(mdbmaps, "Top40", "977861c399b47a9d9ee34202e4948ba1", "mn0001462437")   ### [Cludia Leitte]
        #addAllMusic(mdbmaps, "Top40", "eedb05531b63fb5d38bbd64ea7fadc02", "mn0003297073")   ### [Krishane]
        #addAllMusic(mdbmaps, "Top40", "33985f65bc8922ad74c4ecc74df60e0d", "mn0003105389")   ### [Chris Lorenzo]
        #addAllMusic(mdbmaps, "Top40", "f94f10108c3c0f8bcb90cc9406eff356", "mn0003220113")   ### [KSI]
        #addAllMusic(mdbmaps, "Top40", "2051f3df9b30eefb8f0957994e86068f", "mn0002871297")   ### [Krept]
        #addAllMusic(mdbmaps, "Top40", "2be3576efb7250ccde9930a410225d9c", "mn0000909806")   ### [Costi]
        #addAllMusic(mdbmaps, "Top40", "c0eb1400d5993ffd8bbba43c21c3220d", "mn0002961009")   ### [Fuse Odg]
        #addAllMusic(mdbmaps, "Top40", "61209c7a42f9f1b71d78bc92af7e20cb", "mn0003496468")   ### [George Kwali]
        ##addAllMusic(mdbmaps, "Top40", "e47b4afb91d451258bb347e8ad0d1fef", "mn0003504948")   ### [Tom Zanetti]
        #addAllMusic(mdbmaps, "Top40", "2f0f3c80c18996d0fcdaf1e3665e5889", "mn0003241123")   ### [Sandro Cavazza]
        #addAllMusic(mdbmaps, "Top40", "8229261e1705f29d7f40840f930c474d", "mn0003687506")   ### [Ziv Zaifman]
        #addAllMusic(mdbmaps, "Top40", "9a5f8a2dcace1d96bdbe35e960c0a348", "mn0003650946")   ### [Lotto Boyzz]
        #addAllMusic(mdbmaps, "Top40", "4e52d5d137bcce4579f92fe098a0133b", "mn0003565650")   ### [Aj Tracey]
        #addAllMusic(mdbmaps, "Top40", "aec80957e142afdca5815e2b7e0014ba", "mn0003705226")   ### [Au/Ra]
        #addAllMusic(mdbmaps, "Top40", "ef7dcbdaf15fd3269409d5e32368f82e", "mn0002638712")   ### [Lily James]
        #addAllMusic(mdbmaps, "Top40", "bb14989fefc1ff0333af020efc663161", "mn0003747970")   ### [Alexa Davies]
        #addAllMusic(mdbmaps, "Top40", "b629a83f0d9d9aae74780acbd70a86c4", "mn0003076656")   ### [Dalton Harris]
        #addAllMusic(mdbmaps, "Top40", "e352bab9cb5dadf2803730eae6189866", "mn0003185359")   ### [5SOS]        
        #addAllMusic(mdbmaps, "Top40", "ebcd3654818b99298f164b501b45bf65", "mn0003747558")   ### [Swarmz]
        #addAllMusic(mdbmaps, "Top40", "6e33a55e24bfe720352f55bbea21a4bd", "mn0003180459")   ### [DaBeatfreakz]
        #addAllMusic(mdbmaps, "Top40", "54fe0bc1dee2d4af1ab53ddf5a66d89c", "mn0003446630")   ### [Mostack]
        #addAllMusic(mdbmaps, "Top40", "1c6bd0c5d43de540717c51826ea39505", "mn0003455181")   ### [Young ADZ]
        #addAllMusic(mdbmaps, "Top40", "b90179d8ef2f121903bc19926b62015b", "mn0003934536")   ### [Icee Tgm]
        #addAllMusic(mdbmaps, "Top40", "4b77d39026ce653e5bc9af8c19996c75", "mn0003908179")   ### [M24]
        #addAllMusic(mdbmaps, "Top40", "2f4d50ddbb0c5910de290b5ad05c0def", "mn0000413000")   ### [P Diddy]
        #addAllMusic(mdbmaps, "Top40", "6f70887cd82af0fda52880c24077c37a", "mn0000929905")   ### [Dice Gamble]
        #addAllMusic(mdbmaps, "Top40", "24a0bec7f410ed6d5038da34f83e70c2", "mn0001536028")   ### [Crystal Dove]
        #addAllMusic(mdbmaps, "Top40", "778154e470364c0cb7f1ad4baa4b02d8", "mn0001358136")   ### [Dj Drama]
        #addAllMusic(mdbmaps, "Top40", "dde4d7edd427a043f5199823628960d8", "mn0001579334")   ### [El Greco]
        #addAllMusic(mdbmaps, "Top40", "df7a414766c07b227b947fe19d735cca", "mn0000527296")   ### [P.I.]
        #addAllMusic(mdbmaps, "Top40", "3d692f4e84c3c775a5cd65894a763bf0", "mn0000924780")   ### [Anti-flag]    
        #addAllMusic(mdbmaps, "Top40", "b2edd3cb9c353c6c4fe4eb63d48253ae", "mn0002540639")   ### [The Vanillas]
        #addAllMusic(mdbmaps, "Top40", "949dba6828d73d97e2c50e03cf4e95fc", "mn0000480317")   ### [Steve Kazee]
        #addAllMusic(mdbmaps, "Top40", "9e0d9fc64b4b3ec5e7534e78f3dd2520", "mn0002989492")   ### [Lily Rose Cooper]
        #addAllMusic(mdbmaps, "Top40", "54c32d678aeec6155db6023b97e6f314", "mn0003170454")   ### [Green Shoe Studio]
        #addAllMusic(mdbmaps, "Top40", "dd3f0d98a8b58b402f1880762372251f", "mn0003170457")   ### [Jacob Colgan]
        #addAllMusic(mdbmaps, "Top40", "7921cd78d8776f3e14d16a28a1976976", "mn0003170453")   ### [Fred Stobaugh]
        #addAllMusic(mdbmaps, "Top40", "b7428890726a5fbe7b599eebb911f87e", "mn0000726348")   ### [B.o.b.]
        #addAllMusic(mdbmaps, "Top40", "767f8733ed00f2f6c9047d696baf629d", "mn0003125737")   ### [Colleen D` Agostino]
        #addAllMusic(mdbmaps, "Top40", "03441a2dcd40a582806544349a64cfd3", "mn0002808033")   ### [Anami Vice]
        #addAllMusic(mdbmaps, "Top40", "646d335e41f98d03b7c3fa5a2e5575b9", "mn0003075926")   ### [Mo]
        #addAllMusic(mdbmaps, "Top40", "2eeaf831193dbf94567b6adcbd4de009", "mn0003308066")   ### [Bryce Vine]
        #addAllMusic(mdbmaps, "Top40", "4532559cfa14536d7fdcc4841a34f2e3", "mn0003847096")   ### [Bbno$]
        #addAllMusic(mdbmaps, "Top40", "c82cbb6b20301ca63b302f0b334bb3fb", "mn0003829424")   ### [Y2K]
        #addAllMusic(mdbmaps, "Top40", "cc7cdd540d61531146e970c900a50547", "mn0001514049")   ### [Rachel O'Donnell]
        #addAllMusic(mdbmaps, "Top40", "f57a4e5394fc6b6b643e965035eec629", "mn0000083013")   ### [The Jackson Five]
        #addAllMusic(mdbmaps, "Top40", "0eecedaa1ccc32c09b81a81ec75c5fb9", "mn0001315050")   ### [Blof]
        #addAllMusic(mdbmaps, "Top40", "9279c754c49a3c40f9156b3c8c2dd592", "mn0000516868")   ### [Hakan Hellstrom]
        #addAllMusic(mdbmaps, "Top40", "b44c3d5c561812173cb1fadc6bbadad0", "mn0003726124")   ### [Node]
        #addAllMusic(mdbmaps, "Top40", "fa02711d096d1a7ca7ff5743a3cf095b", "mn0002013372")   ### [Raf Camora]
    
        #addAllMusic(mdbmaps, "Top40", "996dc2db2e60fc3de7a14828df795171", "mn0003729938")   ### [Z. E.]

        #addAllMusic(mdbmaps, "Top40", "38cab1fb43cfee792ffbe27ee1a8b402", "mn0000534528")   ### [Helene Segara]

        #addDiscogs(mdbmaps, "Top40", "ab418d4cdc49904fd3cb918b534f2e32", "6721597")    ### [Billy Hlapeto]
        ### Bashmaistorska  ,  Kogato Ti Triabvam  ,  Kakto Iskash  ,  Malkite Neshha  ,  Skochi Nad Men  ,  Kazhi Mi Veche Vsichko  ,  Zlatnite Momcheta  ,  Zapazeno Mjasto

        #addDiscogs(mdbmaps, "Top40", "60e0b849d26d3ca9fd7495fd7e7d6de6", "7630813")    ### [Dim4ou]
        ### Bashmaistorska  ,  Kogato Ti Triabvam  ,  Kakto Iskash  ,  Malkite Neshha  ,  Skochi Nad Men  ,  Kazhi Mi Veche Vsichko  ,  Zlatnite Momcheta  ,  Zapazeno Mjasto

        #addAllMusic(mdbmaps, "Top40", "fa393c6150d3f872306dee987670e110", "mn0001462042")   ### [Keen`V]
        ### Dis-Moi Oui (Marina)  ,  Rien Qu'une Fois  ,  Le Son Qui Bam Bam  ,  Les Mots  ,  Ma Vie Au Soleil  ,  Keen V Elle T A Mata  ,  La Vie Du Bon Cote  ,  Petite Emilie

        #addAllMusic(mdbmaps, "Top40", "7061e79e486007acdc5409139bcfcc07", "mn0002526100")   ### [LaCrim]
        ### Pronto  ,  Sablier  ,  Mon Glock Te Mettra A Genoux  ,  Tout Le Monde Veut Des Loves  ,  Corleone  ,  Pocket Coffee  ,  Billets En Lair  ,  Grande Armee

        #addAllMusic(mdbmaps, "Top40", "81121caec82e95ee97bbaf3d3fd1a1a5", "mn0003373493")   ### [SA4]
        ### Allstars  ,  Haifischnikez Allstars  ,  Super Lemon Haze  ,  Mercy Mercy  ,  Strassenbande  ,  Sa4  ,  Perdono  ,  The Party Is Over

        #addAllMusic(mdbmaps, "Top40", "01849a34338bbba9d47201944a326596", "mn0002050239")   ### [Opposites]
        ### Broodje Bakpao  ,  Licht Uit  ,  Slapeloze Nachten  ,  Sukkel Voor De Liefde  ,  Slaap  ,  Brief Aan Jou  ,  Hey DJ

        #addAllMusic(mdbmaps, "Top40", "fb2419f9e6b98ed6e7dab91410e0edf1", "mn0002083163")   ### [Evelyn]
        ### One Night In Ibiza  ,  2012 (If The World Would End)  ,  Everybody  ,  Everybody  ,  Insomnia  ,  Sunshine (fly So High)  ,  Take Control

        
        
        mdbmaps["Top40"].save()        

        
        
def extraAddsForBillboardYE(mdbmaps, chartType):
    if chartType == "BillboardYE":
        
        addAllMusic(mdbmaps, "BillboardYE", "4e47b741a3360c9b898fc24d54d61d63", "mn0003075926")   ### MØ
        addDiscogs(mdbmaps, "BillboardYE", "4e47b741a3360c9b898fc24d54d61d63", "1883733")    ### MØ
        ### Lean On  ,  Turn Down For What

        addAllMusic(mdbmaps, "BillboardYE", "4b85c05fcea846216375d950a0ae3cba", "mn0003534306")   ### [Grey]
        ### The Middle  ,  Stay

        addAllMusic(mdbmaps, "BillboardYE", "a6b2d85fd2bb6caa2dbbfb632d160254", "mn0002908858")   ### [Myles Kennedy And The Conspirators]
        ### Apocalyptic Love

        addDiscogs(mdbmaps, "BillboardYE", "b332342e9204701073a4fb8ec26daf78", "1702929")    ### [Nayer]
        ### Give Me Everything  ,  Hey Mama
        
        addAllMusic(mdbmaps, "BillboardYE", "a3b3b076b58dd330bfbb945bfd7484c3", "mn0000315463")   ### [Scarface]
        ### EMERITUS  ,  Made

        addAllMusic(mdbmaps, "BillboardYE", "9bd03e0a0b2968d93ff9f1ff8e095bad", "mn0001225951")   ### [Mustard]
        ### Ballin'  ,  High Fashion  ,  Pure Water

        addAllMusic(mdbmaps, "BillboardYE", "98b48695d58c81efb7b5738dbd19b2e4", "mn0001530959")   ### [Casino]
        ### Move That Doh  ,  Mercy

        addAllMusic(mdbmaps, "BillboardYE", "610e1c1e3a97b72aa0a95f704a6630fd", "mn0000111898")   ### [Jim Jones]
        ### We Fly High  ,  Pop Champagne

        addAllMusic(mdbmaps, "BillboardYE", "825d65c4b54ef8b06078343824c28e3a", "mn0001383182")   ### [Brook-Lyn]
        ### Enough Cryin

        addAllMusic(mdbmaps, "BillboardYE", "7312d9edc361e6f15379ec76aef91960", "mn0003557359")   ### [Cutty]
        ### Some Cut

        addAllMusic(mdbmaps, "BillboardYE", "62c1f64ef936e85ff5aa024d7c8234bd", "mn0002550537")   ### [Skipper]
        ### UP!

        addAllMusic(mdbmaps, "BillboardYE", "04946a42dff27d365f0310305da04a23", "mn0001411030")   ### [Hollis]
        # ## White Walls
        
        addAllMusic(mdbmaps, "BillboardYE", "6e54ade5fccad0d154b819907082e869", "mn0003496874")   ### [Ashe]
        ### Moral Of The Story

        addAllMusic(mdbmaps, "BillboardYE", "6f7b92661d32c01bf942e69bef32a55f", "mn0003750925")   ### The Carters
        addDiscogs(mdbmaps, "BillboardYE", "6f7b92661d32c01bf942e69bef32a55f", "6543907")    ### The Carters
        ### Apes**t
        
        addDiscogs(mdbmaps, "BillboardYE", "bbca5a23b3a285175d0ba3ec4c7bee30", "4995184")    ### [John P. Kee & The New Life Community Choir]
        ### Life & Favor (You Don't Know My Story)  ,  Life And Favor

        addAllMusic(mdbmaps, "BillboardYE", "e85b799ff93adee24288d23a8742dfb9", "mn0000391908")   ### ["New G" New Generation Chorale]
        ### The Light  ,  Release

        addAllMusic(mdbmaps, "BillboardYE", "1ac2db404a4530bbdc1312a2a537fb55", "mn0000281564")   ### [Mark Harris]
        ### Find Your Wings

        addAllMusic(mdbmaps, "BillboardYE", "605d71c214a2565c2281c226f46c78c8", "mn0001049094")   ### [RKM]
        ### The Royalty/La Realeza  ,  The Last Chapter  ,  Masterpiece: Nuestra Obra Maestra  ,  Forever

        addAllMusic(mdbmaps, "BillboardYE", "f19201e31420fee5b8b4b8d31afac756", "mn0000958533")   ### [Dave Brubeck]
        ### Time Out Featuring Take Five  ,  Bennett/Brubeck: The White House Sessions, Live 1962

        addAllMusic(mdbmaps, "BillboardYE", "351d86cdac7a86101f8f5cd34460ca17", "mn0000306033")   ### [Lucero]
        ### Indispensible  ,  Un Lu* Jo

        addAllMusic(mdbmaps, "BillboardYE", "0daf21abe59aac57d10e0fe76f304077", "mn0002686289")   ### [Ben Williams]
        ### Unity Band  ,  Day Trip

        addAllMusic(mdbmaps, "BillboardYE", "dd88591508a27fecc4b05c47f7d9698f", "mn0000806283")   ### [James F. Twyman]
        ### I Am: Wishes Fulfilled Meditation

        addAllMusic(mdbmaps, "BillboardYE", "11389bc481f02fd48134f589375bdd3c", "mn0000605345")   ### [London Voices John Williams]
        ### Star Wars Episode III: Revenge Of The Sith (Soundtrack)

        addAllMusic(mdbmaps, "BillboardYE", "38b9f54e4d361e14ffea8c30fc37cc51", "mn0001647942")   ### [Bruckner Orchester Linz Conducted By Dennis Russell Davies]
        ### Glass: Symphony No. 9

        addAllMusic(mdbmaps, "BillboardYE", "d98278206c2f7c2e6232599ee9cb6bc0", "mn0003035943")   ### [Adam Holzman]
        ### The Most Relaxing Piano Music In The Universe
        
        addDiscogs(mdbmaps, "BillboardYE", "9397a5c4ab0e4fb8cb8f309fc2880f4d", "7118")    ### [DJ Snake]

        addDeezer(mdbmaps, "BillboardYE", "c8abf18e25a2ca4d30ffb6035445dd51", "406342")    ### [Unspoken]
        ### Reason  ,  Start A Fire
        ### Reason  ---> [['Unspoken']]
        ### Start A Fire  ---> [['Unspoken']]


        addDeezer(mdbmaps, "BillboardYE", "6b4ea7f06bfc6d3e2914f906d49b2f9c", "4831298")    ### [Pat Barrett]
        ### Build My Life  ,  The Way (New Horizon)
        ### Build My Life  ---> [['Pat Barrett']]
        ### The Way (New Horizon)  ---> [['Pat Barrett']]


        addDeezer(mdbmaps, "BillboardYE", "1516885e1eb960fe8ce48b8b0c18013f", "13669055")    ### [LIL PHAG]
        ### The Final Album (EP)  ,  resERECTION (EP)
        ### The Final Album (EP)  ---> [['LIL PHAG']]
        ### resERECTION (EP)  ---> [['LIL PHAG']]


        addDeezer(mdbmaps, "BillboardYE", "be0f0791c0f7ba1718fdabe23ad825f0", "7797")    ### [Keith Anderson]
        ### Every Time I Hear Your Name  ,  I Still Miss You
        ### Every Time I Hear Your Name  ---> [['Keith Anderson']]
        ### I Still Miss You  ---> [['Keith Anderson']]


        addDeezer(mdbmaps, "BillboardYE", "2b1e6a7e423a10610fe08af987a95e10", "4037981")    ### [Trinidad James]
        ### All Gold Everything  ,  I Luv This Sh*t
        ### All Gold Everything  ---> [['Trinidad James']]
        ### I Luv This Sh*t  ---> [['August Alsina Featuring Trinidad James']]


        addDeezer(mdbmaps, "BillboardYE", "dd41af3d62ed157a1cf87b2874ec4221", "205804")    ### [Unk]
        ### Walk It Out  ,  2 Step
        ### Walk It Out  ---> [['Unk']]
        ### 2 Step  ---> [['Unk']]


        addDeezer(mdbmaps, "BillboardYE", "0930d7117fbf6bdc9e8841a02ba609a3", "49992552")    ### [The Bonfyre]
        ### Automatic  ,  U Say
        ### Automatic  ---> [['Miranda Lambert', 'The Bonfyre']]
        ### U Say  ---> [['The Bonfyre Featuring 6LACK']]


        addDeezer(mdbmaps, "BillboardYE", "2e8eeabf755112170bd4aa85bde811d7", "282934")    ### [Selah]
        ### Bless The Broken Road
        ### Bless The Broken Road  ---> [['Rascal Flatts', 'Selah']]


        addDeezer(mdbmaps, "BillboardYE", "0fe0f6e89f6d9620861e9ceb1b36f711", "712900")    ### [KONGOS]
        ### Come With Me Now
        ### Come With Me Now  ---> [['KONGOS']]


        addAllMusic(mdbmaps, "BillboardYE", "8d693828c3945e42f5d73723212ac3d4", "mn0003322275")   ### [I LOVE MAKONNEN]
        addDeezer(mdbmaps, "BillboardYE", "8d693828c3945e42f5d73723212ac3d4", "6901127")    ### [I LOVE MAKONNEN]
        ### Tuesday
        ### Tuesday  ---> [['I LOVE MAKONNEN Featuring Drake']]


        addDiscogs(mdbmaps, "BillboardYE", "79d15dbe07efb6748a2e6f46094b7b75", "268902")    ### [Paul McCoy]
        ### Bring Me To Life
        ### Bring Me To Life  ---> [['Evanescence Featuring Paul McCoy']]
        

        addDeezer(mdbmaps, "BillboardYE", "d83c1191555126f2bba5f3cbc30c12c2", "566096")    ### [Last Call]
        ### Victory
        ### Victory  ---> [['Yolanda Adams', 'Fred Jerkins Featuring Last Call', 'The Clark Sisters', 'Tye Tribbett & G.A.']]
        

        addAllMusic(mdbmaps, "BillboardYE", "814300eaeabc9ea9a440bb5069e8bd22", "mn0000573965")   ### [Helen Jane Long]
        ### Porcelain
        ### Porcelain  ---> [['Helen Jane Long']]


        addDeezer(mdbmaps, "BillboardYE", "207e27adc7483948baea636ad0293d00", "129723")    ### [Dora The Explorer]
        ### Dora The Explorer: Dance Fiesta!
        ### Dora The Explorer: Dance Fiesta!  ---> [['Dora The Explorer']]


        addDeezer(mdbmaps, "BillboardYE", "2c9e9667a41636bf52e6604dd765d044", "8907120")    ### [Arsenal Efectivo]
        ### En La Fuga
        ### En La Fuga  ---> [['Arsenal Efectivo']]


        addDeezer(mdbmaps, "BillboardYE", "40047f23a7ebcc10b31de43a3294c35c", "13916083")    ### [Fuerza Regida]
        ### Del Barrio Hasta Aqui
        ### Del Barrio Hasta Aqui  ---> [['Fuerza Regida']]


        addDeezer(mdbmaps, "BillboardYE", "78eac13a6059146e01c35f744e91e8c6", "1183466")    ### [Asian Meditation Music Collective]
        ### Asian Meditation Music: 101 Songs
        ### Asian Meditation Music: 101 Songs  ---> [['Asian Meditation Music Collective']]


        addDeezer(mdbmaps, "BillboardYE", "f7325c4bc982455f674db476ebd013ff", "13788905")    ### [Henricci]
        ### Sister Caro (EP)
        ### Sister Caro (EP)  ---> [['Henricci']]


        addDeezer(mdbmaps, "BillboardYE", "171f8644afcd1bb3b25dfc0b7334b295", "242975")    ### [Chloe]
        ### Walking In The Air
        ### Walking In The Air  ---> [['Chloe']]


        addDiscogs(mdbmaps, "BillboardYE", "48418341b2d3cd5101f072b0ea38f67c", "778532")   ### [The Polish National Radio Symphony Orchestra]
        addDeezer(mdbmaps, "BillboardYE", "48418341b2d3cd5101f072b0ea38f67c", "6764825")    ### [The Polish National Radio Symphony Orchestra]
        ### Henryk Gorecki: Symphony No. 3 "Symphony Of Sorrowful Songs" Op. 36
        ### Henryk Gorecki: Symphony No. 3 "Symphony Of Sorrowful Songs" Op. 36  ---> [['Beth Gibbons And The Polish National Radio Symphony Orchestra/Krzysztof Penderecki']]


        addAllMusic(mdbmaps, "BillboardYE", "c995a8d4bfc131004a14915b152f7bdf", "mn0000164050")   ### [Vienna Philharmonic Orchestra]
        addDeezer(mdbmaps, "BillboardYE", "c995a8d4bfc131004a14915b152f7bdf", "287113")    ### [Vienna Philharmonic Orchestra]
        ### Chopin: The Piano Concertos
        ### Chopin: The Piano Concertos  ---> [['Lang Lang ::: Vienna Philharmonic Orchestra']]


        ### Lean On  ,  Turn Down For What
        ### Lean On  ---> [['Major Lazer & DJ Snake Featuring MO']]
        ### Turn Down For What  ---> [["DJ Snake ::: Lil' Jon"]]
        
        #addAllMusic(mdbmaps, "BillboardYE", "6f7b92661d32c01bf942e69bef32a55f", "mn0003750925")   ### The Carters
        #addDiscogs(mdbmaps, "BillboardYE", "6f7b92661d32c01bf942e69bef32a55f", "6543907")    ### The Carters
        ### 
                
        #addAllMusic(mdbmaps, "BillboardYE", "a3b3b076b58dd330bfbb945bfd7484c3", "mn0000315463")   ### [Scarface]
        ### EMERITUS  ,  Made

        #addAllMusic(mdbmaps, "BillboardYE", "f8ad87bec3bbfcedf98ecaea06cb1bbe", "mn0001981371")   ### [DTP]
        ### Ludacris Presents...Disturbing Tha Peace

        #addAllMusic(mdbmaps, "BillboardYE", "daafe83a627a390818a4d84a1cc2b584", "mn0000103872")   ### [Jacoby Shaddix]
        ### Wolf Totem

        ### We Fly High  ,  Pop Champagne

        ### Moral Of The Story

        #addAllMusic(mdbmaps, "BillboardYE", "9bd03e0a0b2968d93ff9f1ff8e095bad", "mn0001225951")   ### [Mustard]
        ### Ballin'  ,  High Fashion  ,  Pure Water

        ### White Walls

        ### Move That Doh  ,  Mercy

        #addAllMusic(mdbmaps, "BillboardYE", "480f2343a34e5dfdc3a9e853668146f3", "mn0000996880")   ### [Casha]
        ### The Business

        #addAllMusic(mdbmaps, "BillboardYE", "eca8432d3d451115782d1479791fa1a6", "mn0002901034")   ### [IamSu]
        ### UP!

        ### UP!

        ### Enough Cryin

        #addAllMusic(mdbmaps, "BillboardYE", "58e412876626c75080c985969ec165c2", "mn0000774428")   ### [Infamous 2.0]
        ### Move B***h

        #addAllMusic(mdbmaps, "BillboardYE", "91c9ff6003246d7b8bd73530947e6f93", "mn0002535175")   ### [Uncle Charlie Wilson]
        ### Beautiful

        #addAllMusic(mdbmaps, "BillboardYE", "f0c78d6fdfb4c77b8ee510edb322b7b4", "mn0000372481")   ### [Rob Bacon]
        ### Something Keeps Calling  ,  Never Give You Up

        #addAllMusic(mdbmaps, "BillboardYE", "f77e2738751ea675c6377e1d30738531", "mn0003875442")   ### [Lonr.]
        ### Make The Most

        #addAllMusic(mdbmaps, "BillboardYE", "897017fe8e9f515f9531948eaf514833", "mn0000370867")   ### [KeKe Wyatt]
        ### You & I

        #addAllMusic(mdbmaps, "BillboardYE", "3be798b593f6ba9b653fa8722e2aca47", "mn0001524051")   ### [George Tandy]
        ### March

        #addAllMusic(mdbmaps, "BillboardYE", "6573b38fdc8d4787be33704d4c619bb5", "mn0002404073")   ### [Marcus Mumford]
        ### Lay Your Head On Me
    
        #addAllMusic(mdbmaps, "BillboardYE", "8b99c1cff43fefe67ab31e5f6df6f136", "mn0000101616")   ### [Cherine Anderson]
        ### Say Hey (I Love You
        
        #addAllMusic(mdbmaps, "BillboardYE", "c271d8b907625e9a57e14b00578d3a13", "mn0003498068")   ### [Josh Baldwin]
        ### Stand In Your Love

        #addAllMusic(mdbmaps, "BillboardYE", "e6c4cc7277a55f68ba0a9553dfa64494", "mn0003492731")   ### [Micah Tyler]
        ### Never Been A Moment  ,  Amen

        #addAllMusic(mdbmaps, "BillboardYE", "6ea0ac7bf7679a09b82feecf9282260d", "mn0003870377")   ### [We The Kingdom]
        ### Holy Water  ,  God So Loved

        #addAllMusic(mdbmaps, "BillboardYE", "e5e41fbe40ec9cb306a44dd470d57909", "mn0002698695")   ### [Hope Darst]
        ### Peace Be Still

        ### Find Your Wings

        #addAllMusic(mdbmaps, "BillboardYE", "e6d7745eb03517e668489d1ea3c7ce19", "mn0000979519")   ### [Echoing Angels]

        #addAllMusic(mdbmaps, "BillboardYE", "2828bf7a9fa1f4fd3f6eab39212ab82d", "mn0001562036")   ### [Jo Jo Jorge Falcon]

        #addAllMusic(mdbmaps, "BillboardYE", "0c549661a6664c25879ca7886710ac23", "mn0003811002")   ### [Maverick City Music]
        ### Maverick City, Vol. 3: Part 1

        #addAllMusic(mdbmaps, "BillboardYE", "131e357fb035d7f65af3dd3a523332e9", "mn0001044136")   ### [The Lost Fingers]
        ### Lost In The 80's


        
        #addAllMusic(mdbmaps, "BillboardYE", "446a9112614084c5c98d9c8c3fcc70be", "mn0002114807")   ### [Dillon Chase]

        #addAllMusic(mdbmaps, "BillboardYE", "9c4b5988c62a8b61d08cf2f5255124d2", "mn0002687866")   ### [Madelyn Berry]
        ### Waymaker

        #addAllMusic(mdbmaps, "BillboardYE", "62000351594925ac0c8d2e7da8447458", "mn0002335388")   ### [Vanessa Campagna]
        ### Waymaker

        #addAllMusic(mdbmaps, "BillboardYE", "a44e538382b982fdcd999f67e958cf6f", "mn0000204077")   ### [Bart Millard]
        ### Words  ,  No Matter What

        #addAllMusic(mdbmaps, "BillboardYE", "9ec2841d41a59e221a0b3497b334e2be", "mn0002586063")   ### [Larry Callahan]
        ### The Evolution II

        ### Life And Favor

        #addAllMusic(mdbmaps, "BillboardYE", "f63d2bfca3bdfdb66dd01e6eb02a28a7", "mn0000772877")   ### [Bishop G.E. Patterson]
        ### Singing The Old Time Way Volume 2    
        
        #addAllMusic(mdbmaps, "BillboardYE", "2f830a49735827c268b03100faf4dc57", "mn0003873062")   ### [Cochren & Co.]

        #addAllMusic(mdbmaps, "BillboardYE", "81141bff183291877791b21cf759c22b", "mn0003652026")   ### [Kingsway Music]
        ### Praise Is Rising

        #addAllMusic(mdbmaps, "BillboardYE", "d6316e7b2e17b6098435d0b89dfe8aeb", "mn0002568764")   ### [Jonathan Nelson & Purpose]
        ### My Name Is Victory

        #addDiscogs(mdbmaps, "BillboardYE", "56432a0b6d0f343b997aa1733acefb67", "2601994")    ### [C-Lite]
        ### Background

        #addAllMusic(mdbmaps, "BillboardYE", "d4fc93655d9fc0cc087779d5631be60a", "mn0003864623")   ### [Tobbi & Tommi]
        ### He Promised Me

        #addAllMusic(mdbmaps, "BillboardYE", "439d0b42646b340620ac6cfe27b4ff6a", "mn0003534387")   ### [The Restoration Worship Center Choir]
        ### God's Grace  ,  You Keep On Blessing Me

        #addAllMusic(mdbmaps, "BillboardYE", "104253751900601cbafa4e1d439806a3", "mn0003411838")   ### [Doretha 'Dodi' Sampson]
        ### Bless The Lord

        ### The Light  ,  Release

        #addAllMusic(mdbmaps, "BillboardYE", "fcee99068cfcac5d601b39d93d8fe879", "mn0003230844")   ### [BreeAnn Hammond]
        ### I Will Trust

        #addAllMusic(mdbmaps, "BillboardYE", "5a2a6f049cc1d5cdcf9d31be418cc1ef", "mn0000589863")   ### [Strength In Praise]
        #addDiscogs(mdbmaps, "BillboardYE", "5a2a6f049cc1d5cdcf9d31be418cc1ef", "2180021")    ### [Strength In Praise]
        ### Thank Ya Jesus

        ### Some Cut
        
        
        #addAllMusic(mdbmaps, "BillboardYE", "605d71c214a2565c2281c226f46c78c8", "mn0001049094")   ### [RKM]
        #addAllMusic(mdbmaps, "BillboardYE", "8fa2b339a599cf7e9966ff519d931f15", "mn0000015398")   ### [Paul Brown]
        #addAllMusic(mdbmaps, "BillboardYE", "6f5829462aae3a179ae2a69d43afe175", "mn0003715465")   ### [Casper Magico]
        #addAllMusic(mdbmaps, "BillboardYE", "816fd62e7d802af89d874511ff64ccca", "mn0003580276")   ### [La Trakalosa de Monterrey]
        #addAllMusic(mdbmaps, "BillboardYE", "31d88bddadced306f00f7868eb818312", "mn0002396941")   ### [Vikingur Olafsson]
        #addAllMusic(mdbmaps, "BillboardYE", "1c1f079f1b14f10634bac202a839473b", "mn0003416511")   ### [Tomas The Latin Boy]
        #addAllMusic(mdbmaps, "BillboardYE", "ddd26d0d410a80b9d1d438548ed5c84b", "mn0003596740")   ### [ROSALIA]
        #addAllMusic(mdbmaps, "BillboardYE", "33597d0fac6ecdb294dcfa01b4007d92", "mn0000037865")   ### [Andy Montanez]
        #addAllMusic(mdbmaps, "BillboardYE", "dcf3dfcb418a15b594e90547223a0458", "mn0003231211")   ### [Lenin Ramirez]
        #addAllMusic(mdbmaps, "BillboardYE", "d599a7dd63cf6aea2387149d3573fcf9", "mn0002228422")   ### [Yannick Nezet-Seguin]
        #addAllMusic(mdbmaps, "BillboardYE", "cdbbba7ed67a7f6d6887d4a78e743837", "mn0001669928")   ### [Jun Markl]
        #addAllMusic(mdbmaps, "BillboardYE", "d4fc16f18c6fa28fa12d3aae2afd9c48", "mn0002867101")   ### [Leslie Grace or Becky G]
    
        #addAllMusic(mdbmaps, "BillboardYE", "223401b51c44ac9706ca74916c1c56d0", "mn0003126486")   ### [Dominican Sisters Of Mary]
        #addAllMusic(mdbmaps, "BillboardYE", "fed3e6afd4f1a9b572ad5213d4464b5b", "mn0003475586")   ### [Banda Clave Nueva de Max Peraza]
        #addAllMusic(mdbmaps, "BillboardYE", "a8a1b9d6acec6f48e4723ef71efb5df0", "mn0000402170")   ### [DJ Lil' Cee]
        #addAllMusic(mdbmaps, "BillboardYE", "aa7b592871b62b1a94b14a092fd83439", "mn0003672931")   ### [Banda Populares del Llano]
        #addAllMusic(mdbmaps, "BillboardYE", "d7f3bc04ef9b824d9b016e891072e91c", "mn0001255339")   ### [La Tribu]
        #addAllMusic(mdbmaps, "BillboardYE", "3ad5860698af7988a2a903e640c09874", "mn0002218005")   ### [The Choir Of King's College]
        #addAllMusic(mdbmaps, "BillboardYE", "1386b48a0d69d0f062c5a1626fa9a90f", "mn0003414462")   ### [MOFRO]
        #addAllMusic(mdbmaps, "BillboardYE", "ba368914dde86a6e86a643d599797f98", "mn0003306844")   ### [The Boys Of St. Paul's Choir School]
        #addAllMusic(mdbmaps, "BillboardYE", "9cb65498d65011a90ea84ed59b7875de", "mn0000581661")   ### [PNAU]
        #addAllMusic(mdbmaps, "BillboardYE", "ccf17919991238a27fb101a87b48654a", "mn0002396830")   ### [VOCES8]

        
        #addAllMusic(mdbmaps, "BillboardYE", "90983c7d7cb7b6c4e4443c4909116d16", "mn0000392428")   ### [Sus Bravos Del Norte]
        ### Antologia De Un Rey  ,  Antologia De Un Rey Vol. 2  ,  Leyenda Nortena: 30 Grandes Exitos

        #addAllMusic(mdbmaps, "BillboardYE", "011bd3e083e5725d5ad05892efd1004e", "mn0002184322")   ### [The Colorado Symphony]
        ### The Soft Bulletin: Recorded Live At Red Rocks Amphitheatre  ,  Live At Red Rocks  ,  Gregory Alan Isakov With The Colorado Symphony

        ### Time Out Featuring Take Five  ,  Bennett/Brubeck: The White House Sessions, Live 1962

        #addAllMusic(mdbmaps, "BillboardYE", "e3a5f3c7406f8572acc2f5d83bcdf7b4", "mn0000695943")   ### [Lennox]
        ### Motivan2  ,  Los Verdaderos

        #addAllMusic(mdbmaps, "BillboardYE", "0157a440c9d2d339120f95d28ea6dd03", "mn0000929220")   ### [Orchestra At Temple Square Jessop]
        ### Called To Serve  ,  Showtime! Music Of Broadway And Hollywood

        #addAllMusic(mdbmaps, "BillboardYE", "4ae32bbd2fe0e39284a6e3ad43d73669", "mn0003289856")   ### [Los Plebes del Rancho]
        ### El Karma  ,  Hablemos

        #addAllMusic(mdbmaps, "BillboardYE", "4fbbf7f930cb6537d418c785882a2b89", "mn0002261581")   ### [Yoncheva]
        ### George Frideric Handel: Messiah  ,  George Frideric Handel: Messiah, Highlights

        #addAllMusic(mdbmaps, "BillboardYE", "4e4dfbbafd57b7224bd51dc9ae473cd4", "mn0000017748")   ### [Patti LaBelle]
        ### The Gospel According to Patti LaBelle  ,  BEL Hommage

        #addAllMusic(mdbmaps, "BillboardYE", "c31265b36042cb96f154dec857ef762a", "mn0000929220")   ### [Orch. At Temple Square]
        ### George Frideric Handel: Messiah  ,  George Frideric Handel: Messiah, Highlights

        ### I Am: Wishes Fulfilled Meditation

        #addAllMusic(mdbmaps, "BillboardYE", "c7b1b183f35ee9f505e55de718ac37d6", "mn0003652039")   ### [The Dubplates]
        ### Box Full Of Steel

        #addAllMusic(mdbmaps, "BillboardYE", "149c5c27b9197ec6015f8231269aaefb", "mn0000767746")   ### [The Kentucky Ramblers]
        ### 40th Anniversary Celebration

        #addAllMusic(mdbmaps, "BillboardYE", "55932e14762136bb5cb432d6f40b97ae", "mn0000806126")   ### [Quicksilver]
        ### More Behind The Picture Than The Wall
    
        #addAllMusic(mdbmaps, "BillboardYE", "011bd3e083e5725d5ad05892efd1004e", "mn0002184322")   ### [The Colorado Symphony]
        ### The Soft Bulletin: Recorded Live At Red Rocks Amphitheatre  ,  Live At Red Rocks  ,  Gregory Alan Isakov With The Colorado Symphony

        #addAllMusic(mdbmaps, "BillboardYE", "b6c810361319b5470f93843765b79fd6", "mn0002184322")   ### [Colorado Symphony Gomes]
        ### Juno Concerto  ,  The Soft Bulletin: Recorded Live At Red Rocks Amphitheatre  ,  Live At Red Rocks  ,  Gregory Alan Isakov With The Colorado Symphony

        #addAllMusic(mdbmaps, "BillboardYE", "6b10ef8d3731e5f0f7873bc3081ea86f", "mn0002905562")   ### [Il Pomo D'oro]
        ### Handel: Agrippina

        #addAllMusic(mdbmaps, "BillboardYE", "7b031a551aa8a00d1346d25a03ccd8ea", "mn0003289856")   ### [Los Plebes del Rancho de Ariel Camacho]
        ### Recuerden Mi Estilo

        #addAllMusic(mdbmaps, "BillboardYE", "db4edbe11ff7f75efc9d0552b7a16275", "mn0000062200")   ### [Bernie Williams]
        ### Moving Forward

        #addAllMusic(mdbmaps, "BillboardYE", "8389366584ae35f1d522243b1e0563cf", "mn0002414433")   ### [Conductor Andre de Ridder]
        ### The Soft Bulletin: Recorded Live At Red Rocks Amphitheatre  ,  Live At Red Rocks  ,  Gregory Alan Isakov With The Colorado Symphony

        #addAllMusic(mdbmaps, "BillboardYE", "f19201e31420fee5b8b4b8d31afac756", "mn0000958533")   ### [Dave Brubeck]
        ### Time Out Featuring Take Five  ,  Bennett/Brubeck: The White House Sessions, Live 1962

        #addAllMusic(mdbmaps, "BillboardYE", "fa654b2bf8377fb2f280b380e157f125", "mn0002786123")   ### [The London Classical Orchestra (Wilson)]
        ### Paul McCartney's Ocean's Kingdom

        #addAllMusic(mdbmaps, "BillboardYE", "d50c212bc2abec5c7775570a784d9a19", "mn0000110033")   ### [Chicago Symphony Orchestra Harth-Bedoya]
        ### New Impossibilities

        #addAllMusic(mdbmaps, "BillboardYE", "d63ab8a7ace72ff99ea01dee91da9ca7", "mn0000586735")   ### [the Detroit Symphony Orchestra Slatkin]
        ### The Melody Of Rhythm: Triple Concerto & Music For Trio

        #addAllMusic(mdbmaps, "BillboardYE", "a81073dea2066fe28437143e4bf6b881", "mn0002123863")   ### [Simon Bolivar Symphony Orchestra Of Venezuela Dudamel]
        ### Rachmaninov #3/Prokofiev #2

        #addAllMusic(mdbmaps, "BillboardYE", "038ea1091a1b327ec76e8e08ebef9cc3", "mn0000803128")   ### [English Chamber Orchestra Mercurio]
        ### Air: The Bach Album

        #addAllMusic(mdbmaps, "BillboardYE", "45d369d672d7ae1af68cdf510935b299", "mn0002203162")   ### [Swedish Radio Symphony Orchestra Salonen]
        ### Schoenberg: Violin Concertos

        #addAllMusic(mdbmaps, "BillboardYE", "917bff3ce41261695e216b0ec4155ec0", "mn0000820912")   ### [Rolando Villazon]
        ### DUETS

        #addAllMusic(mdbmaps, "BillboardYE", "f36bdff8df56b917b8a15f1486487801", "mn0002949423")   ### [Sus Parientes]
        ### Estilo Italiano

        #addAllMusic(mdbmaps, "BillboardYE", "2f8359c8b167014562c6293ec613efc0", "mn0002267344")   ### [Fagioli]
        ### Handel: Agrippina

        #addAllMusic(mdbmaps, "BillboardYE", "c14872a732f4dc6d15d3705b014ab7ed", "mn0003427196")   ### [Maxim Enelyonychev]
        ### Handel: Agrippina

        #addAllMusic(mdbmaps, "BillboardYE", "0ee3b0a70711e034c0ceeb5c6d8f5fdc", "mn0003034067")   ### [Pizzuti]
        ### Handel: Agrippina

        #addAllMusic(mdbmaps, "BillboardYE", "5a58ed5d170621ceb0065bf388328f96", "mn0003326643")   ### [Vistoli]
        ### Handel: Agrippina

        #addAllMusic(mdbmaps, "BillboardYE", "5147a5ea8f87cb56c7e4e7be03336dd6", "mn0002173324")   ### [Orlinski]
        ### Handel: Agrippina

        #addAllMusic(mdbmaps, "BillboardYE", "642efb1f7835b85d16236bcccf72442a", "mn0003126486")   ### [Mother Of The Eucharist]
        ### Jesu, Joy Of Man's Desiring: Christmas With The Dominican Sisters Of Mary

        #addDiscogs(mdbmaps, "BillboardYE", "45c7ae95591f95a218b1377b824a0bf2", "7752063")    ### [Yoga Meditation Tribe]
        ### Music For Meditation And Relaxation: Yoga

        ### The Most Relaxing Piano Music In The Universe

        #addAllMusic(mdbmaps, "BillboardYE", "05e0d332b9f74ac7121c675dab8c0f04", "mn0000295970")   ### [Draco]
        #addDiscogs(mdbmaps, "BillboardYE", "05e0d332b9f74ac7121c675dab8c0f04", "218710")    ### [Draco]
        ### Amor Vincit Omnia

        #addAllMusic(mdbmaps, "BillboardYE", "bdf4da0190632f1aefc4290498f0ef97", "mn0001775164")   ### [The Count Basie Orchestra (Barnhart)]
        ### A Very Swingin' Basie Christmas!

        #addAllMusic(mdbmaps, "BillboardYE", "b3c73494913749db4bebadc154093360", "mn0003441995")   ### [Comet Is Coming]
        ### Trust In The Lifeforce Of The Deep Mystery

        #addAllMusic(mdbmaps, "BillboardYE", "b1442ee63ae410a8bfff1ce96c32ee61", "mn0002725593")   ### [NERO]
        ### Welcome Reality

        #addAllMusic(mdbmaps, "BillboardYE", "90c9680ad17018702c4cf367e2ca9b53", "mn0002131959")   ### [The Christmas Piano]
        ### PIANO MUSIC FOR CHRISTMAS

        #addAllMusic(mdbmaps, "BillboardYE", "b3bb271f42af7f329edee36e466e6982", "mn0000929776")   ### [Arvo Part]
        ### In Principio
        
        #addAllMusic(mdbmaps, "BillboardYE", "ab8ffd7146a0d5ba246166ce43748193", "mn0000061744")   ### [Nashville Symphony Guerrero]
        ### So There

        #addAllMusic(mdbmaps, "BillboardYE", "8440130be86752a376222db6f9c34370", "mn0001736241")   ### [Orchestre De Paris Eschenbach]
        ### Beethoven: Piano Concertos Nos. 1 & 4

        #addAllMusic(mdbmaps, "BillboardYE", "60b3428c59799dcbc4317fbecc3bf615", "mn0001910370")   ### [The Deutsche Kammerphilharmonie Bremen Jarvi]
        ### Violin Concertos: Mozart 5, Vieuxtemps 4

        #addAllMusic(mdbmaps, "BillboardYE", "f6c015cd690456b102f45b6b506656ac", "mn0000804708")   ### [Helene Grimaud]
        ### Water

        #addAllMusic(mdbmaps, "BillboardYE", "66ef2fa13fcb07a377721756340ca190", "mn0000263103")   ### [Seattle Symphony (Morlot)]
        ### John Luther Adams: Become Ocean

        #addAllMusic(mdbmaps, "BillboardYE", "ec63d28d5f452ef22833c3b22309fc29", "mn0001650844")   ### [Royal Liverpool Philharmonic Orchestra Petrenko]
        ### Hilary Hahn Plays Higdon & Tchaikovsky: Violin Concertos        

        #addAllMusic(mdbmaps, "BillboardYE", "74dc33ff69c1cb2f5284b058e4a4271b", "mn0003678368")   ### [Grupo Canaveral de Humberto Pabon]
        #addDiscogs(mdbmaps, "BillboardYE", "74dc33ff69c1cb2f5284b058e4a4271b", "3619794")    ### [Grupo Canaveral de Humberto Pabon]
        ### Juntos Por La Cumbia

        ### Glass: Symphony No. 9

        #addAllMusic(mdbmaps, "BillboardYE", "944fdb15a3576bba78d8467b0e662d12", "mn0002769031")   ### [Syreeta Thompson Trumpetlady]
        ### Evolution Of A Winner

        #addAllMusic(mdbmaps, "BillboardYE", "7f64551367c3181b7d052302680a15e0", "mn0003531694")   ### [Mau y Ricky]
        ### Para Aventuras y Curiosidades

        #addAllMusic(mdbmaps, "BillboardYE", "80e93e9d98e40b7b942073f7a710e118", "mn0000193772")   ### [Boston Symphony Orchestra Levine]
        ### Lorraine Hunt Lieberson Sings Peter Lieberson: Neruda Songs

        #addAllMusic(mdbmaps, "BillboardYE", "67be402b4ce838e8779f9eeb8d77c194", "mn0001826631")   ### [Roma Sinfonietta Orchestra Morricone]
        ### Yo-Yo Ma Plays Ennio Morricone

        #addAllMusic(mdbmaps, "BillboardYE", "eb33c715a0d6545882f7cea7835888d4", "mn0001661699")   ### [Sistine Chapel Choir Palombella]
        ### Veni Domine: Advent & Christmas At Sistine Chapel

        #addAllMusic(mdbmaps, "BillboardYE", "f5de6631de52a0f4ba7dcbbb9dc1c962", "mn0000350127")   ### [The Royal Philharmonic Concert Orchestra Mercurio]
        ### Sting: Live In Berlin        


        mdbmaps["BillboardYE"].save()