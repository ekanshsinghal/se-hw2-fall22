import math
import sys
import os
import re
from data.help import getHelp


class Func:
    def __init__(self):
        self.help = getHelp("help")
        tthe = self.createThe()
        self.the = self.cli(tthe)
        

    def createThe(self):
        matches = re.findall("\n [-][^\s]+[\s]+[-][-]([^\s]+)[^\n]+= ([^\s]+)", self.help)
        newthe = {}
        for match in matches:
            newthe[match[0]] = self.coerce(match[1])
        return newthe

    def coerce(self, s):
        def fun(s1):
            if s1.lower() == 'true':
                return True
            elif s1.lower() == 'false':
                return False
            return s1
        ss = s
        try:
            ss = float(s)
            # if ss == int(ss):
            #     ss = int(ss)
        except:
            ss = fun(re.search('^\s*(.+?)\s*$', s).group(1))
        # return int(ss) if float(ss) == int(ss) else fun(re.search('^\s*(.+?)\s*$', s))
        
        return ss

    def cli(self, t):
        args = sys.argv
        match = False
        for slot, v in t.items():
            v = str(v)
            for i in range(1, len(args)):
                if args[i] == '-' + slot[0] or args[i] == "--" + slot:
                    match = True           
                    v = v == "false" and "true" or v == "true" and "false" or args[i+1]
            t[slot] = self.coerce(v)
        
        if t["help"] or not match:
            print(self.help)

        return t

    def o(self, t, show=None, u=None):
        if not isinstance(t, dict):
            if not isinstance(t, list):
                return str(t)
        
        def show(k, v):
            if str(k).find('_') != 0:
                v = self.o(v)
                return isinstance(t, dict) and (":"+str(k)+" "+str(v)) or str(v)
        
        u = []
        if isinstance(t, dict):
            for k, v in t.items():
                showop = show(k,v)
                if showop:
                    u.append(showop) 
                u.sort()

        elif isinstance(t, list):
            u = t
        
        return "{" + " ".join(str(val) for val in u) + "}"

    def oo(self, t):
        print(self.o(t))
        return t

    # def rogues(self, b4):
    #     envs = dict(os.environ)
    #     for key, val in envs.items():
    #         if not b4[key]:
    #             print('?', key, type(val))

    

    


    # def push(t, x):
    #     t[1 + len(t)] = x
    #     return x

    # def rnd(x, places=3):
    #     mult = pow(10, places)
    #     return math.floor(x * mult + 0.5) / mult

    # def copy(self, t, u=None):
    #     if type(t) != 'dict':
    #         return t
    #     u = {}    
    #     for k,v in t.items():
    #         u[k] = copy[v]
        
    #     return u