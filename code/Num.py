from cmath import inf
import math
from collections import OrderedDict

from attr import NOTHING

the = {}

def per(self, t=None, p=None):
	p = math.floor(((p if p else 0.5) * len(t)) + 0.5)
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
		if not (self.isSorted): 
			self._has = OrderedDict(sorted(self._has.items()))
			self.isSorted = True
		return self._has


	def add(self, v=None, pos = None):
		pass

	def mid(self, a=None):
		return per(self.nums,0.5)

	def div(self):
		a = self.nums
		return (per(a, 0.9)-per(a,0.1))/2.58

	