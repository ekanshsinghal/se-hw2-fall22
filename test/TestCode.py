import pytest
from code.Sym import Sym
from code.Num import Num
from code.Data import Data
from code.Func import Func
import os

funcObj = Func()

class TestCode:
    def __init__(self):
        self.fails = 0

    def runTests(self):

        eg = {
            "bad": TestBad().bad,
            "sym": TestSym().sym,
            "all": TestAll().all,
            "num": TestNum().num,
            "bignum": TestBigNum().bignum,
            "the": TestThe().the,
            "data": TestData().data,
            "stats": TestStats().stats
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
                out = eg[k](eg, runs, self.fails)
                
            else:
                status = False
                if 1:
                    out = eg[k](eg, runs, self.fails)
                    status = True
                # except Exception as ex:
                    # print(ex)
                else:
                    self.fails += 1

            for test, value in old.items():
                funcObj.the[test] = value
            
            msg = status and ((out == True and "PASS") or "FAIL") or "CRASH"
            print("!!!!!!", msg, k, status)
            return out or "Error"

        # print(funcObj.the["eg"])
        runs(funcObj.the["eg"])
        return self.fails

class TestBad:
    def bad(self, eg, runs, fails):
        print("Invalid field")
        return True

class TestSym:
    def sym(self, eg, runs, fails):
        sym = Sym()
        for _, x in enumerate(["a","a","a","a","b","b","c"]):
            sym.add(x)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//1/1000
        funcObj.oo({"mid":mode, "div":entropy})
        return mode == "a" and 1.37 <= entropy <= 1.38

class TestAll:
    def all(self, eg, runs, fails):
        testNames = list(eg.keys())
        for test in testNames:
            if test == 'all':
                continue
            if not runs(test):
                fails += 1
        return True 

class TestNum:
    def num(self, eg, runs, fails):
        num = Num(funcObj.the)
        for i in range(1, 101):
            num.add(i)
        mid, div = num.mid(), num.div()
        return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

class TestBigNum:
    def bignum(self, eg, runs, fails):
        num = Num(funcObj.the)
        funcObj.the["nums"] = 32
        for i in range(1,1001):
            num.add(i)
        funcObj.oo(num.nums())
        return 32 == len(num._has)

class TestThe:
    def the(self, eg, runs, fails):
        funcObj.oo(funcObj.the) 
        return True

class TestData:
    def data(self, eg, runs, fails):
        d = Data(funcObj, "data/hw2-csv.csv")
        for i in d.cols.y:
            funcObj.oo(vars(i))
        return True

class TestStats:
    def stats(self, eg, runs, fails):
        data = Data(funcObj, "data/hw2-csv.csv")
        def div(col): #Diversity
            #Have to figure out how to diversity
            return col.div()
        def mid(col): #Mid
            #Have to figure out how to find median
            return col.mid()
        print("xmid",funcObj.o(data.stats(2,data.cols.x,mid)))
        print("xdiv",funcObj.o(data.stats(2,data.cols.x,div)))
        print("ymid",funcObj.o(data.stats(3,data.cols.y,mid)))
        print("ydiv",funcObj.o(data.stats(3,data.cols.y,div)))
        return True

# class TestCSV:
#     def test_csv(self):
#         def row_function(row):
#             print(row)
#         self.csv("data/hw2-csv.csv",row_function)





