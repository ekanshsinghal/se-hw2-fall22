import math
class Sym:
	def __init__(self, c=None, s=None):
		self.n = 0
		self.at = c if c else 0
		self.name = s if s else ""
		self._has = {}

	def add(self, v):
		if v!="?":
			self.n = self.n+1
			self._has[v] = 1 + ((self._has[v]) if v in self._has else 0)

	def mid(self, col, most, mode):
		most=-1
		for k,v in enumerate(self._has):
			if v>most:
				mode,most=k+1,v
		return mode

	def div(self, e, fun):
		def fun(p):
			return p*math.log(p,2)
		e=0
		for _,n in enumerate(self._has):
			if n>0:
				e=e-fun(n/self.n)
		return e