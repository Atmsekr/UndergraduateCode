import scipy
from scipy import sparse
from scipy.sparse.linalg import spsolve
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
dx = dy = 0.02
x = y = np.arange(start=dx, stop=1, step=dx)
N = x.shape[0]
xs, ys = np.meshgrid(x, y)
rhs = (-np.sin(np.pi*xs)*np.sin(np.pi*ys)).reshape(-1) # f(x, y) = -sin(pi*x)*sin(pi*y)
one_dim_laplace = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(N,N), format="csr")/(dx**2)
lhs = sparse.kron(sparse.eye(N), one_dim_laplace) + sparse.kron(one_dim_laplace, sparse.eye(N))
u = spsolve(lhs, rhs)

u_m = u.reshape(N, N)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(xs, ys, u_m, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()

# u_analytic = (np.sin(np.pi*xs)*np.sin(np.pi*ys))/(2*np.pi**2)
# diff_u = np.abs(u_analytic - u_m)
# plt.contour(xs, ys, diff_u)
# plt.colorbar()
# plt.show()