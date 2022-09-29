# import copy

class Row:
    def __init__(self, t=None):
        self.cells = t
        self.cooked = self.copy(t)
        self.isEvaled = False

    def copy(self, t, u=None):
        if type(t) != 'dict':
            return t
        u = []    
        for k,v in t.items():
            u.append(self.copy[v])

        return u

