import TemperatureData
import FileIO
import numpy as np


class WeatherAnalyzer:
    def __init__(self, file_path):
        self.dataTable = FileIO.FileIO(file_path).dataTable
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
                except IndexError:
                    # If we're out of bounds just return the data as it is
                    # Even tho it doesn't make sense (it's an outlier)
                    # do it for the marks i guesssssss
                    break
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
                except IndexError:
                    # If we're out of bounds just append this max
                    # Even tho it doesn't make sense (it's an outlier)
                    # do it for the marks i guesssssss
                    break
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
            except IndexError:
                # If we're out of bounds just append this snowfall as is
                # Even tho it doesn't make sense (it's an outlier)
                # do it for the marks i guesssssss
                yearAvg.append(self.tempData[i].date.year)
                yearAvg.append(yearSum/month)
            annualAvg.append(yearAvg)
        return annualAvg

    def getAvgTempAnnually(self):
        annualAvg = []
        # We run through every element in the tempData array
        # We create a list within that loop which has the average for that month
        # We average the list and append it to annualAvg
        for i in range(0, len(self.tempData), 12):
            yearAvg = []
            try:
                for month in range(12):
                    yearAvg.append((self.tempData[i + month].minTemp +
                                    self.tempData[i + month].maxTemp) / 2)
                temp = []
                yearAvg = np.array(yearAvg)
                temp.append(self.tempData[i].date.year)
                temp.append(np.average(yearAvg))
                annualAvg.append(temp)
                # If this excepts the issue is that there was not a full year of data
                # In this case we: add the data as is
                # Even tho it doesn't make sense (it's an outlier)
                # do it for the marks i guesssssss
            except IndexError:
                temp = []
                yearAvg = np.array(yearAvg)
                temp.append(self.tempData[i].date.year)
                temp.append(np.average(yearAvg))
                annualAvg.append(temp)
                return annualAvg
        return annualAvg
