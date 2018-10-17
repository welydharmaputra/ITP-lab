import matplotlib.pyplot as plt
import numpy as np
import math as m                    #to importing all libraries that needs for using codes
import sys

try:                                                #for using try and except to make the worng input shows that is the wrong input
    howmuch=int(input("How many trajectories: "))       #to input the number of trajectories
except ValueError:
    print("Invalid input type")             #to prove the wrong input so the code doesn't have an error
    sys.exit()

g=9.8                                   #gravity of earth on physics
num=1                                   #intial value for trajectory numbers
legends=[]                              #container for the names of trajectories
plt.rcParams.update({'font.size':11,'font.style':'oblique','font.weight':'bold'})   #font format for the matplot

for i in range(0,howmuch):              #looping as many times as inputted

    xAxis=[]
    yAxis=[]                              #containers for all the X and Y axis

    try:
        initvel=int(input("Enter the initial velocity (m/s): "))            #the initial velocity input
        ang=int(input("Enter the angle of projection (degrees): "))         #initial angle input
    except ValueError:
        print("Invalid input type")             #same try and except as the first input
        sys.exit()

    bent=ang*(m.pi/180)
    fx=initvel*m.cos(bent)
    fy=initvel*m.sin(bent)                 #all the necessary values for the parabola
    tMax=(2*fy)/g
    t1 = np.linspace(0, tMax, num=100)      # making an array of time from 0 to tMax in a 100th seconds increments

    for k in t1:
        x = ((initvel*k)*np.cos(bent))
        y = ((initvel*k)*np.sin(bent))-((0.5*g)*(k**2))       #the physcis formula to know the x and y coordinate
        xAxis.append(x)
        yAxis.append(y)
        
    plt.plot(xAxis,yAxis)   #this will plot each trajectory
    a="Trajectory "+str(num)            #making trajectory name and appending it into the container
    legends.append(a)
    num+=1                      #indicating the increasing number of trajectories

plt.xlabel("Travel Distance(X)",fontweight='bold')    #x and y labels
plt.ylabel("Aerial Position(Y)",fontweight='bold')
plt.legend(legends)         #creating a legend for each trajectory
plt.show()  #to show the parabola


