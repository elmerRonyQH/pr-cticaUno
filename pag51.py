print 
print "ESTE PPROGRAMA HACE LA MULTIPLICACION RUSA"
a = input("ingrese valor de a = ")
b = input("ingrese valor de b = ")
suma = 0
while b>0:
	if b%2==1:
		suma = suma + a	
	a = 2*a
	b = abs(b/2)
print "la suma es ",suma