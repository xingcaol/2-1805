def ll(hh):
	def pp():
		return '**' + hh() + '**'
	return pp

def yy(ii):
	def pp():
		return '--' + ii() + '---'
	return pp
	


@ll
def cc():
	return '哈哈哈'


@ll
def cc1():
	return '呵呵呵'


@ll
@yy
def cc2():
	return '好好好'


print(cc())	
print(cc1())
print(cc2())

