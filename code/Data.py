from code.Row import Row
from code.Cols import Cols
from code.Num import Num, the
# from code.Sym import the
import io
import math
import os

def push(t, x):
	t[1 + len(t)] = x
	return x

def rnd(x, places=3):
    mult = pow(10, places)
    return math.floor(x * mult + 0.5) / mult

class Data:
    def __init__(self, src):
        self.cols = None
        self.rows = []
        if isinstance(src, str):
            def add_rows(row):
                self.add(row)
            self.readCSV(src, add_rows) # Check row
        else:
            for row in src:
                self.add(row)

    def add(self, xs=None, row=None):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, xs.cells and xs or Row(xs))
            for _, todo in enumerate(self.cols.x + self.cols.y):
                for _, col in todo.items():
                    col.add(row.cells[col.at]) # Check what is col.at

    def stats(self, places=3, showCols=None, fun=None, t=None, v=None):
        showCols = showCols or self.cols.y
        fun = fun or "mid"

        t = {}

        for col in showCols:
            v = fun(col)
            v = isinstance(v, int) and rnd(v, places) or v
            t[col.name] = v

        return t

    def readCSV(fname, fun, sep=None, src=None, s=None, t=None):
        # sep = "([^" + the["Seperator"] + "]+)"
        sep = "([^" + "]+)"
        src = open(fname,"r")
        path = os.path.join(os.path.dirname(__file__), fname)
        columns = src.readline()
        while True:
            s = src.readline()
            if not s:
                src.close()
                break
            else:
                t = {}
                s_list=s.split(",")
                # for s1 in s_list:
                #     t[1+len(t)] = coerce(s1)
                fun(t)
