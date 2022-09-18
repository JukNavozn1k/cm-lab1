def f(x): # функция
    return (x-5)**2
def d1(x): # первая производная
    return 2*x -10 
def d2(x): # вторая производная
    return 2
def combined(a,b,e): # комбинированный метод решения нелинейных уравнений
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
combined(0,10,0.01)


    