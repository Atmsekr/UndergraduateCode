import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags,csr_matrix
from scipy.sparse.linalg import spsolve

beta = 0.1
x = np.linspace(0, 1,101)
u0 = np.exp(-10*(x-0.7)**2)
Nx = u0.shape[0]
Nt = 500
dx = x[1] - x[0]
dt = 0.01

a1 = -beta*dt/dx
a2 = 1+beta*dt/dx
a3 = 0

A_Periodic = csr_matrix(diags([a1, a3, a2, a1, a3],[1-Nx,-1,0,1,Nx-1], shape=(Nx,Nx)))
A_Dirichlet = csr_matrix(diags([a3, a2, a1],[-1,0,1], shape=(Nx,Nx)))

A_Periodic = A_Periodic.toarray()
A_Dirichlet = A_Dirichlet.toarray()

A_Periodic = np.linalg.inv(A_Periodic)
A_Dirichlet = np.linalg.inv(A_Dirichlet)

sol = np.zeros((Nt+1,Nx))

sol[0,:] = u0

for ti in range(Nt):
    # sol[ti+1] = sol[ti] @ A_Periodic
    sol[ti+1] = sol[ti] @ A_Dirichlet

for ti in [0,10,100,200,500]:
    plt.plot(x, sol[ti,:], label="t=%.3f"%(dt*ti))

plt.legend()
plt.grid()
plt.show()