import cvxpy as cp
import numpy as np

# 商品组合的价格系数
c = np.array([6,3,12,12,8,16])
# 商品组合限制
a = np.array([[1,0,0,1,0,1],[0,1,0,0,1,0],[0,0,1,1,0,1],[0,0,1,0,1,1]])
b = np.array([1,1,1,1])

# 求解
x = cp.Variable(6,integer = True)
obj = cp.Maximize(cp.sum(cp.multiply(c,x)))
cons = [a*x<=b,x>=0,x<=1]
prob = cp.Problem(obj,cons)
prob.solve(solver = 'GLPK_MI',verbose = True)

# 最优方案和最优解
print(x.value)
print(prob.value)

