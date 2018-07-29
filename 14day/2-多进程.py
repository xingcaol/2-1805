import os

pid = os.fork()

if pid == 1 :
	print('啦啦啦')

else:
	print('哈哈哈')
	
