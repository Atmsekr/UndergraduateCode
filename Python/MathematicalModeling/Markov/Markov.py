import numpy as np
import matplotlib.pyplot as plt


alpha = 0.3
beta = 0.1

max_m = 1001
Transition_martrix = np.array([[1-alpha, alpha],[beta, 1-beta]])

ini = np.array([[0, 1]])
ans = 0
x = np.linspace(0, 1,1001)
y = [0]
for m in range(1,max_m):
    ini = ini @ Transition_martrix
    ans = ans + ini[0][0]
    y.append(ans/m)

y_ = np.array(y)

print(y_)

plt.plot(x,y_)
plt.show()