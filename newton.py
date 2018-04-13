import numpy as np
from scipy import linalg

# I should rewrite my LQR solver in the lagrange form. It's very reasonable and if i use banded, very fast.

# If is composition of Ax+b then there is a slight optimizatiomn that can be performed for backtracking
def linesearch(f, df0, x, dx, alpha=0.25, beta=0.1):
	f0 = f(x)
	t = 1
    while f(x + t * dx) > f0 + alpha * t * df0 @ dx:
    	t *= beta 
    return t

def newton(f, x0, grad, hessInv):
	while True:
	    df = grad(x)
	    dx = - hessInv(df)
	    newton_decrement = - df @ dx
	    t = linesearch(f, df, x, dx)
	    x += t * dx 
	    if newton_decrement / 2 < 1e-10:
	      return x  

def interiorPoint(f, x, grad, hessInv, phis, gradphis, hessPhis):
	def gradB(x,t): 
		return t * grad(x) - (grad phi) / phi(x)
	def HessInvB(x,t):
		# use low rank update. Assumes that less inequality constraint than 
	t = 1
	while True:
		x = newton(f, x gradB(t), hessInvB(t))


		if gap < 1e-10:
			break
		t *= 10
def constrainednewton(f, x0, A, b):

def interiorpointqp(f, x, grad, hessInv, A1, b1, A2, b2): #A1 x = b1, A2 x < b2
	A22 = A2.T @ A2
	b22 = A2.T @ b2
    def gradB(x,t): 
		return t * grad(x) - (A) / np.log(np.linalg.norm2(A2 @ x - b2))
	def HessInvB(x,t):
		# use low rank update. Assumes that less inequality constraint than 
	t = 1
	while True:
		x = constrainednewton(f, x gradB(t), hessInvB(t), A1, b1)


		if gap < 1e-10:
			break
		t *= 10

def interiorqp_banded()
def interiorqp_sparse(f, x, grad, hess, A1, b1, A2, b2):
	hessi = t * hess - 


#[T, Nconstraints + NVars]



def blocksolve(Ainv, B, C, D, b0, b1): # Ainv is in functional form
	'''
	Ainv is called multiple times.
	Precompute any factorizations that may help that (or memoize them)
	D is small
	A B | x0 = b0
	C D | x1 = b1
	'''
	#b1 -= C @ Ainv(b0)
	x1 = linalg.solve(D - C @ Ainv(B), b1 - C @ Ainv(b0) )
	x0 = Ainv(b0 - B @ x1)
	return x0, x1

#Look in Strang. He may indeed have already had these algorithms in this form
def gauss(A):
	n = A.size[0]
	U = np.copy(A)
	L = np.zeroeslike(A)
	pivots = []
	while n > 0:        
        pivot = np.argmax(U[:,0])
        pivots.append(pivot)
        swap(U[pivot,:], U[0,:])
        L[0,0] = 1
        L[:,0] = - U[:,0] / U[0,0]
        U[1:,:] += U[0,:].reshape(1. -1) * L[:,0].reshape(-1,1) 
        U = U[1:,1:]
        L = L[1:,1:]
		n--
	return L, U, pivots

def householderQR(A):
	reflectors = []
	while n > 0:
		x = np.copy(A[:,0])
		#	e = np.zeroslike(x)
		norm2 = np.linalg.norm(x[1:])
		x[0] -= np.sqrt(norm2 + x[0]**2)
		x = x / (np.sqrt(norm2 + x[0]**2))

		reflectors.append(x) 
		A -=  2 * v.reshape(-1,1) * (v @ A).reshape(1,-1)
		n--
	return reflectors, A

def hessenberg(A):
	reflectors = []
	while n > 1:
		x = np.copy(A[:,0])
		x[0]=0
		#	e = np.zeroslike(x)
		norm2 = np.linalg.norm(x[2:])
		x[1] -= np.sqrt(norm2 + x[1]**2)
		x = x / (np.sqrt(norm2 + x[1]**2))

		reflectors.append(x) 
		A -=  2 * v.reshape(-1,1) * (v @ A).reshape(1,-1)
		A -=  2 * (A @ v).reshape(-1,1) * v.reshape(1,-1)
		n--
	return reflectors, A


