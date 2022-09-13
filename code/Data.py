import code.Row as Row
import code.Cols
# from code.Sym import the
import io

class Data:
    def __init__(self, src):
        self.cols = None
        self.rows = {}
        if isinstance(src, str):
            def add_rows(row):
                self.add(row)
            csv(src, add_rows) # Check row
        else:
            for _, row in src.items():
                self.add(row)

    def add(self, xs=None, row=None):
        if not self.cols:
            self.cols = code.Cols.Cols(xs)
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
            v = isinstance(v, int) and round(v, places) or v
            t[col.name] = v

        return t

def coerce(s):
    def fun(s1):
        if s1 == "true":
            return True
        elif s1 == "false":
            return False
        return s1
    try:
        return int(s)
    except:
        try:
            return float(s)
        except:
            return fun(s.find("^%s*(.−)%s*$"))
    # return int(s) or float(s) or fun(s.find("^%s*(.−)%s*$"))

def csv(fname, fun, sep=None):
    # if sep:
    #     sep = "([^" + the[sep] + "]+)"
    # else:
    #     sep = "([^,]+)"
    src = open(fname,"r")
    columns = src.readline()
    while True:
        s = src.readline()
        if not s:
            src.close()
            break
        else:
            t = {}
            s_list=s.split(",")
            for s1 in s_list:
                t[1+len(t)] = coerce(s1)
            fun(t)
