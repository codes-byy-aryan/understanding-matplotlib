#add textbox...
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,1,5,3]
y1=[1,2,3,4,5]
y2=[5,4,3,2,1]

plt.plot(x,y,marker='o',linestyle='dashed',label='graph_1')
plt.plot(x,y1,marker='o',linestyle='dashed',label='graph_2')
plt.plot(x,y2,marker='o',linestyle='dashed',label='graph_3')

plt.title('Solving the Question',fontsize='16',color='blue')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.xlim([1,7])
plt.ylim([1,7])

text',bbox=dict(facecolor='lightyellow'))

plt.legend()
plt.grid()
plt.show()