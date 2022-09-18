from math import *
from telnetlib import theNULL


def localizateOne(f, df, a, b, pogr):
    intervals = [[a, f(a)], [b, f(b)]]
    if intervals[0][1] == 0:
        answer = a
    flag = False
    while intervals[0][0] > pogr / 8:
        for i in range(1, len(intervals)):
            if intervals[i][1] == 0:
                answer = 0
                Flag = True
                break
            elif intervals[i][1] * intervals[i - 1][1] < 0:
                intervals = intervals[i - 1] + intervals[i]
                Flag = True
                break
            else:
                newPoint = [intervals[i - 1][0] + intervals[i][0] / 2]
                newPoint.append(f(newPoint[0])) 
                intervals = intervals[:i] + newPoint + intervals[i:]
        if Flag == True:
            break
    else:
        return 'Корень не локализован'
    return [intervals[0][0], intervals[1][0]]

    
        
        

