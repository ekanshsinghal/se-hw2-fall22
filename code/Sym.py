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
			self._has[v] = 1 + ((self._has[v]) if v in self._has else 0)

	def mid(self, col=None, most=None, mode=None):
		most=-1
		for k,v in self._has.items():
			if v>most:
				mode,most=k,v
		return mode

	def div(self, e=None, fun=None):
		def fun(p):
			return p*math.log(p,2)
		e=0
		for _,n in self._has.items():
			if n>0:
				e=e-fun(n/self.n)
		return e

def o(t, show=None, u=None):
	if not isinstance(t, dict):
		return str(t)
	def show(k, v):
		if not str(k).find("\0"):
			v = o(v)
			return len(t)==0 and (":"+k+" "+v) or str(v)
	u = {}
	for k, v in t.items():
		u[1+len(u)] = show(k,v)
	if len(t) == 0:
		u.sort()
	return u

def oo(t):
	print(o(t))
	return t

def test_Sym():
	sym = Sym()
	for _, x in enumerate(["a","a","a","a","b","b","c"]):
		sym.add(x)
	mode, entropy = sym.mid(), sym.div()
	entropy = (1000*entropy)//1/1000
	oo({"mid":mode, "div":entropy})
	print(mode, entropy)

# test_Sym()
