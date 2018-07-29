from threading import Thread,Lock
import time 
a = 0
def work1():
	global a 
	#mutex.acquire(True)
	for i in range(1000000):
		mutex.acquire(True)
		a += 1
		mutex.release()
	#mutex.release()
	print('进程一%d'%a)


def work2():
	global a
	#mutex.acquire(True)
	for i in range(1000000):
		mutex.acquire(True)
		a +=1
		mutex.release()
	#mutex.release()
	print('线程二%d'%a)

mutex = Lock()

t = Thread(target=work1)
t1 = Thread(target=work2)

t.start()
t1.start()
