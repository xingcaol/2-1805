def ss(o):
	def inner(*args,**kwargs):
		print('曹宗亮')
		return o(*args,**kwargs)
	return inner


@ss
def play():#无参无返回值
	print('***********啦啦啦啦啦***************')
play()


@ss
def play1(a,b):#有参无返回值
	print('**********呵呵哈哈哈%s%s**************'%(a,b))
play1('哦哦','好好')


@ss
def play2():#无参有返回值
	return '好了好了好了'
pp = play2()
print(pp)

@ss
def play3(a,b):#有参有返回值
	return '乐山乐水懒死了%s%s'%(a,b)
pp = play3('3','4')
print(pp)

