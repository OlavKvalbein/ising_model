import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/data.csv", header=None)

plt.imshow(df.values, cmap="gray")
plt.show()