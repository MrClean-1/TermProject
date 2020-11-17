import TemperatureData
import FileIO


class WeatherAnalyzer:
    def __init__(self):
        self.dataTable = FileIO.FileIO().dataTable
        self.tempData = []
        for i in range(len(self.dataTable)):
            self.tempData.append(TemperatureData.TemperatureData(i, self.dataTable))

    def getMinTemp(self):
        minTemp = 600
        for i in range(len(self.tempData)):
            if self.tempData[i].minTemp < minTemp:
                minTemp = self.tempData[i].minTemp
        return minTemp

    def getMinTempAnnually(self):
        annuallMin = []
        for i in range(0, len(self.tempData), 12):
            localYearMin = []
            localYearMin.append(self.tempData[i].date.year)
            localMin = 600
            for month in range(12):
                try:
                    if self.tempData[i + month].minTemp < localMin:
                        localMin = self.tempData[i + month].minTemp
                    # If we got an out of bounds there's not enough data for that year
                    # In this case we don't want to append that year
                except:
                    # If we're out of bounds just return the data as it is
                    return annuallMin
            localYearMin.append(localMin)
            annuallMin.append(localYearMin)
        return annuallMin

    def getMaxTemp(self):
        maxTemp = -600
        for i in range(len(self.tempData)):
            if self.tempData[i].maxTemp > maxTemp:
                maxTemp = self.tempData[i].maxTemp
        return maxTemp

    def getMaxTempAnnually(self):
        annuallMax = []
        for i in range(0, len(self.tempData), 12):
            localYearMax = []
            localYearMax.append(self.tempData[i].date.year)
            localMax = -600
            for month in range(12):
                try:
                    if self.tempData[i+month].maxTemp > localMax:
                        localMax = self.tempData[i+month].maxTemp
                    # If we got an out of bounds there's not enough data for that year
                    # In this case we don't want to append that year
                except:
                    # If we're out of bounds just return the data as it is
                    return annuallMax
            localYearMax.append(localMax)
            annuallMax.append(localYearMax)
        return annuallMax

    def getAvgSnowfallAnnually(self):
        annualAvg = []
        for i in range(0, len(self.tempData), 12):
            yearAvg = []
            yearSum = 0
            try:
                for month in range(12):
                    yearSum += self.tempData[i + month].snowfall
                # If we got an out of bounds there's not enough data for that year
                # In this case we don't want to append that year
                yearAvg.append(self.tempData[i].date.year)
                yearAvg.append(yearSum/12)
            except:
                # If we're out of bounds just return the data as it is
                return annualAvg
            annualAvg.append(yearAvg)
        return annualAvg

    def getAvgTempAnnually(self):
        annualMax = self.getMaxTempAnnually()
        annualMin = self.getMinTempAnnually()
        # both of these arrays will be the same length
        # we compare them and create a new array
        annualAvg = []
        for i in range(len(annualMax)):
            annualAvgYear = []
            annualAvgYear.append(annualMax[i][0])
            # compare and average the max and min and append
            annualAvgYear.append((annualMax[i][1] + annualMin[i][1]) / 2)
            # then we append that year to the annualAvg 2d array
            annualAvg.append(annualAvgYear)
        return annualAvg

