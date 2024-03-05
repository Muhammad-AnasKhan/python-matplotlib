"""
If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., 
depending on the length of the y-points.
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# The x-points in the example above are [0, 1, 2, 3, 4, 5].
