import matplotlib.pyplot as plt

a = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
b = [10, 20, 35, 21, 50]
c= [5,15,40,28,45]

plt.scatter(a,b,color='orange',label='Department A')
plt.scatter(a,c,color='red',label='Department B')

plt.title('Scatter Plot')

plt.xlabel('Days')
plt.ylabel('Revenue')
plt.legend()
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

plt.show()