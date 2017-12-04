print 
print "ESTE PROGRAMA HALLA EL VALOR INTERMEDIO DE TRES VALORES"
a = input("ingrese a = ")
b = input("ingrese b = ")
c = input("ingrese c = ")
if a < b:
	max = b
	min = a
if max < c:
	max = c
if c < min:
	min = c
inter = (a+b+c)-(max + min)
print "intermedio es : ", inter
	