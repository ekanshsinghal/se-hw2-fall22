import copy

class Row:
    def __init__(self, t=None):
        self.cells = t
        self.cooked = copy.copy(t)
        self.isEvaled = False
