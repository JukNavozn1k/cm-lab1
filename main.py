from math import *
from telnetlib import theNULL


def localizateOne(f, df, a, b, pogr):
    pointsXY = [[a, f(a)], [b, f(b)]]
    if pointsXY[0][1] == 0:
        return [a, a]
    numberOfPoints = 2
    while pointsXY[0][0] > pogr / 8:
        i = 1
        while i < numberOfPoints:
            if pointsXY[i][1] == 0: # Проверка, вдруг новая точка является корнем
                return [pointsXY[i][0], pointsXY[i][0]]
            elif pointsXY[i][1] * pointsXY[i - 1][1] < 0: # Проверка, есть ли в интервале нечётное число корней
                pointsXY = pointsXY[i - 1] + pointsXY[i] # если да, то удаляем остальные интервалы
                numberOfPoints = 2
                break
                if df(pointsXY[0][0]) * df(pointsXY[1][0]) > 0: # Мож, >=?    ???
                    return [pointsXY[0][0], pointsXY[1][0]] # возвращает в виде списка интервал с корнем
            else: # дальше дробим интервалы
                newPoint = [pointsXY[i - 1][0] + pointsXY[i][0] / 2]
                newPoint.append(f(newPoint[0])) 
                pointsXY = pointsXY[:i] + newPoint + pointsXY[i:]
                numberOfPoints += 1
                i += 2
    else:
        return 'Корень не локализован'
    return [pointsXY[0][0], pointsXY[1][0]] # возвращает в виде списка интервал с корнем 

    
        
        

