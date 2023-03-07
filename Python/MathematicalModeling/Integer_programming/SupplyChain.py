import cvxpy as cp
import numpy as np

# ��Ӧ�����ĳɱ�ϵ��
c=np.array([[39,14,11,14,16,82,8],
            [27,1e9,12,1e9,26,95,17],
	    [24,14,17,13,28,99,20]])
# ��������������
supply = np.array([1400,2600,2900])
demand = np.array([900,1200,600,400,1700,1100,1000])

# ���
x = cp.Variable((3,7),integer=True)
obj = cp.Minimize(cp.sum(cp.multiply(c,x)))
cons = [cp.sum(x, axis=0, keepdims=True)==demand.reshape(1,7),
        cp.sum(x, axis=1, keepdims=True)==supply.reshape(3,1),
        x>=0]
prob = cp.Problem(obj, cons)
prob.solve(solver='GLPK_MI',verbose = True)

# ���ŷ��������Ž�

print(x.value)
print(prob.value)



