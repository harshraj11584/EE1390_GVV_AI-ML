import numpy as np
import matplotlib.pyplot as plt
A = np.array([-2,-2])
B = np.array([1,3])
C = np.array([4,-1])
P = np.array([2.32,1.24])
Q = np.array([1.72972974,-1.37837838])
R = np.array([0.02941177,1.38235295])
D=(B+C)/2;E=(A+C)/2;F=(A+B)/2;
def plot_line(a,b,s):
	plt.plot((a[0],b[0]),(a[1],b[1]),label=s)
plot_line(A,P,"AD")
plot_line(B,Q,"BE")
plot_line(C,R,"CF")
plot_line(A,B,"AB")
plot_line(B,C,"BC")
plot_line(C,A,"CA")
plt.grid()
plt.legend(loc='best')
plt.show()