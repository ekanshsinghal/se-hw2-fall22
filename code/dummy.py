import copy

class Dummy:
    def __init__(self, t=None):
        self.cells = t
        self.cooked = copy.copy(t)
        self.isEvaled = False
        
    def dummy_add(self, a, b):
        return a+b
