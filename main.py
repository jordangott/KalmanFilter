import numpy as np
import pdb
import matplotlib.pyplot as plt

mean = np.array([[0, 0]]).T
cov = np.array([[0, 0], [0, 0]])

x = np.array([[0, 0]]).T
h = np.array([1, 0]).reshape(1,2)

dt = .5
siga = .2
sigz = 1
#sigz^2 = R

f = np.array([[1, dt], [.5*dt**2, dt]])
g = np.array([[.5*dt**2, dt]]).T
q = np.dot(g,g.T)*(siga**2)
r = sigz**2
zlist = []
truth = []
xpredict = []
ppredict = []
identity = np.array([[1, 0], [0, 1]])
timestep = []


for i in range (0, 100):
	x =  np.dot(f,x) + np.random.multivariate_normal(np.array([0, 0]), q).reshape(-1,1)
	truth.append(x)
	z = x[0] + np.random.normal(0, r)
	zlist.append(z)
	timestep.append(i)

x0 = x = np.array([[0, 0]]).T
p0 = cov


for i in range(0, 100):
	z = zlist[i]
	#Predict Step
	xpred = np.dot(f, x0)
	p1 = np.dot(f, p0)
	p2 = np.dot(p1, f.T)
	p = p2 + q
	#Update Step
	y = (z - xpred[0]).reshape(1, 1)
	s = r + p[0, 0]
	k = (np.dot(p, h.T) * 1/s).reshape(2, 1)
	#pdb.set_trace()
	xupd = xpred + np.dot(k, y)
	x0 = xupd
	xpredict.append(xupd)
	
	pupd1 = np.dot(identity - np.dot(k, h), p)
	pupd2 = np.dot(pupd1, (identity - np.dot(k, h)).T)
	pupd3 = np.dot(k, r)
	pupd4 = np.dot(pupd3, k.T)
	pupd = pupd2 + pupd4

	p0 = pupd
	ppredict.append(pupd)

##need to figure out how to plot! 

for i in range(0, 100):
	print('x =', truth[i])
	print('xpred =', xpredict[i])

truthx, truthy = zip(*truth)
predx, predy = zip(*xpredict)
plt.scatter(timestep, predy, c = 'b')
plt.scatter(timestep, truthy, c = 'g')

plt.show()
