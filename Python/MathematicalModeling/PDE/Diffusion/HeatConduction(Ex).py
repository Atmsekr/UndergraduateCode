import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags,csr_matrix
from scipy.sparse.linalg import spsolve

# alpha、x步长、原函数等设置
alpha = 0.1
x = np.linspace(0, 1,101)
u0 = np.exp(-10*(x-0.7)**2)
Nx = u0.shape[0]
Nt = 3000
dx = x[1] - x[0]
dt = 0.0001

# 在推导中求解的系数
a1 = alpha*dt/dx**2
a2 = 1-2*alpha*dt/dx**2
a3 = alpha*dt/dx**2

# 计算两种边界下的带状矩阵
A_Periodic = csr_matrix(diags([a1, a3, a2, a1, a3],[1-Nx,-1,0,1,Nx-1], shape=(Nx,Nx)))
A_Dirichlet = csr_matrix(diags([a3, a2, a1],[-1,0,1], shape=(Nx,Nx)))

A_Periodic = A_Periodic.toarray()
A_Dirichlet = A_Dirichlet.toarray()

# 初始化解矩阵
sol = np.zeros((Nt+1,Nx))
sol[0,:] = u0

# 求解不同时间下的曲线，通过注释另一种边界可绘制不同边界下的图像
for ti in range(Nt):
    # sol[ti+1] = sol[ti] @ A_Periodic
    sol[ti+1] = sol[ti] @ A_Dirichlet

# 展示特定时间下的图像
for ti in [0,10,100,200,500,1000,3000]:
    plt.plot(x, sol[ti,:], label="t=%.3f"%(dt*ti))

plt.legend()
plt.grid()
plt.show()