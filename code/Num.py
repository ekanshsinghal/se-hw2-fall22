from cmath import inf
import math
from math import floor
from collections import OrderedDict
from random import random
import re
import sys

class Num:
	def __init__(self, the, c=0, s=""):
		self.n = 0
		self.at = c+1
		self.name = s
		self._has = {}
		self.lo=inf
		self.hi=-inf
		self.isSorted=True
		self.the = the
		self.w= -1 if re.find('-$', s) else 1

	def nums(self):
		if not self.isSorted:
			self._has.sort()
			self.isSorted = True
		return self._has

	def add(self, v = None, pos = -1):
		if float(v) != '?':
			self.n = self.n + 1
			self.lo = min(float(v), self.lo)
			self.hi = max(float(v), self.hi)
			if len(self._has) < self.the['nums']:
				pos = len(self._has) + 1
			elif random() < (self.the['nums'] / self.n):
				pos = random.randint(1, len(self._has))
			if pos != -1:
				self.isSorted = False
				self._has[pos] = int(v)
	
	
	def per(self, t, p = None):
		p = math.floor(((p if p else 0.5) * len(t)) + 0.5)
		return t[max(1, min(len(t), p)) - 1]

	def mid(self):
		return self.per(self.nums(), 0.5)

	def div(self, a = None):
		a = self.nums()
		return (self.per(a, 0.9) - self.per(a, 0.1)) / 2.58

