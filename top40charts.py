from fsUtils import setDir, isDir, setFile, isFile
from webUtils import getURL, getHTML
from time import sleep
from timeUtils import getDateTime, isDate
from ioUtils import getFile


class top40:
    def __init__(self, debug=False):
        self.chartsDir = "/Volumes/Piggy/Charts"
        if not isDir(self.chartsDir):
            raise ValueError("Charts directory [{0}] does not exist".format(self.chartsDir))
        self.dataDir   = setDir(self.chartsDir, "data")
        self.dataDir   = setDir(self.dataDir, "top40")
        if not isDir(self.dataDir):
            raise ValueError("Data directory [{0}] does not exist".format(self.dataDir))
            
        self.baseURL = "https://top40-charts.com"
        
        
class top40chart(top40):
    def __init__(self, chartID, chartName, chartURL, debug=False):
        super().__init__()
        self.chartStarterDir = setDir(self.dataDir, "starters")
        self.chartDir        = setDir(self.dataDir, chartName.replace("/", " "))
        self.chartID         = chartID
        self.chartName       = chartName
        self.chartBaseURL    = chartURL
        self.starterFile     = setFile(self.chartStarterDir, "{0}.p".format(self.chartName.replace("/", " ")))
        self.resultsFile     = setFile(self.dataDir, "{0}.p".format(self.chartName.replace("/", " ")))
        
        self.setChartDates()
        if debug:
            print("There are {0} dates for this chart".format(len(self.chartDates)))
        
            
            
    ####################################################################################
    # Chart Starter File
    ####################################################################################    
    def downloadStarterChart(self):
        getURL(url=self.chartBaseURL, savename=self.starterFile, debug=True)
        sleep(2)
        
        
    def setChartDates(self):
        if isFile(self.starterFile):
            fdata = getHTML(self.starterFile)
            dates = []
            for iform,formdata in enumerate(fdata.findAll("form")):
                for isel,seldata in enumerate(formdata.findAll("select", {"name": "date"})):
                    for iop,opdata in enumerate(seldata.findAll("option")):
                        attrs  = opdata.attrs
                        value  = attrs['value']
                        dates.append(value)
            self.chartDates = sorted(list(set(dates)))
        
        
            
    ####################################################################################
    # Chart Starter File
    ####################################################################################    
    def downloadChartDates(self):
        if len(self.chartDates) == 0:
            self.setChartDates()
            
        print("There are {0} dates for the {1} chart".format(len(self.chartDates), self.chartName))
        for idts,value in enumerate(self.chartDates):
            if value is None:
                continue

            try:
                if getDateTime(value).year < 1900:
                    continue
            except:
                continue

            url   = "https://top40-charts.com/chart.php?cid={0}&date={1}".format(self.chartID, value)
            savename = setFile(self.chartDir, "{0}.p".format(value))
            if savename is None:
                continue

            if isFile(savename):
                continue
                #print("Touching {0}".format(savename))
                #Path(savename).touch()
            else:
                print(idts,'/',len(self.chartDates),'\t',url,'\t',savename)
                getURL(url=url, savename=savename, debug=True)
                sleep(2)


    def getCharts(self):
        fdata = getHTML(self.starterFile)
        charts = {}
        for iform,formdata in enumerate(fdata.findAll("form")):
            for isel,seldata in enumerate(formdata.findAll("select", {"name": "cid"})):
                for iop,opdata in enumerate(seldata.findAll("option")):
                    attrs  = opdata.attrs
                    cid    = attrs['value']
                    name   = opdata.text
                    url    = 'https://top40-charts.com/chart.php?cid={0}'.format(cid)
                    charts[name] = {"ID": cid, "URL": url}
        return charts

    
        url  = "{0}{1}".format(self.baseURL, href)
        try:
            cid = int(href.split("cid=")[1])
        except:
            raise ValueError("Could not find CID from {0}".format(ref))            
        self.chartIDs[name] = {"ID": cid, "URL": url}
        
    
    
    ####################################################################################
    # Individual Charts
    ####################################################################################  
    def getFullChartData(self):
        return getFile(self.resultsFile)
    
    
    def parseCharts(self):
        chartResults = {}
        for chartDate in self.chartDates:
            chartFile = setFile(self.chartDir, "{0}.p".format(chartDate))
            if isFile(chartFile):
                chartResults[chartDate] = self.parseChart(chartFile)
        saveFile(idata=chartResults, ifile=self.resultsFile, debug=True)
        
    def parseChart(self, chartFile):
        chartData = getHTML(chartFile)
        results = []
        pos = 1

        debVars = None

        for it,table in enumerate(chartData.findAll("table")):
            ths = table.findAll("th")
            trs = table.findAll("tr")
            attrs = table.attrs
            #if debug:
            #    print(it,len(ths),len(trs),attrs)

            if attrs == {'cellpadding': '0', 'cellspacing': '0', 'borer': '0'}:
                if len(trs) == 1:
                    tds = trs[0].findAll("td")
                    if len(tds) == 3:
                        refs = tds[2].findAll("a")
                        if len(refs) == 2:
                            album  = refs[0].text
                            artist = refs[1].text
                            results.append({"Artist": artist, "Album": album})
                            #if debug:
                            #    print(pos,'\t',artist,'\t',album)
                            pos += 1

        return results        

        
class top40starter(top40):
    def __init__(self, debug=False):
        super().__init__()
        self.starterURL  = self.baseURL
        self.starterFile = setFile(self.dataDir, "starter_test.p")
                   
        self.chartIDs = {}
        
    def getChartIDs(self):
        return self.chartIDs
            
    def download(self):
        url      = self.starterURL
        savename = self.starterFile
        getURL(url=url, savename=savename, debug=True)
        
    def parse(self):
        fdata = getHTML(self.starterFile)
        rows  = fdata.findAll("div", {"class": "row"})
        for i,row in enumerate(rows):
            divs = row.findAll("div", {"class": "latc_song"})
            for j,div in enumerate(divs):
                span = div.find("span", {"class": "bigblue"})
                if span is not None:
                    ref = span.find("a")
                    self.parseChartID(ref)
        
    def parseChartID(self, ref):
        name = ref.text
        href = ref.attrs['href']
        url  = "{0}{1}".format(self.baseURL, href)
        try:
            cid = int(href.split("cid=")[1])
        except:
            raise ValueError("Could not find CID from {0}".format(ref))            
        self.chartIDs[name] = {"ID": cid, "URL": url}
        