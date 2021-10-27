import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import csv

#increase font size
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 35}

matplotlib.rc('font', **font)

#read csv
c = open('100.csv', 'r')
r = csv.DictReader(c)

#var
x_values = []
y_values = []
x_axis = []
y_axis = []

highest_length = 0

#setting values for x and y and also setting up axises
for row in r:
    x_values.append(int(row["Cycle"]))
    y_values.append(int(row["Length"]))
    
    x_axis.append(int(row["Cycle"]))

    if highest_length < int(row["Length"]):
        highest_length = int(row["Length"])

interval = highest_length/len(x_values)
current_interval = interval

for i in range(x_axis[-1]): #because lists for x and y values need to the the same
    y_axis.append(int(current_interval))
    current_interval += interval

plt.figure(figsize=(len(x_values)/3,len(x_values)/4))


#plt.ylim(1,50)
print(x_axis)
plt.title('Number of steps required to complete the Collatz Conjecture for each integer from 1-100')
plt.xlabel('Positive Integers from 1-100')
plt.ylabel('Amount of Steps taken to complete the collatz conjecture')

plt.scatter(x_axis,y_axis)
plt.plot(x_axis, y_axis)
plt.plot(x_values,y_values)
plt.show()