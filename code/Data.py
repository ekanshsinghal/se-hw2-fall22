from code.Row import Row
from code.Cols import Cols
from code.Num import Num
from code.Row import Row
import io
import math
import os
import csv



class Data:
    def __init__(self, funcObj, src):
        self.cols = None
        self.rows = []
        self.funcObj = funcObj
        self.the = funcObj.the
        
        if isinstance(src, str):
            self.readCSV(src, self.add)
            
        else:
            for row in src:
                self.add(row)

    def readCSV(self, fname, fun, sep=None, src=None, s=None, t=None):
        # sep = "([^" + the["Seperator"] + "]+)"
        
        sep = self.the["Seperator"]
        # src = open(fname,"r")
        # path = os.path.join(os.path.dirname(__file__), fname)

        src = open(fname)
        reader = csv.reader(src, delimiter=sep)

        for n, row in enumerate(reader):
            x = []
            for col in row:
                x.append(self.funcObj.coerce(col))
            fun({n+1: x})

        # while True:
        #     s = src.readline()
        #     if not s:
        #         src.close()
        #         break
        #     else:
        #         t = {}
        #         s_list=s.split(",")
        #         # for s1 in s_list:
        #         #     t[1+len(t)] = coerce(s1)
        #         fun(t)

    def add(self, xs):
        if not self.cols:
            self.cols = Cols(list(xs.values())[0], self.the)
        else:
            row = Row(xs)
            self.rows.append(row)
            for todo in [self.cols.x + self.cols.y]:
                for col in todo:
                    col.add(list(row.cells.values())[0][col.at-1]) # Check col.at -1 or col.at

    def stats(self, places=3, showCols=None, fun=None, t=None, v=None):
        showCols = showCols or self.cols.y
        fun = fun or "mid"

        t = {}

        for col in showCols:
            v = fun(col)
            v =  self.rnd(v, places) if isinstance(v, float) else v
            t[col.name] = v

        return t

    def rnd(self, x, places=3):
        return round(x, places)
