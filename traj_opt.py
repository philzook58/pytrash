import numpy as np
from cvxopt.solvers import qp, conelp, lp
from cvxopt import matrix, sparse
'''

We need to build the appropriate matrices for a cartpole trajectory optimization

The linear constraint comes from lienarized dynamics

The inequality constraint comes from unwillingness to hit the walls.

'''
np.set_printoptions(precision=4, linewidth=1000)
dt = 0.01
# Lookahead
T = 50
## of variables per time step
N = 5

# Indexing into the variables
X = 0
XDOT = 1
THETA = 2
THETADOT = 3
U = 4 #we call acceleration U to avoid conflict with the constraint matrix A

# A is the matrix storing for all time steps the equations of motion
A = np.zeros((T,N-1,T,N))
initial_conditions = np.array([0,0,0,0])

theta = np.ones(T)
theta_avg = (theta[:-1] + theta[1:]) / 2 

Ts = np.arange(T-1) + 1

# The first index is the output variable ("xdot"), the second index is the input ("x")
A[Ts, X, Ts, XDOT] = .5
A[Ts, X, Ts-1, XDOT] = .5

A[Ts, THETA, Ts, THETADOT] = .5
A[Ts, THETA, Ts-1, THETADOT] = .5

A[Ts, THETADOT, Ts, U] = .5 * np.cos(theta_avg) #* m * L/2
A[Ts, THETADOT, Ts-1, U] = .5 * np.cos(theta_avg)# * m  * L/2

#gravity
A[Ts, THETADOT, Ts, THETA] = .5 * np.cos(theta_avg)# * m * g * L/2
A[Ts, THETADOT, Ts-1, THETA] = .5 * np.cos(theta_avg)# * m * g * L/2

# finite difference
for i in range(N-1):
	A[Ts, i, Ts, i] = 1 / dt
	A[Ts, i, Ts-1, i] = -1 / dt
	A[0,i,0,i] = 1 # initial condition block

#print(A.reshape((T*(N-1), T*N)))


b = np.zeros((T,N-1))

b[Ts,THETADOT] = np.cos(theta_avg) #* m * g * L/2
b[0,:] = initial_conditions

#print(b)

# B = A[:,:,:, 4]
# Aprime = A[:,:,:,:4]
# extract direct sum pieces via slicing. Hopefully this affects the parent structure.

# Ineqyakiuty constraints
# Gx<h
# We have to make half the inequalities negative
# Maybe hsouldn't make 0th time have a constraint?
G = np.zeros((T,6,T,N)) # One less than one greater than
Ts = np.arange(T)
G[Ts,0,Ts,X]= -1
G[Ts,1,Ts,X]= 1
G[Ts,2,Ts,XDOT]= -1
G[Ts,3,Ts,XDOT]= 1
G[Ts,4,Ts,U]= -1
G[Ts,5,Ts,U]= 1

h = np.zeros((T,6))

h[:,0] = 0
h[:,1] = 1

#XDOT lower and upper
h[:,2] = 1
h[:,3] = 1

# acceleration lower and upper
h[:,4] = 20
h[:,5] = 20


# Cost = 1/2 xPx + qx
cost = np.zeros((T,N))
cost[:,2] = 1.0 # Theta cost
P = np.diag(cost.flatten())
#print(P)
# or maybe we should only care about the end

q = np.zeros((T,N))
q[:,2] = -np.pi # offset

P = sparse(matrix(P))
q = matrix(q.flatten())
A = sparse(matrix(A.reshape((T*(N-1), T*N))))
b = matrix(b.flatten())
G = sparse(matrix(G.reshape((T*6,N*T))))
h = matrix(h.flatten())

# If sin(theta) is cost, 
# cos(theta) would be a c vector for cost
# maybe an initial guess for x could help
# It all kind of seems too slow, but maybe glpk could help
for i in range(10):
	lp(q,G,h, A,b)
	#qp(P, q, G, h, A, b)

