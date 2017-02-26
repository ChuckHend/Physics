import numpy as np
from matplotlib import pyplot as plt

f = open('Euler.txt', 'w')    # open stream to data file to export data
theta = np.pi*172/180         # starting angle of pendulum
thetaDot = 0                  # m/s starting velocity, (light tap)
thetaDotDot = 0               # m/s^2 starting velocity
dt = 0.01                     # increments in seconds
timeTotal = 1000              # total time to run simulation seconds
t = 0                         # start time seconds

# vector (array) from t to timeTotal, equally spaced in length
#   of timeTotal/dt. Used in the loop instead of counter.
time = np.linspace(t, timeTotal, timeTotal/dt)

gamma = 0.0033   # linear decay constant (from experiment)
alpha = 0.003    # square decay constant

k = -22.04148    # k is  computed from sqrt(I/mgL)

for t in time:
    # calculate acceleration
    thetaDotDot = k * np.sin(theta) - gamma*thetaDot - alpha*abs(thetaDot)*thetaDot
    thetaDot += thetaDotDot * dt                        # calcualte velocity
    theta += thetaDot * dt                              # calculate position
    s = str(t) + "," + str(theta*180/np.pi) + "\n"      # out string
    f.write(s)

f.close()