from cmath import inf
from math import floor
from collections import OrderedDict
from random import random

the = {}

def per(t, p = None):
	p = floor(((p if p else 0.5) * len(t)) + 0.5)
	return t[max(1, min(len(t), p))]


class Num:
	def __init__(self, c=None, s=None):
		self.n = 0
		self.at = c if c else 0
		self.name = s if s else ""
		self._has = OrderedDict()
		self.lo=inf
		self.hi=-inf
		self.isSorted=True
		self.w= -1 if (s if s else '').endswith('-') else 1

	def nums(self):
		if not self.isSorted:
			self._has = OrderedDict(sorted(self._has.items()))
			self.isSorted = True
		return self._has


	def add(self, v = None, pos = None):
		if v != '?':
			self.n += 1
			self.lo = min(v, self.lo)
			self.hi = max(v, self.hi)
			if len(self._has) < the['nums']:
				pos = len(self._has)
			elif random() < (the['nums'] / self.n):
				pos = random(len(self._has))
			if pos:
				self.isSorted = False
				self._has[pos] = float(v)
	
	def mid(self):
		return per(self.nums(), 0.5)

	def div(self, a = None):
		a = self.nums()
		return (per(a, 0.9) - per(a, 0.1)) / 2.58


	def test_Num():
		pass

	test_Num()