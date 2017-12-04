

for n in range(1,99):
	for m in range((n+1),100):
		a = (m*m)-(n*n)
		b = 2*m*n
		h = (m*m)+(n*n)
		if h <= 100:
			print "valores",a ,b ,h
		