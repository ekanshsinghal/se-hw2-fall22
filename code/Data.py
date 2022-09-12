import Row
import Cols
from Sym import the
import io

class Data:
    def __init__(self, src=None):
        self.cols = None
        self.rows = {}
        if isinstance(src, "str"):
            csv(src, self.add(row)) # Check csv
        else:
            for _, row in src.items():
                self.add(row)

    def add(self, xs=None, row=None):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = self.rows.append(xs.cells and xs or Row(xs))
            for _, todo in enumerate([self.cols.x, self.cols.y]):
                for _, col in todo.items():
                    col.add(row.cells[col]) # Check what is col.at

    def stats(self, places, showCols, fun, t, v):
        showCols = showCols or self.cols.y
        fun = fun or "mid"

        t = {}

        for _, col in showCols.items():
            v = fun(col)
            v = isinstance(v, "int") and round(v, places) or v
            t[col.name] = v

        return t