import numpy as np
import matplotlib.pyplot as plt
A = np.matrix('-2;-2')
B = np.matrix('1;3')
C = np.matrix('4;-1')
def normal_vector(a,b):
	omat = np.matrix('0,1;-1,0')
	return np.matmul(omat,b-a)
def line_intersect_AP_BQ(a,b,c):
	#solving Wx=y
	W=np.vstack(((c-b).T,(c-a).T))
	y=np.vstack(( np.matmul((c-b).T,a) , np.matmul((c-a).T,b)))
	return np.matmul(np.linalg.inv(W),y)
print(line_intersect_AP_BQ(A,B,C))