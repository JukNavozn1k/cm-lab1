from sympy import *
import numexpr as ne

def genFunc(s):
    def func(x):
       return ne.evaluate(s)
    return func

def genFiSTR(equation):
    good = True
    newEquation = ''
    for i in equation:
        if i == 'x' and good:
            newEquation += 'y'
            good  = False
        else:
            newEquation += i
    return str(solve(newEquation,'x')[0]).replace('y','x') 
