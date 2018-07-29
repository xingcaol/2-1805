def l(ooo):
	def inner():
		print('验证')
		ooo()
	return inner

@l
def test():
	print('********啦啦啦*********')



#test = l(test)
test()


@l
def test1():
	print('------------哈哈哈--------------')

test1()


@l
def test2():
	print('++++++++++++++哦哦哦++++++++++++++++++')
test2()
