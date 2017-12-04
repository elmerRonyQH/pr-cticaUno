print 
print "ESTE PROGRAMA NO DICE SI UN NUMERO E PRIMO O NO"
n = input("ingrese numero = ")
i = n/2

flag = True
while i>1 & flag == True:
	if n % i == 0:
		flag = False
	i = i - 1
if flag == True:
	print "es primo"
else:
	print "no es primo"