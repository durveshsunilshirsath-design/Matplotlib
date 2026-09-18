import matplotlib.pyplot as plt

a = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
b = [10, 20, 35, 21, 50]

plt.pie(b, labels=a, colors=['blue', 'orange', 'green', 'red', 'purple'], autopct='%1.1f%%')

plt.title('Pie Chart')
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
plt.legend()
plt.show()