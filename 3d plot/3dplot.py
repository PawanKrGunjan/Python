import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import projections
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Step -1
iris = sns.load_dataset('iris')

#Step -2
sns.set_style('whitegrid')
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Step-3
x = iris['petal_length']
y = iris['petal_width']
z = iris['sepal_width']
# Step-4
ax.scatter(x, y, z)
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal width (cm)')
ax.set_zlabel('Sepal width (cm)')
ax.set_title('3D Plot')

plt.show()
