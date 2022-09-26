import pytest
from code.Sym import Sym
# from code.Num import Num
# from code.Data import Data
from code.Func import Func

funcObj = Func()

class TestCode:
    def __init__(self):
        self.fails = 0

    def runTests(self):

        eg = {
            # "BAD": TestBad().bad,
            "sym": TestSym().sym,
        }

        def runs(k):

            if k not in eg:
                return
            old = {}
            out = None
            for test in funcObj.the.keys():
                old[test] = funcObj.the[test]

            if funcObj.the['dump']:
                status = True
                out = eg[k]()
                
            else:
                status = False
                try:
                    out = eg[k]()
                    status = True
                except:
                    self.fails += 1

            for test, value in old.items():
                funcObj.the[test] = value
            
            msg = status and ((out == True and "PASS") or "FAIL") or "CRASH"
            print("!!!!!!", msg, k, status)
            return out or "Error"

        # print(funcObj.the["eg"])
        runs(funcObj.the["eg"])
        return self.fails

class TestSym:
    def sym(self):
        sym = Sym()
        for _, x in enumerate(["a","a","a","a","b","b","c"]):
            sym.add(x)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//1/1000
        funcObj.oo({"mid":mode, "div":entropy})
        return mode == "a" and 1.37 <= entropy <= 1.38

# def test_csv():
#     def row_function(row):
#         print(row)
#     csv("data/hw2-csv.csv",row_function)

# def test_data():
#     d = Data("data/hw2-csv.csv")
#     for _,i in d.cols.y.items():
#         print(i)


# def o(t, show=None, u=None):
# 	if not isinstance(t, dict):
# 		return str(t)
# 	def show(k, v):
# 		if not str(k).find("\0"):
# 			v = o(v)
# 			return len(t)==0 and (":"+k+" "+v) or str(v)
# 	u = {}
# 	for k, v in t.items():
# 		u[1+len(u)] = show(k,v)
# 	if len(t) == 0:
# 		u.sort()
# 	return u

# def test_stats():
#     data = Data("data/hw2-csv.csv")
#     def div(col): #Diversity
#         #Have to figure out how to diversity
#         return True
#     def mid(col): #Mid
#         #Have to figure out how to find median
#         return True
#     print("xmid",o(data.stats(2,data.cols.x,mid)))
#     print("xdiv",o(data.stats(2,data.cols.x,div)))
#     print("ymid",o(data.stats(3,data.cols.y,mid)))
#     print("ydiv",o(data.stats(3,data.cols.y,div)))

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