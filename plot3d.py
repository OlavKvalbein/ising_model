import matplotlib.pyplot as plt
import numpy as np

with open("data.txt", "r") as f:
	text_data = f.read()

voxelarray = np.array(list(text_data), dtype=int)
size = round((voxelarray.size)**(1/3))
voxelarray = voxelarray.reshape((size, size, size))

ax = plt.figure().add_subplot(projection="3d")
ax.voxels(voxelarray)
plt.show()