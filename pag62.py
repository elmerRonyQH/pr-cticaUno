n = input("ingrese n = ")
m = input("ingrese m = ")
x=1
y=1
for i in range(1,m):
	x = x*(n+1-i)
	y = y*i
coef = x/y
print "el coeficiente es: ",coef
