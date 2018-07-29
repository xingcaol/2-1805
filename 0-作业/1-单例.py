class Dog(object):
	__DDD = None
	def __new__(cls):
		if cls.__DDD == None:
			cls.__DDD = object.__new__(cls)
			return cls.__DDD
		else:
			return cls.__DDD

	def __init__(self,name):
		self.name = name	



dog = Dog('二哈')
dog1 = Dog('啦啦')


