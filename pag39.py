print 
print "ESTE PROGRAMA TE DICE SI FORMAN UN TRIANGULO O NO"
a = input("ingrese a = ")
b = input("ingrese b = ")
c = input("ingrese c = ")
if a>b:
	max = a
else:
	max = b
if max < c:
	max = c
s = (a+b+c)/2
if s > max:
	print "FORMAN TRIANGULO"
else:
	print "NO FORMAN TRIANGULO"