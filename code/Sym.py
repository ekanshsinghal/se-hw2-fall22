import math
class Sym:
	def __init__(self, c=None, s=None):
		self.n = 0
		self.at = c if c else 0
		self.name = s if s else ""
		self._has = {}

	def add(self, v=None):
		if v!="?":
			self.n = self.n+1
			if v in self._has:
				self._has[v] += 1
			else:
				self._has[v] = 1
		return self._has

	def mid(self, col=None, most=-1, mode=None):

		for k,v in self._has.items():
			if v>most:
				mode,most=k,v
		return mode

	def div(self, e=0):
		def fun(p):
			return p*math.log(p,2)
		for _,n in self._has.items():
			e -= fun(n/self.n)
		return e

