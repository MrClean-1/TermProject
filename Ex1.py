import numpy as np
from random import randint

# Create the array and set up the random stuff
array = []
for index in range(10):
    array.append(randint(0, 100))

# Convert to a numpy array
array = np.array(array)

# Use numpy to find and display some stuff about the array
print(array)
print('min:', np.min(array))
print('max:', np.max(array))
print('average:', np.average(array))
print('median:', np.median(array))
print('std:', np.std(array))
