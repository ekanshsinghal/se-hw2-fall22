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
        sep = self.the["Seperator"]
        src = open(fname)
        reader = csv.reader(src, delimiter=sep)

        for n, row in enumerate(reader):
            x = []
            for col in row:
                x.append(self.funcObj.coerce(col))
            fun(x)

    def add(self, row):
        if not self.cols:
            self.cols = Cols(row, self.the)
        else:
            row = Row(row)
            self.rows.append(row)
            for _, todo in enumerate([self.cols.x, self.cols.y]):
                for _, col in enumerate(todo):
                    col.add(row.cells[col.at]) # Check col.at -1 or col.at
                

    def stats(self, places=3, showCols=None, fun=None, t=None, v=None):
        showCols = showCols or self.cols.x
        fun = fun or "mid"

        t = {}

        for col in showCols:
            v = fun(col)
            v =  self.rnd(v, places) if isinstance(v, float) else v
            t[col.name] = v

        return t

    def rnd(self, x, places=3):
        return round(x, places)
