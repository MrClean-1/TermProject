import WeatherAnalyzer
import Chart
import numpy as np


# This is the "menu bar"
def main():
    weatherAnal = WeatherAnalyzer.WeatherAnalyzer()
    chart = Chart.Chart()
    running = True
    while running:
        print('1- Get Minimum Temperature of 1990-2019')
        print('2- Get Maximum Temperature of 1990-2019')
        print('3- Get Minimum Temperature of 1990-2019 Annually')
        print('4- Get Maximum Temperature of 1990-2019 Annually')
        print('5- Get Average Snowfall between 1990-2019 Annually')
        print('6- Get Average Temperature between 1990-2019 Annually')
        try:
            choice = int(input('11- Exit Program'))
            if choice == 1:
                print(weatherAnal.getMinTemp())
            elif choice == 2:
                print(weatherAnal.getMaxTemp())
            elif choice == 3:
                matrix = weatherAnal.getMinTempAnnually()
                for row in matrix:
                    for col in row:
                        print(col, end=' ')
                    print()
            elif choice == 4:
                matrix = weatherAnal.getMaxTempAnnually()
                for row in matrix:
                    for col in row:
                        print(col, end=' ')
                    print()
            elif choice == 5:
                matrix = weatherAnal.getAvgSnowfallAnnually()
                for row in matrix:
                    for col in row:
                        print(col, end=' ')
                    print()
            elif choice == 6:
                matrix = weatherAnal.getAvgTempAnnually()
                for row in matrix:
                    for col in row:
                        print(col, end=' ')
                    print()
            elif choice == 7:
                # Since we can't slice the array when it's nested we convert it to a numpy array first then slice
                data = np.array(weatherAnal.getMinTempAnnually())
                chart.drawLineChart(data[:, 0], data[:, 1],
                                    'Minimum Temperatures of 1990-2019 annually', 'Year', 'Min Temp (F)')
            elif choice == 8:
                # Since we can't slice the array when it's nested we convert it to a numpy array first then slice
                data = np.array(weatherAnal.getMaxTempAnnually())
                chart.drawLineChart(data[:, 0], data[:, 1],
                                    'Maximum Temperatures of 1990-2019 annually', 'Year', 'Max Temp (F)')
            elif choice == 9:
                # Since we can't slice the array when it's nested we convert it to a numpy array first then slice
                data = np.array(weatherAnal.getAvgSnowfallAnnually())
                chart.drawBarChart(data[:, 0], data[:, 1],
                                   'Average Snowfall between 1990-2019 annually', 'Year', 'Average snowfall (cm)')
            elif choice == 10:
                # Since we can't slice the array when it's nested we convert it to a numpy array first then slice
                data = np.array(weatherAnal.getAvgTempAnnually())
                chart.drawBarChart(data[:, 0], data[:, 1],
                                   'Average Temperature between 1990-2019 annually', 'Year', 'Average Temp (F)')
            elif choice == 11:
                running = False
            else:
                raise
        except:
            print('Invalid selection, try again')


if __name__ == '__main__':
    main()
