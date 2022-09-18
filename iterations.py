def function(x):
    return (x-3)**2
def fi(x):
    return (-9-(x**2))/-6
def iterations(e,imax,x0,x1): # e окрестность,imax наибольшее количество итераций x0 начало отрезка x1 конец отрезка
    
    i = 0
    x = fi(x0)
    while True:
        print('Iteration ',i)
        i = i + 1   
        x0 = x
        x = fi(x)
        if ((abs(x-x0) < e) and (i > imax)) or x0 > x1:
            break
    print('root ',x)
    print('iterations ',i)
iterations(0.0001,10000,0,3)
    