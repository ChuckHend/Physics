import numpy as np

# Runge-Kutta Method
# Adam Hendel and Matthew Sheldon

f = open('RungeKutta.txt', 'w')    # open stream to data file to export data

dt = .0025                # step size
totalTime = 1000  # total time
stepsTotal = int(totalTime / dt)  # total slices

gamma = 0.0033  # friction factor
alpha = 0.003    # square decay constant
k = -22.04148

theta = np.pi * 172 / 180  # initial angle
thetaDot = 0               # initial angular velocity
t = 0

for j in range(stepsTotal):
    # m velocity
    # n position
    m1 = (k * np.sin(theta) - gamma*thetaDot - alpha*abs(thetaDot)*thetaDot) * dt
    n1 = thetaDot * dt

    m2 = (k * np.sin(theta + n1/2) - gamma*(thetaDot + m1/2) - alpha*abs(thetaDot + m1/2)*thetaDot + m1/2) * dt
    n2 = (thetaDot + m1 * 0.5) * dt

    m3 = (k * np.sin(theta + n2/2) - gamma*(thetaDot+m2/2) - alpha*abs(thetaDot+m2/2)*thetaDot+m2/2) * dt
    n3 = (thetaDot + m2 * 0.5) * dt

    m4 = (k * np.sin(theta + n3) - gamma*(thetaDot+m3) - alpha*abs(thetaDot+m3)*thetaDot+m3) * dt
    n4 = (thetaDot * m3) * dt

    thetaDot = thetaDot + (m1 + 2*m2 + 2*m3 + m4)/6
    theta = theta + (n1 + 2*n2 + 2*n3 + n4)/6

    t = t + dt
    s = str(t) + "," + str(theta*180/np.pi) + "\n"
    f.write(s)

    #print(str(t), str(theta*180/np.pi))


f.close()