import matplotlib.pyplot as plt             #to importing all libraries that needs for using codes
x1 = (int(input("input coordinate x: ")))   #to input the range
y1 = (int(input("input coordinate y: ")))
a=[]
b=[]            #the list that will be show


for x in range(10*-x1,10*y1,1):
    y=-x**2-2*x-2                   #the physics formula
    a.append(x)                     #to input the data to list
    b.append(y)

fig= plt.figure()
axes=fig.add_subplot(111)       #to choose the diagram and where the place that will be show
axes.plot(a,b,c='k')              #what will be input to the diagram and to set the color of the line
plt.show()                      #to show the plot
