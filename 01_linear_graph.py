import matplotlib

# print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

# To plot lines
# plt.plot(xpoints, ypoints)

# To plot only the markers, 
# you can use shortcut string notation parameter 'o', which means 'rings'.
plt.plot(xpoints, ypoints, "o")

plt.show()
