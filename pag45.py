print 
print "ESTE PROGRAMA SACA EL MAXIMO COMUN DIVISOR DE DOS NUMEROS"
a = input("ingrese a = ")
b = input("ingrese b = ")
while a != b:
	if a>b:
		a = a - b
	else:
		b = b -a
print "el MCD es ",b