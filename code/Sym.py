class Sym:
	def __init__(self, c, s):
		self.n = 0
		self.at = c if c else 0
		self.name = s if s else ""
		self._has = {}

	def add(self, v):
		if v!="?":
			self.n = self.n+1
			self._has[v] = 1 + ((self._has[v]) if self._has[v] else 0)

	def mid(self):
		pass

	def div(self):
		pass