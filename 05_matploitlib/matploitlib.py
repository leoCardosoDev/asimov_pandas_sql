import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x,y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()

plt.bar(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Bar Chart')
plt.show()

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

fig, axs = plt.subplots(2)
# Primeiro subplot
axs[0].plot(x, y)
axs[0].set_title('First Subplot')
# Segundo subplot
axs[1].bar(x, y)
axs[1].set_title('Second Subplot')
plt.tight_layout()
plt.show()

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('First Subplot')
axs[0, 1].bar(x, y)
axs[0, 1].set_title('Second Subplot')
axs[1, 0].scatter(x, y)
axs[1, 0].set_title('Third Subplot')
axs[1, 1].hist(y)
axs[1, 1].set_title('Fourth Subplot')
plt.tight_layout()
plt.show()

plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Customized Line Plot')
plt.show()

plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Customized Plot with Labels')
plt.show()


from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
ax.plot_surface(x, y, z, cmap='viridis')
plt.title('3D Surface Plot')
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

ax.scatter(x, y, z)
plt.title('3D Scatter Plot')
plt.show()

data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.title('Heatmap')
plt.colorbar()
plt.show()


plt.imshow(data, cmap='coolwarm', interpolation='bilinear')
plt.title('Customized Heatmap')
plt.colorbar()
plt.show()
