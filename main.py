from sympy import *
import numexpr as ne
def genFunc(s):
    def func(x):
       return ne.evaluate(s)
    return func
f = genFunc('cos(x)')
print(f(3))