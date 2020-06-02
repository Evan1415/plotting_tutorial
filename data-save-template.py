# ------------------------------- #
# ------- Package imports ------- #
# ------------------------------- #

import numpy as np # imports the entire namespace of functions belonging to numpy
import matplotlib # imports the entire namespace of functions belonging to matplotlib
import matplotlib.pyplot as plt # shortens matplotlib.pyplot -> plt


# ------------------------- #
# ------- Plotting  ------- #
# ------------------------- #

fig,axs = plt.subplots()       # creates a figure object
x = np.linspace(0, 10, 100)    # creates array from 0->100 with 100 elements in increments
                               # of 10/100
y = np.sin(x)                  # evaluates sin(x) on the array x

np.savetxt("my_file.txt",(x,y)) # saves data to the file "my_file.txt"
x,y=np.loadtxt("my_file.txt")

axs.plot(x, y, 'r')            # plots y(x), 'r': colour red
axs.set_xlabel('x-axis label') # xlabel
axs.set_ylabel('y-axis label') # ylabel
axs.set_title('My first plot') # title

plt.show()                     # displays the figure in the X-window


