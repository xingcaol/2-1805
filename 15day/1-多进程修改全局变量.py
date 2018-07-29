import os
import time

num = 1


pid = os.fork()

if pid == 0:
	print('我是子进程')
	time.sleep(3)
	print('我是子进程num=%d'%num)
else:
	
	num+=1
	print('我是父进程，我给num加上1')
	print('我是父进程 num=%d'%num)
