class GExpr():
	def __mul__
	def __add__
	def __ampersand__
	def __sub__
	def __eq__
	def __lt__

class GAdd(Expr):
	def compile():
		A, b = compile(self.left)
		A2, b2 = compile(self.right)
		return A + A2, b2 + b

class GSub(Expr):
	def compile():
		A, b = compile(self.left)
		A2, b2 = compile(self.right)
		return A - A2, b - b2

class GEq():
	def compile():
		A, b = compile(self.left)
		A2, b2 = compile(self.right)
		return A - A2, b2 - b

class GConst():
	def 

class GVar(): #Maybe we want it to find it's own placement?
	__init__(self, name, begin, end):
		self.begin = begin
		self.end = end
	def compile(self):
		return value? return lambda? return codestring? cps? lambda var : x[begin:end] = var return lambda cont: cont x 


class GMatrix()


'''

Quadratic Expressions
-- uses symmettric methods.

xQx + b x + c

Linear expressions
A @ x + B @ (y - y0) == c


'''