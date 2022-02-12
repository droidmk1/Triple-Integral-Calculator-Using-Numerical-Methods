import matplotlib.pyplot as plt
from sympy import Symbol, sympify, pi, evalf

# Vectores para las graficas
angulo = []
angulo1 = []
angulo2 = []

tiempo = []

velocidad = []
velocidad1 = []
velocidad2 = []

# Variables
t = Symbol('t')
z = Symbol('z')
y = Symbol('y')

# Funciones
f = sympify('y')
g = sympify('-(9.81/0.5)*z')

# Valor de Variables
z0 = [pi/8, pi/4, pi/2]

# Derivada
y0 = 0

# Variable comodin
k = y0

# Intevarlo de t
a = 0
b = 5

# n iteraciones y calculo de h
n = 100
h = (b-a)/n

j = 0
print(f'Runge Kutta con h: {h} y con interaciones #n: {n}')
print(f'f = {f}; g = {g}')
print('\nValores iniciales: ')
print(f'Tiempo: {a:.1f}	Angulos: {z0}	Velocidad: {y0}')
for j in range(0,3):
	y0 = k
	print(f'\nCalculo para el angulo: {z0[j]}')
	print('#iter	tiempo	angulo		velocidad')
	print(f'{0}	{a:.1f}	{z0[j].evalf():.6f}	{y0:.6f}')
	for i in range(0, n):
		t0 = a + h*i

		# Para K1 y L1
		K1 = h*f.subs([(t, t0), (z, z0[j]), (y, y0)])
		L1 = h*g.subs([(t, t0), (z, z0[j]), (y, y0)])

		# Para K2 y L2
		K2 = h*f.subs([(t, t0 + h/2), (z, z0[j] + K1/2), (y, y0 + L1/2)])
		L2 = h*g.subs([(t, t0 + h/2), (z, z0[j] + K1/2), (y, y0 + L1/2)])

		# Para K3 y L3
		K3 = h*f.subs([(t, t0 + h/2), (z, z0[j] + K2/2), (y, y0 + L2/2)])
		L3 = h*g.subs([(t, t0 + h/2), (z, z0[j] + K2/2), (y, y0 + L2/2)])

		# Para K4 y L4
		K4 = h*f.subs([(t, t0 + h), (z, z0[j] + K3), (y, y0 + L3)])
		L4 = h*g.subs([(t, t0 + h), (z, z0[j] + K3), (y, y0 + L3)])

		# Hallamos y(t+1) y z(t+1)
		z1 = z0[j] + (K1 + 2*K2 + 2*K3 + K4)/6
		y1 = y0 + (L1 + 2*L2 + 2*L3 + L4)/6

		# Evaluacion adicional para pi
		z1 = z1.evalf()
		y1 = y1.evalf()

		if j == 0:
			angulo.append(z1)
			velocidad.append(y1)
			tiempo.append(t0)
		elif j == 1:
			angulo1.append(z1)
			velocidad1.append(y1)
		else:
			angulo2.append(z1)
			velocidad2.append(y1)

		# Imprimir valores
		'''Descomentar el print si se desean ver todos las aproximaciones'''
		print(f'{i+1}	{(t0+h):.1f}	{z1:.6f}	{y1:.6f}')

		# Valores iniciales reiniciados
		y0 = y1
		z0[j] = z1
	# Imprimir aproximaciones finales para el angulo dado
	print(f'\nValores aproximados: ')
	print(f'{i+1}	{(t0+h):.1f}	{z1:.6f}	{y1:.6f}')

#Plot de graficas
fig, ax = plt.subplots()
ax.plot(tiempo, angulo1, 'g')
ax.plot(tiempo, angulo2, 'r')
ax.plot(tiempo, angulo, 'b')
ax.legend([f'Theta: {pi/8}', f'Theta: {pi/4}',f'Theta: {pi/2}'])
ax.axis([0,5,-2,2])
ax.set_xlabel('Tiempo')
ax.set_ylabel('Angulo')
ax.grid(True)
plt.show()

fig, ax1 = plt.subplots()
ax1.plot(tiempo, velocidad, 'b')
ax1.plot(tiempo, velocidad1, 'g')
ax1.plot(tiempo, velocidad2, 'r')
ax1.legend([f'Theta: {pi/8}', f'Theta: {pi/4}',f'Theta: {pi/2}'])
# ax.axis([0,5,-7,7])
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Velocidad')
ax1.grid(True)
plt.show()

'''
UNMSM 2022
Alumno: Alvaro Farfan Vera
Codigo: 19140106
'''