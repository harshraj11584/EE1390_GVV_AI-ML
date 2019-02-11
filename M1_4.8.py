import numpy as np
import matplotlib.pyplot as plt
A = np.matrix('-2;-2')
B = np.matrix('1;3')
C = np.matrix('4;-1')
def dist(a,b):
	return np.linalg.norm(b-a,2)
def normal_vector(a,b):
	omat = np.matrix('0,1;-1,0')
	return np.matmul(omat,b-a)
def dist(a,b):
	return np.linalg.norm(b-a,2)
BA=AB=dist(A,B)
CB=BC=dist(B,C)
AC=CA=dist(C,A)
I = (BC*A+CA*B+AB*C)/(AB+BC+CA)
n=normal_vector(A,B)
X= np.matmul(  np.linalg.inv((np.vstack((n.T, (B-A).T)))) , np.vstack((np.matmul(n.T,A),np.matmul((B-A).T,I))) )
IX = dist(I,X)
IX2 = np.linalg.norm(np.matmul(n.T,(I-A)),2)/np.linalg.norm(n,2)
print("Verify IX values")
print ("LHS=",IX)
print("RHS=",IX2)