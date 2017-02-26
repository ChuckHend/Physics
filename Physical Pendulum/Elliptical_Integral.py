import numpy as np
import csv

# if we want to plot using plot.ly
# tls.set_credentials_file(username='hendel.adam', api_key='QWIYtQiopT7KmsdqCuSy')
f = open('EllipticalIntegral.txt', 'w')    # open stream to data file to export data

c = 0.213  # constant for sqrt(I/mgl)
T = 0
y = 0
const = 4*c # constant for 4*sqrt(I/mgl)

slices = 1000
theta0 = np.linspace(0, np.pi, slices)
phi = np.linspace(0, np.pi/2, slices)
dPhi = np.pi/2/slices

for j in theta0:
    k = np.sin(j / 2)
    T = 0
    for i in phi:
        y = np.power(1 - np.power(k * np.sin(i), 2), -0.5)
        T += y*dPhi
    T = T*const
    print (T, ",", j)
    s = str(T) + "," + str(j) + "\n"
    f.write(s)

