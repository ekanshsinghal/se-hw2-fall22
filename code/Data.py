import Row
import Cols

class Data:
    def __init__(self, src=None):
        self.cols = None
        self.rows = {}
        if isinstance(src, "str"):
            csv(src, self.add(row)) # Check csv
        else:
            for _, row in src.items():
                self.add(row)

