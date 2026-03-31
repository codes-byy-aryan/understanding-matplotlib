# Q-2 Design a plot that contains :
#     x = [1,2,3,4,5]
#     y = [2,4,1,5,3]
#     y1 = [1,2,3,4,5]
#     y2 = [5,4,3,2,1]
#Use different color,add legends , title, xlabel, ylabel.
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,1,5,3]
y1 = [1,2,3,4,5]
y2 = [5,4,3,2,1]

plt.title("Plot Practice")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.plot(x,y,color='red',label="Plot(0,0)")
plt.plot(x,y1,color='blue',label="Plot(0,1)")
plt.plot(x,y2,color='green',label="Plot(0,2)")

plt.legend()
plt.show()