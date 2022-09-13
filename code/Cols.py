import re

import code.Num as Num
import code.Sym as Sym


def push(t, x):
	t[1 + len(t)] = x
	return x

class Cols:
	def __init__(self, names) -> None:
		self.names = names
		self.all = []
		self.klass = None
		self.x = {}
		self.y = {}
		regex = re.compile(r'^[A-Z]*')
		for c, s in enumerate(names):
			if regex.match(s):
				col = push(self.all, Num(c,s))
			else:
				col = push(self.all, Sym(c,s))
			if not s.endswith(':'):
				string = 'sca'
				if '!' in s or '+' in s or '-' in s:
					push(self.y, col)
				else:
					push(self.x, col)
				if s.endswith('!'):
					self.klass = col