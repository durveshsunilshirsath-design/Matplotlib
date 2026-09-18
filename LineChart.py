import matplotlib.pyplot as plt

a=['Mon','Tue','Wed','Thu','Fri']
b=[10,20,35,21,50]

plt.plot(a,b,marker='o',color='g',linestyle='--')
plt.title('Line Chart')
plt.xlabel('Days')
plt.ylabel('Revenue')
plt.grid(color='grey',linestyle='-',linewidth=0.25,alpha=0.5)

plt.show()