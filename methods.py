def f(x): # функция
    return (x-5)**2
def d1(x): # первая производная
    return 2*x -10 
def d2(x): # вторая производная
    return 2
def fi(x): # эквивалентная функция фи(х)
    return (-25-(x**2))/-10
# метод простых итераций для решения нелинейных уравнений
def iterations(x0,x1,e,imax=1000): # e окрестность,imax наибольшее количество итераций x0 начало отрезка x1 конец отрезка
    
    i = 0
    x = fi(x0)
    while True:
        i = i + 1   
        x0 = x
        x = fi(x)
        if ((abs(x-x0) < e) and (i > imax)) or x0 > x1:
            break
    print('root ',x)
# комбинированный метод решения нелинейных уравнений
def combined(a,b,e):  # a начало, b конец,e окрестность
   while True:
    if f(a) * d2(a) < 0:
        a = a - (f(a)*(a-b))/(f(a)-f(b))
    else:
        a = a - f(a)/d1(a)
    if f(b) * d2(b) < 0:
        b = b - (f(b)*(b-a))/(f(b)-f(a))
    else:
        b = b - f(b)/d1(b)
    if abs(a-b) <= 2*e:
        break
    x = (a+b)/2
   print('root ',x)
iterations(0,10,0.000001)
