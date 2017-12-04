print 
print "ESTE PROGRAMA EDINTIFICA DE UN NUMERO REAL EL SIGNO LA MAGNITUD Y LA FRACCION"
n = input("ingrese n = ")
if n > 0:
	signo = '+'
elif n == 0:
	signo = ''
else:
	signo = '-'
magnitud = float(abs(n))
entero = int(abs(magnitud))
fraccion = magnitud - entero
print
print "el signo es: ",signo," el entero es: ",entero," la fraccion es: ",fraccion