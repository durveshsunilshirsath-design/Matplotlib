import matplotlib.pyplot as plt

a = [10, 20, 35, 21, 50]

plt.hist(a, bins=4, color='b',edgecolor='black', alpha=0.7)

plt.title('Histogram')
plt.xlabel('Revenue')
plt.ylabel('Frequency')

plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

plt.show()