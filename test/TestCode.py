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
            "all": self.all,
            "list": self.list,
            "ls": self.ls,
            "sym": self.sym,
            "num": self.num,
            "bignum": self.bignum,
            "the": self.the,
            "data": self.data,
            "bad": self.bad,
            "stats": self.stats,
            "csv": self.csv
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
                try:
                    out = eg[k](eg, runs, self.fails)
                    status = True
                except Exception as ex:
                    print(ex)
                    self.fails += 1

            for test, value in old.items():
                funcObj.the[test] = value
            
            msg = status and ((out == True and "PASS") or "FAIL") or "CRASH"
            print("!!!!!!", msg, k, status)
            return out or "Error"

        # print(funcObj.the["eg"])
        runs(funcObj.the["eg"])
        return self.fails

    def bad(self, eg, runs, fails):
        print("Invalid field")

    def sym(self, eg, runs, fails):
        sym = Sym()
        for _, x in enumerate(["a","a","a","a","b","b","c"]):
            sym.add(x)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//1/1000
        funcObj.oo({"mid":mode, "div":entropy})
        return mode == "a" and 1.37 <= entropy <= 1.38

    def all(self, eg, runs, fails):
        testNames = list(eg.keys())
        # for test in testNames:
        for test in self.list(eg, runs, fails):
            if test != 'all':
                print("\n------------------------------------------------")
                if not runs(test):
                    fails += 1
        return True 

    def num(self, eg, runs, fails):
        num = Num(funcObj.the)
        for i in range(1, 101):
            num.add(i)
        mid, div = num.mid(), num.div()
        return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

    def bignum(self, eg, runs, fails):
        num = Num(funcObj.the)
        funcObj.the["nums"] = 32
        for i in range(1,1001):
            num.add(i)
        funcObj.oo(num.nums())
        return 32 == len(num._has)

    def the(self, eg, runs, fails):
        funcObj.oo(funcObj.the) 
        return True

    def data(self, eg, runs, fails):
        d = Data(funcObj, "data/hw2-csv.csv")
        for i in d.cols.y:
            funcObj.oo(vars(i))
        return True

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

    def csv(self, eg, runs, fails):
        self.n = 0
        data = Data(funcObj, [])
        data.readCSV("data/hw2-csv.csv", self.fun)
        return True

    def fun(self, row):
        self.n = self.n + 1
        if self.n > 10:
            return self.n
        else:
            return funcObj.oo(row)


    def list(self, eg, runs, fails):
        t = []
        for key in eg.keys():
            t.append(key)
        t.sort()
        # print(len(t))
        return t

    def ls(self, eg, runs, fails):

        print("\nExamples: \npython -m code.main -e <test_name>\n")
        print("List of available test names : ")
        for test in self.list(eg, runs, fails):
            print("\t", test)
        return True
