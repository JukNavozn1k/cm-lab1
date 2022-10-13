import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos
def f(x): # функция
    return 3*x-cos(x)+0.1
def d1(x): # первая производная
    return sin(x) + 3
def d2(x): # вторая производная
    return cos(x)
def fi(x): # эквивалентная функция фи(х)
    return (cos(x)-0.1) / 3
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
    return x
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
   return x

#инициализация параметров
a,b = 0,0.9


# вывод интерфейса
print('Equation: 3*x-cos(x)+0,1=0')
print('Interval: [0;0,9]')
print('dy/dx: sin(x) + 3')
print('d^2y/dx^2: cos(x)')

# решение уравнения 2-мя способами
iterations_solution = iterations(a,b,0.00001)
combined_solution = combined(a,b,0.00001)

# вывод решений
print('Combined solution: ', combined_solution)
print('Iterations solution: ', iterations_solution)
# вывод округлённых решений
print('Rounded combined: ',round(combined_solution,4))
print('Rounded iterations: ',round(iterations_solution,4))



# график
x = np.arange(-10,10, 0.00001)

# отключаем


#subplot 4
sp = plt.subplot()
plt.plot(x, 3*x-np.cos(x)  + 0.1)
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')
plt.title(r'$f(x) =  3*x-cos(x)+0,1$')

plt.show()
