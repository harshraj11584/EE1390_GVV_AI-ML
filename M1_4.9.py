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
BA=AB=dist(A,B)
CB=BC=dist(B,C)
AC=CA=dist(C,A)
I = (BC*A+CA*B+AB*C)/(AB+BC+CA)
nAB=normal_vector(A,B)
nBC=normal_vector(B,C)
nCA=normal_vector(C,A)
IX = np.linalg.norm(np.matmul(nAB.T,(I-A)),2)/np.linalg.norm(nAB,2)
IY = np.linalg.norm(np.matmul(nBC.T,(I-B)),2)/np.linalg.norm(nBC,2)
IZ = np.linalg.norm(np.matmul(nCA.T,(I-C)),2)/np.linalg.norm(nCA,2)
print("IX=",IX)
print("IY=",IY)
print("IZ=",IZ)