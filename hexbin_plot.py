import numpy as np 
import matplotlib.pyplot as plt 

x = np.random.randn(180)  # ← define x with 180 random values
y = np.random.randn(180)  # ← optional: define y for clarity

plt.hexbin(x, y, gridsize=25, cmap='Blues') 
plt.colorbar() 
plt.show()

