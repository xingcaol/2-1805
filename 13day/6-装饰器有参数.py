def lll(yyy):
	def llll(fun):
		def inner(*args,**kwargs):
			if yyy == 1:
				print('验证')
			elif yyy == 2:
				print('验证2')

			return fun(*args,**kwargs)
		return inner
	return llll


@lll(1)
def play(a,b):
	print('%d我要入地%d'%(a,b))

play(1,2)


@lll(2)
def play1():
	print('我要上天')
play1()
