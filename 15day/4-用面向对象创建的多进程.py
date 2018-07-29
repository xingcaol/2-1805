from multiprocessing import Process
import time
class MyProcess(Process):
	def __init__(self,name):
		super().__init__()#这句话给父类初始化，初始化父类会我们提供一些功能 千万记着初始化
		self.name = name 

	def run(self):
		for i in range(5):
			time.sleep(1)
			print('我重写了run方法%s'%(self.name))



p = MyProcess('老王')
p1 = MyProcess('老宋')
p.start()
p1.start()
p.join()
p1.join()
print('我是主线程')

