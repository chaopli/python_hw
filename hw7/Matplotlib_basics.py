__author__ = 'Noha'

import matplotlib.pyplot as plt
#from pylab import figure, hold, plot, show

# Define x any y lists to plot a line segment
x = [1,2,3]
y = [5,7,4]

# Define x any y lists to plot a line segment
x2 = [1,2,3]
y2 = [10,14,12]

def plot_line_basic():
    plt.plot(x, y)
    plt.show()

#plot_line_basic()

def plot_line_labels():
    plt.plot(x, y)
    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.show()

def plot_line_title():
    plt.plot(x, y)
    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.title('Interesting Graph')
    #plt.title('Interesting Graph\nCheck it out')
    plt.show()
#plot_line_title()

def plot_two_lines():
    plt.plot(x, y)
    plt.plot(x2, y2)
    #Here, we plot as we've seen already, only this time we add another parameter "label."
    # This allows us to assign a name to the line, which we can later show in the legend.
    # The rest of our code:
    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.title('Interesting Graph\nCheck it out')
    plt.show()

#plot_two_lines()

def plot_two_lines_legends():
    plt.plot(x, y, label='First Line')
    plt.plot(x2, y2, label='Second Line')
    #Here, we plot as we've seen already, only this time we add another parameter "label."
    # This allows us to assign a name to the line, which we can later show in the legend.
    # The rest of our code:
    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

#plot_two_lines_legends()


import matplotlib.pyplot as plt
# Define x any y lists to plot a line segment
x = [1,2,3]
y = [5,7,4]
# Define x any y lists to plot a line segment
x2 = [1,2,3]
y2 = [10,14,12]

def plot_two_lines_markers():
    plt.plot(x, y, label='First Line', color = 'k', marker = '*' )
    plt.plot(x2, y2, label='Second Line', color = 'r', marker = 'o')
    #Here, we plot as we've seen already, only this time we add another parameter "label."
    # This allows us to assign a name to the line, which we can later show in the legend.
    # The rest of our code:
    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

plot_two_lines_markers()

def plot_two_lines_markers_v2():
    figure()
    plot(x, y, 'b-')
    plot(x[0:2], y[0:2], 'ro')
    #Here, we plot as we've seen already, only this time we add another parameter "label."
    # This allows us to assign a name to the line, which we can later show in the legend.
    # The rest of our code:
    # plt.xlabel('Plot Number')
    # plt.ylabel('Important var')
    # plt.title('Interesting Graph\nCheck it out')
    # plt.legend()
    show()

#plot_line_labels()
#plot_line_title()
#plot_two_lines()
#plot_two_lines_legends()
#plot_two_lines_markers()
#plot_two_lines_markers_v2()