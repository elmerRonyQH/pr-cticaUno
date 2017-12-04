print 
print "ESTE PPROGRAMA EVALUA EL EXPONECIAL APLICANDO LA SERIE DE TAYLOR DEL 1 A 15"
x = input("ingrese valor de x = ")
suma = 1
i = 1
t = 1
while (i<=15) & (abs(t) > -1):
	t = t * (x/i)
	suma = suma + t
	i = i + 1
print "la suma exponecial es ",suma