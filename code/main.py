from code.Func import Func
from test.TestCode import TestCode
import os
import re
import sys

def main():
    b4 = {}
    _ENV = dict(os.environ)
    
    for k, v in _ENV.items():
        b4[k] = v
    funcObj = Func()
    nFail = TestCode().runTests()

    # funcObj.rouges(b4)
    print("# Failures", nFail)

if __name__ == "__main__":
    main()




