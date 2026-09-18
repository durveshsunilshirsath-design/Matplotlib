import matplotlib.pyplot as plt

a=['Mon','Tue','Wed','Thu','Fri']
b=[10,20,35,21,50]

plt.bar(a,b,color='b',width=0.4)
plt.title('Bar Chart')
plt.xlabel('Days')
plt.ylabel('Revenue')
plt.grid(color='grey',linestyle='-',linewidth=0.25,alpha=0.5)

plt.show()