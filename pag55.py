print 
print "ESTE PPROGRAMA ES PARA DETERMINAR LA RAIZ APLICANDO EL ALGORITMO DE NEWTON"
n = input("ingrese valor de n = ")
x1 = 1

while True:
	x = x1
	x1 = 0.5*(x+(n/x))
	if abs(x-x1) <= 0.001:
		break
print "la interseccion es ",x1