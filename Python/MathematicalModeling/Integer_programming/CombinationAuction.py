import cvxpy as cp
import numpy as np

# ��Ʒ��ϵļ۸�ϵ��
c = np.array([6,3,12,12,8,16])
# ��Ʒ�������
a = np.array([[1,0,0,1,0,1],[0,1,0,0,1,0],[0,0,1,1,0,1],[0,0,1,0,1,1]])
b = np.array([1,1,1,1])

# ���
x = cp.Variable(6,integer = True)
obj = cp.Maximize(cp.sum(cp.multiply(c,x)))
cons = [a*x<=b,x>=0,x<=1]
prob = cp.Problem(obj,cons)
prob.solve(solver = 'GLPK_MI',verbose = True)

# ���ŷ��������Ž�
print(x.value)
print(prob.value)

