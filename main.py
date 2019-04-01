import numpy as np

mean = np.array([[0, 0]]).T
cov = np.array([[0, 0], [0, 0]])

x = np.array([[0, 0]]).T

dt = .5
siga = .2
sigz = 1
#sigz^2 = R

f = np.array([[1, dt], [.5*dt**2, dt]])
g = np.array([[.5*dt**2, dt]]).T
q = np.dot(g,g.T)*(siga**2)
zlist = []


for i in range (0, 100):
	x =  np.dot(f,x) + np.random.multivariate_normal(np.array([0, 0]), q).reshape(-1,1)
	z = x[0] + np.random.normal(0, sigz**2)
	print('x =', x)
	print('z =', z)
	zlist.append(z)

for i in range(0, 100):
	z = zlist[i]
	#estimate x from z!!
	'''
	you can use models f g q dt siga sigz
	you cannot use X
	output should be a sequence of x's
	if we make obs noise really big, this will do poorly
	add plotting
	plot ground truth and estimates and see how close they are
	'''


