class Row:
    def __init__(self, t=None):
        self.cells = t
        self.cooked = self.copy(t)
        isEvaled = False

    def copy(self, t, u=None):
        if type(t) != 'dict':
            return t
        u = {}    
        for k,v in t:
            u[k] = self.copy[v]

