import numpy as np
import matplotlib.pyplot as plt
def direction_vector(a,b):
	return b-a
def normal_vector(a,b):
	omat = np.array([[0,1],[-1,0]])
	return np.matmul(omat,b-a)
A=np.array([-2,-2])
B=np.array([1,3])
print("A=",A,"\nB=",B)
print ("Dir vec=",direction_vector(A,B))
print ("Normal  vec=",normal_vector(A,B))