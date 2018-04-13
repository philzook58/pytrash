

def unpack(x):
	return x[:nstate], u[nstate:nstate+ncontrols], lam[nstate+ncontrol:]

x = map(lambda _ : np.zeros(nstate+ncontrols+nlambda),range(lookaead))	


class Expr():
	def __mul__
	def __add__
	def __ampersand__
	def __sub__
	def __eq__
	def __lt__

class Add(Expr):
	def compile():
		A, b = compile(self.left)
		A2, b2 = compile(self.right)
		return A + A2, b2 + b

class Sub(Expr):
	def compile():
		A, b = compile(self.left)
		A2, b2 = compile(self.right)
		return A - A2, b - b2

class Eq():
	def compile():
		A, b = compile(self.left)
		A2, b2 = compile(self.right)
		return A - A2, b2 - b

class Const():
	def 

class Var():
	__init__(self, name, begin, end):
		self.begin = begin
		self.end = end
	def compile(self):
		return value? return lambda? return codestring? cps? lambda var : x[begin:end] = var return lambda cont: cont x 


class Matrix()




A @ x + B @ (y - y0) == c

Upper
Diag = map(lambda x :  , x)

Diag = []
Upper = []
Lower = []

b = []
Upper[0] = solve(Diag[0], Upper[0])
b[0] = solve(Diag[0], b[0])

for i in range(1,len(Diag)):	
	Diag[i] -= Lower[i]@Upper[i-1]
	b[i] -= Lower[i]@b[i-1]
	Upper[i] = solve(Diag[i], Upper[i])
	b[i] = solve(Diag[i], b[i])

#triangular solve
for i in range(len(Diag), 0, -1):	
	b[i] -= Upper[i]@b[i+1]


