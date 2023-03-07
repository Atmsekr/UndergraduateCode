import scipy
from scipy import sparse
from scipy.sparse.linalg import spsolve
import numpy as np
import matplotlib.pyplot as plt
dx = 0.01
x = np.arange(start=dx, stop=1, step=dx)
N = x.shape[0]
rhs = np.sin(2*np.pi*x) # f(x)
lhs = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(N,N), format="csr")/(dx**2)
u = spsolve(lhs, rhs) # solve u=A/B
print(N)
plt.plot(x, u, label="Numerical")
plt.plot(x, -np.sin(2*np.pi*x)/(4*np.pi**2), "--", label="Analytic")
plt.legend()
plt.grid()
plt.show()
