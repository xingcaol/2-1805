def fil(num):
	a,b = 0,1
	print('************1***************')
	for i in range(num):
		print('*************2***************')

		temp = yield i     
		print('**************3****************')
		print(temp)
		a,b = b,a+b

a = fil(4)
print(a)
