import matplotlib.pyplot as plt

a=['Mon','Tue','Wed','Thu','Fri']
b = [10, 20, 35, 21, 50]

plt.scatter(a,b,marker='D',color='r',s=100)

plt.title('Scatter Plot')
plt.xlabel('Days')
plt.ylabel('Revenue in Pcs')

plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

plt.show()