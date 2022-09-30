import re
from code.Num import Num
from code.Sym import Sym

class Cols:
	def __init__(self, names, the) -> None:
		self.names = names
		self.all = []
		self.klass = None
		self.x = []
		self.y = []
		for c, s in enumerate(names):
			if type(s) == str and s[0].isupper():
				self.all.append(Num(the, c, s))
			else:
				self.all.append(Sym(c, s))
			
			if type(s) == str and s[-1] != ':':
				if '+' in s or '-' in s:
					self.y.append(self.all[c])
				else:
					self.x.append(self.all[c])
				if s[-1] == '!':
					self.klass = self.all[c]
