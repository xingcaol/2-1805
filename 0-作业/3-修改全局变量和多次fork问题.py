import os 
import time

num = 0

	
p = os.fork()

if p == 0:
	print('我是子进程')
	time.sleep(1)
	print('num = %d'%num)
else :
	num+=1
	print('我是父进程,我给num加上1')
	print('我是父进程 num=%d'%num)
