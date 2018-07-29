class Dog():#父类
	__instance = None
	def __init__(self):
		print("初始化属性")
		self.name = "tom"
	def __str__(self):
		print("打印对象调用，要有返回值")
		return "哈哈"

	def __del__(self):
		print("删除对象调用")
    
	def __new__(cls):#创建对象的方法
		print("创建对象，并返回对象引用")
		if cls.__instance != None:
			return cls.__instance
		else:
			cls.__instance = object.__new__(cls)
		return cls.__instance
class d(Dog):#子类
	pass
dog = d()
print(dog)


