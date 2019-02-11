import numpy as np
import matplotlib.pyplot as plt
A = np.array([-2,-2])
B = np.array([1,3])
C = np.array([4,-1])
D=(B+C)/2;E=(A+C)/2;F=(A+B)/2;
def plot_line(a,b,s):
	plt.plot((a[0],b[0]),(a[1],b[1]),label=s)
plot_line(A,D,"AD")
plot_line(B,E,"BE")
plot_line(C,F,"CF")
plt.grid()
plt.legend(loc='best')
plt.show()