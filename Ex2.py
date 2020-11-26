import numpy as np
import matplotlib.pyplot as pyplot


# A function to read the file weather.csv into a numpy array
def read_weather():
    # Read the file into a numpy array
    file_name = 'weather.csv'
    data = np.loadtxt(file_name, delimiter=',', skiprows=1,
                      usecols=(0, 1, 2, 3, 4), dtype=np.float)
    return data


# A function to draw a chart with pyplot
def drawChart(x, y):
    fig = pyplot.figure()
    pyplot.title('Temperature in Calgary between Jan-Dec in 2000')
    pyplot.ylabel('Min Temperature (F)')
    pyplot.xlabel('Month of Year')

    pyplot.plot(x, y, marker='o')
    pyplot.show()


# Little main function to interact with the two functions above
def main():
    data = read_weather()
    drawChart(data[:, 1], data[:, 3])


if __name__ == '__main__':
    main()
