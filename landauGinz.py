# Convex Landau Ginzburg
# See Blog post for more

x = np.linspace(0,1,100).reshape((-1,1))
y = np.linspace(0,1,100).reshape((1,-1))


row = np.zeros(100)
row[0] = -2
row[1] = 1
col = row
K = np.toeplitz(row, col)
K2 = np.kron(np.eye(100), K) + np.kron(K, np.eye(100))

def V(phi):
	a = 1 # The setpoint of the field
	V1 = (phi[:,0] - a) #(phi - a)**2
	V2 = -(phi[:,0] + a)
	V3 = (phi[:,1] - a) #(phi - a)**2
	V4 = -(phi[:,1] + a)
	V5 = 0
	return np.max(V1, V2, V3, V4, V5)


min (del phi**2 + V)
V > V1
V > V2
.. etc


It is a QP.

Because we do not penalize the hump in the middle, it may spend more time in there than necessary, vortices will tend to delocalize. But sharps corners tend to collect solutions. 

Using abs(del phi) it is an lp

nonlinear sigma model -> Quadratic constraint QP. if we relax the equality to inequality. It is a reasonable heurstic.

Nonlinear permittivty model -- applications to magnetic problems?


So there are options. What about Chern-Simons, Yang Mills? Do these have an interesting convex relaxation?
Navier Stokes?
Other nonlinear field theories?

XY model. The cuteness of the XY model lies in the MANY minima. That leads me to think there isn't much hope there. One could restrict to 0 to 2 pi. But the potential ias still almost maximally nonconvex. Ok. But again, relaxing the xy model to enclose the bulk of the circle rather than just the rim gives you the lndau-gnizburg equation with infinite walls. QCQP

Approxiation of electron specturm with abs. Useful in bosonization. Or the 2d wedge cone in the 2d extesions.

Quantization: Maybe this is useful. However quantum must consider ALL minima, not just the global minima, Hence the convex relaxation is taking the approximation that the other minima are dominated. Quantum is forall (exhaustive search, universal), classical is exists (existential, search).

H = (H0, V)