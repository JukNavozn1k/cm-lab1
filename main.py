import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos
from tabulate import tabulate
from matplotlib import ticker


def f(x): # функция
    return 3*x-cos(x)+0.1
def d1(x): # первая производная
    return sin(x) + 3
def d2(x): # вторая производная
    return cos(x)
def fi(x): # эквивалентная функция фи(х)
    return (cos(x)-0.1) / 3
# метод простых итераций для решения нелинейных уравнений
def iterations(x0,x1,e,imax=100): # e окрестность,imax наибольшее количество итераций x0 начало отрезка x1 конец отрезка
    i = 0
    x = fi(x0)
    print('=====================================')
    print('Iterations method')
    print('function =  3*x-cos(x)+0,1=0')
    print('fi = (cos(x)-0.1) / 3')
    print('d/dx fi(x) = -sin(x) / 3   d/dx fi(a) =  ',-sin(x0+ 10**-10) / 3, '  d/dx fi(b) =  ', -sin(x1) / 3)
    print('Вывод двухсторонняя сход')
    col_names = ["Iteration", "x","fi(x)","delta"]
    data = []
    while True:

        i = i + 1
        x0 = x
        x = fi(x)
        if ((abs(x-x0) < e) or (i > imax)) or x0 > x1:
            break
        data.append([i,x0,x,(abs(x-x0))])
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid",stralign='center'))
    print('Iterations solution:', x)
# комбинированный метод решения нелинейных уравнений
def combined(a,b,e):  # a начало, b конец,e окрестность
   print('=====================================')
   print('Combined Method')
   print('f(x) = 3*x-cos(x)+0,1')
   print('dy/dx: sin(x) + 3')
   print('d^2y/dx^2: cos(x)')
   print('f(a) = {} f(b) = {} f`(a) = {} f`(b) = {} f``(a) = {} f``(b) = {}'.format(f(a),f(b),d1(a),d1(b),d2(a),d2(b)))
   print('По недостатку - хорды по избытку касательные')
   col_names = ["Iteration", "!xn ", "f(!xn)","xn","f(xn)","delta"]
   data = []
   i = 0
   xa,xb = a,b
   while True:
    if i == 0: data.append([i,xa,f(xa),xb,f(xb),abs(xa-xb)])
    i = i + 1
    if f(a) * d2(a) < 0:
        a = a - (f(a)*(a-b))/(f(a)-f(b))
        xa = a
    else:
        a = a - f(a)/d1(a)
        xa = a
    if f(b) * d2(b) < 0:
        b = b - (f(b)*(b-a))/(f(b)-f(a))
        xb = b
    else:
        b = b - f(b)/d1(b)
        xb = b
    x = (a + b) / 2
    data.append([i, xa, f(xa), xb, f(xb), abs(a - b)])
    if abs(a-b) <= e:
        break


   print(tabulate(data, headers=col_names, tablefmt="fancy_grid", stralign='center'))
   print('Combined solution: ', x)


#инициализация параметров
a,b = 0,0.9

# вывод интерфейса
print('Equation: 3*x-cos(x)+0,1=0')
print('Interval: [0;0,9]')
print('dy/dx: sin(x) + 3')
print('d^2y/dx^2: cos(x)')

# решение уравнения 2-мя способами
iterations(a,b,0.00001)
combined(a,b,0.000001)

# график
x = np.arange(-10,10, 0.01)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(x,3*x-np.cos(x)+0.1,label='f(x) = 3x-cos(x) + 0.1')


#  Устанавливаем интервал основных и
#  вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))


#  Добавляем линии основной сетки:
ax.grid(which='major',
        color = 'k')

#  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#  Теперь можем отдельно задавать внешний вид
#  вспомогательной сетки:
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figwidth(12)
fig.set_figheight(8)
plt.title('f(X) = 3*x - cos(x) + 0.1')
plt.show()

