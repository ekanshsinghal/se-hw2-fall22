from cmath import inf
from math import floor
from collections import OrderedDict
from random import random

# from Sym import o, oo

the = {}

def per(t, p = None):
	p = floor(((p if p else 0.5) * len(t)) + 0.5)
	return t[max(1, min(len(t), p))]

# def cli(the):
# 	for key, val in the.items():
# 		val = str(val)
# 		for n, x in 


class Num:
	def __init__(self, c=None, s=None):
		self.n = 0
		self.at = c if c else 0
		self.name = s if s else ""
		self._has = []
		self.lo=inf
		self.hi=-inf
		self.isSorted=True
		s=s if s else ''
		self.w= -1 if s.endswith('-') else 1

	def nums(self):
		if not self.isSorted:
			self._has.sort()
			self.isSorted = True
		return self._has

	def add(self, v = None, pos = None):
		if v != '?':
			self.n = self.n + 1
			self.lo = min(v, self.lo)
			self.hi = max(v, self.hi)
			if len(self._has) < the['nums']:
				pos = len(self._has) + 1 # Check + 1
			elif random() < (the['nums'] / self.n):
				pos = random(len(self._has))
			if pos:
				self.isSorted = False
				self._has[pos] = int(v)
	
	def mid(self):
		return per(self.nums(), 0.5)

	def div(self, a = None):
		a = self.nums()
		return (per(a, 0.9) - per(a, 0.1)) / 2.58

def cli(t):
	for slot, v in t.items():
		v = str(v)
		# Implement other modules to finish this.

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

# def test_Num():
# 	num = Num()
# 	for i in range(1, 101):
# 		num.add(i)
# 	mid, div = num.mid(), num.div()
# 	print(mid, div)
# 	return 50 <= mid and min <= 51 and 30.5 < div and div < 32

# def test_bignum(num=None):
# 	num = Num()
# 	the["nums"] = 32

# 	for i in range(1,1000):
# 		num.add(i)
	
# 	# Implement oo(num.nums())

# 	return 32 == len(num._has)

# def test_the():
# 	return oo(the)

# test_bignum()
# test_Num()
# test_the()
