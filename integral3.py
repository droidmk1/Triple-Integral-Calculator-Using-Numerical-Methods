import numpy as np #para el calculo en arrays
from sympy import * #para variables
import math #funciones trigo y valor de pi

# creacion de simbolos
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# funcion
fun = (x*cos(y)*x*sin(y)*cos(z) + (x*sin(y)*sin(z))**2)*(x**2)*abs(sin(y))

# extremo1
b1 = 1
a1 = 0

# extremo2
b2 = (math.pi)/2
a2 = 0

#extremo3
b3 = (math.pi)/2
a3 = (math.pi)/4

n = 10 # cantidad de puntos

# SIMPSON COMPUESTO
def f(x):
    f = fun.subs('x',x)
    return f

# extremos de integracion
b = b1
a = a1

h = (b-a)/(n) # calculamos la separacion
x = [None]*(n+1) # creacion de lista para x_i

# datos iniciales de lista para x_i
x[0] = a
x[-1] = b

# calculo de los x_i
for i in range(1,n): 
    x[i] = (a + h*i)

y1 = [None]*(n+1) # creacion de lista para f(x_i)

# calculo de los y_i
for i in range(0,n+1): 
    y1[i] = f(x[i])

y1 = np.array(y1) # conversion a un array

I1 = (h/3)*(y1[0] + 2*np.sum(y1[2:n:2]) + 4*np.sum(y1[1:n:2]) + y1[-1])
I1 = I1.evalf() # evaluacion extra antes de imprimir

print('1. APROX: ')
print(I1)

# cambio de variables
I1 = I1.subs('y','x')
I1 = I1.subs('z','y')

# TRAPECIO COMPUESTO
def f1(x):
    f = I1.subs('x',x)
    return f

# extremos de integracion
b = b2
a = a2

h = (b-a)/(n) # calculamos la separacion
x = [None]*(n+1) # creacion de lista para x_i

# datos iniciales de lista para x_i
x[0] = a
x[-1] = b

# calculo de los x_i
for i in range(1, n): 
    x[i] = (x[0] + h*i)

y2 = [None]*(n+1) # creacion de lista para f(x_i)

# calculo de los y_i
for i in range(0, n+1):
    y2[i] = f1(x[i])

y2 = np.array(y2) # conversion a un array

I2 = (h/2)*(y2[0] + 2*np.sum(y2[1:n]) + y2[-1])

I2 = I2.evalf() # evaluacion extra antes de imprimir

print('2. APROX: ')
print(I2)

# cambio de variables
I2 = I2.subs('y','x')
I2 = I2.subs('z','y')

# SIMPSON COMPUESTA
def f2(x):
    f = I2.subs('x',x)
    return f

# extremos de integracion
b = b3
a = a3

h = (b-a)/(n) # calculamos la separacion
x = [None]*(n+1) # creacion de lista para x_i

# datos iniciales de lista para x_i
x[0] = a
x[-1] = b

# calculo de los x_i
for i in range(1,n): 
    x[i] = (a + h*i)

y3 = [None]*(n+1) # creacion de lista para f(x_i)

# calculo de los y_i
for i in range(0,n+1): 
    y3[i] = f2(x[i])

y3 = np.array(y3) # conversion a un array

I3 = (h/3)*(y3[0] + 2*np.sum(y3[2:n:2]) + 4*np.sum(y3[1:n:2]) + y3[-1])

I3 = I3.evalf() # evaluacion extra antes de imprimir

print('3. APROX: ')
print(I3)