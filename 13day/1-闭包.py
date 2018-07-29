def ll(b,d,f):
	def nn(c):
		return b*c+d*c+f*c

	return nn

w = ll(1,2,3)
w2 = ll(9,8,7)	
print(w(9))
print(w2(5))

