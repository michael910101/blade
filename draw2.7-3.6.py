import sys
import numpy as np
import pylab as pl
import math
#x = [1, 2, 3, 4, 5]# Make an array of x values
#y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
#pl.plot(x, y)# use pylab to plot x and y
#pl.title('Plot of y vs. x')# give plot a title
#pl.xlabel('x axis')# make axis labels
#pl.ylabel('y axis')
#pl.xlim(0.0, 7.0)# set axis limits
#pl.ylim(0.0, 30.)
#pl.show()# show the plot on the screen

x_values=[]
y_values=[]
num=0.0
while num<math.pi*4:
    y_values.append(math.sin(num))
    x_values.append(num)
    num+=0.1
# now plot
pl.plot(x_values,y_values,'ro')
pl.show()
