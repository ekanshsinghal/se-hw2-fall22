import pytest
from code.Sym import Sym, oo
from code.Num import Num, the

def test_Sym():
    sym = Sym()
    for _, x in enumerate(["a","a","a","a","b","b","c"]):
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000*entropy)//1/1000
    oo({"mid":mode, "div":entropy})
    assert mode == "a" and 1.37 <= entropy <= 1.38

# def test_Num():
# 	num = Num()
# 	for i in range(1, 101):
# 		num.add(i)
# 	mid, div = num.mid(), num.div()
# 	print(mid, div)
# 	assert 50 <= mid and min <= 51 and 30.5 < div and div < 32

# def test_bignum(num=None):
# 	num = Num()
# 	the["nums"] = 32

# 	for i in range(1,1000):
# 		num.add(i)
	
# 	oo(num.nums())

# 	assert 32 == len(num._has)

# def test_the():
#     oo(the) 
#     return True