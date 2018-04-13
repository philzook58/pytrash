
#assume symmettric

upper_diag = []
diag = []
b = []

schur_diag = []
schur_b = []

''' SHould I use explicit alternating constraints?'''

# Maintain schur_lu strcture and use lu_solve. Really I don't think we need to maintain schur_diag anyhow.
def lin_solve(diag, upper, b):
	#Unfortunately the first step needs to be different...?
	# OR. Just put a HUGE weight on the initiasl condition matching the actual initial conditions. The weight also goes on the ic vectro 
	# OR IC - 0.001 < x < IC + 0.0001 and use logarithmic barriers. We you could say that we don't know it to some accuracy anyhow (although it might try to be optimistic?)
	# why not just replace ALL dynamics with these constraints?
	schur_b[0] = b[0]
	schur_diag[0] = diag[0] #np.eye(Nstate + Ncontrol)
	#schur_diag[NState:] = 0.001
	#special_upper = np.copy(upper_diag[0])
	#special_upper[:,:NState] = 0
	#schur_diag[1] = diag[1] - upper_diag[0] @ schur_diag[0].inv @ special_upper

	for block in range(1, len(diag)):
		temp_block = upper_diag[block-1].T @ schur_diag[block-1].inv
		schur_diag[block] = diag[block] - upper_diag[block-1].T @ schur_diag[block-1].inv  @ upper_diag[block-1]
		schur_b[block] = b[block] - upper_diag[block-1].T @  schur_diag[block-1].inv @ schur_b[block-1]

	sol[N] = schur_diag[N].inv @ schur_b[N]

	for block in range(N-1, 0):
		sol[block] = schur_diag[block].inv @ ( schur_b[block]  - upper_diag[block] @ sol[block+1])


def state_slice(x):
	return x[:NState]
def control_slice(x):
	return x[NState:]

def lineq_hess(x, a):
	return 1/(x-a)**2

def lin_cost():
	P = np.zeros((T, NState + NControl, NState + NControl))
	q = np.zeros((T, NState + NControl))


	P[0,:NState] = 1/(xs[0,:NState]-(ic+0.001))**2 + 1/(xs[0,:NState]-(ic-0.001))**2
	q[0,:Ntate] = diag[0,:NState] * ic
	return P, q



def build_system(xs, ic):
	#diag[0] = np.eye(Nstate + Ncontrol) # Maybe this is ok. I'm concered about inverting this. Aregularized unit cost first action?
	#diag[:NState] = 1000 * T #Grows with T so that total path sum can never overwhelm this constraint
	#b[0] = 1000 * T * initial_conditions

	# No. Wait. I'm asking for least squares initial conditions. That isn't right. I need a lagrange multiplier enforcing.

	A, b = lin_eq_of_motion(x, u) # a linearized respose of xdot given x and u

	P, q = lin_cost(x, u) # Linear cost. q is going to 1/2(x-x0)P(x-x0) = 1/2xPx+ qx + c => q = -P@x0
	for t in range(T):
		diag.append(P) # Build costs# Costs tend to be easy to linearize.
		upper.append(np.eye(NState+NControl)/dt + A/2) #Write linearized eq of motion
		b.append(q)
		if t != 0 and t != T-1:
			#COnstraitnts / Lagrange mutlplier rows
			diag.append(np.zeros(NState)) # Build costs# Costs tend to be easy to linearize.
			upper.append(A/2 - np.eye(NState+NControl)/dt) #Write linearized eq of motion
			b.append(b)

	# Add in the inequality constraint for the initial conditions
	diag[0][:NState] = 1/(xs[0,:NState]-(ic+0.001))**2 + 1/(xs[0,:NState]-(ic-0.001))**2
	b[0][:Ntate] = diag[0][:NState] * ic
#upper_diag, b = zip(map(lambda x: lin_eq_motion(x[:Nstate], x[[Nstate:]])  , x))
# but we also need to intercalate the lin_cost
for i in range(T):
	if i % 2 == 0:
		A, b1 = lin_eq_of_motion(x, u) 
		upper_diag.append(A)
		b.append(b)
	else:
		P, q = lin_cost(x, u)
		upper_diag.append(P)
		b.append(q)

def newton():
	x = np.zeros(T, NState + NControls)
	while newton_decrement > eps:
		diag, upper, b = build_system(x)
		step = lin_solve(diag, upper, b)
		alpha = linesearch(step)
		x += alpha * step


def linesearch(x, step):
	alpha = 1
	while not check_bounds() and check_ineq():
		alpha *= 0.2
	return alpha


import torch
from torch.autograd import Variable

xs = Variable(torch.zeros(T, NState + NControl))

x = xs[:,0]
xdot = xs[:,1]
theta = xs[:,2]
thetadot = xs[:,3]
a = xs[:,4]

s = torch.sin(theta)
c = torch.cos(theta)




A = np.zeros(T, NState, NState + NControl)
A[:, 0, 1] = 1
A[:, 3, 2] = s.grad.numpy()



#etc

b = np.zeros(T, NState)
b[3] = s.numpy() + np.dot(A, xs)

#evenutally slice up these big matrices
[A[t, :, :] for t in range(T)]
#No wait. Why ever do this? Oh. Right. Because of the interleaving of constraintsd and other
# Could do explicit interleavcing in schur loop
# No that is poor sepearation of concerns
A, b, P, q



for t in range(T):



# 












a.numpy()
b = torch.from_numpy(a)

