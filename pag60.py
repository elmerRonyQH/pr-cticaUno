print
print "ESTE PROGRAMA CALCULA EL SALARIO DE LOS N EMPLEADOS "
total = 0
contador = 0
numero = input("ingrese el numero de empleados: ")
while contador < numero:
	horas = input("ingrese horas: ")
	salario = input("ingrese salario: ")
	pago = horas * salario
	total = total + pago
	contador = contador + 1
	print "el pago es: ",pago
print "el total es: ",total

