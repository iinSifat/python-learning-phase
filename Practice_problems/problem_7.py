import numpy as np
import matplotlib.pyplot as plt
import math
plt.xlabel("x")
plt.ylabel("y")
plt.title("Piecewise Function Plot")
plt.grid(True)
x1 = np.arange(0, 4,.01) 
y1 = np.square(x1)
plt.plot(x1,y1,"red")
x2 = np.arange(4,8,.01)
y2 = np.full_like(x2,16) # direct assigning 16 will not work
plt.plot(x2,y2, "blue")
x3 = np.arange(8,12.01,.01)
y3 = np.square(12-x3)
plt.plot(x3, y3, "green")
plt.show()


