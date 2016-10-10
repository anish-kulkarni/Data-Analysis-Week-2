"""
Assignment 2 Problem 3 - Linear Expansion
Objectives:
a) Make a scatter plot for length of aluminum rod vs temperature
b) Find the best fit line for the same. Estimate Length of the rdo at 0 degree celsius and coefficient of linear expansion
c) Predict length of rod at 15 degree celsius and estimate error in the prediction

"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import csv
import xlrd

#input data from csv file
temperature = [0.0]*0
length = [0.0]*0

with open('linearexpansion.csv') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in reader:
         temperature.append(float(row[0]))
         length.append(float(row[1]))

# scatter plot
plt.plot(temperature, length , 'o')
plt.title("Thermal Expansion of Aluminum rod")
plt.ylabel("Length in mm")
plt.xlabel("Temperature in degree celsius")
#plt.show()

# best fit line
N = len(temperature)   # N = number of data points
sumT = 0.0             # sum of all temperature
sumTsquare = 0.0       # sum of squares of temperatures
sumL = 0.0             # sum of lengths
sumTL = 0.0            # summation Ti*Li

"""
best fit line is L = m*T + c
m and c satisfy the linear equations: (refer report for derivation)
c * N    + m * sumT       = sumL
c * sumT + m * sumTsquare = sumLT
We solve this set of equations using Cramer's rule
"""
for t,l in zip(temperature,length):
    sumT += t
    sumTsquare += t**2
    sumL += l
    sumTL += t*l

D1 = sumL*sumTsquare - sumT*sumTL
D2 = N*sumTL - sumT*sumL
D = N*sumTsquare - sumT**2

c = D1/D
m = D2/D

print "Length at 0 degree celsius = ", c , "mm"
print "Coefficient of linear expansion = ", m , "mm/Kelvin"
plt.plot([0,17],[c,m*17+c],label='Slope = ' + str(round(m,2)) + 'mm/Kelvin and Intercept = ' + str(round(c,2)) +'mm')
plt.legend()

# predict length at 15 degree celsius and estimate error in prediction
predicted_length = m*15 + c;            # length corresponding to 15 degree celsius according to best fit line
print "Predicted length at 15 degree celsius = ", predicted_length, "mm"
plt.plot((15,15),(900,predicted_length),'r--')
plt.xticks(range(20),range(20))
plt.plot((15,0),(predicted_length,predicted_length),'r--')
yticks = range(900,1400,100)
yticks.append(round(predicted_length,2))
plt.yticks(yticks,yticks)

errorSquare = 0                         # initialization
for t,l in zip(temperature,length):
    errorSquare += (l - (m*t + c) )**2  # calculating error
errorSquare /= N-2
error = errorSquare**0.5
print "Estimate of error in predicted length at 15 degree celsius = ", error, "mm"

plt.show()